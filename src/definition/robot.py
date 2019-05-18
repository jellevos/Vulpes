

class Robot(object):

    def __init__(self, physical_definition_file: str):
        """
        Initializes a Robot object from the physical definition represented by an SDF or URDF file.

        :param physical_definition: SDF or URDF file representing the physical robot
        """
        self._physical_definition_file = physical_definition_file
