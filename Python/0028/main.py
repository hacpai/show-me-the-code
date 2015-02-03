from polygon import * 


def koch( t, length ):
    """Draws a Koch curve with the given length.

    t: Turtle
    length: length
    """
    if length < 3:
        return bk( t, length )
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
        rt( t, 120 )
        koch( t, length )


world = TurtleWorld()    

bob = Turtle()
bob.delay = 0

bob.x = -120
bob.y = 20
bob.redraw()

snowflake( bob, 200)

world.mainloop()

