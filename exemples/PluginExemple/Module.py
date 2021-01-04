from Core.Module.AbstractModule import AbstractModule

class Exemple(AbstractModule):
    order = 11
    def init(self):
        return ''

    def getString(self):
        return "This is and exemple"
