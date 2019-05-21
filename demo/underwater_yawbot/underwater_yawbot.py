"""
The underwater_yawbot module defines the Underwater Yawbot robot.
"""
from src.definition.core import Core
from src.definition.robot import Robot, Functionality
from src.definition.sensing import Sensing
from src.estimations.imu import OrientationEstimator


class UnderwaterYawbot(Robot):
    """
    The UnderwaterYawbot is a robot that yaws around a central axis underwater.
    """

    def __init__(self, functionality: Functionality):
        """
        Initializes an UnderwaterYawbot with the given functionality.

        :param functionality: Robot's functionality
        """
        super().__init__('underwater_yawbot/underwater_yawbot.urdf', functionality)

    @classmethod
    def with_pid_control(cls):
        """
        Initializes an UnderwaterYawbot with a PID-based feedback controller.

        :return: UnderwaterYawbot instance
        """
        sensing = Sensing()
        sensing.add_estimator(OrientationEstimator(None, None, None, 10))

        return cls(Functionality(sensing, PIDUnderwaterYawbotCore(), None))


class PIDUnderwaterYawbotCore(Core):
    """
    The PIDUnderwaterYawbotCore implements the feedback control using a PID controller.
    """

    def __init__(self):
        super().__init__(None)

        self.listen_to_event('orientation', self.update_thrust)

    def update_thrust(self, orientation):
        """
        Callback that updates the thrust command for the actuators when there is a new orientation estimate.

        :param orientation: Updated orientation estimate
        """
