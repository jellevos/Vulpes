"""
This module defines the classes representing the core behaviour of the robot. The core is the part which should not
change: Whether it is tested in real-life, in simulation with sensors, or without.
"""


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
