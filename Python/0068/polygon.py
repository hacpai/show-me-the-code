import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


class PolygonTurtle(Turtle):
    """Respents a Turtle that draws polygon.
    """

    def square(self, length):
        """Draws a square with sides of the given length.

        Returns the Turtle to the starting position and location.
        """
        for i in range(4):
            self.fd(length)
            self.lt()

    def polyline(self, n, length, angle):
        """Draws n line segments.

        n: number of line segments
        length: length of each segment
        angle: degrees between segments
        """
        for i in range(n):
            self.fd(length)
            self.lt(angle)

    def polygon(self, n, length):
        """Draws a polygon with n sides.

        n: number of sides
        length: length of each side.
        """
        angle = 360.0/n
        self.polyline(n, length, angle)

    def arc(self, r, angle):
        """Draws an arc with the given radius and angle.

        r: radius
        angle: angle subtended by the arc, in degrees
        """
        arc_length = 2 * math.pi * r * abs(angle) / 360
        n = int(arc_length / 4) + 1
        step_length = arc_length / n
        step_angle = float(angle) / n

        # making a slight left turn before starting reduces
        # the error caused by the linear approximation of the arc
        self.lt(step_angle/2)
        self.polyline(n, step_length, step_angle)
        self.rt(step_angle/2)

    def circle(self, r):
        """Draws a circle with the given radius.

        r: radius
        """
        self.arc(r, 360)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    world = TurtleWorld()    
    bob = PolygonTurtle()

    wait_for_user()
