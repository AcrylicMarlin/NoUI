
from NoUI import Extension, instruction

class Items(Extension):
    """Ayo??"""
    @instruction(name = 'command')
    async def newCommand(self, arg:str):
        print(arg)
