def sed( pattern, replacement, file1, file2 ):
    """Read the first file and write the contents into the second file.
    if the pattern string appears in the file, replace it.
    """
    try:
        fin = open( file2, 'w' )
        with open( file1, 'r' ) as fout:
            for line in fout:
                line = line.replace( pattern, replacement )
                fin.write( line )

        fin.close()
    except:
        print 'Something went wrong.'

