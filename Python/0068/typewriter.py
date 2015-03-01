try:
    from swampy.TurtleWorld import *
except ImportError:
    from TurtleWorld import *

try:
    from letters import *
except ImportError as e:
    message = e[0]
    if message.startswith('No modle'):
        raise ImportError(message +
                '\nYou have to provide a module named letters.py')

class TyperTurtle(SmartTurtle):

    def teleport(self, x, y):
        """Moves the turtle to a position in absolute coordinates."""
        self.x = x
        self.y = y
        self.redraw()

def keypress(event):
    """Handles the event when a user presses a key.

    Checks if there is a function with the right name; otherwise it prints an error message.
    """
    if bob.busy:
        return
    else:
        bob.busy = True

    if event.char in ['\n', '\r']:
        bob.teleport(-180, bob.y-size*3)
        bob.busy = False
        return

    try:
        if event.char == ' ':
            bob.draw_(size)
            bob.busy = False
            return
        method = getattr(bob, 'draw_' + event.char)
        method(size)
    except AttributeError:
        print 'I don\'t know how to draw an', event.char
        bob.busy = False
        return

    bob.skip(size/2)
    bob.busy = False

if __name__ == '__main__':
    world = TurtleWorld()
    bob = TyperTurtle()
    bob.delay = 0
    size = 22
    bob.busy = False
    bob.teleport(-180, 150)

    world.bind('<Key>', keypress)
    world.mainloop()
