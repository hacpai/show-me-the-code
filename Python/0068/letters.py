try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

from polygon import *

import math


class SmartTurtle(PolygonTurtle):

    def fdbk(self, size):
        """Forward and back, ending at the original position."""
        self.fd(2*size)
        self.pu()
        self.bk(2*size)
        self.pd()

    def skip(self, size):
        """Lift the pen and move forward."""
        self.pu()
        self.fd(2*size)
        self.pd()

    def jump(self, size):
        """Don't draw and move the turtle at the top then face right."""
        self.lt()
        self.skip(size)
        self.rt()

    def top(self, size):
        """Draw move the turtle at the top then face right."""
        self.lt()
        self.fd(2*size)
        self.rt()

    def updown(self, size):
        """Draws straight up and down."""
        self.top(size)
        self.jump(-size)

    def bump(self, size):
        """Draw a half circle and face right."""
        self.arc(size, -180)
        self.rt(180)

    def drift(self, height, length):
        """Draws straight up and turn right."""
        self.top(height)
        self.fdbk(length)
        self.jump(-height)

    def frift(self, height, length):
        """Don't draw straight and turn right."""
        self.jump(height)
        self.fdbk(length)
        self.jump(-height)

    def diagonal(self, x, y):
        """make a diagonal line to the given x, y offsets and return"""
        angle = math.atan2(y, x) * 180 / math.pi
        dist = math.sqrt(x**2 + y**2)
        self.lt(angle)
        self.fdbk(dist)
        self.rt(angle)

    def vshape(self, x, y):
        self.diagonal(-x, y)
        self.diagonal(x, y)

    def fdlt(self, size, angle=90):
        """Forward and left."""
        self.fd(size)
        self.lt(angle)

    def draw_a(self, size):
        self.diagonal(size/4, size)
        self.frift(size/2, size/2)
        self.skip(size/2)
        self.diagonal(-size/4, size)

    def draw_b(self, size):
        self.top(size)
        self.bump(size/2)
        self.bump(size/2)
        self.skip(size/2)

    def draw_c(self, size):
        self.skip(size/2)
        self.jump(size)
        self.lt(180)
        self.arc(size, 180)

    def draw_d(self, size):
        self.top(size)
        self.bump(size)
        self.skip(size/2)

    def draw_e(self, size):
        self.drift(size, size/2)
        self.drift(size/2, size/2)
        self.fd(size)

    def draw_f(self, size):
        self.drift(size, size/2)
        self.drift(size/2, size/2)
        self.skip(size/2)

    def draw_g(self, size):
        self.drift(size, size/2)
        self.fd(size)
        self.drift(size/2, -size/4)

    def draw_h(self, size):
        self.updown(size)
        self.drift(size/2, size/2)
        self.skip(size/2)
        self.updown(size)

    def draw_i(self, size):
        self.frift(size, size/2)
        self.fd(size/2)
        self.drift(size, size/4)
        self.fd(size/2)

    def draw_j(self, size):
        self.frift(size, size/2)
        self.arc(size/2, 90)
        self.fd(3*size/2)
        self.skip(-size)
        self.rt()
        self.skip(size/4)

    def draw_k(self, size):
        self.updown(size)
        self.jump(size/2)
        self.diagonal(size/2, size/2)
        self.diagonal(size/2, -size/2)
        self.skip(size/2)
        self.jump(-size/2)

    def draw_l(self, size):
        self.updown(size)
        self.fd(size)

    def draw_m(self, size):
        self.updown(size)
        self.draw_v(size)
        self.updown(size)

    def draw_n(self, size):
        self.updown(size)
        self.skip(size/2)
        self.diagonal(-size/2, size)
        self.updown(size)

    def draw_o(self, size):
        self.skip(size/2)
        self.circle(size)
        self.skip(size/2)

    def draw_p(self, size):
        self.top(size)
        self.bump(size/2)
        self.jump(-size/2)
        self.skip(size/2)

    def draw_q(self, size):
        self.draw_o(size)
        self.diagonal(-size/3, size/2)

    def draw_r(self, size):
        self.draw_p(size)
        self.diagonal(-size/2, size/2)

    def draw_s(self, size):
        self.fd(size/2)
        self.arc(size/2, 180)
        self.arc(size/2, -180)
        self.fd(size/2)
        self.jump(-size)

    def draw_t(self, size):
        self.frift(size, size)
        self.skip(size/2)
        self.updown(size)
        self.skip(size/2)

    def draw_u(self, size):
        self.updown(size)
        self.fd(size)
        self.updown(size)

    def draw_v(self, size):
        self.skip(size/3)
        self.vshape(size/3, size)
        self.skip(size/3)

    def draw_w(self, size):
        self.draw_v(size)
        self.draw_v(size)

    def draw_x(self, size):
        self.diagonal(size/2, size)
        self.skip(size/2)
        self.diagonal(-size/2, size)

    def draw_y(self, size):
        self.skip(size/4)
        self.top(3*size/4)
        self.vshape(size/4, size/4)
        self.jump(-3*size/4)
        self.skip(size/4)

    def draw_z(self, size):
        self.frift(size, size/2)
        self.diagonal(size/2, size)
        self.fd(size)

    def draw_(self, size):
        """Draw a space."""
        self.skip(size)

if __name__ == '__main__':
    world = TurtleWorld()
    bob = SmartTurtle()
    size = 20
    bob.delay = 0.01

    for s in 'hello':
        m = 'draw_' + s
        method = getattr(bob, m)
        method(size)
        bob.skip(size/2)

    world.mainloop()
