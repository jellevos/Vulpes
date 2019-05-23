import unittest

from src.definition.sensing import Sensing
from src.estimations.imu import OrientationEstimator


class TestAddingEstimators(unittest.TestCase):

    def setUp(self):
        self.sensing = Sensing()

    def test_adding_new(self):
        estimator = OrientationEstimator(None, None, None, 2)

        self.sensing.add_estimator(estimator)

        self.assertEqual(self.sensing._estimators[0], estimator)
