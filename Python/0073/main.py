class Point( object ):
    """Represents a Point with 2-D space.

    attribute: x, y
    """
    def __init__( self, x = 0, y = 0 ):
        self.x = x
        self.y = y

    def __add__( self, other ):
        point = Point()
        point.x = self.x + other.x
        point.y = self.y + other.y
        return point

    def __str__( self ):
        return '( %d, %d )' % ( self.x, self.y )


point = Point( x = 10, y = 10 )
print point
orig_point = Point()
print orig_point
print point + orig_point
