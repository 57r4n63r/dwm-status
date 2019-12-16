from importlib import import_module
from os.path import dirname, basename, isfile, join
import glob

class Importer:
    __instance = None
    modules = []

    def loadModules(self):
        modules = glob.glob(join(dirname(__file__), "*/register.py"))
        for module in modules:
            module = module.replace(dirname(__file__),'Modules').replace('/','.').replace('.py','')
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
