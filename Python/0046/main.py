def make_word_dict():
    """Generate a word dictionary with words.txt.
    """
    word_dict = {}
    fin = open( 'words.txt', 'r' )
    for line in fin:
        word = line.strip()
        word_dict[word] =  word

    return word_dict


def rotate_letter( letter, n ):
    """Rotate a letter by n place.
    """
    return chr( ( ord( letter ) - ord( 'a' ) + n ) % 26 + ord( 'a' ) )


def rotate_word( word, n ):
    """Rotate a word by n place.
    """
    res = ''
    for w in word:
        res += rotate_letter( letter, n )

    return res


def print_rotate_pairs( word, word_dict ):
    """Checks word has rotate pairs in word_dict.
    """
    for i in range( 1, 14 ):
        rotated = rotate_word( word, i )
        if rotated in word_dict:
            print word, i, rotated


word_dict = make_word_dict()

for word in word_dict:
    print_rotate_pairs( word, word_dict )
