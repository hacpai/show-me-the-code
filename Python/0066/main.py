from Card import *


class Hist(dict):

    def __init__(self, seq=None):
        if seq == None:
            seq = []
        for x in seq:
            self.count(x)

    def count(self, x):
        """Counts a number of x.
        """
        self[x] = self.get(x, 0) + 1

class PokerHand(Hand):
    """Represents a poker hand."""

    labels = ['straightflush', 'fourkind', 'fullhouse', 'flush',
            'straight', 'threekind', 'twopair', 'pair', 'highcard']

    def make_hist(self):
        """
        Builds a histogram of suits and ranks that appear in the hand.

        Creates attributes:
            suits: a histogram of the suits in the hand.
            ranks: a histogram of the ranks.
            sets: a list of the ranks values.
        """
        self.ranks = Hist()
        self.suits = Hist()
        for card in self.cards:
            self.ranks.count(card.rank)
            self.suits.count(card.suit)

        self.sets = self.ranks.values()
        self.sets.sort(reverse=True)

    def has_same_suit(self, num):
        """Return True if the number of hand has same suits, False otherwise.
        """
        for val in self.suits.values():
            if val >= num:
                return True
        return False

    def check_sets(self, *kinds):
        """Checks whether self.sets contains sets that are at least as big as the requirements in kinds.

        kinds: list of int
        """
        for kind, ranks_val in zip(kinds, self.sets):
            if kind > ranks_val:
                return False
        return True

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        return self.has_same_suit(5)

    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise.

        Note that this works correctly for hands with more than 2 cards.
        """
        return self.check_sets(2)

    def has_twopair(self):
        """Returns True if the hand has two pair, False otherwise.

        Note that this works correctly for hands with more than 4 cards.
        """
        return self.check_sets(2, 2)

    def has_threekind(self):
        """Return True if the hand has three of a kind, False otherwise.

        Note that this works correctly for hands with more than 3 cards.
        """
        return self.check_sets(3)

    def has_straight(self):
        """Return True if the hand has five cards with ranks in sequence.

        Note that this works correctly for hands with more than 5 cards.
        """
        ranks = self.ranks.copy()
        ranks[14] = ranks.get(1, 0)
        return self.check_row(ranks)

    def check_row(self, ranks, n=5):
        """Checks whether the histogram has n ranks in a row.

        hist: map from rank to frequency
        n: number we need to get to
        """
        count = 0
        for n in range(1, 15):
            if n in ranks:
                count += 1
                if count >= 5:
                    return True
            else:
                count = 0
        return False

    def has_fullhouse(self):
        """Return True the hand has three cards with one rank, two cards with another.

        Note that this works correctly for hands with more than 5 cards.
        """
        return self.check_sets(3,2)

    def has_fourkind(self):
        """Return True if the hand has four of a kind, False otherwise.

        Note that this works correctly for hands with more than 4 cards.
        """
        return self.check_sets(4)

    def has_straightflush(self):
        """Return True if the hand has five cards in sequence and with the same suit.

        Note that this works correctly for hands with more than 5 cards.
        """
        d = Hist()
        for c in self.cards:
            d.setdefault(c.suit, PokerHand()).add_card(c)
        for hand in d.itervalues():
            if len(hand.cards) < 5:
                continue
            hand.make_hist()
            if hand.has_straight():
                return True
        return False

    def has_highcard(self):
        """Return True if this hand has a high card."""
        return len(self.cards)

    def classify(self):
        """Figures out the highest-value classification for a hand and
        sets the label attribute accordingly.
        """
        for label in PokerHand.labels:
            f = getattr(self, 'has_'+label)
            if f():
                self.label = label
                return

def print_attributes(obj):
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)


if __name__ == '__main__':
    kinds = Hist()
    for k in range(10000):
        if k % 1000 == 0:
            print k
        for i in range(10):
            deck = Deck()
            deck.shuffle()
            hand = PokerHand()
            deck.move_cards(hand, 5)
            hand.make_hist()
            hand.classify()
            kinds.count(hand.label)

    for label in PokerHand.labels:
        try:
            print label, 100.00 * kinds[label]/100000, '%'
        except KeyError:
            continue
