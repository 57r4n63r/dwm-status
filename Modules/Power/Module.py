import os
from Core.Module.AbstractModule import AbstractModule
from subprocess import call, check_output
from Core.Core import Core
from Core.Icons import Icons

class Power(AbstractModule):

    capacityPath = '/sys/class/power_supply/{battery}/capacity'
    statusPath = '/sys/class/power_supply/{battery}/status'
    chargeNowPath = '/sys/class/power_supply/{battery}/charge_now'
    chargeFullPath = '/sys/class/power_supply/{battery}/charge_full'
    batteryName = None

    def init(self):
        core = Core.getInstance()
        if 'power' in core.configurations and 'battery' in core.configurations['power'] :
            self.batteryName    = core.configurations['power']['battery']
            self.capacityPath   = self.capacityPath.replace('{battery}',self.batteryName)
            self.statusPath     = self.statusPath.replace('{battery}',self.batteryName)
            self.chargeNowPath  = self.chargeNowPath.replace('{battery}',self.batteryName)
            self.chargeFullPath = self.chargeFullPath.replace('{battery}',self.batteryName)

    def getValue(self,path):
        return check_output(
            ['cat', path]).strip().decode('utf-8')

    def getString(self):
        if self.batteryName == None :
            return Icons.get('battery_pluged')

        capacity =  self.getValue(self.capacityPath)
        status =  self.getValue(self.statusPath)
        chargeNow =  self.getValue(self.chargeNowPath)
        chargeFull =  self.getValue(self.chargeFullPath)

        statusIcon = Icons.get( 'battery_unpluged' )
        level = "100%"

        if capacity == "0" or status == "Charging":
            statusIcon = Icons.get( 'battery_pluged' )

        floatLevel = float(capacity) / float(chargeFull) * 100
        level = str(int(floatLevel)) + '%'

        return level+' | '+statusIcon

