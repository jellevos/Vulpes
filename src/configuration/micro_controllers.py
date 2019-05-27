"""
The micro_controllers module specifies the supported micro controllers.
"""
from src.configuration.general_devices import Device


class MicroController(Device):
    """
    The abstract MicroController describes a device to be compiled for.
    """

    def __init__(self, compile_target: str):
        """
        Target to cross-compile Rust code to.

        :param compile_target: Thumb instruction set name
        """
        self._compile_target = compile_target

    def compile(self):
        """
        Cross-compile the Rust code that will run on this micro controller.

        :return: Reference to the compiled code
        """


class STM32F3(MicroController):
    """
    The STM32F3 represents a family of micro controllers utilizing the Cortex-M4F core.
    """

    def __init__(self):
        super().__init__('thumbv7em-none-eabihf')
