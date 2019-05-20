"""
The simulator class defines all the necessary classes to start a simulation.
"""
from typing import List

import pybullet

from src.definition.robot import Robot


class Simulator:
    """
    The Simulator represents a simulation instance, in which robots can be spawned to be tested.
    """

    def __init__(self):
        self._client = pybullet.connect(pybullet.GUI)
        pybullet.setGravity(0, 0, -10)

    def spawn_robot(self, robot: Robot, position: List[float] = None, orientation: List[float] = None):
        """
        Spawns a robot in the simulator.

        :param robot: Robot object to be spawned
        """
        if position is None:
            position = [0, 0, 0]

        if orientation is None:
            orientation = [0, 0, 0]

        pybullet.loadURDF(robot.physical_definition_filename, position, pybullet.getQuaternionFromEuler(orientation),
                          physicsClientId=self._client)

    def stop(self):
        """
        Stops the simulator, terminating the GUI.
        """
        pybullet.disconnect(self._client)
