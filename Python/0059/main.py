import urllib


def print_zip_information():
    """Prompts the user for a zip code and
    prints the name and population of the corresponding town.
    """
    zip_code = raw_input( 'Please input a zip code: ' )
    url = 'http://www.uszip.com/zip/%s' % zip_code
    conn = urllib.urlopen( url )
    for line in conn.fp:
        line = line.strip()
        if 'Population' in line:
            print line
        if 'Logitude' in line:
            print line
        if 'Latitude' in line:
            print line

    conn.close()


print_zip_information()
