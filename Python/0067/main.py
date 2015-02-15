import copy


class Time( object ):
    """Represents the time of day.

    attributes: hour, minute, second
    """

def increment( time, second ):
    """Returns a new time Object that adds a given number of seconds to a Time object.

    doesn't contain any loops
    """
    new_time = copy.copy( time )
    total_second = time.hour * 60 * 60 + time.minute * 60 + time.second \
            + second
    minute, new_time.second = divmod( total_second, 60 )
    new_time.hour, new_time.minute = divmod( minute, 60 )

    return new_time


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
