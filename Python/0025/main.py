from polygon import *

def petal( t, r, angle ):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle subtended by the arc, in degrees
    """
    for i in range( 2 ):
        arc( t, r, angle )
        lt( bob, 180 - angle )

def draw_flower( t, n, r, angle ):
    """Draws a flower.

    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle subtended by the arc, in degrees
    """
    for i in range( n ):
        petal( t, r, angle )
        lt( t, 360.0 / n )

def flower1( t ):
    """Draws a flower of picture1 

    t: Turtle
    """
    move( t, -100 )
    draw_flower( t, 7, 60.0, 60.0 )

def flower2( t ):
    """Draws a flower of picutre2

    t: Turtle
    """
    move( t, 100 )
    draw_flower( t, 10, 40.0, 80.0 )

def flower3( t ):
    """Draws a flower of picutre3

    t: Turtle
    """
    move( t, 100 )
    draw_flower( t, 20, 140.0, 20.0 )

def move( t, length ):
    """Move Turtle( t ) to three part of canvas to draw flowers.
    """
    pu( t )
    fd( t, length )
    pd( t )

world = TurtleWorld()

bob = Turtle()
bob.delay = 0

flower1( bob )
flower2( bob )
flower3( bob )

die( bob )

# dump the contents of the campus to the file canvas.eps
world.canvas.dump()

wait_for_user()

