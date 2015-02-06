def bisect_search( t, target, start, end ):
    """Return the index of the value in the sorted list,
    None if it's not.

    Precondition: the words in the list using bisecton search.

    t: sorted list
    target: a target value
    """
    middle_index = ( start + end ) / 2
    middle_value = t[middle_index]
    if target == middle_value:
        return middle_index + 1
    elif end <= start:
        return 'None'
    elif target > middle_value:
        return bisect_search( t, target, middle_index+1, end )
    else:
        return bisect_search( t, target , start, middle_index )


def make_word_list():
    """Reads lines from a file and builds a sorted list using append."""
    word_list = []
    fin = open( 'words.txt', 'r' )
    for line in fin:
        word = line.strip()
        word_list.append( word )

    return word_list


word_list = make_word_list()

for word in ['alien', 'allen']:
        start = 0
        end = len( word_list )
        print word, 'in list', bisect_search( word_list, word, start, end )
