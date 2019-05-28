"""
The robot module contains the classes that define a robot.
"""
from src.configuration.configuration import DevicesConfiguration


class Robot:
    """
    The Robot class represents the physical entity of the robot in the software.
    """

    def __init__(self, physical_definition_file: str, devices_configuration: DevicesConfiguration):
        """
        Initializes a Robot object from the physical definition represented by an SDF or URDF file.

        :param physical_definition_file: SDF or URDF file representing the physical robot
        :param devices_configuration: Configuration of the devices that the robot's software will be run on
        """
        self._physical_definition_filename = physical_definition_file
        self._devices_configuration = devices_configuration

    @property
    def physical_definition_filename(self) -> str:
        """
        Gets the name of the physical definition file.

        :return: Name of the physical definition file
        """
        return self._physical_definition_filename
