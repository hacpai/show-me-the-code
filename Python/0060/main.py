import math


class Point( object ):
    """Represents a Point in 2-D space."""


def distance_between_point( pa, pb ):
    """Competes the distance between two Point object.
    """
    return math.sqrt( ( pa.x - pb.x ) ** 2 + ( pa.y - pb.y ) ** 2 )

