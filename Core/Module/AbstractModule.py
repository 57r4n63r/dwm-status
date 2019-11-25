
from abc import ABC, abstractmethod

class AbstractModule(ABC):
    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def getString(self):
        pass
