def check_fermat( a, b, c, n ):
    """Check Fermat's Last Theorem with the given a, b, c and n.
    """
    if a**n + b**n - c**n == 0 and n > 2:
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."


def prompt_user_input_and_check_fermat():
    """Prompts the user to input values for a, b, c and n,
        converts the to integers and uses check_fermat to check.
    """
    a = int( raw_input( "Please input a 'a': " ) )
    b = int( raw_input( "Please input a 'b': " ) )
    c = int( raw_input( "Please input a 'c': " ) )
    n = int( raw_input( "Please input a 'n', 'n' need greater than 2: " ) )
    check_fermat( a, b, c, n )


prompt_user_input_and_check_fermat()
