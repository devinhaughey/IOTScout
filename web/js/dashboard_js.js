let mqtt;
let reconnectTimeout = 2000;
let host = '10.3.141.1'; //"127.0.0.1";
let port = 9001; //61623;
let username = 'pi'; //'user'
let password = '12345678'; //'password';
let instant_help = document.getElementById('btn_instant_help')
let payload = {
    "timestamp": "2018-10-22T04:34:16 -03:00",
    "latitude": 60.480,
    "longitude": 24.246,
    "msg": "Officia qui proident ullamco laboris adipisicing laboris sunt ad. Magna ipsum id aute dolore laboris exercitation ad officia reprehenderit esse dolore. Sunt Lorem eiusmod ullamco incididunt velit labore occaecat duis minim culpa anim est.\r\n",
    "tags": [
      "danger"
    ]
  };


instant_help.onclick = function() {
    console.log('Boom bitch!');
    MQTTconnect();
};

function onFailure(message) {
  console.log("Connection Attempt to Host "+host+" Failed");
  setTimeout(MQTTconnect, reconnectTimeout);
}

function onConnect() {
  // Once a connection has been made, make a subscription and send a message.

  console.log("Connected ");
  mqtt.subscribe("testTopic");
  //let message = new Paho.MQTT.Message("Hello World App Bitches!");
  let message = new Paho.MQTT.Message(JSON.stringify(payload));
  message.destinationName = "testTopic";
  mqtt.send(message);

var IS_JSON = true;
  let data_input;
  try { var json = JSON.parse(payload);
        data_points = json;}
  catch(err) { IS_JSON = false}
    console.log(IS_JSON);
}

function MQTTconnect() {
  console.log("connecting to "+ host +" "+ port);
  mqtt = new Paho.MQTT.Client(host,port,"webApp");
  //document.write("connecting to "+ host);
  let options = {
    timeout: 3,
    onSuccess: onConnect,
    onFailure: onFailure
  };
  options.userName = username;
  options.password = password;
  // mqtt.onMessageArrived = onMessageArrived;

  mqtt.connect(options); //connect
  //mqtt.onMessageArrived = onMessageArrived;
}
