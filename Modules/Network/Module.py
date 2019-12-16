import re
from subprocess import call, check_output
from Core.Module.AbstractModule import AbstractModule
from Core.Core import Core
from Core.Icons import Icons

class Network(AbstractModule):
    configurations = None
    getWanIpCommand = ['curl','-s']
    getLanIpCommand = ['ip','addr','show']
    interfaceStatePath = '/sys/class/net/{interface}/operstate'
    wanIp = None
    additionnal = []
    interfaces = []
    wifiIcon = 'wifi_good'
    wiredIcon = 'wired'

    order=40

    def init(self):
        core = Core.getInstance()
        self.configurations = core.configurations

        if 'wanProvider' in self.configurations['networking']:
            self.getWanIpCommand.append(self.configurations['networking']['wanProvider'])

        if("additionnal" in self.configurations['networking']):
            self.additionnal = self.configurations['networking']['additionnal']

        if 'wired' in self.configurations['networking']:
            self.interfaces.append(self.configurations['networking']['wired'])

        if 'wifi' in self.configurations['networking']:
            self.interfaces.append(self.configurations['networking']['wifi'])

        if 'wifi-icon' in self.configurations['networking']:
            self.wifiIcon = self.configurations['networking']['wifi-icon']

        if 'wired-icon' in self.configurations['networking']:
            self.wiredIcon = self.configurations['networking']['wired-icon']

        self.interfaces = [*self.interfaces,*self.additionnal]

    def isInterfaceUp(self, interface):
        path = self.interfaceStatePath.replace('{interface}',interface)
        command = ['cat',path]
        output = check_output(command).strip().decode('utf-8')
        return True if output == 'up' else False


    def getWAN(self):
       if 'wanProvider' in self.configurations['networking']:
           self.wanIp = check_output(self.getWanIpCommand).strip().decode('utf-8') 
       return self.wanIp

    def getLan(self):
        ips = [];
        for interface in self.interfaces:
            if(self.isInterfaceUp(interface)):
                currentLanIpCommand = self.getLanIpCommand[:]
                currentLanIpCommand.append(interface)
                output = check_output(currentLanIpCommand).strip().decode('utf-8')
                ip = re.findall('(inet .+/)',output)[0].replace('inet ','').replace('/','')
                ips.append(ip)

        return ' | '.join(ips)

    def getStates(self):
        icons = []
        if 'wired' in self.configurations['networking']:
            wired = self.configurations['networking']['wired']
        else:
            wired = 'off'
        if 'wifi' in self.configurations['networking']:
            wifi = self.configurations['networking']['wifi']
        else:
            wifi = 'off'

        if(wifi != 'off'):
            if(self.isInterfaceUp(wifi)):
                icons.append(Icons.get(self.wifiIcon))
        if(wired != 'off'):
            if(self.isInterfaceUp(wired)):
                icons.append(Icons.get(self.wiredIcon))

        return ' '.join(icons)



    def getString(self):
        output = []
        wan = self.getWAN()
        lan = self.getLan()
        states = self.getStates()

        if wan != None:
            output.append(wan)
        if lan != "":
            output.append(lan)
        if states != "":
            output.append(states)

        return ' | '.join(output)

