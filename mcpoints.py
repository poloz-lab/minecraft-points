#!/usr/bin/python3
# -*-coding:utf-8 -*

"""module to reprensent points in minecraft, and manage them in a list"""

class Point:
    """Class to represent a point in a minecraft world, represented by:
        - x component
        - y component
        - z component
        - dimension (overworld or nether or end)
        - short description with the point"""

    def __init__(self, x, y, z, dimension, description):
        """Initialize a point in a minecraft world
        Parameters:
            x: x component (integer)
            y: y component (integer)
            z: z component (integer)
            dimension: string, possible values are:
                - "overworld"
                - "nether"
                - "end"
            description: string to describe the point
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
        if not isinstance(description, str):
            raise TypeError("description must be a string")
        self.description = description

    def __repr__(self):
        return "Point x: {} y: {} z: {} dimension: {} description: {}".format(self.x,
                                                                              self.y,
                                                                              self.z,
                                                                              self.dimension,
                                                                              self.description)
