def ack( m, n ):
    """Evaluates Ackermann's function with the given m and n.
    """
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack( m - 1, 1 )
    elif m > 0 and n > 0:
        return ack( m - 1, ack( m, n - 1) )
    else:
        print "Please input natural number."


print ack( 3, 4 )
