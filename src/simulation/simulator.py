"""
The simulator class defines all the necessary classes to start a simulation.
"""
from src.definition.robot import Robot


class Simulator:
    """
    The Simulator represents a simulation instance, in which robots can be spawned to be tested.
    """

    def spawn_robot(self, robot: Robot):
        """
        Spawns a robot in the simulator.

        :param robot: Robot object to be spawned
        """
