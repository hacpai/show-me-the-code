def capitalize_nested( nested_strings ):
    """Return a new nested list with all capitalized.
    """
    global capitalize_list

    for i in nested_strings:
        if type( i ) == type( [] ):
            capitalize_nested( i )
        else:
            capitalize_list.append( i.upper() )
    return capitalize_list


capitalize_list = []
print capitalize_nested( [['abc','a'], 'ca', ['a', ['a',],['a',['a','a']]] ] )
