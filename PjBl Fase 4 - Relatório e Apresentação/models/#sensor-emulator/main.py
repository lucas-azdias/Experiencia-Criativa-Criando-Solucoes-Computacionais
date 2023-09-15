"""
https://wokwi.com/projects/366337537871660033

To view the data:
1. Go to http://www.hivemq.com/demos/websocket-client/
2. Click "Connect"
3. Under Subscriptions, click "Add New Topic Subscription"
4. In the Topic field, type "wokwi-weather" then click "Subscribe"
"""

import network
from time import sleep
from machine import Pin
import dht
import ujson
from umqtt.simple import MQTTClient

id_sensor = 1
delta_time = 60

# MQTT Server Parameters
MQTT_CLIENT_ID = f"soil-humidity-sensor-{id_sensor}"
MQTT_BROKER    = "broker.mqttdashboard.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC     = "soil-humidity-system/data"

WIFI_SSID = 'Wokwi-GUEST'
WIFI_PASSWORD = ''

sensor = dht.DHT22(Pin(15))

print("Connecting to Wi-Fi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
while not sta_if.isconnected():
  print(".", end="")
  sleep(0.1)
print(" Connected!")

print("Connecting to MQTT server... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.connect()

print("Connected!")

while True:
  print("Measuring humidity... ")
  sensor.measure() 
  message = ujson.dumps({
    "id_sensor": id_sensor,
    "value": sensor.humidity()
  })
  print(f"Sending data {MQTT_TOPIC}: {message}")
  client.publish(MQTT_TOPIC, message)
  sleep(delta_time)
