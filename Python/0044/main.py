def invert_dict( d ):
    """invert key and value in dictionary using setdefault method.
    """
    invert = dict()
    for key in d:
        val = d[key]
        if invert.setdefault( val, [key] ):
            invert[val].append( key )

    return invert


