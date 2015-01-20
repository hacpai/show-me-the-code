senten = raw_input()
  
#def addHay ( word ):
    #if word[0] in 'aeiouAEIOU':
        #return word + 'hay'
  
#def addQuay ( word ):
    #if word[0] == 'q' and word[1] == 'u':
        #return word[2:] + 'quay'

def isCons ( word ):
    word = word[1:] + word[0]
    for w in word:
        if w in 'aeiouy':
            return False
            break
    else:
        return True
  
def addAy ( word ):
    word_change = word[1:] + word[0]
    word_new = ''
    index = 0
    for w in word_change:
        if w not in 'aeiouy':
           word_change +=  w 
           index += 1
        else:
            word_new = word_change[index:] + 'ay'
            break

    return word_new
  
#def ifCapTurnToSmaLett ( word ):
    #for w in word:
        #if w >= 'A' and w <= 'Z':
            #word = word.lower()
            #break;
    #return word
  
#senten = 'Welcome to the Python world Are you ready'
senten = senten.lower()  
words  = senten.split()
for word in words:
#    print word
    #print word[0]
    #word = ifCapTurnToSmaLett( word )
    if word[0] in 'aeiou':
        print word + 'hay',
    elif word[0] == 'q' and word[1] == 'u':
        print word[2:] + 'quay',
    elif isCons( word ) == True:
        print word + 'ay',
    else:
        print addAy ( word ),
  
  
#s = 'eAt'
#print ifCapTurnToSmaLett(s)
