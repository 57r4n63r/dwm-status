import os
import time
from Core.Module.AbstractModule import AbstractModule
from Core.Core import Core
from Core.Icons import Icons

class Time(AbstractModule):
    timeZone = "Canada/Eastern"
    timeFormat = "%Y/%m/%d %H:%M:%S"

    def init(self):
        os.environ['TZ'] = self.timeZone

    def getString(self):
        time.tzset()
        timeString = time.strftime(self.timeFormat)
        output = [Icons.get('clock1')]
        output.append(timeString)
        return " ".join(output)