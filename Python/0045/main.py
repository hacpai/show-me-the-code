def has_duplicates( t ):
    """Checks whether any element appears more than once in a sequence.

    Simple version using a for loop.

    t: sequence
    """
    d = dict()
    for i in t:
        if i in d:
            return True
        d[i] = True
    return False


def has_duplicates_v2( t ):
    """Checks whether any element appears more than once in a sequence.

    Faster version using a set.

    t: sequence
    """
    return len( set( t ) ) < len( t )

