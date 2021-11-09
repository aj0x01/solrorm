from abc import ABC, abstractclassmethod, abstractmethod

class BaseCore(ABC):

    def __init__(self, core, host, port):
        self.core = core
        self.host = host
        self.port = port

    
    @abstractmethod
    def get_base_url(self):
        pass

    @property
    @abstractmethod
    def objects(self):
        pass

    

