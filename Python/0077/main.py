class Time( object ):
    """Represents a time of whole day.

    attributes: seconds
    """
    def __init__( self, hour, minute, second ):
        minutes = hour * 60 + minute
        self.seconds = minutes * 60 + second

    def __comp__( self, other ):
        """Returns a positive number if the first object is greater,
        a negative number if the second object is greater,
        and 0 if they are equal to each other.
        """
        return cmp( self.seconds, other.seconds )
