import random


def markov_analysis( fname, n ):
    """Reads a text file and perfom Markov analysis.

    Return a dictionary that maps from prefixes to a collection of suffixes.

    fname: a text file
    n: n order
    """
    d = {}
    prefix = tuple()
    fin = open( fname )
    for line in fin:
        words = line.strip().split()
        for word in words:
            if len( prefix ) < 2:
                prefix += ( word, )
                break
            # if there is no entry for this prefix,
            #make one d[prefix] = [word]
            if d.setdefault( prefix, [word] ):
                d[prefix].append( word )
            prefix = prefix[1:] + ( word, )

    return d


def generate_random_text( suffix_map, n ):
    """Generates a random text with n words based on the Markov analysis.
    """
    prefix = random.choice( suffix_map.keys() )
    for i in range( n ):
        suffixes = suffix_map.get( prefix, None )
        if suffixes == None:
            # if the start isn't in map, wo got to the end of the 
            # original text, so we have to start again.
            generate_random_text( n - i )
            return
        word = random.choice( suffixes )
        print word,
        prefix = prefix[1:] + ( word, )


generate_random_text( markov_analysis( 'emma.txt', 2 ), 100 )
