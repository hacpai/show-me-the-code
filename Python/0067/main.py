try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *
import math


class PieTurtle(Turtle):

    def draw_pie(self, n, length):
        """Draws a pie, then moves into position to the right.

        n: number of segments
        length: length of the radial spokes
        """
        self.pie(n, length)
        self.pu()
        self.fd(length * 2 + 10)
        self.pd()

    def pie(self, n, length):
        """Draws a pie divided into radial segments.

        n: number of segments
        length: length of the radial spokes
        """
        angle = 360 / n
        for i in range(n):
            self.isosceles(length, angle / 2)
            self.lt(angle)


    def isosceles(self, length, angle):
        """Draws an icosceles triangle.

        length: length of the equal legs
        angle: peak angle in degree
        """
        y = length * math.sin(angle * math.pi / 180)
        self.rt(angle)
        self.fd(length)
        self.lt(90 + angle)
        self.fd(2 * y)
        self.lt(90 + angle)
        self.fd(length)
        self.lt(180 - angle)

    def move_right_position(self):
        self.delay = 0
        self.pu()
        self.bk(100)
        self.pd()


if __name__ == '__main__':
    world = TurtleWorld()

    bob = PieTurtle()
    length = 40

    bob.move_right_position()
    bob.draw_pie(5, length)
    bob.draw_pie(6, length)
    bob.draw_pie(7, length)
    bob.die()

    world.mainloop()
