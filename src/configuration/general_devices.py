"""
The general_devices module specifies devices that can execute robot code.
"""
from abc import ABC


class Device(ABC):
    """
    The abstract Device represents any Device that can run code.
    """


class PythonDevice(Device):
    """
    The PythonDevice represents a device that runs Python and does not need to compile Rust code.
    """
