known = {}
def ackermann( m, n ):
    """Memoize the Ackermann function.
    """
    if ( m, n ) in known:
        return known[( m, n )]
    if m == 0:
        #known[( m, n )] = n + 1
        return n + 1
    elif m > 0 and n == 0:
        #known[( m, n )] = ackermann( m - 1, 1 )
        return ackermann( m - 1, 1 )
    elif m > 0 and n > 0:
        known[( m, n )] = ackermann( m - 1, ackermann( m, n - 1 ) )
        return known[( m, n )]


def ackermann_no_memo( m, n ):
    """Evaluates Ackermann's function.
    """
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann_no_memo( m - 1, 1 )
    elif m > 0 and n > 0:
        return ackermann_no_memo( m - 1, ackermann_no_memo( m, n - 1 ) )


start = time.time()
print ackermann_no_memo( 3, 4 )
print time.time() - start

start = time.time()
print ackermann( 3, 4 )
print time.time() - start

