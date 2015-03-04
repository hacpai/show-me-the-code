def sort_alphabetical_order(lst):
    """Sorts a list of words by length,

    Then sorts a list of words by alphabetical order for same word's len.
    """
    t = []
    new_t = []
    for word in lst:
        if ord(word[0]) > ord('Z'):
            flag = 0
        else:
            flag = 1
        t.append((len(word), word[0].lower(), flag, word))
    t.sort()

    for index, initial, _, word in t:
        new_t.append(word)
    return new_t


if __name__ == '__main__':
    word_list = ['A', 'a', 'AB', 'aB']
    for w in sort_alphabetical_order(word_list):
        print w

