import machine
import time

class Clock:
    def __init__(self):
        self.rtc = machine.RTC()

    def sync(self):
        self.rtc.ntp_sync("pool.ntp.org")
        while not self.rtc.synced():
            machine.idle()
        print("RTC synced with NTP time")
        #adjust your local timezone, by default, NTP time will be GMT
        time.timezone(2*60**2) #we are located at GMT+2, thus 2*60*60
        self.time = time

    def getSeconds(self):
        return self.time.localtime()[5]

    def getMinutes(self):
        return self.time.localtime()[4]
