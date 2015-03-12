def make_word_dict(filename='words.txt'):
    """Reads the words in words.txt and return a dictionary
    that contains the word as key.
    """
    word_set = set() 
    with open(filename, 'r') as fin:
        for line in fin:
            word = line.strip()
            word_set.add(word)
    for letter in ['a', 'i', '']:
        word_set.add(letter)
    return word_set


def children(word, word_dict):
    """Return a list of all words
    that can be formed by removing one letter.
    """
    t = []
    for i in range(len(word)):
        subword = word[:i] + word[i+1:]
        if subword in word_dict:
            t.append(subword)
    return t


memo = {}
memo[''] = ['']
def is_reducible(word, word_dict):
    """If word is reducible, return a list of its reducible children.

    Also adds an entry to the memo dictionary.

    A word is reducible if it has at least one child that is
    reducible. The empty word is also reducible.
    """
    res = []
    if word in memo:
        return memo[word]
    for subword in children(word, word_dict):
        t = is_reducible(subword, word_dict)
        if t:
           res.append(subword)
    memo[word] = res
    return res


def print_trail(word):
    """Prints the sequence of words
    that reduces this word to hte empty string.

    If there is more than one choice, it chooses the first.
    """
    if len(word) == 0:
        return
    print word,
    t = is_reducible(word, word_dict)
    print_trail(t[0])


def all_reducible(word_dict):
    """Checks all words in the word_dict; returns a list reducible ones.
    """
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            res.append(word)
    return res


def print_longest_word(word_dict):
    """Print the longest 5 word in word_dict."""
    words = all_reducible(word_dict)
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)
    for length, word in t[:5]:
        print_trail(word)
        print


if __name__ == '__main__':
    word_dict = make_word_dict()
    print_longest_word(word_dict)
