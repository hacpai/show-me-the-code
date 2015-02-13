import os


def file_mp3_list( dirname, suffix ):
    """Return a list of complete paths for all files with a given suffix,
    like .mp3.
    """
    paths_list = []
    for root, dirs, names in os.walk( dirname ):
        for name in names:
            if name.endswith( suffix ):
                paths_list.append( os.path.join( root, name ) )

    return paths_list


def recognize_duplicates_use_md5sum( file_list ):
    """Uses md5sum to compute a "checsum" for each files in file list
    to recognize duplicates.
    """
    md5_dict = {}
    for filename in file_list:
        cmd = 'md5sum ' + filename
        fp = os.popen( cmd )
        md5, _= fp.read().split()
        if md5 not in md5_dict:
            md5_dict[md5] = [filename]
        else:
            md5_dict[md5].append( filename )
        fp.close()
    return md5_dict


def is_duplicates_use_diff( file_list ):
    """Uses the unix command diff to double-check.
    """
    for file1 in file_list:
        for file2 in file_list:
            if file1 < file2:
                cmd = 'diff %s %s' % ( file1, file2 )
                fp = os.popen( cmd )
                res = fp.read()
                fp.close()
                if res:
                    return False

    return True


def print_duplicates( dirname, suffix ):
    """Prints duplicates file.
    """
    md5_dict = recognize_duplicates_use_md5sum( file_mp3_list( dirname, suffix ) )
    for md5, files in md5_dict.iteritems():
        if len( files ) > 1:
            print 'The following files have the same checksum:'
            for file in files:
                print file,

            if is_duplicates_use_diff( files ):
                print '\nAnd they are identical.'


print_duplicates( '.', '.py' )
