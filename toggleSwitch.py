import machine
adc = machine.ADC()

class ToggleSwitch:
    def __init__(self, pinNumber):
        self.switchPin = adc.channel(pin=pinNumber)

    def isOn(self):
        return self.switchPin() == 1023
