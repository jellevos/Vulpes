import unittest

from configuration.configuration import DevicesConfiguration, PythonDevice
from configuration.micro_controllers import STM32F3


class TestAddingDevices(unittest.TestCase):

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
