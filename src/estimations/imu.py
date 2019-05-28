"""
The imu module defines existing attitude and heading estimators.
"""
from src.definition.robot import Robot
from src.representations.rotations import Quaternion
from src.sensing.estimation import Estimator


class PerfectOrientationEstimator(Estimator[Quaternion]):
    """
    The PerfectOrientationEstimator cuts out (simulated) sensors and returns the correct simulated orientation.
    """

    def __init__(self, name: str, robot: Robot, update_frequency: float):
        super().__init__(name, update_frequency)

        self._robot = robot

    def _estimate(self) -> Quaternion:
        _, orientation = self._robot.get_position_and_orientation()

        return orientation


class OrientationEstimator(Estimator[Quaternion]):
    """
    The OrientationEstimator estimates a quaternion orientation from an accelerometer, gyroscope and magnetometer.
    """

    def __init__(self, name: str, accelerometer, gyroscope, magnetometer, update_frequency: float):
        super().__init__(name, update_frequency)

        self._accelerometer = accelerometer
        self._gyroscope = gyroscope
        self._magnetometer = magnetometer

    def _estimate(self) -> Quaternion:
        pass
