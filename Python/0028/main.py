from polygon import * 


def koch( t, length ):
    """Draws a Koch curve with the given length.

    t: Turtle
    length: length
    """
    if length < 3:
        return fd( t, length )
    else:
        length = length / 3.0
        #fd( t, length / 3 )
        koch( t, length )
        lt( t, 60 )
        #fd( t, length / 3 )
        koch ( t, length )
        rt( t, 120 )
        #fd( t, length / 3 )
        koch( t, length )
        lt( t, 60 )
        #fd( t, length / 3 )
        koch ( t, length )


def snowflake( t, length ):
    """Draws a snowflake with three koch curves

    t: Turtle
    length: length
    """
    for i in range( 3 ):
        koch( t, length )
        rt( t, 120 )


world = TurtleWorld()    

bob = Turtle()
bob.delay = 0

bob.x = -150
bob.y = 90
bob.redraw()

snowflake( bob, 300)

world.mainloop()

