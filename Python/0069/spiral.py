try:
    from swampy.TurtleWorld import *
except ImportError:
    from TurtleWorld import *


class SpiralTurtle(Turtle):

    def draw_spiral(self, n, length=3, a=0.01, b=0.001):
        """Draws an Archimedian spiral starting at the origin.

        Args:
            n: how many line segments to draw
            length: how long each segment is
            a: how loose the initial spiral starts out
            b: how loosly coiled the spiral is
        """
        theta = 0.0

        for i in range(n):
            self.fd(length)
            dtheta = 1 / (a + b * theta)

            self.lt(dtheta)
            theta += dtheta


if __name__ == '__main__':
    world = TurtleWorld()
    bob = SpiralTurtle()
    bob.delay = 0
    bob.draw_spiral(1000)

    wait_for_user()
