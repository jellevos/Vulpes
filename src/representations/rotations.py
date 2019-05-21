"""
The rotations module defines rotation representations to offer consistency in notations and easier conversion.
"""


class Quaternion:
    """
    The Quaternion class represents a rotation using 4 orthogonal axes x, y, z and w.
    """

    def __init__(self, x, y, z, w):
        self._quaternion = [x, y, z, w]
