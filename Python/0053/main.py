import string
import sys
import matplotlib.pyplot as pyplot


def process_file( filename ):
    """Reads a text from a file, counts word freqencies.

    Return a dictionary that key-value pairs.
    """
    hist = {}
    skip_head( filename )
    with open( filename, 'r' ) as file_handle:
        for line in file_handle:
            words = line.replace( '-', ' ' ).lower().strip()
            for word in words.split():
                word = word.strip( string.whitespace + string.punctuation )
                hist[word] = hist.get( word, 0 ) + 1

    return hist


def skip_head( filename ):
    """Skips the head information in file.
    """
    with open( filename, 'r' ) as file_handle:
        for line in file_handle:
            if line.startswith( '*END*THE SMALL PRINT!' ):
                break

def rank_freq( hist ):
    """Reurrn a list of tuples where each tuple is a rank
    and the number of times the item with that rank appeared.
    """
    freqs = hist.values()
    freqs.sort( reverse = True )
    rf = [( r, f ) for r, f in enumerate( freqs, start = 1 )]

    return rf


def print_ranks( rank_freq ):
    """Prints the rank vs. frequency data."""
    for r, f in rank_freq:
        print r, f


def plot_ranks( rank_freq, scale = 'log' ):
    """Plots frequency vs. rank."""
    rs, fs = zip( *rank_freq )

    pyplot.clf()
    pyplot.xscale( scale )
    pyplot.yscale( scale )
    pyplot.title( 'Zipf plot' )
    pyplot.xlabel( 'rank' )
    pyplot.ylabel( 'frequency' )
    pyplot.plot( rs, fs, 'r-' )
    pyplot.show()


def main( name, filename = 'emma.txt', flag = 'plot', *args ):
    hist = process_file( filename )
    rf = rank_freq( hist )
    if flag == 'print':
        print_ranks( rf )
    elif flag == 'plot':
        plot_ranks( rf )
    else:
        print 'Usage: python main.py filename [print|plot]'


main( *sys.argv )
