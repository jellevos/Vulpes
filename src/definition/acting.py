"""
The acting module defines the Acting class, which accepts action requests and outputs actuator actions.
"""


class Acting:
    """
    The Sensing class represents the outputs of the robot, where action requests are turned into actuator commands.
    """

    def __init__(self):
        self._actions = []
