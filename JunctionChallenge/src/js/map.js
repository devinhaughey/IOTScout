
let route_lines;
let data_points;

let test_points = [
  {
    'clientXCoord': 22.603227,
    'clientYCoord': 60.72309,
    'shipmentSeq': '2254415582',
    'trackingCode': 'JJFI99992201000544210',
    'volume': 19.3,
    'height': 255,
    'width': 230,
    'depth': 330,
    'weight': 3700,
    'deliveryTime': 14
  },
  {
    'clientXCoord': 22.668648,
    'clientYCoord': 60.718454,
    'shipmentSeq': '66447832',
    'trackingCode': 'JJFI61199020012789814',
    'volume': 3.5,
    'height': 55,
    'width': 220,
    'depth': 295,
    'weight': null,
    'deliveryTime': 16
  },
  {
    'clientXCoord': 22.748679,
    'clientYCoord': 60.705265,
    'shipmentSeq': '784515582',
    'trackingCode': 'JJFI64136210012245552',
    'volume': 6.4,
    'height': 75,
    'width': 230,
    'depth': 375,
    'weight': 650,
    'deliveryTime': 16
  },
  {
    'clientXCoord': 22.75498,
    'clientYCoord': 60.7036,
    'shipmentSeq': '11534532',
    'trackingCode': 'JJFI62842899996479553',
    'volume': 13.5,
    'height': 95,
    'width': 380,
    'depth': 385,
    'weight': 600,
    'deliveryTime': 14
  },
  {
    'clientXCoord': 22.784765,
    'clientYCoord': 60.561008,
    'shipmentSeq': '844415582',
    'trackingCode': 'JJFI62842899954001518',
    'volume': 14.8,
    'height': 155,
    'width': 265,
    'depth': 360,
    'weight': 800,
    'deliveryTime': 14
  },
  {
    'clientXCoord': 22.674358,
    'clientYCoord': 60.61825,
    'shipmentSeq': '446515582',
    'trackingCode': 'JJFI63440020012598382',
    'volume': 5.5,
    'height': 204,
    'width': 129,
    'depth': 207,
    'weight': 200,
    'deliveryTime': 16
  },
  {
    'clientXCoord': 22.583696,
    'clientYCoord': 60.6037955,
    'shipmentSeq': '9543415582',
    'trackingCode': 'JJFI60002920012901648',
    'volume': 45.6,
    'height': 159,
    'width': 405,
    'depth': 784,
    'weight': 17660,
    'deliveryTime': 14
  }
];

var map = L.map("map", {editable: false, doubleClickZoom: false}).setView([60.543, 24.923], 9);
// map.zoomControl.setPosition('bottomleft');
// var popup = L.popup();

L.esri.basemapLayer("Topographic").addTo(map);
//L.marker([23.4345,62.234543]).addTo(map);

let heat = L.heatLayer([
  [60.543, 24.923, 0.2], // lat, lng, intensity
  [60.343, 22.923, 1]
], {radius: 100, // default value
  blur : 15, // default value
  gradient : {1: 'blue'} });

heat.addTo(map);

/**
 * The updateMapLayers function removes all the different layers from the map.
 * It queries the ArcGIS server for the routes of the requested area. The
 * returned JSON data is then parsed through the Leaflet plugin to generate
 * routes automatically. With each route, the route id is attached to it as a
 * popup along with a random color to display it.
 */
