from machine import Pin
import time

class Led:
    def __init__(self, pinNumber):
        self.led = Pin(pinNumber, mode=Pin.OUT)

    def on(self):
        self.led.value(1)

    def off(self):
        self.led.value(0)
    def blink(self, times):
        for value in range(times):
            self.led.value(1)
            time.sleep_ms(200)
            self.led.value(0)
            time.sleep_ms(200)
