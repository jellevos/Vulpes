"""
The estimation module defines classes that use sensor data to estimate robot properties.
"""
from abc import abstractmethod
from typing import Generic, TypeVar

E = TypeVar('E')  # pylint: disable=C0103


class Estimator(Generic[E]):
    """
    The Estimator class polls Sensors to update a list of estimations.
    """

    def __init__(self, update_frequency):
        """
        Initializes an Estimator object with a list of the names of estimations that it computes at the set frequency.

        :param estimations:
        :param update_frequency:
        """
        self._estimations = None

        self._update_frequency = update_frequency

    @property
    def estimations(self) -> E:
        """
        Get the names of the estimations that this Estimator computes.

        :return: List of estimation names
        """
        return self._estimations

    @abstractmethod
    def _estimate(self) -> E:
        """
        Compute the estimations with data from the given sensors.

        :return: Estimations following the class type definition
        """

    def _update_estimations(self):
        """
        (Re)computers and updates the cached estimations
        """
        self._estimations = self._estimate()
