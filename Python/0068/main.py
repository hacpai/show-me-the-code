class Time( object ):
    """Represents the time of day.

    attributes: hour, minute, second
    """


def time_to_int( time ):
    """Converts Times to integers.
    """
    minute = time.hour * 60 + time.minute
    second = minute * 60 + time.second
    return second


def int_to_time( second ):
    """Converts int to Time.
    """
    time = Time()
    minute, time.second = divmod( second, 60 )
    time.hour, time.minute = divmod( minute, 60 )
    return time


def increment( time, second ):
    """Returns a new time Object that adds a given number of seconds to a Time object.

    doesn't contain any loops
    """
    seconds = time_to_int( time ) + second
    return int_to_time( seconds )


time1 = Time()
time1.hour = 11
time1.minute = 3
time1.second = 4

time2 = Time()
time2.hour = 2
time2.minute = 30
time2.second = 50

new_time = increment( time1, 1200 )
print new_time.hour, new_time.minute, new_time.second
