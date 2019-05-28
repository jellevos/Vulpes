import unittest

from src.configuration.general_devices import PythonDevice
from src.estimations.imu import OrientationEstimator


class TestAddingEstimators(unittest.TestCase):

    def setUp(self):
        self.device = PythonDevice()

    def test_adding_new(self):
        estimator = OrientationEstimator('test', None, None, None, 2)

        self.device.add_estimator(estimator)

        self.assertEqual(self.device._estimators[0], estimator)

    def test_name_overlap(self):
        estimator1 = OrientationEstimator('orientation', None, None, None, 2)
        estimator2 = OrientationEstimator('orientation', None, None, None, 3)

        self.device.add_estimator(estimator1)

        with self.assertRaises(Exception):
            self.device.add_estimator(estimator2)
