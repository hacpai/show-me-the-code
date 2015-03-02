def is_reverse(son, mom):
    """Checks if son's age reversed resulted mom's age."""
    return str(son).zfill(2)[::-1] == str(mom)[::]


def check():
    """Assume the difference of son's age and mom's age is 15 to 50.

    mom's max age is less than 50.
    """
    for difference in range(15, 50):
        son = 0
        mom = difference
        t = []
        while mom < 100:
            if is_reverse(son, mom):
                t.append(son)
            if len(t) == 8:
                return t[-3]
            son += 1
            mom += 1

if __name__ == '__main__':
    print 'Son age that the problem is',
    print check()
