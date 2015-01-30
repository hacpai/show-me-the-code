def is_palin_str ( name ):
    for i in range( len( name ) / 2 ):
        if name[i] != name[-1-i]:
            return False
    return True

print "The name list is: "

with open ( 'names.txt', 'r' ) as file_handler:
    max_len = 0
    for line in file_handler:
        word = line.strip()
        if is_palin_str( word ) == True:
            print word
            if max_len < len( word ):
                max_len = len( word )
                max_name = word

print "The max length of name is:", max_name
