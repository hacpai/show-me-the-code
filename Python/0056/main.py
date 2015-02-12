import shelve

from 0049/main.py import *


def store_anagrams( dbname, filename ):
    """Store the anagram dictionary in a 'shelf'.
    """
    db = shelve.open( dbname )
    anagram_dict = make_anagrams_dict( make_word_list( filename ) )
    for key, values in anagram_dict.iteritems():
        db[key] = values

    db.close()

def read_anagrams( dbname, word ):
    """Looks up a word and return a list of its anagrams.
    """
    db = shelve.open( dbname )
    sig = signature( word )
    try:
        return db[sig]
    except KeyError:
        return []
