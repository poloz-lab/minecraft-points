#!/usr/bin/python3
# -*-coding:utf-8 -*

"""module to reprensent points in minecraft, and manage them in a list"""

class Point:
    """Class to represent a point in a minecraft world, represented by:
        - x component
        - y component
        - z component
        - dimension (overworld or nether or end)"""

    def __init__(self, x, y, z, dimension):
        """Initialize a point in a minecraft world
        Parameters:
            x: x component (integer)
            y: y component (integer)
            z: z component (integer)
            dimension: string, possible values are:
                - "overworld"
                - "nether"
                - "end"
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        self.x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        self.y = y
        if not isinstance(z, int):
            raise TypeError("z must be an integer")
        self.z = z
        if dimension != "overworld"\
           and dimension != "nether"\
           and dimension != "end":
            raise ValueError("unknown dimension \"{}\", sould be \"overworld\" or \"nether\" or \"end\"".format(dimension))
        self.dimension = dimension

    def __repr__(self):
        return "Point x: {} y: {} z: {} dimension: {}".format(self.x,
                                                              self.y,
                                                              self.z,
                                                              self.dimension)
