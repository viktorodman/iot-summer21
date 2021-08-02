from machine import Pin
from machine import ADC
import machine

class LightSensor:
    def __init__(self, pinNumber):
        adc = machine.ADC(bits=10)
        self.lightSensor = adc.channel(attn=ADC.ATTN_11DB, pin=pinNumber)

    def getMeasurement(self):
        return self.lightSensor()

    def isBright(self):
        return 1 if self.lightSensor() < 900 else 0
