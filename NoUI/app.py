import typing



class App:
    def __init__(
        self,
        *,
        name:str,
        description:str,
        desc:str
    ):
        self._description = desc or description
        self._name = name
    
    def run(self):
        ...