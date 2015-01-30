word_freq_dict = {}

with open( 'emma.txt', 'r' ) as file_handle:
    for line in file_handle:
        words = line.strip().split()
        for word in words:
            if word in word_freq_dict:
                word_freq_dict[word] += 1
            else:
                word_freq_dict[word] = 1

word_freq_lst = []

for word, freq in word_freq_dict.items():
    word_freq_lst.append( (word, freq ) )

word_freq_lst.sort( reverse = True)

for word, freq in word_freq_lst:
    print word + ': ' + str( freq )
