def create_pronounce_dict(filename = 'c06d'):
    """Reads from a file and
    crates a dictionay that maps from each word to a string that describes its primary prounciation.

    returns: map form string to prounciation
    """
    d = {}
    with open(filename, 'r') as fin:
        for line in fin:
            if line.startswith('#'): continue
            line = line.strip().split()
            word = line[0].lower()
            pron = ' '.join(line[1:])
            d[word] = pron
    return d


def check(words = 'words.txt'):
    """Removes either of the first two letters to make two, new four-letter words.
    Checks the three words have same homophones.
    """
    prounciation_dict = create_pronounce_dict()
    with open(words, 'r') as fin:
        for line in fin:
            word = line.strip()
            try:
                if prounciation_dict[word] == prounciation_dict[word[1:]]\
                    and prounciation_dict[word] == prounciation_dict[word[0]+word[2:]]:
                        print word, word[1:], word[0]+word[2:]
            except KeyError:
                continue


if __name__ == '__main__':
    check()
