"""
The underwater_yawbot module defines the Underwater Yawbot robot.
"""
from src.definition.robot import Robot


class UnderwaterYawbot(Robot):
    """
    The UnderwaterYawbot is a robot that yaws around a central axis underwater.
    """

    def __init__(self):
        super().__init__(None, None)
