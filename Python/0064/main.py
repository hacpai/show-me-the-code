class Time( object ):
    """Represents the time of day.

    attributes: hour, minute, second
    """


def print_time( time ):
    """Prints it in the from hour:minute:second.
    """
    print '%.2d:%.2d:%.2d' % ( time.hour, time.minute, time.second )


time = Time()
time.hour = 11
time.minute = 3
time.second = 4
print_time( time )
