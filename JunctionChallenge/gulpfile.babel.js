import fs from 'fs';
import path from 'path';

import gulp from 'gulp';

// Load all gulp plugins automatically
// and attach them to the `plugins` object
import plugins from 'gulp-load-plugins';

// Temporary solution until gulp 4
// https://github.com/gulpjs/gulp/issues/355
import runSequence from 'run-sequence';

import archiver from 'archiver';
import glob from 'glob';
import del from 'del';
import ssri from 'ssri';
import modernizr from 'modernizr';

import browserSync from 'browser-sync';
import swPrecache from 'sw-precache';
import gulpLoadPlugins from 'gulp-load-plugins';


import pkg from './package.json';
import modernizrConfig from './modernizr-config.json';


const dirs = pkg['h5bp-configs'].directories;
const reload = browserSync.reload;

// ---------------------------------------------------------------------
// | Helper tasks                                                      |
// ---------------------------------------------------------------------

// Lint JavaScript
gulp.task('lint', () =>
  gulp.src(['src/js/**/*.scripts','!node_modules/**', 'src/js/*.js'])
    .pipe($.eslint())
    .pipe($.eslint.format())
    .pipe($.if(!browserSync.active, $.eslint.failAfterError()))
);

gulp.task('archive:create_archive_dir', () => {
  fs.mkdirSync(path.resolve(dirs.archive), '0755');
});

gulp.task('archive:zip', (done) => {

  const archiveName = path.resolve(dirs.archive, `${pkg.name}_v${pkg.version}.zip`);
  const zip = archiver('zip');
  const files = glob.sync('**/*.*', {
    'cwd': dirs.dist,
    'dot': true // include hidden files
  });
  const output = fs.createWriteStream(archiveName);

  zip.on('error', (error) => {
    done();
    throw error;
  });

  output.on('close', done);

  files.forEach((file) => {

    const filePath = path.resolve(dirs.dist, file);

    // `zip.bulk` does not maintain the file
    // permissions, so we need to add files individually
    zip.append(fs.createReadStream(filePath), {
      'name': file,
      'mode': fs.statSync(filePath).mode
    });

  });

  zip.pipe(output);
  zip.finalize();

});

gulp.task('clean', (done) => {
  del([
    dirs.archive,
    dirs.dist
  ]).then(() => {
    done();
  });
});

gulp.task('copy', [
  'copy:.htaccess',
  'copy:index.html',
  'copy:jquery',
  'copy:license',
  'copy:main.css',
  'copy:misc',
  'copy:normalize'
]);

