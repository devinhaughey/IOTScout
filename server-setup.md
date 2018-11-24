Set up a WiFi hotspot and MQTT broker on Raspberry Pi 3 B+
==========================================================

WiFi hotspot
------------
Follow the instruction on [raspap-webgui project](https://github.com/billz/raspap-webgui).


MQTT broker
-----------
Once we created the WiFi hotspot, we need to set up a MQTT broker. Follow the instruction [here](https://gist.github.com/smoofit/dafa493aec8d41ea057370dbfde3f3fc) to install Mosquitto with websockets.

Below is the content of the configuration file `/etc/mosquitto/mosquitto.conf`:
```
pid_file /var/run/mosquitto.pid

persistence true
persistence_location /var/lib/mosquitto/

log_dest file /var/log/mosquitto/mosquitto.log

max_queued_messages 200
message_size_limit 0
allow_duplicate_messages false

port 1883
listener 9001
protocol websockets
autosave_interval 900
allow_anonymous true
password_file /etc/mosquitto/passwd
```

Start the broker daemon `sudo mosquitto -c /etc/mosquitto/mosquitto.conf -d`



