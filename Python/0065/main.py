class Time( object ):
    """Represents the time of day.

    attributes: hour, minute, second
    """


def is_after( t1, t2 ):
    """Returns True if t1 follow t2 chronologically and False otherwise.

    don't use an if staatement.

    t1: Time object
    t2: Time object
    """
    return ( t1.hour, t1.minute, t1.second ) > ( t2.hour, t2.minute, t2.second )


time1 = Time()
time1.hour = 11
time1.minute = 3
time1.second = 4

time2 = Time()
time2.hour = 2
time2.minute = 30
time2.second = 50

print is_after( time1, time2 )
