import re
from subprocess import call, check_output
from Core.Module.AbstractModule import AbstractModule
from Core.Core import Core
from Core.Icons import Icons

class Volume(AbstractModule):
    volumeCommand = ['amixer', 'get']
    interface = None

    def init(self):
        core = Core.getInstance()
        if 'sound' in core.configurations and 'interface' in core.configurations['sound'] :
            self.interface = core.configurations['sound']['interface']
            self.volumeCommand.append(self.interface)


    def getString(self):
        if self.interface == None:
            return Icons.get('speaker_mute')
        volumeOutput = check_output(
            self.volumeCommand).strip().decode('utf-8')
        volumeExtractList = re.findall('(\[\w+\%\])', volumeOutput)
        mute = re.search('(\[off\])', volumeOutput)
        volumePercentage = Icons.get( 'speaker' )
        if volumeExtractList:
            volumePercentage = Icons.get( 'speaker' ) + volumeExtractList[0].strip('[').strip(']').strip(' ')
            if mute:
                volumePercentage = Icons.get( 'speaker_mute' )

        return volumePercentage
