"""
The robot module contains the classes that define a robot.
"""
from typing import List

import pybullet

from src.configuration.configuration import DevicesConfiguration
from src.representations.rotations import Quaternion


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

        self._simulation_id = None
        self._robot_id = None

    @property
    def physical_definition_filename(self) -> str:
        """
        Gets the name of the physical definition file.

        :return: Name of the physical definition file
        """
        return self._physical_definition_filename

    def attach_to_simulation(self, simulation_id, robot_id):
        """
        Attaches the Robot to a Simulator by specifying the corresponding IDs.

        :param simulation_id: ID of the simulation client
        :param robot_id: ID of the robot's object in the simulation
        """
        self._simulation_id = simulation_id
        self._robot_id = robot_id

    def get_position_and_orientation(self) -> (List[float], Quaternion):
        """
        Gets the current position and orientation of the robot object from the simulation.

        :return: Current position and orientation from the simulation
        """
        position, orientation = pybullet.getBasePositionAndOrientation(self._robot_id, self._simulation_id)

        return position, Quaternion(*orientation)

    def update_applied_forces(self):
        """
        Applies the set of (continuous) external forces (or torques) on the robot.
        """


class UnderwaterRobot(Robot):
    """
    The UnderwaterRobot class represents a robot upon which acts a buoyant force.
    """

    def __init__(self, physical_definition_file: str, devices_configuration: DevicesConfiguration,
                 buoyant_volume: float, centre_of_buoyancy: list = None, water_density: float = 1030):
        super().__init__(physical_definition_file, devices_configuration)

        if centre_of_buoyancy is None:
            centre_of_buoyancy = [0, 0, 0]

        self._centre_of_buoyancy = centre_of_buoyancy
        self._buoyant_force = buoyant_volume * water_density * 10  # Weight of displaced water

    def update_applied_forces(self):
        """
        Applies the continuous buoyant force on the base link of the robot.
        """
        pybullet.applyExternalForce(self._robot_id, -1, [0, 0, self._buoyant_force], self._centre_of_buoyancy,
                                    pybullet.WORLD_FRAME, self._simulation_id)
