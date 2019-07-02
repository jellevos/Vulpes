import math
import unittest
from unittest.mock import Mock

from definition.robot import UnderwaterRobot
from src.simulation.simulator import Simulator


class TestBuoyantForce(unittest.TestCase):

    def test_robot_floats(self):
        simulator = Simulator()

        robot = UnderwaterRobot('simple_cylinder_light.urdf', Mock(),
                                0.2 * 0.2 * math.pi * 0.6)
        simulator.spawn_robot(robot, [0, 0, -2])

        simulator.simulate(5)

        simulator.stop()

    def test_robot_sinks(self):
        simulator = Simulator()

        robot = UnderwaterRobot('simple_cylinder_heavy.urdf', Mock(),
                                0.2 * 0.2 * math.pi * 0.6)
        simulator.spawn_robot(robot, [0, 0, -2])

        simulator.simulate(5)

        simulator.stop()
