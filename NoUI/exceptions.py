"""
Module containting all app related exceptions
"""

from typing import Any, Callable, Coroutine


class AppError(Exception):
    """
    Base Error for all app related errors
    """
    def __init__(self, message):
        super().__init__(message)


class InvalidArgType(AppError):
    """
    Raised when an invalid type is given to the callback
    """
    def __init__(self, arg:str, expected:Any):
        super().__init__(f'\nArgument [{arg}] was given an invalid type\nExpected [{expected.__name__}] got [{type(arg).__name__}]')

class InstructionNotCoroutine(AppError):
    """
    Raised when an Instruction causes a problem
    """
    def __init__(self, command:Callable):
        super().__init__(f'Command [{command.__name__}] is not a Coroutine')
