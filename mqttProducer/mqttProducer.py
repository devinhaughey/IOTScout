# Team: Mysterious Mad Trippers

import paho.mqtt.client as mqtt #import the client1
import time
from random import randint
import requests
import json

data_list = [
    #{ 'priority':, 'lat':,'long': ,'msg':'','tags':['']},
  {
    "timestamp": "2018-10-22T04:34:16 -03:00",
    "latitude": -73.47847,
    "longitude": -11.44797,
    "msg": "Officia qui proident ullamco laboris adipisicing laboris sunt ad. Magna ipsum id aute dolore laboris exercitation ad officia reprehenderit esse dolore. Sunt Lorem eiusmod ullamco incididunt velit labore occaecat duis minim culpa anim est.\r\n",
    "tags": [
      "danger"
    ]
  },
  {
    "timestamp": "2018-07-23T07:35:31 -03:00",
    "latitude": -9.677408,
    "longitude": 172.61834,
    "msg": "Consectetur Lorem ullamco culpa quis irure id. Eu minim do nostrud aute aliqua non irure velit ad sunt qui mollit. Minim culpa adipisicing duis dolor veniam consectetur proident ut. Labore eiusmod incididunt exercitation occaecat ea dolor.\r\n",
    "tags": [
      "medical attention",
      "water"
    ]
  },
  {
    "timestamp": "2018-05-12T10:29:29 -03:00",
    "latitude": 9.198898,
    "longitude": -99.830518,
    "msg": "Excepteur amet anim amet labore sit eiusmod proident ea do non occaecat cillum consectetur consectetur. Non commodo enim tempor adipisicing proident. Id minim deserunt magna do consequat minim id dolore incididunt quis. Aliquip fugiat occaecat laboris consectetur. Dolor qui aliquip ut deserunt eiusmod Lorem dolor ullamco est amet eiusmod aute.\r\n",
    "tags": [
      "flood"
    ]
  },
  {
    "timestamp": "2018-03-26T02:10:54 -03:00",
    "latitude": 71.811668,
    "longitude": -170.047661,
    "msg": "Dolore labore non fugiat duis magna deserunt adipisicing pariatur sunt duis Lorem sint. Enim enim non proident laboris officia. Aute anim mollit sint qui nisi esse aliqua Lorem incididunt aliquip veniam consectetur nostrud ad. Officia ullamco eiusmod elit nulla ipsum Lorem in dolore cillum proident. Commodo nostrud incididunt excepteur eu cupidatat aute mollit velit ex culpa id. Eu qui irure enim nulla qui proident amet in voluptate est. Ea enim esse non officia.\r\n",
    "tags": [
      "flood",
      "other",
      "food",
      "injured"
    ]
  },
  {
    "timestamp": "2018-02-26T05:39:54 -02:00",
    "latitude": 32.274875,
    "longitude": -100.959989,
    "msg": "Fugiat est esse aliquip velit sint non tempor officia. Velit nulla esse excepteur Lorem nulla in occaecat ad nostrud commodo duis veniam veniam voluptate. Cillum consequat adipisicing do exercitation mollit incididunt nisi tempor ea sint. Irure adipisicing consectetur Lorem ullamco irure qui minim pariatur aliqua. Officia duis elit magna sint. Dolore tempor nulla eiusmod nostrud irure reprehenderit sint et occaecat laboris aliquip quis. Amet fugiat sit anim sit sit aliqua Lorem laborum veniam enim anim aliqua.\r\n",
    "tags": [
      "injured",
      "water",
      "injured",
      "injured"
    ]
  },
  {
    "timestamp": "2018-07-15T08:57:53 -03:00",
    "latitude": -52.897481,
    "longitude": -110.082362,
    "msg": "Culpa ipsum quis et ex amet aliqua occaecat eu aliqua mollit. Pariatur excepteur ipsum sint commodo labore. Ea pariatur reprehenderit labore ullamco cupidatat officia anim. Fugiat ut reprehenderit minim veniam ea excepteur nostrud ad esse sit aliquip quis aliqua nulla. Enim commodo magna veniam laborum nulla officia eu tempor cillum nulla tempor adipisicing anim. Irure ea deserunt in qui officia non id ipsum consectetur veniam tempor do dolor. Occaecat ullamco ad ut in aliqua qui pariatur laborum.\r\n",
    "tags": [
      "food",
      "injured",
      "flood",
      "eathquake"
    ]
  },
  {
    "timestamp": "2018-07-13T12:58:41 -03:00",
    "latitude": 26.431104,
    "longitude": -125.689499,
    "msg": "Exercitation do veniam adipisicing ex sint aliqua. Lorem id voluptate consectetur elit deserunt magna Lorem mollit sit incididunt. Dolore ipsum velit in voluptate consequat occaecat excepteur. Magna proident aliqua velit dolore enim irure sit anim sunt do.\r\n",
    "tags": [
      "food"
    ]
  },
  {
    "timestamp": "2018-04-29T05:01:57 -03:00",
    "latitude": 50.098043,
    "longitude": -122.453235,
    "msg": "Lorem proident duis fugiat labore exercitation nulla ex tempor labore anim pariatur sunt magna. Reprehenderit sint laborum nulla consequat deserunt quis tempor est. Qui minim cillum eiusmod laborum ut laboris eiusmod duis ullamco dolore dolor duis nostrud Lorem. Excepteur esse et exercitation aliquip reprehenderit magna dolore.\r\n",
    "tags": [
      "fire",
      "eathquake",
      "fire",
      "danger"
    ]
  },
  {
    "timestamp": "2018-10-08T11:20:20 -03:00",
    "latitude": -32.309305,
    "longitude": -155.062298,
    "msg": "Esse est nostrud cupidatat eiusmod cupidatat irure exercitation ex. Reprehenderit ut duis cillum nulla. Nulla consequat consectetur sit laborum laborum excepteur do ut commodo consectetur. Dolor velit dolor fugiat aute magna in ad voluptate dolor irure et nisi. In commodo adipisicing quis occaecat ipsum aute mollit quis et excepteur ex. Officia est quis consequat incididunt commodo dolore esse. Ullamco irure cupidatat adipisicing sit commodo officia quis ipsum commodo aliqua aliquip labore Lorem.\r\n",
    "tags": [
      "injured",
      "medical attention",
      "injured",
      "flood"
    ]
  },
  {
    "timestamp": "2018-01-31T08:50:42 -02:00",
    "latitude": -85.423606,
    "longitude": 92.095372,
    "msg": "Tempor ut ullamco consectetur ut exercitation et qui. Sit labore eiusmod minim ullamco officia adipisicing cupidatat in dolor incididunt id dolor. Ullamco sint commodo incididunt ea ut proident ad qui do deserunt officia commodo id labore. Cupidatat irure aliquip commodo dolor cupidatat eu ipsum.\r\n",
    "tags": [
      "injured",
      "eathquake",
      "food",
      "danger"
    ]
  },
  {
    "timestamp": "2018-03-01T10:38:16 -02:00",
    "latitude": -71.328192,
    "longitude": -162.945555,
    "msg": "Consequat consectetur incididunt sint occaecat enim. Ipsum velit nostrud veniam reprehenderit amet officia ut. Cupidatat consequat incididunt occaecat eu aliqua Lorem consectetur. Reprehenderit do sint aute pariatur occaecat ad reprehenderit ullamco dolore in. Voluptate ad occaecat dolor pariatur occaecat amet magna culpa labore velit eu.\r\n",
    "tags": [
      "water",
      "food",
      "medical attention",
      "food"
    ]
  },
  {
    "timestamp": "2018-11-21T11:40:34 -02:00",
    "latitude": 44.925256,
    "longitude": -29.325997,
    "msg": "Lorem do est reprehenderit eu in ipsum consequat qui reprehenderit eu incididunt. Culpa anim est exercitation culpa. Reprehenderit esse adipisicing sint est. Aliqua aliquip elit cillum enim sunt excepteur nostrud Lorem aliquip duis. Tempor tempor reprehenderit minim voluptate enim.\r\n",
    "tags": [
      "eathquake"
    ]
  },
  {
    "timestamp": "2018-11-16T03:14:16 -02:00",
    "latitude": 12.505564,
    "longitude": 13.103706,
    "msg": "Commodo anim cupidatat in cupidatat occaecat pariatur sit sit. Reprehenderit in et ad voluptate in do enim officia do commodo adipisicing non cupidatat do. Est minim ex nisi labore nostrud qui anim. Lorem mollit fugiat fugiat proident ex est irure pariatur.\r\n",
    "tags": [
      "flood"
    ]
  },
  {
    "timestamp": "2018-06-13T07:49:27 -03:00",
    "latitude": -30.666719,
    "longitude": -2.924132,
    "msg": "Aute incididunt commodo minim irure ipsum culpa qui reprehenderit. Est duis est incididunt labore commodo ullamco irure culpa. Consequat aute officia consectetur nulla. Reprehenderit mollit eiusmod eiusmod sint cillum tempor. Voluptate elit sint culpa eiusmod ad elit est voluptate aliqua adipisicing labore ullamco. Sit excepteur irure id nisi duis ut enim enim laboris commodo aliqua officia ea excepteur. Amet laborum id tempor nostrud anim qui.\r\n",
    "tags": [
      "food",
      "injured",
      "fire"
    ]
  },
  {
    "timestamp": "2017-11-22T07:41:06 -02:00",
    "latitude": 79.587225,
    "longitude": 125.787507,
    "msg": "Qui dolor ad proident cupidatat sunt tempor aliqua tempor adipisicing fugiat est sunt cupidatat. Et qui dolore nisi amet eu laborum esse excepteur enim adipisicing dolor aute non incididunt. Ut excepteur minim mollit minim ad mollit consequat ullamco sunt ipsum ipsum labore. Pariatur et Lorem deserunt laborum dolore sit dolor magna sunt velit non cupidatat nulla.\r\n",
    "tags": [
      "danger",
      "water"
    ]
  },
  {
    "timestamp": "2018-05-11T01:41:24 -03:00",
    "latitude": -25.814893,
    "longitude": -138.334799,
    "msg": "Et esse laboris id nulla eiusmod officia sit qui. Esse ut voluptate officia sunt non elit anim eu elit exercitation dolor. Incididunt culpa dolore esse velit veniam magna elit ullamco veniam Lorem qui id et.\r\n",
    "tags": [
      "water",
      "food"
    ]
  },
  {
    "timestamp": "2018-01-24T11:39:54 -02:00",
    "latitude": 31.665121,
    "longitude": 81.706543,
    "msg": "Consequat veniam non sint Lorem adipisicing tempor qui aliquip occaecat in non ipsum. Aute aliquip voluptate deserunt tempor ea occaecat aliquip. Esse excepteur anim elit quis nostrud ut dolore minim et ea irure id dolor. Sint magna elit do esse. Veniam dolore duis nulla elit incididunt ex officia enim. Aliqua id consectetur deserunt voluptate ullamco magna ad amet esse cillum occaecat dolore do. Cupidatat tempor fugiat anim ut ipsum nostrud duis deserunt deserunt voluptate quis incididunt ad ipsum.\r\n",
    "tags": [
      "food",
      "injured",
      "injured",
      "other"
    ]
  },
  {
    "timestamp": "2018-10-01T09:45:54 -03:00",
    "latitude": -87.414196,
    "longitude": -130.102084,
    "msg": "Sit dolor tempor mollit nostrud do anim cupidatat cillum nulla. Aute aute ea anim duis mollit labore cupidatat anim incididunt elit dolore qui. Laborum officia exercitation proident sit officia qui veniam. Velit tempor minim dolore sit magna et excepteur id sint voluptate.\r\n",
    "tags": [
      "injured"
    ]
  },
  {
    "timestamp": "2018-03-24T02:34:03 -02:00",
    "latitude": -41.196886,
    "longitude": -107.250587,
    "msg": "Eu qui mollit enim consectetur esse et Lorem do. Cupidatat anim enim nisi esse consectetur enim dolore in irure mollit do reprehenderit. Aliquip do Lorem ex sint in minim mollit nulla id minim qui tempor esse. Amet nulla consectetur voluptate magna minim anim Lorem laborum id exercitation do. Velit incididunt amet minim sint consectetur. Lorem duis Lorem cillum sunt sunt ad mollit irure occaecat. Sit aliqua amet cillum sit.\r\n",
    "tags": [
      "flood",
      "other"
    ]
  },
  {
    "timestamp": "2018-05-23T03:07:31 -03:00",
    "latitude": -50.109761,
    "longitude": -149.505598,
    "msg": "Mollit reprehenderit anim ut esse magna. Laboris consectetur labore occaecat et aute reprehenderit officia eiusmod irure cillum duis. Sint tempor consectetur reprehenderit anim magna duis amet eiusmod amet do ipsum culpa.\r\n",
    "tags": [
      "food",
      "OK",
      "food"
    ]
  },
  {
    "timestamp": "2017-12-04T04:56:22 -02:00",
    "latitude": -49.04928,
    "longitude": 128.306432,
    "msg": "Do dolore consequat tempor dolor. Aute consectetur ea laborum reprehenderit pariatur commodo nulla aliqua quis tempor. Tempor officia fugiat laborum ullamco ullamco. Sunt et sunt dolore occaecat magna laboris ex. Magna velit magna sint Lorem elit commodo pariatur labore do esse nisi qui eiusmod.\r\n",
    "tags": [
      "injured",
      "danger",
      "other",
      "OK"
    ]
  },
  {
    "timestamp": "2018-11-06T02:55:08 -02:00",
    "latitude": 32.388548,
    "longitude": -37.348357,
    "msg": "Ut pariatur mollit non nisi aliquip. Tempor voluptate id exercitation mollit in adipisicing in quis est reprehenderit amet. Nulla sunt laborum non id do fugiat anim culpa irure velit ut aliqua. Voluptate sit reprehenderit duis magna pariatur do sint nulla dolor veniam anim. Lorem exercitation consectetur proident aute. Do eiusmod adipisicing ea in minim veniam. Nostrud reprehenderit minim eiusmod quis ullamco aliqua.\r\n",
    "tags": [
      "injured",
      "food",
      "medical attention"
    ]
  },
  {
    "timestamp": "2018-04-03T07:10:14 -03:00",
    "latitude": -80.840575,
    "longitude": 122.368658,
    "msg": "Qui tempor id consequat qui dolor proident ea cupidatat non duis culpa anim. Consequat amet non nulla adipisicing nisi. Ullamco sit esse sint elit aliqua commodo fugiat eu proident. Duis do laboris ut mollit ullamco amet consequat sunt anim nisi quis sint amet.\r\n",
    "tags": [
      "injured"
    ]
  },
  {
    "timestamp": "2018-07-14T11:45:10 -03:00",
    "latitude": -45.772944,
    "longitude": -169.060173,
    "msg": "Aliquip do do aliqua in dolore. Et consectetur incididunt aliqua cillum fugiat nulla cupidatat nostrud laboris eiusmod. Labore deserunt id ullamco culpa magna dolor nostrud. Sint nisi elit consequat minim occaecat et id deserunt mollit irure. Dolor irure occaecat aute aliquip eu id dolor duis amet non duis in.\r\n",
    "tags": [
      "food"
    ]
  },
  {
    "timestamp": "2018-05-16T11:29:15 -03:00",
    "latitude": -72.970583,
    "longitude": -45.733469,
    "msg": "Sint aute consectetur ex cillum culpa ullamco sint. Cillum tempor reprehenderit voluptate consequat dolore mollit dolore eiusmod nulla cillum sit. Nulla dolor mollit irure reprehenderit nulla ea enim voluptate culpa velit. Est fugiat proident sunt duis duis incididunt veniam irure ad et. Nostrud amet veniam magna sit excepteur. Ea est et enim culpa elit enim incididunt eiusmod veniam enim esse duis.\r\n",
    "tags": [
      "OK",
      "food",
      "food"
    ]
  },
  {
    "timestamp": "2018-09-27T08:26:51 -03:00",
    "latitude": 87.549812,
    "longitude": -36.73642,
    "msg": "Velit velit sunt ad pariatur in ad quis. Tempor ullamco non consequat reprehenderit do dolor ipsum ut anim ad deserunt consectetur labore. Nostrud tempor officia laboris qui cupidatat anim commodo occaecat enim qui laboris. Reprehenderit sunt cupidatat ut est minim labore mollit laborum.\r\n",
    "tags": [
      "other"
    ]
  },
  {
    "timestamp": "2017-11-23T05:53:07 -02:00",
    "latitude": -70.605422,
    "longitude": -173.40112,
    "msg": "Deserunt ex non sunt cillum aute amet nisi ex enim enim qui aliquip est. Est nulla quis aliqua excepteur magna consequat veniam commodo duis excepteur qui amet. Veniam occaecat duis magna cupidatat. Adipisicing laboris tempor culpa in sint eu deserunt laborum velit aliqua proident. Non laborum mollit consectetur proident. Commodo ea reprehenderit aute officia eiusmod. Occaecat ullamco laboris exercitation eu id pariatur sunt sit qui do ad esse.\r\n",
    "tags": [
      "eathquake"
    ]
  },
  {
    "timestamp": "2018-07-02T05:04:02 -03:00",
    "latitude": 47.551088,
    "longitude": -166.2351,
    "msg": "Pariatur fugiat quis cupidatat exercitation incididunt laborum labore magna ullamco nisi laboris magna in commodo. Pariatur adipisicing sint sint duis aliquip irure duis fugiat excepteur eiusmod. Non deserunt eu voluptate consequat Lorem aliquip aliquip eu quis. Est nulla nostrud dolor irure laborum sint. Incididunt cillum amet et enim sint ad et mollit ea ipsum sit nostrud non.\r\n",
    "tags": [
      "food"
    ]
  },
  {
    "timestamp": "2018-10-15T08:40:44 -03:00",
    "latitude": 72.575881,
    "longitude": 74.742372,
    "msg": "Fugiat et cupidatat id proident commodo sint culpa veniam est proident adipisicing Lorem anim. Occaecat dolor eu deserunt tempor qui. Minim mollit dolor labore laboris fugiat.\r\n",
    "tags": [
      "flood"
    ]
  },
  {
    "timestamp": "2018-09-29T03:52:44 -03:00",
    "latitude": -55.154525,
    "longitude": -96.513474,
    "msg": "Ea amet consectetur aute officia et duis ex ipsum voluptate. Consequat pariatur do id elit officia. Do duis aliquip velit ad sunt Lorem velit occaecat id esse commodo sint. Mollit ipsum ex Lorem ipsum cillum ad eu in est ut nisi. Ea fugiat excepteur esse ut sint minim nostrud velit ex eiusmod ullamco sint sunt tempor. Excepteur veniam Lorem sit cillum dolore sit sunt exercitation.\r\n",
    "tags": [
      "fire",
      "OK"
    ]
  },
  {
    "timestamp": "2017-11-29T12:15:50 -02:00",
    "latitude": 62.801935,
    "longitude": -81.1218,
    "msg": "Incididunt nulla quis voluptate ut nostrud irure nisi magna non. Id tempor magna Lorem cillum enim ullamco nisi cillum in veniam minim dolor ea labore. Ad commodo esse consectetur labore proident ex pariatur sint commodo dolor quis ullamco. Non deserunt incididunt eiusmod laborum tempor. Id nulla est incididunt dolore sint labore amet dolore nostrud minim fugiat labore anim. Duis pariatur quis sit dolor anim ullamco.\r\n",
    "tags": [
      "OK"
    ]
  },
  {
    "timestamp": "2018-02-12T08:12:48 -02:00",
    "latitude": -78.215237,
    "longitude": 8.966034,
    "msg": "Nostrud eiusmod dolore ex excepteur voluptate aliquip ipsum esse magna proident officia id non. Pariatur est sit esse non ex magna qui minim. Dolore et est sit in commodo. Et adipisicing aute laborum minim excepteur eu irure irure velit. Dolor voluptate et laboris aliquip et. Consectetur cillum proident et nostrud enim cillum nostrud velit commodo mollit do do esse.\r\n",
    "tags": [
      "food"
    ]
  },
  {
    "timestamp": "2018-02-04T09:55:19 -02:00",
    "latitude": 88.447803,
    "longitude": -17.0544,
    "msg": "Incididunt do qui sint voluptate laborum culpa pariatur irure labore commodo velit excepteur. Officia laborum exercitation consectetur ullamco voluptate. Id minim voluptate esse consequat culpa quis fugiat et labore eiusmod consequat cillum.\r\n",
    "tags": [
      "flood",
      "medical attention"
    ]
  },
  {
    "timestamp": "2017-11-27T05:22:10 -02:00",
    "latitude": -52.192263,
    "longitude": -56.572223,
    "msg": "Deserunt qui sunt velit ad commodo nisi ipsum id et magna. Mollit excepteur dolore anim magna nisi anim in. Consectetur enim anim officia magna qui do incididunt nostrud cupidatat. Sit deserunt laborum cillum et mollit excepteur et qui proident cupidatat quis.\r\n",
    "tags": [
      "eathquake",
      "eathquake",
      "danger"
    ]
  },
  {
    "timestamp": "2018-07-09T10:07:58 -03:00",
    "latitude": -82.937836,
    "longitude": 82.394993,
    "msg": "Cillum consequat Lorem velit esse esse eu. Nostrud laborum sunt nisi in consequat ut deserunt dolor cillum mollit aliquip aute. Nostrud sit ex ea laboris voluptate sint ea ipsum aute cupidatat Lorem et. Esse nisi aute sit aute esse. Eu elit consequat dolor nostrud laborum cupidatat tempor qui mollit proident et consequat elit.\r\n",
    "tags": [
      "water"
    ]
  },
  {
    "timestamp": "2018-03-23T08:33:14 -02:00",
    "latitude": -26.330682,
    "longitude": 165.229368,
    "msg": "Enim ex exercitation sit aliquip deserunt. Irure do laboris laborum et exercitation ex nisi qui irure. Occaecat anim sit aliquip sint. Labore qui excepteur ea veniam aliquip pariatur duis nulla ex consequat ea enim.\r\n",
    "tags": [
      "medical attention",
      "injured",
      "other"
    ]
  },
  {
    "timestamp": "2018-10-18T12:39:47 -03:00",
    "latitude": -66.474967,
    "longitude": 138.784078,
    "msg": "Ipsum amet ea voluptate velit fugiat labore sint labore ullamco. Qui qui quis aliquip anim do ad ea enim ea anim tempor veniam tempor. Eu tempor in enim ullamco nisi sunt. Officia quis ut voluptate ipsum amet sunt nostrud sit. Ad est velit ullamco laboris enim tempor. Consectetur esse dolor nisi id officia tempor incididunt labore ex ea. Cupidatat nulla et et ullamco.\r\n",
    "tags": [
      "flood"
    ]
  },
  {
    "timestamp": "2018-04-24T07:49:03 -03:00",
    "latitude": 63.46819,
    "longitude": -146.971336,
    "msg": "Nostrud adipisicing ullamco dolor laborum. Dolore occaecat laborum proident laboris ea fugiat nulla commodo anim Lorem aliquip occaecat laboris nisi. In sit cupidatat do velit. Ipsum mollit magna exercitation mollit minim anim culpa consectetur. Aliquip nisi officia do velit voluptate sint.\r\n",
    "tags": [
      "flood"
    ]
  },
  {
    "timestamp": "2018-04-30T07:49:04 -03:00",
    "latitude": 87.716928,
    "longitude": 43.906264,
    "msg": "Officia fugiat enim sunt reprehenderit. Voluptate labore culpa cillum adipisicing reprehenderit officia commodo. Incididunt amet laboris laboris dolor enim ad dolore. Ut magna aute magna et aute ea proident ipsum id.\r\n",
    "tags": [
      "eathquake",
      "injured",
      "flood"
    ]
  },
  {
    "timestamp": "2018-04-19T03:14:50 -03:00",
    "latitude": -4.28173,
    "longitude": -34.282592,
    "msg": "Incididunt reprehenderit nostrud exercitation irure id occaecat aliqua. In excepteur proident do ullamco aliqua labore commodo laborum ex ut proident ut nulla consequat. Ad sunt aliqua culpa qui. Est nisi irure adipisicing ad proident sint proident voluptate elit aliquip ex.\r\n",
    "tags": [
      "medical attention",
      "medical attention",
      "food",
      "food"
    ]
  },
  {
    "timestamp": "2018-05-22T05:01:50 -03:00",
    "latitude": -64.737582,
    "longitude": -141.274942,
    "msg": "Amet est tempor occaecat aute elit cillum fugiat dolor pariatur magna. Et nulla dolore do magna laborum mollit cillum dolore quis. Consequat amet occaecat amet est pariatur ea duis culpa incididunt enim Lorem aliquip cillum commodo. Velit veniam veniam proident sint non labore proident. In excepteur in nulla aliquip consectetur laboris nostrud eu aute exercitation reprehenderit ad. Mollit sint incididunt et culpa Lorem. Officia eiusmod mollit magna excepteur ea mollit consectetur tempor exercitation sint sunt Lorem eiusmod exercitation.\r\n",
    "tags": [
      "other",
      "danger",
      "other",
      "injured"
    ]
  },
  {
    "timestamp": "2018-03-02T08:22:04 -02:00",
    "latitude": 24.283235,
    "longitude": 75.436999,
    "msg": "Magna proident ex velit quis laborum anim ea amet. Fugiat ad ullamco velit adipisicing exercitation ipsum sint dolor consectetur commodo sint dolor esse et. Do in occaecat sit qui minim ullamco exercitation ad sint ipsum id quis qui. Dolore elit excepteur do aliquip irure sit veniam culpa est nostrud. Ea deserunt commodo anim reprehenderit ipsum enim aliqua ullamco sit. Ipsum et aliqua elit esse adipisicing elit cillum ut exercitation eu deserunt sit Lorem.\r\n",
    "tags": [
      "OK",
      "flood",
      "water",
      "food"
    ]
  },
  {
    "timestamp": "2017-12-12T01:51:48 -02:00",
    "latitude": -54.495597,
    "longitude": -62.210041,
    "msg": "Adipisicing minim officia ea laborum ad anim est id sit adipisicing deserunt deserunt Lorem consectetur. Cillum culpa dolore consequat qui sint. Exercitation duis ipsum sunt Lorem irure voluptate. Ea sint nostrud anim excepteur.\r\n",
    "tags": [
      "fire"
    ]
  },
  {
    "timestamp": "2018-04-04T03:46:34 -03:00",
    "latitude": -64.328848,
    "longitude": 92.986103,
    "msg": "Et qui reprehenderit velit minim deserunt reprehenderit. Sint nulla anim reprehenderit excepteur excepteur fugiat commodo aliqua Lorem in ipsum in. Sit deserunt cillum enim adipisicing laboris ea aute exercitation pariatur quis. Nostrud elit proident deserunt elit nisi consectetur enim quis aute ullamco. Ut ipsum dolore cillum sint eu ex enim ad dolor ad. Culpa culpa cupidatat commodo ullamco occaecat sunt et qui et magna laboris consectetur.\r\n",
    "tags": [
      "danger",
      "injured",
      "medical attention"
    ]
  },
  {
    "timestamp": "2018-03-13T04:04:11 -02:00",
    "latitude": -17.150293,
    "longitude": -106.848811,
    "msg": "Elit laborum sit tempor exercitation minim qui veniam deserunt velit laborum. Deserunt non eu veniam nisi culpa officia qui occaecat voluptate veniam magna quis. Tempor ea sint dolore in qui.\r\n",
    "tags": [
      "OK"
    ]
  },
  {
    "timestamp": "2018-01-15T06:29:06 -02:00",
    "latitude": -57.658645,
    "longitude": 80.284815,
    "msg": "Cillum eiusmod adipisicing proident duis minim dolore aliqua et culpa. Est officia minim nisi do fugiat minim mollit ipsum dolor consectetur non adipisicing voluptate. Nisi do adipisicing anim sit est cillum cillum reprehenderit mollit cupidatat do. Minim veniam fugiat aliquip enim. Magna occaecat aute deserunt sit cillum labore non dolore. Amet eiusmod consectetur qui pariatur est non sint duis aliquip. Nulla exercitation dolore voluptate officia sit pariatur Lorem sit officia dolore pariatur id.\r\n",
    "tags": [
      "injured"
    ]
  },
  {
    "timestamp": "2018-03-08T03:36:55 -02:00",
    "latitude": 34.448794,
    "longitude": -84.339399,
    "msg": "Pariatur ea pariatur non mollit exercitation nisi. Dolore sint elit voluptate quis incididunt dolor occaecat est aliquip nisi qui voluptate. Veniam veniam sit Lorem quis consectetur. Aute velit velit sint culpa proident occaecat ipsum reprehenderit aute adipisicing consectetur nisi. Aliqua in excepteur qui ut nulla nostrud ut exercitation nostrud anim ea amet consectetur. Adipisicing fugiat qui sit quis ad sunt laborum duis nisi reprehenderit est voluptate. Duis voluptate sint pariatur sit ipsum.\r\n",
    "tags": [
      "danger",
      "OK"
    ]
  },
  {
    "timestamp": "2018-02-26T05:00:42 -02:00",
    "latitude": 24.056147,
    "longitude": -105.299051,
    "msg": "Adipisicing consectetur aliquip non eiusmod enim voluptate velit reprehenderit. Exercitation quis tempor minim non aliquip laboris quis cillum anim cupidatat. Pariatur in elit mollit et commodo ipsum ut. Do aliqua minim laboris aliqua.\r\n",
    "tags": [
      "injured",
      "flood",
      "OK"
    ]
  },
  {
    "timestamp": "2018-06-04T11:45:27 -03:00",
    "latitude": -82.283864,
    "longitude": 18.234185,
    "msg": "Pariatur nulla non veniam cillum nostrud Lorem qui culpa sint adipisicing irure nostrud non. Tempor incididunt sit laboris sint enim. Reprehenderit eu officia ex ipsum. Dolore aute laboris dolore duis ipsum cillum elit culpa anim. Est veniam reprehenderit est pariatur aliquip ullamco ad reprehenderit ullamco nisi.\r\n",
    "tags": [
      "OK",
      "fire",
      "OK",
      "medical attention"
    ]
  },
  {
    "timestamp": "2018-02-14T07:39:00 -02:00",
    "latitude": 41.827219,
    "longitude": 143.202133,
    "msg": "Aute occaecat nulla aute Lorem fugiat. Ullamco incididunt veniam cillum proident ad incididunt consectetur. Pariatur reprehenderit ea deserunt nostrud. Sunt magna voluptate cupidatat aliquip minim ut cupidatat. Nisi eiusmod dolore aliqua fugiat ut reprehenderit irure.\r\n",
    "tags": [
      "injured",
      "eathquake"
    ]
  },
  {
    "timestamp": "2017-11-23T02:00:07 -02:00",
    "latitude": -51.82753,
    "longitude": -130.170243,
    "msg": "Laboris magna pariatur id veniam consectetur eu. Amet aliqua minim id sunt ad laboris officia cupidatat laboris velit. Laboris tempor ea velit aliquip quis sint irure est proident id ullamco qui. Occaecat ex ea labore irure reprehenderit do mollit reprehenderit Lorem ex eiusmod adipisicing. Nisi laboris reprehenderit occaecat aliquip laboris consequat reprehenderit deserunt. Nisi irure ad nisi nostrud reprehenderit minim excepteur veniam non anim duis non. Ipsum fugiat magna nostrud ad aute ut elit aliqua cupidatat qui veniam.\r\n",
    "tags": [
      "flood"
    ]
  },
  {
    "timestamp": "2018-01-09T12:39:46 -02:00",
    "latitude": -44.53641,
    "longitude": 143.412411,
    "msg": "Exercitation nisi nostrud cillum id tempor voluptate pariatur enim officia ex elit. Anim id sunt ullamco elit dolore mollit. Laboris laborum deserunt proident incididunt. Sit esse aliqua irure tempor officia veniam dolore tempor magna commodo. Consectetur fugiat aute eiusmod eiusmod aliquip proident aliqua cillum qui elit esse. Pariatur minim aliqua culpa do reprehenderit cillum elit occaecat incididunt dolore fugiat. Adipisicing officia aute esse incididunt in ut eu duis nostrud amet excepteur cupidatat.\r\n",
    "tags": [
      "other",
      "other",
      "OK",
      "danger"
    ]
  },
  {
    "timestamp": "2018-10-15T12:09:17 -03:00",
    "latitude": -40.106378,
    "longitude": -115.478891,
    "msg": "Magna ullamco officia nulla esse incididunt laborum esse aute Lorem deserunt dolor fugiat in dolor. Mollit elit dolore duis ipsum enim reprehenderit et eiusmod consectetur amet in. Cillum consectetur enim adipisicing quis do aliquip mollit sint exercitation fugiat nulla. Sit nulla voluptate consectetur irure fugiat Lorem laboris.\r\n",
    "tags": [
      "flood",
      "flood",
      "eathquake",
      "other"
    ]
  },
  {
    "timestamp": "2018-08-01T01:01:15 -03:00",
    "latitude": -59.88073,
    "longitude": 62.774599,
    "msg": "Duis occaecat mollit pariatur voluptate cupidatat laboris cupidatat sunt. Do anim labore velit mollit id ut irure sit ad eiusmod ad qui minim. Non in dolore irure consequat culpa esse commodo ut est est minim excepteur. Quis aliqua proident esse quis nostrud quis irure ea occaecat ipsum ut quis.\r\n",
    "tags": [
      "injured",
      "fire",
      "other"
    ]
  },
  {
    "timestamp": "2018-11-13T05:22:04 -02:00",
    "latitude": 16.749119,
    "longitude": 31.897899,
    "msg": "Quis cillum cupidatat proident sit occaecat ea id proident cupidatat eu irure cillum tempor est. Sit sit et aliquip sint ullamco irure minim excepteur ex enim non. Duis ex laboris reprehenderit et sunt sunt anim labore irure. Ipsum Lorem aliquip cillum ea anim aute deserunt nostrud. Esse nulla cillum duis aute irure ea aute cillum commodo consequat elit dolore dolor irure.\r\n",
    "tags": [
      "OK",
      "water",
      "injured",
      "flood"
    ]
  },
  {
    "timestamp": "2018-01-12T05:34:18 -02:00",
    "latitude": 84.166465,
    "longitude": -42.81082,
    "msg": "Laboris consectetur in ex non ea consectetur Lorem sunt labore nulla nulla aliquip dolore proident. Veniam sint Lorem adipisicing aliquip minim eu enim nisi aliqua. Ad cupidatat exercitation velit eiusmod irure minim nulla. Cillum magna aliqua enim ad ad laboris in eu duis irure pariatur sunt. Culpa veniam officia pariatur pariatur ex dolore duis excepteur id excepteur Lorem occaecat officia. Proident mollit officia irure non. Officia eiusmod ad et aute minim Lorem proident aliqua nostrud ipsum consequat enim cillum sint.\r\n",
    "tags": [
      "food",
      "danger",
      "fire"
    ]
  },
  {
    "timestamp": "2018-04-01T02:31:30 -03:00",
    "latitude": -80.360468,
    "longitude": 176.990811,
    "msg": "Ad cupidatat laboris cillum cupidatat amet dolor exercitation. Reprehenderit velit amet culpa id ullamco irure nostrud est ullamco veniam. Sit culpa dolor ea officia fugiat nisi aute pariatur.\r\n",
    "tags": [
      "water"
    ]
  },
  {
    "timestamp": "2018-10-26T09:08:28 -03:00",
    "latitude": 66.981666,
    "longitude": 179.046514,
    "msg": "Cillum excepteur est culpa cupidatat aliqua. Non aliqua cillum proident laborum exercitation qui ea amet tempor ipsum duis. Ut culpa labore qui pariatur excepteur in labore. Qui reprehenderit labore amet pariatur magna consectetur non aliquip veniam sit nulla anim.\r\n",
    "tags": [
      "medical attention"
    ]
  },
  {
    "timestamp": "2017-12-02T07:47:19 -02:00",
    "latitude": -80.713594,
    "longitude": -94.020606,
    "msg": "Duis reprehenderit proident labore excepteur est proident amet enim. Sit est elit occaecat est proident adipisicing minim voluptate duis sit aliqua aliquip enim nostrud. Qui velit qui deserunt aute veniam ullamco deserunt anim qui. Amet reprehenderit consectetur amet minim tempor minim id.\r\n",
    "tags": [
      "danger",
      "water"
    ]
  },
  {
    "timestamp": "2018-02-20T09:39:25 -02:00",
    "latitude": -65.077907,
    "longitude": 1.491787,
    "msg": "Amet pariatur deserunt labore amet non consequat incididunt incididunt et nostrud ipsum ut. Velit ex sint irure occaecat ea. Ad ea cupidatat ullamco elit pariatur deserunt dolor cupidatat aliquip adipisicing. Incididunt elit nostrud adipisicing officia et consequat. Deserunt qui enim exercitation labore voluptate ut irure sint eu commodo commodo duis magna et.\r\n",
    "tags": [
      "medical attention",
      "medical attention",
      "eathquake",
      "OK"
    ]
  },
  {
    "timestamp": "2018-02-02T11:12:37 -02:00",
    "latitude": -6.346192,
    "longitude": -140.245838,
    "msg": "Reprehenderit voluptate ex voluptate incididunt exercitation nostrud consequat Lorem officia cillum. Culpa pariatur laborum ea elit esse ad est sit irure aliquip cupidatat laboris laboris ullamco. Veniam mollit do magna voluptate nostrud Lorem ea aliquip enim aliquip fugiat duis ea. Aliqua aliqua fugiat dolor sit ullamco proident et commodo nulla laboris consequat mollit cupidatat. Veniam deserunt nulla exercitation dolor qui sint duis est.\r\n",
    "tags": [
      "injured",
      "OK",
      "fire",
      "water"
    ]
  },
  {
    "timestamp": "2018-01-11T06:01:33 -02:00",
    "latitude": -60.637432,
    "longitude": 6.424233,
    "msg": "Lorem sint est labore consectetur proident officia nulla pariatur. Id eiusmod esse duis tempor exercitation cillum fugiat in laboris sint. Aliquip laborum anim adipisicing Lorem reprehenderit amet nisi laboris minim irure magna dolor. Cillum in velit eiusmod do consectetur adipisicing et tempor labore consequat culpa adipisicing. Nisi aliqua ut excepteur excepteur qui.\r\n",
    "tags": [
      "danger",
      "medical attention"
    ]
  },
  {
    "timestamp": "2018-09-17T09:19:14 -03:00",
    "latitude": -77.468439,
    "longitude": 146.869531,
    "msg": "Velit cillum excepteur id irure culpa voluptate elit occaecat sint magna velit magna consectetur. Pariatur et exercitation consectetur dolor enim sunt et officia aute. Tempor mollit fugiat dolor eiusmod dolor. Labore nisi sit enim non. Est excepteur mollit proident magna enim in id. Aliqua nisi amet tempor ipsum ea et labore commodo.\r\n",
    "tags": [
      "medical attention",
      "food"
    ]
  },
  {
    "timestamp": "2018-11-12T04:27:07 -02:00",
    "latitude": 77.795856,
    "longitude": 154.164732,
    "msg": "Pariatur consectetur nulla mollit irure ipsum anim tempor Lorem in excepteur Lorem minim quis. Velit veniam tempor tempor minim commodo voluptate incididunt non ipsum excepteur veniam dolor. Dolore dolore eiusmod enim minim amet aute in commodo sit commodo aute non esse anim.\r\n",
    "tags": [
      "injured",
      "medical attention",
      "fire"
    ]
  },
  {
    "timestamp": "2018-09-05T01:27:05 -03:00",
    "latitude": -21.485134,
    "longitude": -76.6291,
    "msg": "Consequat aliqua occaecat minim consequat voluptate ut do officia laborum incididunt pariatur incididunt. Commodo cupidatat anim proident aliqua ea officia consequat ut commodo excepteur Lorem. Laborum officia labore irure proident voluptate adipisicing ullamco qui sint dolor labore aute anim id. Officia aliquip mollit excepteur magna. Amet eu laborum amet sunt est do et fugiat ut amet cupidatat voluptate. Mollit anim in amet laboris Lorem laboris et exercitation ipsum.\r\n",
    "tags": [
      "eathquake",
      "medical attention"
    ]
  },
  {
    "timestamp": "2018-11-23T12:57:14 -02:00",
    "latitude": -77.192306,
    "longitude": 179.436746,
    "msg": "Cillum nulla ea consectetur consequat est veniam fugiat occaecat elit mollit veniam mollit reprehenderit. Quis nulla excepteur anim aliquip. Pariatur ut non ipsum voluptate anim nulla reprehenderit elit in enim Lorem.\r\n",
    "tags": [
      "water",
      "medical attention",
      "flood",
      "water"
    ]
  },
  {
    "timestamp": "2018-05-21T05:49:34 -03:00",
    "latitude": 88.916699,
    "longitude": -86.494474,
    "msg": "Labore aliqua cillum eiusmod officia qui pariatur. Esse cupidatat eiusmod eiusmod voluptate do excepteur commodo veniam. Pariatur est pariatur culpa cupidatat tempor anim qui magna id occaecat quis adipisicing. Sint non voluptate mollit in ullamco culpa aliquip amet veniam tempor aliqua aliquip incididunt sit. Sit ipsum dolor non esse veniam reprehenderit officia laborum Lorem cillum ipsum magna laborum. Ipsum commodo quis aute nisi irure eu.\r\n",
    "tags": [
      "eathquake"
    ]
  },
  {
    "timestamp": "2018-07-11T09:15:35 -03:00",
    "latitude": 88.173817,
    "longitude": 25.100854,
    "msg": "Qui anim adipisicing ex adipisicing reprehenderit ut dolor pariatur nulla esse voluptate labore. Culpa velit consectetur voluptate pariatur consectetur officia est ea aliqua ut consectetur. Culpa enim laborum minim ipsum veniam labore eu consequat adipisicing laborum adipisicing. Fugiat nulla non elit non consequat sint est eiusmod sunt consequat nisi incididunt reprehenderit et. Sit officia consectetur ut adipisicing sint tempor. Irure duis enim aute deserunt fugiat excepteur nulla. Occaecat pariatur magna id ut aute enim elit laboris mollit pariatur.\r\n",
    "tags": [
      "food",
      "flood"
    ]
  },
  {
    "timestamp": "2018-04-28T05:24:37 -03:00",
    "latitude": 58.088782,
    "longitude": 112.355018,
    "msg": "Ad in laborum fugiat do in cillum reprehenderit duis deserunt aute in aliqua incididunt. Exercitation enim deserunt non nostrud sint quis esse. Mollit commodo Lorem ad pariatur anim id. Elit dolor esse cupidatat aute ex in cillum fugiat consequat est cupidatat duis. Nisi anim irure qui Lorem sint labore et esse cupidatat in irure.\r\n",
    "tags": [
      "water"
    ]
  },
  {
    "timestamp": "2018-06-15T03:15:46 -03:00",
    "latitude": 35.347266,
    "longitude": -116.10551,
    "msg": "Nulla cupidatat cupidatat nisi eiusmod sint Lorem occaecat ex duis pariatur Lorem nostrud. Pariatur ipsum et nostrud incididunt nulla nulla irure proident aute est et excepteur velit. Adipisicing officia fugiat deserunt eu velit aute cillum commodo fugiat ex tempor ipsum culpa velit. Nostrud ut ad dolore sint id. Consequat anim duis excepteur minim nisi.\r\n",
    "tags": [
      "danger",
      "food"
    ]
  },
  {
    "timestamp": "2018-05-23T12:12:46 -03:00",
    "latitude": -45.224594,
    "longitude": 130.890119,
    "msg": "Dolor sit et culpa excepteur amet ea sit laborum. Laborum duis culpa quis sit do. Ea enim laborum quis et aliquip eiusmod aute do quis esse qui. Laborum ut ex ad exercitation tempor voluptate irure incididunt deserunt dolore cillum consequat nostrud.\r\n",
    "tags": [
      "other",
      "medical attention",
      "injured",
      "injured"
    ]
  },
  {
    "timestamp": "2018-04-18T01:05:46 -03:00",
    "latitude": 62.684607,
    "longitude": -31.57924,
    "msg": "Ad commodo eiusmod veniam eu amet culpa enim cillum eiusmod cupidatat sint anim sint ipsum. Laboris ex elit sint ullamco consectetur nostrud labore eu anim elit laboris cupidatat cillum. Labore eiusmod dolore sunt ullamco eiusmod ut voluptate. Quis nulla cillum amet aliqua Lorem cupidatat.\r\n",
    "tags": [
      "water",
      "danger",
      "other",
      "OK"
    ]
  },
  {
    "timestamp": "2018-05-16T10:03:38 -03:00",
    "latitude": -86.1891,
    "longitude": -133.29568,
    "msg": "Ipsum sint Lorem nisi dolor fugiat culpa quis. Ut aute in eu ullamco voluptate anim commodo laboris et excepteur est occaecat quis. Ea nostrud mollit minim labore laborum ipsum anim est quis consectetur. Et occaecat nostrud eiusmod id culpa nostrud culpa nostrud adipisicing id esse. Dolore nulla ipsum officia do sit sit incididunt do magna culpa enim Lorem. Consectetur minim cupidatat eiusmod magna elit ullamco proident. Eu laborum duis in exercitation.\r\n",
    "tags": [
      "water"
    ]
  },
  {
    "timestamp": "2018-10-25T04:34:31 -03:00",
    "latitude": 78.01543,
    "longitude": -163.868698,
    "msg": "In proident irure exercitation deserunt magna minim eu commodo in esse cillum exercitation do. Ullamco occaecat et ad culpa et sit voluptate elit id eiusmod sunt aute occaecat. Anim sint amet est ex ullamco consequat amet sunt cillum excepteur. Dolor do do nostrud nostrud aute eiusmod. Id eiusmod nisi mollit laboris elit.\r\n",
    "tags": [
      "food"
    ]
  },
  {
    "timestamp": "2018-01-17T06:03:13 -02:00",
    "latitude": 79.785246,
    "longitude": 59.102654,
    "msg": "Lorem cupidatat dolore eiusmod proident eu ex. Consequat mollit ea nisi eiusmod adipisicing enim consectetur laborum reprehenderit magna ut deserunt ipsum. Enim irure aute nulla duis velit nisi amet non ad est velit nulla consectetur velit. Ad officia adipisicing velit reprehenderit. Aute ea reprehenderit quis nulla dolore ex. Cupidatat aliqua nisi est eu nulla officia anim ut et nisi dolore do laborum adipisicing.\r\n",
    "tags": [
      "medical attention",
      "danger",
      "water"
    ]
  },
  {
    "timestamp": "2018-02-06T04:39:52 -02:00",
    "latitude": 57.343893,
    "longitude": 90.398742,
    "msg": "Id sunt magna et in proident voluptate ex exercitation. Cillum duis consectetur sunt consectetur do mollit. Ea non proident ullamco est officia dolore pariatur laborum exercitation ullamco quis nostrud. Est deserunt ullamco aliqua occaecat laborum nisi commodo ut aliquip amet dolor labore deserunt. Velit sint aliquip cupidatat dolore sint laboris reprehenderit sunt tempor laboris ea excepteur nisi. Exercitation duis cillum proident aute quis ad. Laborum consequat ut do dolore anim non exercitation.\r\n",
    "tags": [
      "medical attention",
      "medical attention",
      "fire"
    ]
  },
  {
    "timestamp": "2018-08-24T08:00:03 -03:00",
    "latitude": 28.328166,
    "longitude": -119.706553,
    "msg": "Reprehenderit qui cupidatat et dolore ea anim proident officia culpa aliquip aute. Elit ad esse incididunt est sint qui enim laboris. Sit cillum ex tempor dolor in fugiat dolor in reprehenderit est laborum nulla nostrud. Occaecat est occaecat consectetur veniam sit Lorem. Ullamco anim nostrud ullamco enim magna aliquip dolore nisi aliqua labore culpa quis. Fugiat anim quis cupidatat sunt aliquip dolore occaecat.\r\n",
    "tags": [
      "OK",
      "OK",
      "danger"
    ]
  },
  {
    "timestamp": "2017-11-19T08:32:44 -02:00",
    "latitude": 56.124691,
    "longitude": -2.907814,
    "msg": "Id aliqua labore nisi commodo anim aliqua eu id id ea laboris nisi deserunt duis. Anim consequat laborum proident sit qui mollit adipisicing velit quis. Consequat ad dolor adipisicing voluptate qui occaecat aliqua cillum. Aliqua mollit occaecat et sunt aliquip consequat laboris cillum laborum ex occaecat voluptate nisi. Ipsum ipsum do exercitation id irure non veniam in occaecat veniam dolor ad ea ea.\r\n",
    "tags": [
      "food",
      "danger",
      "eathquake"
    ]
  },
  {
    "timestamp": "2018-07-02T06:04:39 -03:00",
    "latitude": -33.904153,
    "longitude": -168.927535,
    "msg": "Excepteur duis excepteur reprehenderit ut ea reprehenderit veniam adipisicing ex cillum voluptate mollit nulla. Lorem tempor duis consequat id quis labore et est eiusmod. Nulla eu voluptate deserunt ex culpa exercitation commodo nisi do voluptate ex cupidatat sit. Nulla do ut commodo tempor nisi culpa ad proident consectetur sunt consequat nisi exercitation qui. Magna nostrud non mollit mollit deserunt quis. Id magna in ut dolore et et occaecat qui aute ut irure pariatur ipsum minim.\r\n",
    "tags": [
      "water",
      "medical attention",
      "medical attention"
    ]
  },
  {
    "timestamp": "2018-06-20T03:24:57 -03:00",
    "latitude": -59.457213,
    "longitude": -153.772097,
    "msg": "Sunt minim aute excepteur ipsum voluptate. Qui tempor nostrud aliqua commodo amet sunt id duis qui mollit laboris ullamco pariatur cupidatat. Excepteur nostrud amet minim id proident elit sint et ex reprehenderit. Ut laboris commodo id eiusmod ad magna pariatur Lorem incididunt excepteur amet pariatur ex non. Veniam culpa mollit dolore dolore id sit ut. Irure irure tempor cillum nisi laboris dolore eu irure reprehenderit amet velit Lorem.\r\n",
    "tags": [
      "other",
      "medical attention",
      "danger",
      "eathquake"
    ]
  },
  {
    "timestamp": "2018-10-13T12:09:13 -03:00",
    "latitude": -30.18886,
    "longitude": 106.594112,
    "msg": "Ut occaecat aute sunt ea nulla. Non et ut nostrud labore elit quis minim nulla adipisicing laborum commodo sunt nostrud laboris. Magna cupidatat irure est ea exercitation. Ullamco sit magna excepteur eiusmod.\r\n",
    "tags": [
      "fire",
      "OK",
      "eathquake",
      "flood"
    ]
  },
  {
    "timestamp": "2018-06-05T07:02:15 -03:00",
    "latitude": -23.355119,
    "longitude": -93.548081,
    "msg": "Elit amet aute duis enim consequat non quis ex culpa quis ut fugiat. Eiusmod eu mollit excepteur eiusmod aliqua incididunt officia mollit. Ullamco veniam elit amet pariatur amet aliquip incididunt exercitation dolor. Elit labore aliqua laborum aliqua proident amet ullamco ut voluptate cupidatat ut sint ad cupidatat.\r\n",
    "tags": [
      "fire"
    ]
  },
  {
    "timestamp": "2018-04-05T02:51:56 -03:00",
    "latitude": 3.226349,
    "longitude": 83.081001,
    "msg": "Cillum ex exercitation ullamco non ut sit non ut. Amet quis sint eu id ad voluptate sit commodo anim minim fugiat nostrud. Officia eu in sint Lorem do. Occaecat non tempor est velit culpa sint sint eiusmod. Id velit exercitation commodo commodo incididunt dolor minim ipsum. Est elit voluptate est laborum. Labore sit magna quis exercitation ea tempor deserunt duis magna magna amet ullamco.\r\n",
    "tags": [
      "fire",
      "medical attention",
      "food",
      "other"
    ]
  },
  {
    "timestamp": "2018-05-03T03:52:40 -03:00",
    "latitude": -34.714886,
    "longitude": 167.247566,
    "msg": "Excepteur dolor non irure irure enim labore Lorem deserunt. Culpa adipisicing anim qui incididunt esse. Velit velit consectetur ullamco mollit velit est reprehenderit culpa elit esse occaecat. Id enim non consequat ea ut commodo aliquip nulla amet minim. Laboris laborum dolor consequat ut ipsum tempor. Laborum proident pariatur incididunt aliqua nulla do culpa pariatur cillum nostrud velit occaecat est.\r\n",
    "tags": [
      "other",
      "food"
    ]
  },
  {
    "timestamp": "2018-10-29T11:36:39 -02:00",
    "latitude": -17.941403,
    "longitude": 74.083646,
    "msg": "Occaecat cillum est quis sunt elit sint dolore adipisicing. Amet id occaecat laborum nisi amet exercitation. Ipsum duis non fugiat do pariatur eiusmod non eiusmod.\r\n",
    "tags": [
      "medical attention"
    ]
  },
  {
    "timestamp": "2018-10-15T01:54:51 -03:00",
    "latitude": 77.879719,
    "longitude": -0.10823,
    "msg": "Lorem dolor exercitation nulla consequat culpa in ullamco id incididunt deserunt ullamco ea veniam. Nostrud culpa exercitation eu cupidatat proident anim ullamco ex consequat ea consequat enim. Aliqua consectetur ea nostrud Lorem. Cillum est minim laboris nisi laboris ea exercitation ea eu id quis est sunt. Fugiat est enim deserunt cupidatat. Nisi enim fugiat dolore et eu fugiat.\r\n",
    "tags": [
      "water",
      "water",
      "medical attention",
      "food"
    ]
  },
  {
    "timestamp": "2018-08-19T08:33:44 -03:00",
    "latitude": 33.657509,
    "longitude": -132.555116,
    "msg": "Dolor voluptate irure laborum sit dolore incididunt aute nostrud. Ipsum enim occaecat occaecat incididunt aliquip non id id ad. Irure exercitation ex sit dolor ut non tempor minim qui. Sit qui duis reprehenderit commodo tempor commodo eu ad ut ea aute. Ipsum dolore officia mollit ex voluptate officia commodo ea ea nisi incididunt occaecat ex et. Consectetur ea eiusmod nostrud non consequat fugiat cupidatat do in cillum officia.\r\n",
    "tags": [
      "water",
      "food",
      "water"
    ]
  },
  {
    "timestamp": "2018-03-07T08:37:06 -02:00",
    "latitude": 1.820759,
    "longitude": 77.867661,
    "msg": "Amet deserunt irure duis elit consectetur et mollit velit nisi ut nulla eiusmod velit laborum. Adipisicing consequat commodo cillum sit minim esse sint deserunt. In labore eiusmod minim ut voluptate. Aliqua sit aute minim occaecat dolor dolor sint occaecat sint duis cillum cillum. Eu non ipsum nostrud quis duis proident nisi labore commodo nulla id do ut magna. Laborum deserunt est fugiat et.\r\n",
    "tags": [
      "danger"
    ]
  },
  {
    "timestamp": "2018-02-19T05:47:37 -02:00",
    "latitude": -67.120179,
    "longitude": 63.724622,
    "msg": "Laborum laboris enim dolore reprehenderit amet. Incididunt nulla voluptate aute veniam minim veniam. Et id mollit sint ipsum incididunt ad cillum irure excepteur aute reprehenderit sunt nulla ea. Labore do et esse voluptate. Culpa consectetur Lorem est sit pariatur aliqua sunt pariatur irure amet.\r\n",
    "tags": [
      "eathquake",
      "other"
    ]
  },
  {
    "timestamp": "2018-11-20T04:03:12 -02:00",
    "latitude": 35.59737,
    "longitude": 167.340463,
    "msg": "Id officia fugiat consectetur cupidatat pariatur officia mollit proident duis laborum consectetur labore consectetur in. Et occaecat pariatur cupidatat incididunt occaecat non reprehenderit consequat Lorem. Incididunt mollit laboris aute dolore anim fugiat. Consectetur cupidatat enim enim voluptate non aliquip deserunt enim ad consequat. Minim veniam exercitation enim Lorem culpa aliquip elit amet non pariatur fugiat nostrud nulla.\r\n",
    "tags": [
      "eathquake",
      "other"
    ]
  },
  {
    "timestamp": "2018-06-07T01:56:44 -03:00",
    "latitude": -43.782929,
    "longitude": 111.175251,
    "msg": "Id aute incididunt amet anim occaecat aliqua officia minim. Tempor commodo ipsum dolor laboris officia occaecat proident. Cillum eiusmod exercitation est adipisicing Lorem consectetur elit sit occaecat dolore irure dolore. Sint cupidatat irure consectetur anim voluptate sunt culpa aliqua veniam est qui et.\r\n",
    "tags": [
      "flood",
      "injured",
      "danger",
      "fire"
    ]
  },
  {
    "timestamp": "2018-06-12T10:32:46 -03:00",
    "latitude": -15.980212,
    "longitude": -14.394771,
    "msg": "Pariatur exercitation sint commodo ea incididunt non deserunt eiusmod reprehenderit ea do irure Lorem. Anim non ut sint consequat elit anim nisi sit culpa est. Quis ad consectetur ex quis occaecat commodo ad ullamco velit fugiat magna. Eiusmod in excepteur velit sit eu exercitation ullamco magna laborum mollit sunt magna voluptate. Deserunt ad in veniam sint ipsum. Pariatur dolor laboris magna et amet Lorem.\r\n",
    "tags": [
      "water",
      "eathquake",
      "fire",
      "flood"
    ]
  },
  {
    "timestamp": "2018-10-24T12:40:58 -03:00",
    "latitude": -38.809454,
    "longitude": -51.11333,
    "msg": "Labore aliqua commodo ad magna cupidatat esse velit tempor proident ut. Mollit ullamco est quis occaecat nostrud tempor quis laborum sint incididunt eu excepteur dolor. Aute sit laboris aliquip ullamco ea aliquip anim sit aute aute fugiat est. Consequat aute aliqua aute irure aliquip ex in ut officia. Occaecat Lorem occaecat laborum eiusmod elit labore. Officia Lorem aute duis reprehenderit esse adipisicing excepteur cillum. Deserunt elit aliqua et sint sunt minim culpa voluptate.\r\n",
    "tags": [
      "danger",
      "danger",
      "other"
    ]
  },
  {
    "timestamp": "2018-08-11T06:20:02 -03:00",
    "latitude": -71.970165,
    "longitude": 113.269663,
    "msg": "Consequat velit sint est pariatur voluptate. Commodo sunt sit ullamco ex sunt pariatur deserunt exercitation aliqua dolore dolore proident ea cillum. Nisi labore fugiat id proident proident irure eiusmod. Fugiat pariatur elit incididunt reprehenderit anim do reprehenderit veniam. Lorem tempor nostrud sit qui minim sit eu laboris. Ex proident nisi incididunt elit magna incididunt nostrud ad cupidatat id duis. Est nulla cupidatat sit est.\r\n",
    "tags": [
      "OK",
      "injured",
      "OK"
    ]
  },
  {
    "timestamp": "2018-10-11T09:28:07 -03:00",
    "latitude": -72.654897,
    "longitude": 172.740807,
    "msg": "Cupidatat Lorem dolor proident culpa veniam proident culpa in magna aute aute exercitation deserunt exercitation. Consectetur qui dolore adipisicing consequat nisi sint est adipisicing dolor. Pariatur nostrud aliquip sit aliquip aute commodo ea ipsum culpa qui do excepteur. Amet do irure eu reprehenderit eiusmod ex nulla cupidatat non est. Ullamco pariatur incididunt excepteur irure.\r\n",
    "tags": [
      "food",
      "flood",
      "fire"
    ]
  },
  {
    "timestamp": "2018-10-14T06:46:57 -03:00",
    "latitude": -1.251954,
    "longitude": 20.403012,
    "msg": "Magna fugiat voluptate id irure magna labore aliqua ex culpa consectetur. Ut adipisicing excepteur et officia nulla eu ea cupidatat minim laboris officia ea. Nulla et sint pariatur et laborum duis commodo et Lorem laborum dolore laborum. Cillum duis amet deserunt occaecat sunt aute commodo dolore exercitation ex officia consequat sint.\r\n",
    "tags": [
      "other",
      "medical attention"
    ]
  },
  {
    "timestamp": "2018-03-21T06:49:05 -02:00",
    "latitude": -22.715152,
    "longitude": 90.904228,
    "msg": "Ea sunt sunt magna sunt velit enim incididunt ut duis non elit duis cupidatat. Laboris veniam ullamco aliqua sit eiusmod duis dolor Lorem aliqua duis sint qui. Sunt amet excepteur ipsum fugiat excepteur nostrud dolor magna qui dolore ea voluptate sint mollit. Labore consectetur sit consequat veniam quis sint pariatur qui nisi sunt. Et deserunt incididunt deserunt veniam laborum dolor irure incididunt incididunt anim officia fugiat. Ipsum ullamco sunt consequat elit aliqua magna id veniam sunt qui eiusmod mollit.\r\n",
    "tags": [
      "food",
      "fire",
      "danger",
      "eathquake"
    ]
  },
  {
    "timestamp": "2018-08-09T06:57:53 -03:00",
    "latitude": 24.036009,
    "longitude": 144.682783,
    "msg": "Amet consectetur qui nisi nisi laboris mollit dolor aute ad. Anim sit enim Lorem occaecat ut amet in id reprehenderit sit duis pariatur et. Ullamco mollit minim incididunt esse id eu occaecat eu cillum officia. Elit excepteur occaecat id ad cillum aute fugiat mollit aliquip. Adipisicing magna proident dolor eiusmod ea voluptate excepteur irure.\r\n",
    "tags": [
      "injured",
      "medical attention",
      "other"
    ]
  },
  {
    "timestamp": "2018-04-16T11:20:58 -03:00",
    "latitude": -89.082299,
    "longitude": -155.978939,
    "msg": "Id cupidatat sit occaecat fugiat labore nostrud ex amet ut adipisicing commodo ipsum. Mollit ad nulla est labore ea voluptate exercitation aliquip sint eiusmod esse. Enim est eu aute magna laborum cupidatat duis dolor.\r\n",
    "tags": [
      "medical attention",
      "food",
      "water",
      "fire"
    ]
  },
  {
    "timestamp": "2018-11-21T03:28:04 -02:00",
    "latitude": -42.615516,
    "longitude": -32.995731,
    "msg": "Et laboris ea amet Lorem id ea reprehenderit ullamco fugiat deserunt excepteur ea dolore adipisicing. In ut commodo dolor id elit proident consequat. Qui laborum occaecat aute Lorem adipisicing mollit elit dolore cillum labore proident pariatur.\r\n",
    "tags": [
      "food",
      "flood"
    ]
  }
]

broker_address = "10.3.141.1"
broker_port = 1883
keep_alive = 60

def messageParameters(data_msg):
    b_lon = 24 #randint(23, 24)
    b_lat = 60 #randint(62, 63)
    e_lon = randint(115, 1000)
    e_lat = randint(115, 1000)

    lat = str(b_lat) + '.' + str(e_lat)
    lon = str(b_lon) + '.' + str(e_lon)

    data_msg["latitude"] = float(lat)
    data_msg['longitude'] = float(lon)

    return data_msg

client = mqtt.Client("PyMsg") #create new instance
client.connect(broker_address, broker_port, keep_alive) #connect to broker

for x in range(100):
    print('Sending message to: ' + str(broker_address) + ':' + str(broker_port))
    for data in data_list:
        payload = json.dumps(messageParameters(data))
        client.publish("testTopic", payload, 1)#publish
        print(payload)
        time.sleep(randint(1, 3))
