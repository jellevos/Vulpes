"""
This module defines the classes representing the core behaviour of the robot. The core is the part which should not
change: Whether it is tested in real-life, in simulation with sensors, or without.
"""
from typing import Callable


class Core:
    """
    The Core class represents the persistent part of the robot's software, it takes the estimations produced by the
    sensing module and creates action requests for the acting module.
    """

    def __init__(self, safety):
        """
        Initializes a Core object with the given safety module.

        :param safety: Module that enforces safety constraints
        """
        self._safety = safety
        self._listeners = {}

    def listen_to_event(self, estimation_name: str, callback_method: Callable):
        """
        Adds the given method to the list of listeners for this event.

        :param estimation_name: Name of the estimation to listen to for updates
        :param callback_method: Method to be called when the estimation is updated
        """
        if estimation_name in self._listeners:
            self._listeners[estimation_name].append(callback_method)
            return

        self._listeners[estimation_name] = [callback_method]
