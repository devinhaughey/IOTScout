let mqtt;
let reconnectTimeout = 2000;
let host = '10.3.141.1'; //"127.0.0.1";
let port = 9001; //61623;
let username = 'pi'; //'user'
let password = '12345678'; //'password';
let count = 1;

function MQTTPayload( priority, lat, long, msg, tags ) {
  this.priority = priority;
  this.lat = lat;
  this.long = long;
  this.msg = msg;
  this.tags = tags;
}

function onFailure(message) {
  console.log("Connection Attempt to Host "+host+" Failed");
  setTimeout(MQTTconnect, reconnectTimeout);
}

function onMessageArrived(msg){
  let out_msg="Message received "+msg.payloadString+"<br>";
  out_msg=out_msg+"Message received Topic "+msg.destinationName;
  console.log(out_msg);
  //let msg_payload = JSON.parse(msg);
  //console.log(msg_payload);

  var IS_JSON = true;
  let data_input;
  try { var json = JSON.parse(msg.payloadString);
        data_points = json;}
  catch(err) { IS_JSON = false}

  console.log(IS_JSON);
  //console.table(json);
  console.log(data_points['latitude']);
  let lat = data_points['latitude'];
  let lon = data_points['longitude'];
  let time = data_points['timestamp'];
  let tag = data_points['tags'].toString();
  let option = tag.search( 'danger' );

  createDeliveryPoints(option);
  createHTMLTable(option);
}

function onConnect() {
  // Once a connection has been made, make a subscription and send a message.

  console.log("Connected ");
  mqtt.subscribe("testTopic");
  let message = new Paho.MQTT.Message("Hello World");
  message.destinationName = "testTopic";
  //mqtt.send(message);
}

function MQTTconnect() {
  console.log("connecting to "+ host +" "+ port);
  mqtt = new Paho.MQTT.Client(host,port,"clientjs");
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
  mqtt.onMessageArrived = onMessageArrived;
}

function createHTMLTable(option) {
  let table_name = document.getElementById('address_table').getElementsByTagName('tbody')[0];
  let newRow = table_name.insertRow(count);

  let timestamp = newRow.insertCell(0);
  let lat = newRow.insertCell(1);
  let lon = newRow.insertCell(2);
  let tag = newRow.insertCell(3);
  let message = newRow.insertCell(4);

  if ( option === 0 ) {
    timestamp.style.color = 'red';
    lat.style.color = 'red';
    lon.style.color = 'red';
    tag.style.color = 'red';
    message.style.color = 'red';
  }

  let txt_timestamp = document.createTextNode(data_points['timestamp'].substring(0, 19));
  let txt_lat = document.createTextNode(data_points['latitude']);
  let txt_lon = document.createTextNode(data_points['longitude']);
  let txt_tag = document.createTextNode(data_points['tags']);
  let txt_message =document.createTextNode(data_points['msg'].substring(0, 10));

  timestamp.appendChild(txt_timestamp);
  lat.appendChild(txt_lat);
  lon.appendChild(txt_lon);
  tag.appendChild(txt_tag);
  message.appendChild(txt_message);
  count++;
}

function mySearch() {
  var input = document.getElementById("myInput");
  var filter = input.value.toUpperCase();
  var data = document.getElementsByClassName("data");

  for (var i = 0; i < data.length; i++) {
    var tags = data[i].getElementsByTagName("td")[4];
    if (tags.innerHTML.toUpperCase().indexOf(filter) > -1) {
      data[i].style.display = "";
    } else {
      data[i].style.display = "none";
    }
  }
}
