from .base import BaseCore
from .query import Executor

class Core(BaseCore):

    def __init__(self, core_name, host, port, fields="*"):
        self.core_name = core_name
        self.host = host
        self.port = port
        self.fields = fields

    @property
    def get_base_url(self):
        return f"http://{self.host}:{self.port}/solr/{self.core_name}/"

    @property
    def objects(self):
        return Executor(core=self)


    
    

    

