import json
import os
import time
import datetime
import re
import csv
import logging
import subprocess
import glob
import configparser
from threading import Thread
from pathlib import Path
from subprocess import call, check_output


class StatusBar:
    icons = []
    defaultIcons = []
    # CONFIG
    wiredInterfaceName = ""
    wifiInterfaceName = ""
    cachePath = str(Path.home()) + "/.cache/statusbar/"
    pathToVpnConfigFiles = str(Path.home()) + '/.vpn/config/'

    # LOADING
    loaded = False
    loadingIncrement = 0
    loadingFrames = ['/', '—', '\\']
    currentMessage = "Loading"

    # TIME
    timeZone = "Canada/Eastern"
    timeFormat = "%Y/%m/%d %H:%M:%S"

    # VOLUME
    getVolumeCommand = ['amixer', 'get']
    volumeOutput = ''

    # NET
    netWiredState = ''
    netWifiState = ''

    # POWER
    outputPowerNowPath = '/sys/class/power_supply/BAT0/capacity'
    outputPowerSupplyStatusPath = '/sys/class/power_supply/BAT0/status'
    outputEnergyNowPath = '/sys/class/power_supply/BAT0/charge_now'
    outputEnergyFullPath = '/sys/class/power_supply/BAT0/charge_full'

    powerNow = ''
    powerSupplyStatus = ''
    energyNow = ''
    energyFull = ''

    # IP
    currentExternalIp = '---'
    currentLanIp = '---'
    lastIpChecked = None

    # VPN
    vpnIpList = []

    getInternalIpCommand = ['ip', 'addr', 'show']

    # VPN
    openvpnConfigFilePath = "~/.vpn/config"
    getIpCommand = ['curl', 'ip.nucl3on.com/?print']

    elements = {}

    def load(self):
        homedir = os.environ['HOME']
        config = configparser.ConfigParser()
        config.read(homedir+'/.dwm-status')

        #networking
        self.wiredInterfaceName = config['networking']['wired'];
        self.wifiInterfaceName = config['networking']['wifi'];

        self.outputNetWiredStatePath = '/sys/class/net/' + self.wiredInterfaceName + '/operstate'
        self.outputNetWifiStatePath = '/sys/class/net/' + self.wifiInterfaceName + '/operstate'

        #audio
        self.getVolumeCommand.append(config['audio']['interface'])

        #power
        self.outputPowerNowPath = self.outputPowerNowPath.replace('BAT0',config['power']['battery'])
        self.outputPowerSupplyStatusPath = self.outputPowerSupplyStatusPath.replace('BAT0',config['power']['battery'])
        self.outputEnergyNowPath = self.outputEnergyNowPath.replace('BAT0',config['power']['battery'])
        self.outputEnergyFullPath = self.outputEnergyFullPath.replace('BAT0',config['power']['battery'])

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.icons = json.load(open(dir_path+'/icons.json'))
        self.defaultIcons = [' | ', self.icons['dwm'], self.icons['archlinux']]
        t = Thread(target=self.generateVpnCacheFiles)
        t.start()
        while t.isAlive():
            self.printLoading()
        self.getVpnIpList()

    def printLoading(self):
        call(['xsetroot', '-name', self.loadingFrames[self.loadingIncrement] +
              ' ' + self.currentMessage+"".join(self.defaultIcons)], shell=False)
        self.loadingIncrement = self.loadingIncrement + 1
        if self.loadingIncrement >= len(self.loadingFrames):
            self.loadingIncrement = 0
        time.sleep(0.2)

    def generateVpnCacheFiles(self):
        self.currentMessage = "Generating VPN cache files"
        files = glob.glob(self.pathToVpnConfigFiles + "*.ovpn")
        fileContents = []
        ipList = []

        for filename in files:
            command = ['cat', filename]
            fileContents.append(check_output(command).strip().decode('utf-8'))

        for content in fileContents:
            remote = re.findall('(remote [0-9\.]+)', content)
            if remote:
                ipList.append(remote[0].strip('remote '))

        if not os.path.exists(self.cachePath):
            os.makedirs(self.cachePath)

        if os.path.exists(self.cachePath + "ip_list"):
            os.remove(self.cachePath + "ip_list")
        cacheFile = open(self.cachePath + 'ip_list', 'w')

        for item in ipList:
            cacheFile.write("%s\n" % item)
        cacheFile.close()

        self.loaded = True

    def getVpnIpList(self):
        ipList = []
        with open(self.cachePath + 'ip_list', 'r') as f:
            reader = csv.reader(f)
            ipList = list(reader)
        self.vpnIpList = ipList

    def addVolume(self):
        self.volumeOutput = check_output(
            self.getVolumeCommand).strip().decode('utf-8')
        volumeExtractList = re.findall('(\[\w+\%\])', self.volumeOutput)
        mute = re.search('(\[off\])', self.volumeOutput)
        volume_percentage = self.icons['speaker']
        if volumeExtractList:
            volume_percentage = self.icons['speaker'] + volumeExtractList[0].strip('[').strip(']').strip(' ')
            if mute:
                volume_percentage = self.icons['speaker_mute']

        self.addToElementGroup('sound',volume_percentage)

    def addNet(self):
        self.netWiredState = check_output(
            ['cat', self.outputNetWiredStatePath]).strip().decode('utf-8')
        self.netWifiState = check_output(
            ['cat', self.outputNetWifiStatePath]).strip().decode('utf-8')

        net_connection = ""

        if self.netWifiState == "up":
            net_connection = self.icons['wifi_medium']

        if self.netWiredState == "up":
            net_connection = self.icons['wired']

        self.addToElementGroup('connection',net_connection)

    def addPower(self):
        self.powerNow = check_output(
            ['cat', self.outputPowerNowPath]).strip().decode('utf-8')
        self.powerSupplyStatus = check_output(
            ['cat', self.outputPowerSupplyStatusPath]).strip().decode('utf-8')
        self.energyNow = check_output(
            ['cat', self.outputEnergyNowPath]).strip().decode('utf-8')
        self.energyFull = check_output(
            ['cat', self.outputEnergyFullPath]).strip().decode('utf-8')

        status = self.icons['battery_unpluged']
        level = "100%"

        if self.powerNow == "0" or self.powerSupplyStatus == "Charging":
            status = self.icons['battery_pluged']

        float_level = float(self.energyNow) / float(self.energyFull) * 100
        level = str(int(float_level)) + '%'

        self.addToElementGroup('battery',status)
        self.addToElementGroup('battery',level)

    def addDate(self):
        os.environ['TZ'] = self.timeZone
        time.tzset()
        string_time = time.strftime(self.timeFormat)
        self.addToElementGroup('clock',self.icons['clock1'])
        self.addToElementGroup('clock',string_time)

    def addIp(self):
        isConnected = False
        currentConnectionInterface = False
        if self.netWifiState == "up":
            isConnected = True
            currentConnectionInterface = self.wifiInterfaceName

        if self.netWiredState == "up":
            isConnected = True
            currentConnectionInterface = self.wiredInterfaceName

        getInternalIpCommand = None

        if isConnected:
            # Check at every 30 minutes or when reset (None)
            if self.lastIpChecked == None or (self.lastIpChecked + datetime.timedelta(seconds=30)) < datetime.datetime.now():
                try:
                    self.currentExternalIp = check_output(
                        self.getIpCommand).strip().decode('utf-8')
                    self.lastIpChecked = datetime.datetime.now()
                except subprocess.CalledProcessError as e:
                    print(e.output)

                getInternalIpCommand = list(self.getInternalIpCommand)
                getInternalIpCommand.append(currentConnectionInterface)

                lanIpCommandResult = ''

                try:
                    lanIpCommandResult = check_output(
                        getInternalIpCommand).strip().decode('utf-8')
                except subprocess.CalledProcessError as e:
                    print(e.output)

                listResult = re.findall('(inet .+/)', lanIpCommandResult)

                currentLanIp = "---"
                if listResult:
                    currentLanIp = listResult[0].strip('inet ').strip('/')

                self.currentLanIp = currentLanIp
        else:
            self.currentExternalIp = '---'
            self.currentLanIp = '---'

        self.addToElementGroup('connection', self.icons['globe'])
        self.addToElementGroup('connection', self.currentExternalIp)
        self.addToElementGroup('connection', ' | '+self.icons['home'])
        self.addToElementGroup('connection', self.currentLanIp)

    def isVpnOn(self):
        isVpnOn = False
        if [self.currentExternalIp] in self.vpnIpList:
            isVpnOn = True
        if self.currentExternalIp != "---":
            if isVpnOn:
                self.addToElementGroup('connection',self.icons['shield'])

    def addToElementGroup(self, groupName, node):
        try:
            self.elements[groupName]
        except KeyError:
            self.elements[groupName] = []
        self.elements[groupName].append(node)

    def render(self):
        attribute_string = ""

        for element in self.elements:
            attribute_string = attribute_string + "[" + "".join(self.elements[element])+"]"
        attribute_string = re.sub(' +',' ',attribute_string)
        attribute_string = attribute_string +"".join(self.defaultIcons)
        call(['xsetroot', '-name',attribute_string.strip()], shell=False)
        self.elements ={} # reset attributes list
