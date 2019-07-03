import math
import unittest
from pathlib import Path
from unittest.mock import Mock

from src.definition.robot import UnderwaterRobot
from src.simulation.simulator import Simulator


class TestBuoyantForce(unittest.TestCase):

    def test_robot_floats(self, tries=20):
        simulator = Simulator(user_interface=False)

        file_path = (Path(__file__).parent / 'simple_cylinder_light.urdf').resolve()
        robot = UnderwaterRobot(file_path, Mock(),
                                0.2 * 0.2 * math.pi * 0.6)
        simulator.spawn_robot(robot, [0, 0, -2])

        last_depth = -2
        for i in range(tries):
            simulator.step()
            position, _ = robot.get_position_and_orientation()
            self.assertGreater(position[2], last_depth)
            last_depth = position[2]

        simulator.stop()

    def test_robot_sinks(self, tries=20):
        simulator = Simulator(user_interface=False)

        file_path = (Path(__file__).parent / 'simple_cylinder_heavy.urdf').resolve()
        robot = UnderwaterRobot(file_path, Mock(),
                                0.2 * 0.2 * math.pi * 0.6)
        simulator.spawn_robot(robot, [0, 0, -2])

        last_depth = -2
        for i in range(tries):
            simulator.step()
            position, _ = robot.get_position_and_orientation()
            self.assertLess(position[2], last_depth)
            last_depth = position[2]

        simulator.stop()
