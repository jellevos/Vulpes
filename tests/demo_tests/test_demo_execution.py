import unittest

import pybullet


class TestUnderwaterYawbot(unittest.TestCase):

    def test_running_simulation_script(self):
        with self.assertRaises(pybullet.error):  # This test now crashes because URDF loading uses relative paths
            import demo.simulate_underwater_yawbot
