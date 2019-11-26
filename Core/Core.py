import sys
import os
import time
import configparser
from pathlib import Path
from pprint import pprint
from Core.Actions import Actions
from importlib import import_module
from Modules.Importer import Importer
from subprocess import call, check_output

class Core:
    __instance = None

    CONFIGURATION_FILE_LOCATION = str(Path.home()) + "/.config/dwm-status/config.ini"

    configurations = []

    def init(self):
        self.instance = self
        self.loadConfiguration()
        self.loadModules()
        self.actions()

    def loadConfiguration(self):
        self.configurations = configparser.ConfigParser()
        self.configurations.read(self.CONFIGURATION_FILE_LOCATION)

    def loadModules(self):
        importer = Importer.getInstance()
        importer.loadModules()
        # init all modules
        for module in importer.getModules():
            module.init()


    def actions(self):
        self.actions = Actions(self)
        self.actions.handle()

    def print(self):
        importer = Importer.getInstance()
        while True:
            output = ""
            # getString of all module
            for module in importer.getModules():
                output = output + " ["+module.getString()+"] "
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            print(output, flush=True);
            time.sleep(1)

    def xsetroot(self):
        importer = Importer.getInstance()

        while True:
            output = ""
            # getString of all module
            for module in importer.getModules():
                output = output + "[ "+module.getString()+" ]"

            call(['xsetroot', '-name',output], shell=False)
            time.sleep(1)

    @staticmethod
    def getInstance():
        if Core.__instance == None:
            Core.__instance = Core()
        return Core.__instance 
