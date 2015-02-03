def is_triangle ( a, b, c ):
    """Prints either "Yes" or "No" 
    whether form a triangle with the given lengths a, b, c
    """
    if a > b + c or b > a + c or c > a + b:
        print "No"
    else:
        print "Yes"

def prompt_user_input_and_check_form_triangle():
    """Prompts the usert to input three lengths
    conver them to integers and use is_triangle to check.
    """
    a = raw_input( "Please input first stick length: " )
    b = raw_input( "Please input second stick length: " )
    c = raw_input( "Please input third stick length: " )

    is_triangle( a, b, c )

prompt_user_input_and_check_form_triangle()
