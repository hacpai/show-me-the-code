class Time( object ):
    """Represents a Time object.

    attribute: hour, minute, second

    method: time_to_int
    """
    def time_to_int( self ):
        minute = self.hour * 60 + self.minute
        return minute * 60 + self.second


time = Time()
time.hour = 4
time.minute = 34
time.second = 17
print time.time_to_int()
