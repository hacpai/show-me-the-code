def gcd( a, b ):
    """Competes a and b greatest common divisor.
    """
    if b == 0:
        return a
    else:
        return gcd( b, a%b )


print gcd( 70, 15 )
