import unittest

from src.configuration.configuration import DevicesConfiguration, PythonDevice
from src.configuration.micro_controllers import STM32F3, MicroController
from src.estimations.imu import OrientationEstimator


class TestAddingDevicesCorrectly(unittest.TestCase):

    def setUp(self):
        self.devices_configuration = DevicesConfiguration()

    def test_adding_python_device(self):
        device = PythonDevice()

        self.devices_configuration.add_python_device(device)

        self.assertEqual(self.devices_configuration._python_devices[0], device)

    def test_adding_micro_controller(self):
        micro_controller = STM32F3()

        self.devices_configuration.add_micro_controller(micro_controller)

        self.assertEqual(self.devices_configuration._micro_controllers[0], micro_controller)


class TestAddingDoubleDevices(unittest.TestCase):

    def setUp(self):
        self.devices_configuration = DevicesConfiguration()

    def test_adding_double_estimator_python_devices(self):
        device1 = PythonDevice()
        device1.add_estimator(OrientationEstimator('orientation', None, None, None, 4))

        device2 = PythonDevice()
        device2.add_estimator(OrientationEstimator('orientation', None, None, None, 5))

        self.devices_configuration.add_python_device(device1)

        with self.assertRaises(Exception):
            self.devices_configuration.add_python_device(device2)

    def test_adding_double_estimator_micro_controllers(self):
        device1 = MicroController('')
        device1.add_estimator(OrientationEstimator('orientation', None, None, None, 2))

        device2 = MicroController('')
        device2.add_estimator(OrientationEstimator('orientation', None, None, None, 1))

        self.devices_configuration.add_micro_controller(device1)

        with self.assertRaises(Exception):
            self.devices_configuration.add_micro_controller(device2)

    def test_adding_double_estimator_different_devices(self):
        device1 = MicroController('')
        device1.add_estimator(OrientationEstimator('orientation', None, None, None, 2))

        device2 = PythonDevice()
        device2.add_estimator(OrientationEstimator('orientation', None, None, None, 1))

        self.devices_configuration.add_micro_controller(device1)

        with self.assertRaises(Exception):
            self.devices_configuration.add_python_device(device2)
