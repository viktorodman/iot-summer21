from machine import Pin
import machine

class Button:
    def __init__(self, pinNumber):
        self.button = Pin(pinNumber, mode=Pin.IN)

    def isClicked(self):
        return self.button() != 0
