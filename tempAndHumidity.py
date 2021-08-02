from dht import DHT
from machine import Pin

class TempAndHumidity:
    def __init__(self, pinNumber):
        self.th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)

    def getMeasurements(self):
        result = self.th.read()
        while result.humidity == 0:
            result = self.th.read()
        return result
