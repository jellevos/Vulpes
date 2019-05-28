"""
The imu module defines existing attitude and heading estimators.
"""
from src.representations.rotations import Quaternion
from src.sensing.estimation import Estimator


class OrientationEstimator(Estimator[Quaternion]):
    """
    The OrientationEstimator estimates a quaternion orientation from an accelerometer, gyroscope and magnetometer.
    """

    def __init__(self, name, accelerometer, gyroscope, magnetometer, update_frequency):
        super().__init__(name, update_frequency)

        self._accelerometer = accelerometer
        self._gyroscope = gyroscope
        self._magnetometer = magnetometer

    def _estimate(self):
        pass
