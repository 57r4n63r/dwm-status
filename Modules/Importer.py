from importlib import import_module
from os.path import dirname, basename, isfile, join
import os.path
import os
from pathlib import Path
import importlib.util
import glob
import sys

class Importer:
    __instance = None
    modules = []

    def loadModules(self):
        modules = glob.glob(join(dirname(__file__), "*/register.py"))
        for module in modules:
            module = module.replace(dirname(__file__),'Modules').replace('/','.').replace('.py','')
            import_module(module)

        home = str(Path.home());
        pluginsPath = "".join((home,'/.config/dwm-status/Plugins'));
        modules = glob.glob("".join((pluginsPath,"/*/register.py")))
        modulePath = "".join((pluginsPath, "/__init__.py"));
        moduleName= "Plugins";
        file_exists = os.path.isfile("".join((pluginsPath,"/__init__.py")));
 
        if not file_exists:
            os.makedirs(pluginsPath)
            open("".join((pluginsPath,"/__init__.py")), "w") #create it

        if modules:
            spec = importlib.util.spec_from_file_location(moduleName, modulePath)
            module = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = module 
            spec.loader.exec_module(module)

        for module in modules:
            module = module.replace(pluginsPath,'Plugins').replace('/','.').replace('.py','')
            import_module(module)

    def register(self, classStr):
        modulePath, classname = classStr.rsplit('.', 1)
        module = import_module(modulePath)
        moduleClass =  getattr(module, classname)
        self.modules.append(moduleClass())

    def getModules(self):
        orderedDict = {}
        for module in self.modules:
            orderedDict[module.order] = module
        keys = reversed(sorted(orderedDict))

        orderedList = []
        for key in keys:
            orderedList.append(orderedDict[key])
        return orderedList

    @staticmethod
    def getInstance():
        if Importer.__instance == None:
            Importer.__instance = Importer()
        return Importer.__instance 
