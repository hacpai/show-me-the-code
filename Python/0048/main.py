def statistical_letter( word ):
    """Statistical the number of letters in word.
    """
    d = {}
    for w in word:
        d[w] = d.get( w, 0 ) + 1

    return d


def most_frequent( word ):
    """Prints the letters in decreasing order of frequency with the given word.
    """
    t = []
    d = statistical_letter( word )
    for w, freq in d.items():
        t.append( ( freq, w ) )

    t.sort( reverse = True )

    for freq, w in t:
        print w, freq


fin = open( 'words.txt' ).read()
most_frequent( fin )
