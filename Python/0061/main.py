class Point( object ):
    """Represents a Point in 2-D space.

    attributes: x, y
    """


class Rectangle( object ):
    """Represents a rectangle.

    attributes: width, height, corner.
    """


def move_rectangle( rect, dx, dy ):
    """Changes the location of rectangle by adding dx to the x corrdiinate of corner and adding dy to the y coordinate of corner.

    rect: Rectangle object
    dx: change in x coordinate
    dy: change in y coordinate
    """
    rect.corner.x += dx
    rect.corner.y += dy
