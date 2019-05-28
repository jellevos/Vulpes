"""
The configuration module represents the system in full.
"""
from src.configuration.micro_controllers import MicroController
from src.configuration.general_devices import PythonDevice, Device


class DevicesConfiguration:
    """
    The DevicesConfiguration represents the collection of all devices involved in the system.
    """

    def __init__(self):
        self._python_devices = []
        self._micro_controllers = []

    def add_python_device(self, device: PythonDevice):
        """
        Adds a device to the devices configuration that will only run Python code.

        :param device: Python device
        """
        self._check_new_device(device)
        self._python_devices.append(device)

    def add_micro_controller(self, micro_controller: MicroController):
        """
        Adds a micro controller to the devices configuration that will run compiled Rust code.

        :param micro_controller: Micro controller
        """
        self._check_new_device(micro_controller)
        self._micro_controllers.append(micro_controller)

    def _check_new_device(self, device: Device):
        for estimator in device.estimators:
            for existing_device in self._devices():
                if existing_device.contains_estimator(estimator):
                    raise Exception("Device " + str(existing_device) + " already contains an estimator with the same "
                                                                       "name.")

    def _devices(self):
        for python_device in self._python_devices:
            yield python_device

        for micro_controller in self._micro_controllers:
            yield micro_controller
