def make_word_list( filename ):
    """Return word list that a file transformed.
    """
    fin = open( filename, 'r' )
    word_list = []
    for line in fin:
        word = line.strip()
        word_list.append( word )

    return word_list


def signature( word ):
    """Return a signature string include word of all letters.
    """
    t = list( word )
    t.sort()
    return ''.join( t )


def make_anagrams_dict( word_list ):
    """Generators all the sets of  words that are anagrams.
    """
    d = {}
    for word in word_list:
        word_signature = signature( word )
        if word_signature in d:
            d[word_signature].append( word )
        else:
            d[word_signature] = [word]

    return d


def anagrams_in_reversed_order( word_list ):
    """Returns a list that the largest set of anagrams first, followed by the second largeset set, and so on.
    """
    anagrams_dict = make_anagrams_dict( word_list )
    t = []
    for key, value in anagrams_dict.items():
        if len( value ) > 1:
            t.append( ( len( value ), value ) )

    t.sort( reverse = True )
    return t


def filter_length_anagrams_dict( word_list, length ):
    """Returns a anagrams dict with the given length.
    """
    d = make_anagrams_dict( word_list )
    t = []
    for key, words in d.items():
        if len( words ) > 1 and len( key ) == length:
            t.append( ( len( words ), words ) )

    return t

def print_anagrams( t ):
    """Print t line by line.
    """
    for line in t:
        print line


word_list = make_word_list( 'words.txt' )

#t = anagrams_in_reversed_order( word_list )
t = filter_length_anagrams_dict( word_list, 8 )
print_anagrams( t )
