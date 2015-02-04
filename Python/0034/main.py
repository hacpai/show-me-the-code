import math


def factorial( n ):
    """Computes mathematics expression n!
    """
    result = 1
    if n == 0:
        return 1
    else:
        for i in range( 1, n ):
            result *= i

        return result * n

def estimate_pi():
    """Computes an estimate of pi.

    Algorithm due to Srinivasa Ramanujan, from
    http://en.wikipedia.org/wiki/Pi
    """
    precision = 1e-15
    sum = 0
    k = 0
    while True:
        term = ( factorial( 4*k ) * ( 1103 + 26390*k ) ) / \
                ( factorial( k ) ** 4 * 396 ** ( 4*k ) )
        sum += term
        if abs( term - 0.0 ) < precision:
            break
        k += 1

    return 1 / ( 2 * math.sqrt(2) / 9801 * sum )


print estimate_pi()

