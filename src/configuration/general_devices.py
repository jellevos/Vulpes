"""
The general_devices module specifies devices that can execute robot code.
"""
from abc import ABC
from typing import List

from src.sensing.estimation import Estimator


class Device(ABC):
    """
    The abstract Device represents any Device that can run code.
    """

    def __init__(self):
        self._estimators = []

    @property
    def estimators(self) -> List[Estimator]:
        """
        Gets the list of estimators that will run on this Device.

        :return: List of estimators
        """
        return self._estimators

    def add_estimator(self, estimator: Estimator):
        """
        Adds an estimator to the Device.

        :param estimator: Estimator to be run on this Device
        """
        if self.contains_estimator(estimator):
            raise Exception("There already exists an estimator in this device with this name.")

        self._estimators.append(estimator)

    def contains_estimator(self, estimator) -> bool:
        """
        Whether the Device contains an equivalently named Estimator.

        :param estimator: Estimator that the names are compared to
        :return: Boolean whether this Device contains an equivalently named Estimator
        """
        return estimator.name in (other_estimator.name for other_estimator in self._estimators)


class PythonDevice(Device):
    """
    The PythonDevice represents a device that runs Python and does not need to compile Rust code.
    """
