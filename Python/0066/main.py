class Time( object ):
    """Represents the time of day.

    attributes: hour, minute, second
    """

def increment( time, second ):
    """Adds a given number of seconds to a Time object.

    doesn't contain any loops
    """
    total_second = time.hour * 60 * 60 + time.minute * 60 + time.second \
            + second
    minute, time.second = divmod( total_second, 60 )
    time.hour, time.minute = divmod( minute, 60 )


time1 = Time()
time1.hour = 11
time1.minute = 3
time1.second = 4

time2 = Time()
time2.hour = 2
time2.minute = 30
time2.second = 50

increment( time1, 1200 )
print time1.hour, time1.minute, time1.second