function updateMapLayers() {
    let count = 1;
    if (map.hasLayer(route_lines)) {
        route_lines.removeFrom(map);
    }

    function onEachFeature(feature, layer) {
        // does this feature have a property named popupContent?
        if (feature.properties.REITTITUNNUS) { //feature.id
            layer.bindPopup('Route ID: ' + feature.properties.REITTITUNNUS.toString());
            addListEntry(feature.properties.REITTITUNNUS.toString(), feature.properties.REITTITUNNUS.toString(), 'select_route');
            addCheckboxes(feature.properties.REITTITUNNUS.toString(), feature.properties.REITTITUNNUS.toString(), 'div_route_checkboxes', count);
            route_names.push(feature.properties.REITTITUNNUS.toString());
            feature.properties.show_on_map = true;
            count++;
        }
    }

    // console.log(geojson_routes);

    route_lines = L.geoJSON(geojson_routes, {
        // show_on_map: true,
        style: function (features) {
            switch (returnLastDigit(features.properties.REITTITUNNUS)) { // returnLastDigit(features.id)
                case '1':
                    c = '#FF8000';
                    break;
                case '2':
                    c = '#394A58';
                    break;
                case '3':
                    c = '#0073CF';
                    break;
                case '4':
                    c = '#34B233';
                    break;
                case '5':
                    c = '#CB0044';
                    break;
                case '6':
                    c = '#00B74A';
                    break;
                case '7':
                    c = '#0773A1';
                    break;
                case '8':
                    c = '#FF3100';
                    break;
                case '9':
                    c = '#9B1E00';
                    break;
                case '0':
                    c = '#000000';
                    break;
                default:
                    c = '#C0C0C0';
            }
            return {color: c};
        },
        onEachFeature: onEachFeature
    });
}


/**
 * The toggleCheckBox switches the layer from being active or not to be displayed.
 */
function toggleCheckBox() {
    this.classList.toggle('active-class');
    toggleLayerVisibility(this.value);
}

/**
 * The toggleLayerVisibility function checks to see if the selected layer is
 * already appearing on the map or not and switches its visibility.
 *
 * @param layerToToggle The layer to switch its visibility
 */
function toggleLayerVisibility(layerToToggle) {
    if (layerToToggle === "Reitit") {
        if (map.hasLayer(route_lines)) {
            route_lines.removeFrom(map);
        } else {
            route_lines.addTo(map);
        }
    }
}

/**
 * The createDeliveryPoints takes the elements within report_data and adds the
 * point along with their information to popups to markers on the map.
 */
function createDeliveryPoints(option) {
  let LeafIcon = L.Icon.extend({
    options: {
      iconSize:     [23, 45],
      shadowSize:   [50, 64],
      iconAnchor:   [22, 94],
      shadowAnchor: [4, 62],
      popupAnchor:  [-3, -76]
    }
  });
  let redIcon = new LeafIcon({iconUrl: 'css/images/marker-icon_red.png'});
  let data_input = data_points;
  let markerLocation = new L.LatLng(data_input['latitude'], data_input['longitude']);
  let marker;

  if ( option === 0 ) {
    marker = new L.Marker(markerLocation, {icon: redIcon}).bindPopup(function () {
      return L.Util.template(
        '<p><b>Timestamp: </b>' + data_input['timestamp'] + '<br>' +
        '<b>Tags: </b>' + data_input['tags'] + '<br>' +
        '<b>Lat and Long: </b>' + data_input['latitude'] + ', ' + data_input['longitude'] + '<br>'
      )
    });
  } else {
    marker = new L.Marker(markerLocation).bindPopup(function () {
      return L.Util.template(
        '<p><b>Timestamp: </b>' + data_input['timestamp'] + '<br>' +
        '<b>Tags: </b>' + data_input['tags'] + '<br>' +
        '<b>Lat and Long: </b>' + data_input['latitude'] + ', ' + data_input['longitude'] + '<br>'
      )
    });
  }
  map.addLayer(marker);
}

/**
 * The getRandomColor function generates a random number and pulls the color
 * associated with the string. The color is then returned and used for
 * displaying the route.
 *
 * @returns {string} The color code generated by the function
 */
function getRandomColor() {
    let letters = '0123456789ABCDEF'.split('');
    let color = '#';

    for (let i = 0; i < 6; i++) {
        color += letters[Math.round(Math.random() * 15)];
    }

    return color;
}
