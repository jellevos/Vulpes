"""
The sensing module defines the Sensing class, which inputs sensor data and outputs estimations.
"""


class Sensing:
    """
    The Sensing class represents the inputs of the robot, where sensor data is combined by estimators.
    """

    def __init__(self):
        self._estimators = []
