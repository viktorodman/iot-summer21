from network import WLAN
import machine

class WIFI:
    def __init__(self):
        self.wlan = WLAN(mode=WLAN.STA)

    def connect(self, name, password):
        self.wlan.connect(ssid=name, auth=(WLAN.WPA2, password))

        while not self.wlan.isconnected():
            machine.idle()
        print('WIFI Connected')
