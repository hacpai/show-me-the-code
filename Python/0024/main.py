# two-by-two of the grid
def print_side():
    print "+ - - - - ",
def print_node():
    print "+"
def print_verti_space():
    print "|         ",
def print_verti():
    print "|"
def do_twice( func ):
    func()
    func()
def do_four( func ):
    do_twice( func )
    do_twice( func )
def print_sides():
    do_twice( print_side )
    print_node()
def print_all_verti_space():
    do_twice( print_verti_space )
    print_verti()
def print_row():
    print_sides()
    do_four( print_all_verti_space )
def print_two_rows_tow_columns():
    do_twice( print_row )
    print_sides()
print_two_rows_tow_columns()

# four-by-four of the grid
def do_four_and_once( need_do_four, need_do_one ):
    do_four( need_do_four )
    need_do_one()

def print_first_line():
    do_four_and_once( print_side, print_node )

def print_second_line():
    do_four_and_once( print_verti_space, print_verti )
def print_four_all_verti_space():
    do_four( print_second_line )
def print_row_four_col():
    print_first_line()
    print_four_all_verti_space()
def print_four_rows_four_colums():
    do_four_and_once( print_row_four_col, print_first_line )
print_four_rows_four_colums()
