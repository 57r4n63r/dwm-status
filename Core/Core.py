import os
import configparser
from pathlib import Path
from pprint import pprint
from Core.Actions import Actions
from importlib import import_module
from Modules.Importer import Importer

#from Modules.Network.Module import Network

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


    def actions(self):
        self.actions = Actions(self)
        self.actions.handle()

    def print(self):
        importer = Importer.getInstance()
        output = ""
        # init all modules
        for module in importer.getModules():
            module.init()

        # getString of all module
        for module in importer.getModules():
            output = output + " ["+module.getString()+"] "

        print(output);

    def xsetroot(self):
        importer = Importer.getInstance()
        output = ""
        # init all modules
        for module in self.modules:
            module.init()

        # getString of all module
        for module in self.modules:
            output = output + "[ "+module.getString()+" ]"

        #@todo xsetroot

    @staticmethod
    def getInstance():
        if Core.__instance == None:
            Core.__instance = Core()
        return Core.__instance 
