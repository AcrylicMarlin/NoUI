from ast import Call
import asyncio
import functools
import inspect
import json
from typing import Any, Callable, Coroutine, Dict, List, Tuple, TypeVar, Union
from functools import update_wrapper, wraps, partial

from NoUI import exceptions


class ExtMeta:
    name:str
    description:str
    __commands__:List[object]


    

    



class Extension(ExtMeta):
    def __init__(self, name:str=None):
        self.name = name if name else self.__class__.__name__
        self.__commands__: List[InstructionMeta] = []
        self.description = inspect.cleandoc(self.__doc__) if self.__doc__ else '...'
    

    def __init_subclass__(cls) -> None:
        for item in cls.__dict__.values():
            if isinstance(item, Union[Callable, Coroutine]):
                if not inspect.iscoroutinefunction(item):
                    raise exceptions.InstructionNotCoroutine(item)
                
                command = Instruction(item, )

                
        ...
    
    @staticmethod
    def _register_command(self, command):
        self.__commands__.append(command)
        ...


    def __str__(self) -> str:
        string = ""
        string += "Name: " + self.name + "\n"
        string += self.description
        for command in self.__commands__:
            string += "{0.name}\n{0.description}\n{0.ext}\n{0.callback}".format(command)

        return string
        ...



class InstructionMeta:
    name:str
    description:str
    callback:Coroutine
    ext:Extension
    args:Tuple[Any]
    kwargs:Dict[str, Any]


# def instruction(**kwargs) -> InstructionMeta:

#     class Instruction(InstructionMeta):
#         def __init__(self, func):
#             update_wrapper(self, func)
#             try:
#                 name = kwargs.pop('name')
#             except KeyError:
#                 name = self.func.__name__
#             self.name = name
#             self.func = func

#         def __get__(self, obj:Extension, objtype):
#             """Support instance methods."""
#             return partial(self.__call__, obj)

#         def __call__(self, obj:Extension, *args, **kwargs):
#             if not inspect.iscoroutinefunction(self.func):
#                 raise (exceptions.InstructionNotCoroutine(self.name))
            
#             obj._register_command(self)
#             return self.func(obj, *args, **kwargs)
        
#         async def invoke(self, *args, **kwargs):
#             ...
#     return Instruction

class Instruction(InstructionMeta):
    def __init__(self, func:Coroutine, **options:Dict[str, Any]):
        self.callback = func
        self.args = args
        self.kwargs = kwargs
        self.name = options.get('name', func.__name__)
        self.ext = options.get('extension', None)
    
    async def async_invoke(self, *args, **kwargs):
        return await self.callback(*args, **kwargs)

    



def instruction(**options):

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):

            extension = args[0] if isinstance(args[0], Extension) else None
            print(extension)
            if not inspect.iscoroutinefunction(func):
                raise exceptions.InstructionNotCoroutine(func.__name__)
            options['extension'] = extension

            item = Instruction(func, args, kwargs, **options)

            if extension:
                extension._register_command(item)
            
            
            return item.invoke(*args, **kwargs)
            ...
        return inner
    return wrapper

