import sys

class Actions:
    arguments = {}
    core = None
    def __init__(self,core):
        self.core = core
        for arg in sys.argv :
            if arg.find('--') != -1 :
                argname = arg.replace('--','').split('=')[0]
                self.arguments[argname] = arg.split('=')[1]
        self.setDefault()

    def handle(self):
        if self.arguments['output'] == 'print' : 
            self.core.print()
            return
        if self.arguments['output'] == 'xsetroot' :
            self.core.xsetroot()
            return
        raise SystemExit('[error] Selected output is invalid')
            
    def setDefault(self):
        try:
            self.arguments['output']
            if self.arguments['output'] == '' :
                self.arguments['output'] = 'print'
        except KeyError:
            self.arguments['output'] = 'print'

