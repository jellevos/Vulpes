"""
The imu module defines existing attitude and heading estimators.
"""
from src.representations.rotations import Quaternion
from src.sensing.estimation import Estimator

from string_sum import sum_as_string


class OrientationEstimator(Estimator[Quaternion]):
    """
    The OrientationEstimator estimates a quaternion orientation from an accelerometer, gyroscope and magnetometer.
    """

    def __init__(self, accelerometer, gyroscope, magnetometer, update_frequency):
        super().__init__(update_frequency)

        self._accelerometer = accelerometer
        self._gyroscope = gyroscope
        self._magnetometer = magnetometer

    def _estimate(self):
        pass
