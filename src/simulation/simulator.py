"""
The simulator class defines all the necessary classes to start a simulation.
"""
import time
from typing import List

import pybullet

from src.definition.robot import Robot


class Simulator:
    """
    The Simulator represents a simulation instance, in which robots can be spawned to be tested.
    """

    def __init__(self):
        self._client = pybullet.connect(pybullet.GUI)
        pybullet.setGravity(0, 0, -10, self._client)

        self._robots = []

    def spawn_robot(self, robot: Robot, position: List[float] = None, orientation: List[float] = None):
        """
        Spawns a robot in the simulator.

        :param robot: Robot object to be spawned
        :param position: Position to spawn at as a list [x, y, z]
        :param orientation: Orientation to spawn at as a list (Euler angle) [x, y, z]
        """
        if position is None:
            position = [0, 0, 0]

        if orientation is None:
            orientation = [0, 0, 0]

        robot_id = pybullet.loadURDF(robot.physical_definition_filename, position,
                                     pybullet.getQuaternionFromEuler(orientation), physicsClientId=self._client)

        robot.attach_to_simulation(self._client, robot_id)
        self._robots.append(robot)

    def simulate(self, seconds, framerate=240):
        """
        Run the simulation for a given amount of seconds at a set frequency.

        :param seconds: Number of seconds to run the simulation
        :param framerate: Framerate at which to take simulation steps
        :return:
        """
        for _ in range(seconds * framerate):
            for robot in self._robots:
                robot.update_applied_forces()

            pybullet.stepSimulation(self._client)
            time.sleep(1/framerate)

    def stop(self):
        """
        Stops the simulator, terminating the GUI.
        """
        pybullet.disconnect(self._client)
