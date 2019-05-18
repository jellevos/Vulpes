"""
The robot module contains the classes that define a robot.
"""
from src.definition.acting import Acting
from src.definition.core import Core
from src.definition.sensing import Sensing


class Functionality:
    """
    The Functionality class represents the functional part (software) of the robot.
    """

    def __init__(self, sensing: Sensing, core: Core, acting: Acting):
        """
        Initializes a Functionality object that contains the three parts of the robot's software: Sensing, Core, Acting.

        :param sensing: Object that inputs sensor data and computes estimations
        :param core: Object that takes estimations and computes action requests
        :param acting: Object that takes action requests and outputs actuator commands
        """
        self._sensing = sensing
        self._core = core
        self._acting = acting


class Robot:
    """
    The Robot class represents the physical entity of the robot in the software.
    """

    def __init__(self, physical_definition_file: str, functionality: Functionality):
        """
        Initializes a Robot object from the physical definition represented by an SDF or URDF file.

        :param physical_definition_file: SDF or URDF file representing the physical robot
        :param functionality: Object representing the behavioural part of the robot
        """
        self._physical_definition_file = physical_definition_file
        self._functionality = functionality
