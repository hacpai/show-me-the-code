def is_palindrome( word ):
    """Return True if word is a palindrome and False otherwise.

    word: a string
    """
    if len( word ) < 2:
        return True
    elif word[0] == word[-1]:
        return is_palindrome( word[1:-1] )

    return False


print is_palindrome( "python" )
