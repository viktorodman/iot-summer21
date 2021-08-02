import config
import machine
import time
from mqtt import MQTTClient
from machine import Pin
from toggleSwitch import ToggleSwitch
from lightSensor import LightSensor
from tempAndHumidity import TempAndHumidity
from clock import Clock
from wifi import WIFI
from dataTransmitter import DataTransmitter
from network import WLAN
from led import Led
from button import Button

# Different sensor feeds on adafruit
feeds = [
"viktorodman/feeds/sensordata2021.temp",
"viktorodman/feeds/sensordata2021.humidity",
"viktorodman/feeds/sensordata2021.brigthness"
]

####### Setting up modules #########
clock = Clock()
wifi = WIFI()
lightSensor = LightSensor('P14')
button = Button('P18')
toggleOne = ToggleSwitch('P13')
green_led = Led('P3')
red_led = Led('P4')
blue_led = Led('P6')
tempAndHumid = TempAndHumidity('P23')

def sub_cb(topic, msg):
    print(msg)

####### Connecting to WIFI and synchronizing clock #########
wifi.connect(config.WIFI_SSID, config.WIFI_PASSWORD) # Get WIFI credentials from config file. See exampleConfig.py
clock.sync()
dataTransmitter = DataTransmitter(config.MQTT_CLIENT_ID, config.MQTT_HOST, config.MQTT_USER, config.MQTT_PASSWORD, feeds) #clientID, host, username, mqttPassword, mqttTopic
dataTransmitter.connect(sub_cb)

def sendMeasurements():
    tempAndHumidValues = tempAndHumid.getMeasurements()

    dataTransmitter.sendData({"value": tempAndHumidValues.temperature}, feeds[0]) # Sends temperature data
    dataTransmitter.sendData({"value": tempAndHumidValues.humidity}, feeds[1]) # Sends humidity data
    dataTransmitter.sendData({"value": lightSensor.isBright()}, feeds[2]) # Sends brigthness data

    blue_led.blink(3)
    time.sleep(1)


while True:
    if toggleOne.isOn():
        green_led.on()
        red_led.off()
        if (clock.getMinutes() %2 == 0) and (clock.getSeconds() == 0):
            print('Sending Data...')
            sendMeasurements()
        elif button.isClicked():
            print('pressed')
            sendMeasurements()
        else:
            time.sleep(1)
    else:
        red_led.on()
        green_led.off()
        time.sleep(1)
