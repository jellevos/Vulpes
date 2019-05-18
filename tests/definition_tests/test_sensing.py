import unittest

from src.definition.sensing import Sensing
from src.sensing.estimation import Estimator


class TestAddingEstimators(unittest.TestCase):

    def setUp(self):
        self.sensing = Sensing()

    def test_adding_new(self):
        estimator = Estimator(['orientation'], 2)

        self.sensing.add_estimator(estimator)

        self.assertEqual(list(self.sensing._estimators.keys()), ['orientation'])
        self.assertIsNone(self.sensing._estimators['orientation'])

    def test_adding_double(self):
        estimator_alpha = Estimator(['velocity', 'orientation'], 4)
        estimator_beta = Estimator(['temperature', 'velocity'], 3)

        self.sensing.add_estimator(estimator_alpha)

        with self.assertRaises(BaseException):
            self.sensing.add_estimator(estimator_beta)
