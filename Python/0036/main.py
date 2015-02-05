def nested_sum( nested_list ):
    """Add up the elements from all of the nested list.
    """
    global accumulator

    for i in nested_list:
        if type( i ) == type( [] ):
            nested_sum( i )
        else:
            accumulator += i
    return accumulator


accumulator = 0
print nested_sum( [  2, 21 ,1, [ 1,[1, 2] ], [2, 2], [1,[1,2],2] ] )
