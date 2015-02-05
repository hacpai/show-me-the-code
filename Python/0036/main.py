def nested_sum( nested_list ):
    """Add up the elements from all of the nested list.
    """
    accumulator = 0
    for i in nested_list:
        if type( i ) == type( [] ):
            accumulator += nested_sum( i )
            return accumulator
        accumulator += i
    return accumulator


print nested_sum( [  2, 21 , 2, 2, [1, 2] ] )
