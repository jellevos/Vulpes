"""
The estimation module defines classes that use sensor data to estimate robot properties.
"""
from typing import List


class Estimator:
    """
    The Estimator class polls Sensors to update a list of estimations.
    """

    def __init__(self, estimations: List[str], update_frequency):
        """
        Initializes an Estimator object with a list of the names of estimations that it computes at the set frequency.

        :param estimations:
        :param update_frequency:
        """
        self._estimations = estimations

        self._update_frequency = update_frequency

    @property
    def estimations(self):
        """
        Get the names of the estimations that this Estimator computes.

        :return: List of estimation names
        """
        return self._estimations
