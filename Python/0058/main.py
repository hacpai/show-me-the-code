import os


def make_files_list( dirname, suffix ):
    """Traverses directory and Returns a list of files with suffix.
    """
    files_list = []
    for root, dirs, files in os.walk( dirname ):
        for name in files:
            if name.endswith( suffix ):
                files_list.append( os.path.join( root, name ) )

    return files_list


def histogram( file_list ):
    """statistical the number of code line, newline and comment line.
    """
    code_line = 0
    new_line = 0
    comment_line = 0
    for file in file_list:
        with open( file, 'r' ) as file_handler:
            for line in file_handler:
                line = line.strip()
                if line.startswith( ( "\"", "#" ) ):
                    comment_line += 1
                elif not line:
                    new_line += 1
                else:
                    code_line += 1

    return ( code_line, new_line, comment_line )


suffix = raw_input( 'The code suffix is ' ) 
file_list = make_files_list( '.', suffix )
code_line, new_line, comment_line = histogram( file_list )
print 'Code line is', code_line
print 'New line is', new_line
print 'Comment line', comment_line
