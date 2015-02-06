import bisect


def make_word_list():
    """Reads lines from a file and builds a sorted list using append."""
    word_list = []
    fin = open( 'words.txt', 'r' )
    for line in fin:
        word = line.strip()
        word_list.append( word )

    return word_list


def is_match_in_bisect( word_list, word ):
    """Checks whether a word is in a sorted list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    """
    index = bisect.bisect_left( word_list, word )
    if index < len( word_list ) and word_list[index] == word:
        return True
    else:
        return False


def is_palindrome( word ):
    """Checks a word whether palindrome.
    """
    if word != word[::-1]:
        return False
    return True


def find_reverse_pairs():
    """Finds all the reverse pairs in the word list.
    """
    word_list = make_word_list()
    for word in word_list:
        reversed_word = '' 
        reversed_word = reversed_word.join( word[::-1] )
        if is_match_in_bisect( word_list, reversed_word ) \
            and is_palindrome( word ) == False:
            print word, reversed_word


find_reverse_pairs()

