def eval_loop(  ):
    """Print the result with the user input iteratively.

    """
    while True:
        val = raw_input( '> ' )
        if val == 'done':
            return result
        result = eval( val )
        print result


print eval_loop()
