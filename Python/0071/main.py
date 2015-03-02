def is_palindromic(number, start, end):
    """Checks if the number palindromic."""
    str_number = str(number)[start:end]
    return str_number[::] == str_number[::-1]


def check(i):
    """Checks whether the integer(i) has the properties described\
            in the puzzler."""
    return (is_palindromic(i, 2, 6) and
            is_palindromic(i+1, 1, 6) and
            is_palindromic(i+2, 1, 5) and
            is_palindromic(i+3, 0, 6))


def check_all():
    """Enumerates the six-digit numbers and prints any that satisfy the\
            requirements of the puzzler"""
    for i in range(100000, 999998):
        if check(i):
            print i


if __name__ == '__main__':
    print 'The following are the possible odometer readings:'
    check_all()
