import bisect
import random
import string


def make_words_dict( fname ):
    """Reads a file, break each line into words, strips whitespace and
    punctuation from the words, and converte them to lowercase.
    """
    d = {}
    fin = open( fname )
    for line in fin:
        words = line.replace( '-', ' ' )
        for word in words.split():
            word = word.strip( string.whitespace + string.punctuation ).lower()
            d[word] = d.get( word, 0 ) + 1

    return d


def cumulative_sum( d ):
    """Builds a list that contains the cumulative sum of the word frequencise.
    """
    t = []
    cum_sum = 0
    for i in d.values():
        cum_sum += i
        t.append( cum_sum )

    return t


def choose_from_hist( word_list, freq_list ):
    """Bisection search to find the index in freq list
    and use the index to find the corresponding word in the word list.
    """
    x = random.randint( 0, freq_list[-1]-1 )
    index = bisect.bisect_left( freq_list, x )
    return word_list[index]


hist = make_words_dict( 'emma.txt' )
print choose_from_hist( hist.keys(), cumulative_sum( hist ) )
