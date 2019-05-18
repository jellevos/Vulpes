"""
The robot module contains the classes that define a robot.
"""


class Robot:
    """
    The Robot class represents the physical entity of the robot in the software.
    """

    def __init__(self, physical_definition_file: str):
        """
        Initializes a Robot object from the physical definition represented by an SDF or URDF file.

        :param physical_definition_file: SDF or URDF file representing the physical robot
        """
        self._physical_definition_file = physical_definition_file
