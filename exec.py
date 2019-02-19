import time
from StatusBar import StatusBar

statusbar = StatusBar()
statusbar.load()
while True:
    statusbar.addIp()
    statusbar.isVpnOn()
    statusbar.addVolume()
    statusbar.addNet()
    statusbar.addPower()
    statusbar.addDate()

    statusbar.render()

    time.sleep(1)
