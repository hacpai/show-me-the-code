import os


def walk ( dirname ):
    """Walks through a directory, prints the names of all the files,
    and calls itself recursively on all the directories.

    dirname: string name of directory
    """
    for name in os.listdir( dirname ):
        path = os.path.join ( dirname, name )
        if os.path.isfile( path ):
            print path
        else:
            walk( path )


def print_all_file_name( dirname ):
    """Prints the names of the file in a given directory and its subdirectories.
    """
    for root, dirs, file in os.walk( dirname ):
        for f in file:
            print os.path.join( root, f )


walk( '.' )
print_all_file_name( '.' )
