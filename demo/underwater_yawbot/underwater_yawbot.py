"""
The underwater_yawbot module defines the Underwater Yawbot robot.
"""
from pathlib import Path

from src.configuration.configuration import DevicesConfiguration
from src.configuration.general_devices import PythonDevice
from src.definition.core import Core
from src.definition.robot import Robot
from src.estimations.imu import OrientationEstimator


class UnderwaterYawbot(Robot):
    """
    The UnderwaterYawbot is a robot that yaws around a central axis underwater.
    """

    def __init__(self, devices_configuration: DevicesConfiguration):
        """
        Initializes an UnderwaterYawbot with the given functionality.

        :param functionality: Robot's functionality
        """
        file_path = (Path(__file__).parent / 'underwater_yawbot.urdf').resolve()
        super().__init__(file_path, devices_configuration)

    @classmethod
    def with_pid_control(cls):
        """
        Initializes an UnderwaterYawbot with a PID-based feedback controller.

        :return: UnderwaterYawbot instance
        """
        python_device = PythonDevice()
        python_device.add_estimator(OrientationEstimator('orientation', None, None, None, 10))

        configuration = DevicesConfiguration()
        configuration.add_python_device(python_device)

        return cls(configuration)


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
