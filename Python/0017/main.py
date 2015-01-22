def word_max_len ( my_dict ):
    max_len = 1
    my_dict = unicode( my_dict, 'utf-8' )
    my_dict = my_dict.split(" ")
    for word in my_dict:
        if max_len < len( word ):
            max_len = len( word )
    return max_len

def rmm_word_seg( sen, max_len, my_dict ):
    words = []
    sen = unicode( sen, 'utf-8' )
    end = len(sen)
    my_dict = unicode( my_dict, 'utf-8' )
    my_dict = my_dict.split(" ")
    while end > 0:
        for begin in range ( end - max_len, end ):
            if sen[begin:end] in my_dict:
                words.insert( 0, sen[begin:end] )
                break
        else:
            words.insert( 0, sen[begin:end] )

        end = begin 

    return words

my_dict = raw_input()
for sen in iter( raw_input, "" ):
    max_len = word_max_len( my_dict )
    words = rmm_word_seg( sen, max_len, my_dict )
#    delimiter = " "
#    print delimiter.join(words).lstrip().encode('utf_8')
    for k,word in enumerate(words):
        if(k==(len(words)-1)):
            print word.encode('utf-8')
        else:
            print word.encode('utf-8'),
