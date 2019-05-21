"""
The sensing module defines the Sensing class, which inputs sensor data and outputs estimations.
"""
from src.sensing.estimation import Estimator


class Sensing:
    """
    The Sensing class represents the inputs of the robot, where sensor data is combined by estimators.
    """

    def __init__(self):
        self._estimators = []

    def add_estimator(self, estimator: Estimator):
        """
        Add an Estimator to the Sensing module.

        :param estimator: Estimator object
        """
        self._estimators.append(estimator)
