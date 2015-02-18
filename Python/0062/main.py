from datetime import date
from datetime import datetime


def print_day_of_week():
    """Gets the current date and prints the day of the week.
    """
    print date.today().strftime( '%A' )


def get_age( birthday ):
    """Gets the user's age with given birthday.

    birthday: a tuple of (year, month, day )
    """
    my_birthday = date( *birthday )
    current_date = date.today()
    age = current_date.year - my_birthday.year
    if current_date.month > my_birthday.month:
        return age
    return age - 1


def time_to_birthday( birthday ):
    """Gets the number of days, hours, minutes and seconds until next birthday.

    birthday: a tuple of (year, month, day )

    return a date object
    """
    today = datetime.today()
    my_birthday = datetime( today.year, *birthday[1:] )
    if my_birthday < today:
        my_birthday = my_birthday.replace( year = today.year + 1 )

    return my_birthday - today


def double_day( birthday1, birthday2, n ):
    """Computes birthday1 and birthday2 of Double Day.

    birthday1: datetime birthday of the younger person
    birthday2: datetime birthday of the older person
    """
    assert birthday1 > birthday2
    return date( *birthday1 ) +\
            ( date( *birthday1 ) - date ( *birthday2 ) ) * ( n - 1 )


print 'Today',
print_day_of_week()
print 'My age', get_age( ( 1993, 7, 24 ) )
print 'Remain day of next birthday', time_to_birthday( ( 1993, 7, 24 ) )
print 'Double Day',double_day( ( 1994, 8, 9 ), ( 1993, 6, 6 ), 2 )