gulp.task('copy:.htaccess', () =>
  gulp.src('node_modules/apache-server-configs/dist/.htaccess')
    .pipe(plugins().replace(/# ErrorDocument/g, 'ErrorDocument'))
    .pipe(gulp.dest(dirs.dist))
);

gulp.task('copy:index.html', () => {
  const hash = ssri.fromData(
    fs.readFileSync('node_modules/jquery/dist/jquery.min.js'),
    {algorithms: ['sha256']}
  );
  let version = pkg.devDependencies.jquery;
  let modernizrVersion = pkg.devDependencies.modernizr;

  gulp.src(`${dirs.src}/index.html`)
    .pipe(plugins().replace(/{{JQUERY_VERSION}}/g, version))
    .pipe(plugins().replace(/{{MODERNIZR_VERSION}}/g, modernizrVersion))
    .pipe(plugins().replace(/{{JQUERY_SRI_HASH}}/g, hash.toString()))
    .pipe(gulp.dest(dirs.dist));
});

gulp.task('copy:jquery', () =>
  gulp.src(['node_modules/jquery/dist/jquery.min.js'])
    .pipe(plugins().rename(`jquery-${pkg.devDependencies.jquery}.min.js`))
    .pipe(gulp.dest(`${dirs.dist}/js/vendor`))
);

gulp.task('copy:license', () =>
  gulp.src('LICENSE.txt')
    .pipe(gulp.dest(dirs.dist))
);

gulp.task('copy:main.css', () => {

  const banner = `/*! HTML5 Boilerplate v${pkg.version} | ${pkg.license} License | ${pkg.homepage} */\n\n`;

  gulp.src(`${dirs.src}/css/main.css`)
    .pipe(plugins().header(banner))
    .pipe(plugins().autoprefixer({
      browsers: ['last 2 versions', 'ie >= 9', '> 1%'],
      cascade: false
    }))
    .pipe(gulp.dest(`${dirs.dist}/css`));
});

gulp.task('copy:misc', () =>
  gulp.src([

    // Copy all files
    `${dirs.src}/**/*`,

    // Exclude the following files
    // (other tasks will handle the copying of these files)
    `!${dirs.src}/css/main.css`,
    `!${dirs.src}/index.html`

  ], {

    // Include hidden files by default
    dot: true

  }).pipe(gulp.dest(dirs.dist))
);

gulp.task('copy:normalize', () =>
  gulp.src('node_modules/normalize.css/normalize.css')
    .pipe(gulp.dest(`${dirs.dist}/css`))
);

gulp.task('modernizr', (done) =>{

  modernizr.build(modernizrConfig, (code) => {
    fs.writeFile(`${dirs.dist}/js/vendor/modernizr-${pkg.devDependencies.modernizr}.min.js`, code, done);
  });

});

gulp.task('lint:js', () =>
  gulp.src([
    'gulpfile.js',
    `${dirs.src}/js/*.js`,
    `${dirs.test}/*.js`
  ]).pipe(plugins().jscs())
    .pipe(plugins().eslint())
    .pipe(plugins().eslint.failOnError())
);

// Scan your HTML for assets & optimize them
gulp.task('html', () => {
  return gulp.src('app/*.html')
    .pipe($.useref({
      searchPath: '{.tmp,app}',
      noAssets: true
    }))

    // Minify any HTML
    .pipe($.if('*.html', $.htmlmin({
      removeComments: true,
      collapseWhitespace: true,
      collapseBooleanAttributes: true,
      removeAttributeQuotes: true,
      removeRedundantAttributes: true,
      removeEmptyAttributes: true,
      removeScriptTypeAttributes: true,
      removeStyleLinkTypeAttributes: true,
      removeOptionalTags: true
    })))
    // Output files
    .pipe($.if('*.html', $.size({title: 'html', showFiles: true})))
    .pipe(gulp.dest('dist'));
});


// Compile and automatically prefix stylesheets
gulp.task('styles', () => {
  const AUTOPREFIXER_BROWSERS = [
    'ie >= 10',
    'ie_mob >= 10',
    'ff >= 30',
    'chrome >= 34',
    'safari >= 7',
    'opera >= 23',
    'ios >= 7',
    'android >= 4.4',
    'bb >= 10'
  ];

// For best performance, don't add Sass partials to `gulp.src`
return gulp.src([
  'src/css/*.css',
  'src/css/**/*.css'
])
  // .pipe($.newer('.tmp/css'))
  // .pipe($.sourcemaps.init())
  // .pipe($.sass({
  //   precision: 10
  // }).on('error', $.sass.logError))
  // .pipe($.autoprefixer(AUTOPREFIXER_BROWSERS))
  // .pipe(gulp.dest('.tmp/css'))
  // // Concatenate and minify styles
  // .pipe($.if('*.css', $.cssnano()))
  // .pipe($.size({title: 'css'}))
  // .pipe($.sourcemaps.write('./'))
  // .pipe(gulp.dest('dist/css'))
  // .pipe(gulp.dest('.tmp/css'));
});

// Concatenate and minify JavaScript. Optionally transpiles ES2015 code to ES5.
// to enable ES2015 support remove the line `"only": "gulpfile.babel.scripts",` in the
// `.babelrc` file.
gulp.task('scripts', () =>
gulp.src([
  // Note: Since we are not using useref in the scripts build pipeline,
  //       you need to explicitly list your scripts here in the right order
  //       to be correctly concatenated
  './src/js/main.js'
  // Other scripts
  // './app/js/vendor/jquery-3.2.1.min.scripts',
  // './app/js/vendor/jquery-ui.min.scripts',
  // './app/js/vendor/modernizr-2.8.3.min.scripts',
  // './app/js/vendor/xlsx.full.min.scripts',
  // './app/js/vendor/alasql.min.scripts',
  // './app/js/vendor/FileSaver.scripts',
  // './app/js/read_in_file.scripts'
  // './app/js/vendor/esri-leaflet_v2_2_2.js',
  // './app/js/vendor/leaflet_1.3.3.js'

])
  // .pipe($.newer('.tmp/js'))
  // .pipe($.sourcemaps.init())
  // .pipe($.babel())
  // .pipe($.sourcemaps.write())
  // .pipe(gulp.dest('.tmp/js'))
  // .pipe($.concat('main.min.js'))
  // .pipe($.uglify({preserveComments: 'some'}))
  // // Output files
  // .pipe($.size({title: 'js'}))
  // .pipe($.sourcemaps.write('.'))
  // .pipe(gulp.dest('dist/js'))
  // .pipe(gulp.dest('.tmp/js'))
);

// ---------------------------------------------------------------------
// | Main tasks                                                        |
// ---------------------------------------------------------------------

gulp.task('archive', (done) => {
  runSequence(
    'build',
    'archive:create_archive_dir',
    'archive:zip',
    done);
});

gulp.task('build', (done) => {
  runSequence(
    ['clean', 'lint:js'],
    'copy', 'modernizr',
    done);
});

// Watch files for changes & reload
  gulp.task('serve', ['scripts', 'styles'], () => {
    browserSync({
                  notify: false,
                  // Customize the Browsersync console logging prefix
                  logPrefix: 'WSK',
                  // Allow scroll syncing across breakpoints
                  scrollElementMapping: ['main', '.mdl-layout'],
                  // Run as an https by uncommenting 'https: true'
                  // Note: this uses an unsigned certificate which on first access
                  //       will present a certificate warning in the browser.
                  // https: true,
                  server: ['.tmp', 'src'],
                  port: 3000
                });

gulp.watch(['`!${dirs.src}/index.html`'], reload);
gulp.watch(['src/css/*.{css,styles}'], ['styles', reload]);
gulp.watch(['src/js/vendor/*.js','src/js/*.js'], ['lint', 'scripts', reload]);
gulp.watch(['src/img/*'], reload);
});

gulp.task('default', ['build']);

// See http://www.html5rocks.com/en/tutorials/service-worker/introduction/ for
// an in-depth explanation of what service workers are and why you should care.
// Generate a service worker file that will provide offline functionality for
// local resources. This should only be done for the 'dist' directory, to allow
// live reload to work as expected when serving from the 'app' directory.
gulp.task('generate-service-worker', ['copy-sw-scripts'], () => {
  const rootDir = 'dist';
  const filepath = path.join(rootDir, 'service-worker.scripts');

  return swPrecache.write(filepath, {
    // Used to avoid cache conflicts when serving on localhost.
    cacheId: pkg.name || 'web-starter-kit',
    // sw-toolbox.scripts needs to be listed first. It sets up methods used in runtime-caching.scripts.
    importScripts: [
      'scripts/sw/sw-toolbox.scripts',
      'scripts/sw/runtime-caching.scripts'
    ],
    staticFileGlobs: [
      // Add/remove glob patterns to match your directory setup.
      `${rootDir}/img/*`,
      `${rootDir}/js/*.js`,
      `${rootDir}/js/vendor/*.js`,
      `${rootDir}/css/*.css`,
      `${rootDir}/*.{html,json}`
    ],
    // Translates a static file path to the relative URL that it's served from.
    // This is '/' rather than path.sep because the paths returned from
    // glob always use '/'.
    stripPrefix: rootDir + '/'
  });
});
