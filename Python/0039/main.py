import time


def make_word_list_v1():
    """Reads the file words.txt and builds a list with one element per word.
    using append method
    """
    t = []
    fin = open( 'words.txt', 'r' )
    for line in fin:
        word = line.strip()
        t.append( word )

    return t


def make_word_list_v2():
    """Reads the file words.txt and builds a list with one element per word.
    using idiom t = t + [x]
    """
    t = []
    fin = open( 'words.txt', 'r' )
    for line in fin:
        word = line.strip()
        t = t + [word]

    return t


def make_word_list_v2_1():
    """Reads the file words.txt and builds a list with one element per word.
    using idiom t += [x]
    """
    t = []
    fin = open( 'words.txt', 'r' )
    for line in fin:
        word = line.strip()
        t += [word]

    return t


def measure_elapsed_time( f ):
    """use the time module to measure function elapsed time.

    f: function
    """
    start = time.time()

    f()

    return time.time() - start


print measure_elapsed_time( make_word_list_v1 ), 'seconds'
print measure_elapsed_time( make_word_list_v2 ), 'seconds'
print measure_elapsed_time( make_word_list_v2_1 ), 'seconds'
