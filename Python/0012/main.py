import re

def patternHead( s ):
    flag = 0
    pattern_head = '[a-zA-Z_]'
    is_pattern = re.search ( pattern_head, s[0] )

    if is_pattern:
        flag = 1
    elif s[0] == '_':
        flag = 1
    else:
        flag = 0
    if flag == 1:
        return True
    else:
        return False

def patternBody ( s ):
    pattern_body = '\w'
    flag = 1
    for i in s[1:]:
        is_pattern = re.search( pattern_body, i )
        if is_pattern == None:
            flag = 0
            break
        elif i == '_':
            is_pattern = 1
    if flag == 1:
        return True
    else:
        return False
            
#ident = raw_input()

#print patternBody( ident )



#for i in identifie:
    #is_pattern = re.search( pattern_head, i )
    #if is_pattern:
        #print i 
stopword = ""
for line in iter( raw_input, stopword ):
    if patternHead( line ) == True:
        print patternBody( line )
    else:
        print False
