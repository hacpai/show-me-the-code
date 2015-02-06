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


def is_interlock( word_list, word ):
    """Retunr True if a word can be split into two interlocked words.
    """
    event_sequence = word[::2]
    odd_sequence = word[1::2]
    if is_match_in_bisect( word_list, event_sequence ) \
            and is_match_in_bisect( word_list, odd_sequence ):
        return True
    return False


def is_n_interlock( word_list, word, n ):
    """Return True if a word can be split into n interlocked words.
    """
    for i in range( n ):
        if not is_match_in_bisect( word_list, word[i::n] ):
            return False
    return True


word_list = make_word_list()

print 'All pairs of words that interlock: '
for word in word_list:
    if is_interlock( word_list, word ):
        print word, word[::2], word[1::2]

print 'All words that are three-way interlocked: '
for word in word_list:
    if is_n_interlock( word_list, word, 3 ):
        print word, word[::3], word[1::3], word[2::3]
