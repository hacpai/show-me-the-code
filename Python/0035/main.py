def rotate_letter( letter, offset ):
    """Rotates a letter by n places.

    letter: single-letter string
    offset: int

    Returns: single-letter string
    """
    lower_alphabet = ""
    upper_alphabet = ""
    for w in range( 26 ):
        lower_alphabet += chr( ord( 'a' ) + w )
        upper_alphabet += chr( ord( 'A' ) + w )

    if letter.islower():
        alphabet = lower_alphabet
    elif letter.isupper():
        alphabet = upper_alphabet
    else:
        return letter

    return alphabet[( alphabet.find( letter ) + offset ) % 26]

def rotate_word( word, offset ):
    """Rotates a word by n places.

    word: string
    offset: integer

    Returns: string
    """
    encrypt_word = ""
    for w in word:
        encrypt_word += rotate_letter( w, offset )

    return encrypt_word


print rotate_word( "cheer", 7 )
print rotate_word( 'melon', -10 )
print rotate_word( 'sleep', 9 )
print rotate_word( 'CHEER', 7 )
