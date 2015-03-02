def is_triple_double(word):
    """Checks if a word a word contains three consecutive double letters."""
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            count = 0
            i += 1
    return False


def find_triple_double():
    """Finds all words that triple double letters in words.txt"""
    with open('words.txt', 'r') as fin:
        for line in fin:
            word = line.strip()
            if is_triple_double(word):
                print word


if __name__ == '__main__':
    print 'Herre are all the words in the list that have'
    pritn 'three consecutive double letters.'
    find_triple_double()
