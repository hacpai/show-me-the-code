def signature( word ):
    """Return a signature string include word of all letters.
    """
    t = list( word )
    t.sort()
    return ''.join( t )


def make_anagrams_dict( filename ):
    """Generators all the sets of  words that are anagrams.
    """
    d = {}
    fin = open( filename, 'r' )
    for line in fin:
        word = line.strip().lower()
        word_signature = signature( word )
        if word_signature in d:
            d[word_signature].append( word )
        else:
            d[word_signature] = [word]

    return d


def difference_number_of_letters( word1, word2 ):
    """Computes a the number of difference letters from word1 and word2.
    """
    count = 0
    for w1, w2 in zip( word1, word2 ):
        if w1 != w2:
            count += 1

    return count


def print_metathesis_pair( filename ):
    """Prints all of the metathesis pairs in the dictionary.
    """
    d = make_anagrams_dict( filename )
    for words in d.itervalues():
        if len( words ) > 1:
            for word1 in words:
                for word2 in words:
                    if word1 < word2 and \
                            difference_number_of_letters( word1, word2 ) == 2:
                        print word1, word2


print_metathesis_pair( 'words.txt' )

