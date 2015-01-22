def create_index():
    index_dict = {}
    i = 0
    while i < 100:
        line = raw_input()
        words = line.strip().split()
        i += 1
        for word in words:
            if word in index_dict:
                index_dict[word].add(i)
            else:
                index_dict[word] = set()
                index_dict[word].add(i)
    return index_dict

def order_index( word_line ):
    lst = []
    for word in word_line:
        ret = ""
        i = 1 
        #print word + ":",
        ret += ( word + ":" + " " )
        for index in sorted( word_line[word] ):
            if i < len( word_line[word] ):
                #print str(index) + ",",
                ret += ( str(index) + "," + " " )
                i += 1
            else:
                #print index
                ret += ( str( index ) )
        lst.append( ret )
    lst.sort()
    return lst

def print_index( order_lst ):
    for i in range( len(order_lst) ):
        print order_lst[i] 

def print_set ( ret ):
    count = 1 
    ret = sorted( ret )
    for i in ret:
        if count < len( ret ):
            print str(i) + ",",
            count += 1
        else:
            print str(i)

def and_query( word_line, words ):
    ret = set()
    for i in range( 1, 101 ):
        ret.add(i)
    for word in words:
        if word in word_line and ret & word_line[word] != set():
            ret &= word_line[word]
        else:
            ret.clear()
    if len( ret ) > 0:
        print_set( ret )
    else:
        print "None"

def or_query( word_line, words ):
    ret = set()
    for word in words:
        if word in word_line:
            ret |= word_line[word]

    if len( ret ) > 0:
        print_set( ret )
    else:
        print "None"

def query( word_line ):
    for line in iter( raw_input, ""):
        words = line.strip().split()
        if words[0] == "OR:":
            words.remove( "OR:" )
            or_query( word_line, words )
        elif words[0] == "AND:":
            words.remove( "AND:" )
            and_query( word_line, words )
        else:
            and_query( word_line, words )

word_line = create_index()
#print word_line
order_lst = order_index( word_line )
print_index( order_lst )
query( word_line )
