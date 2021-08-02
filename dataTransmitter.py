from mqtt import MQTTClient
import json
import machine

class DataTransmitter:
    def __init__(self, clientID, host, username, mqttPassword, topics, mqttPort=1883):
        self.client = MQTTClient(clientID, host, user=username, password=mqttPassword, port=mqttPort)
        self.topics = topics

    def connect(self, callback):
        self.client.set_callback(callback)
        self.client.connect()
        for t in self.topics:
            self.client.subscribe(topic=t)
            print("Subscribing to topic: ", t)

    def sendData(self, data, dataTopic):
        toJson = json.dumps(data)
        self.client.publish(topic=dataTopic, msg=toJson)
        self.client.check_msg()
