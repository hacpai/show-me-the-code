import random


def has_duplicates( t ):
    """Returns True if there is any element that appears more than once,
    False otherwise."""
    new_t = t[:]
    new_t.sort()
    for i in range( len( new_t ) - 1):
        if new_t[i] == new_t[i+1]:
            return True
    return False


def generate_birthday( n ):
    """Generates a list of birthdays between 1 and 365.

    n: length of list
    """
    birthdays = []
    for i in range( n ):
        birthday = random.randint( 1, 365 )
        birthdays.append( birthday )

    return birthdays


def count_matches( students, samples ):
    """Generates ( samples ) samples of ( students ) students, and counts
    how many of them have at least one pair of students with the same day.
    """
    count = 0
    for i in range( samples ):
        if has_duplicates( generate_birthday( students ) ):
            count += 1

    return count


"""run the birthday simulation 1000 times and print the number of matches"""
num_students = 23
num_simulations = 1000
count = count_matches( num_students, num_simulations )

print 'After %d simulation' % num_simulations
print 'with %d students' % num_students
print 'there were %d simulation with at least one match' % count
print 'and the chances that two of the class have the same birthday is %f' %( 1.0 * count / num_simulations )
