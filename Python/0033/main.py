import math


def square_root ( a ):
    """Computes squar root of a
    """
    espilon = 0.1e-11
    x = a
    while True:
        y = ( x + a / x ) / 2.0
        if abs( y - x ) < espilon:
            return y
        x = y


def test_square_root():
    """Compares custom square and math.sqrt.
    """
    a = 1.0
    while a < 10.0:
        print a, '{:<13}'.format( square_root( a ) ), \
                '{:<13}'.format( math.sqrt( a ) ), \
                abs( square_root( a ) - math.sqrt( a ) )
        a += 1


test_square_root()
