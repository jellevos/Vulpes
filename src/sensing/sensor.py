"""
The sensor module defines a high-level sensor interface.
"""
from abc import abstractmethod, ABC


class Sensor(ABC):
    """
    The Sensor class models a sensor that can be polled safely.
    """

    @abstractmethod
    def poll(self):
        """
        Poll the sensor for its current measurement.

        :return: Current sensor measurement
        """
