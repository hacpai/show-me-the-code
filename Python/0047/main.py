import random


def sort_by_length( word_list ):
    """Sort a list of words in reverse order  by length.

    It is stable that print words with the same length in the same order.
    """
    t = []
    for word in word_list:
        t.append( ( len( word ), word ) )

    t.sort( reverse = True )
    for length, word in t:
        print word


def sort_random_by_length( word_list ):
    """Sort a list of words in reverse order  by length.

    It is unstable that print random words if two words have the same length.
    """
    t = []
    for word in word_list:
        t.append( ( len( word ), random.random(), word ) )

    t.sort( reverse = True )

    for length, _, word in t:
        print  word


print sort_random_by_length( ['hello', 'world', 'applee', 'wooooo', 'Finich', 'Harlod', 'apple', 'nba', 'ibm', 'tuple'] )

