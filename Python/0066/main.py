from Card import *


class PokerHand(Hand):

    def make_hist(self):
        """Builds a histogram of suits and ranks that appear in the hand.

        Stores the result in attribute suits and ranks.
        """
        self.suits = {}
        self.ranks = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
        self.rank_list = self.ranks.keys()
        self.rank_list.sort()
        if self.rank_list[0] == 1:
            self.rank_list.append(14)

    def has_same_suit(self, num):
        """Return True if the number of hand has same suits, False otherwise.
        """
        self.make_hist()
        for val in self.suits.values():
            if val >= num:
                return True
        return False

    def has_same_rank(self, same_rank=2, num=1):
        """Return True if the number of hand has same ranks, False otherwise.
        """
        self.make_hist()
        self.rank_hist = {}
        for kind in self.ranks.values():
            self.rank_hist[kind] = self.rank_hist.get(kind, 0) + 1

        try:
            if self.rank_hist[same_rank] == num:
                return True
        except KeyError:
            return False
        return False

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        return self.has_same_suit(5)

    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise.

        Note that this works correctly for hands with more than 2 cards.
        """
        return self.has_same_rank(2, 1)

    def has_twopair(self):
        """Returns True if the hand has two pair, False otherwise.

        Note that this works correctly for hands with more than 4 cards.
        """
        return self.has_same_rank(2, 2)

    def has_three_of_a_kind(self):
        """Return True if the hand has three of a kind, False otherwise.

        Note that this works correctly for hands with more than 3 cards.
        """
        return self.has_same_rank(3, 1)

    def has_straight(self):
        """Return True if the hand has five cards with ranks in sequence.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.make_hist()
        count = 1
        for i in range(len(self.rank_list)-1):
            if self.rank_list[i] + 1 == self.rank_list[i+1]:
                count += 1
                if count >= 5:
                    return True
            else:
                count = 1
        return False

    def has_full_house(self):
        """Return True the hand has three cards with one rank, two cards with another.

        Note that this works correctly for hands with more than 5 cards.
        """
        return self.has_three_of_a_kind() and self.has_pair()

    def has_four_of_a_kind(self):
        """Return True if the hand has four of a kind, False otherwise.

        Note that this works correctly for hands with more than 4 cards.
        """
        return self.has_same_rank(4, 1)

    def has_straight_flush(self):
        """Return True if the hand has five cards in sequence and with the same suit.
        
        Note that this works correctly for hands with more than 5 cards.
        """
        return self.has_flush() and self.has_straight()

    def classify(self):
        """Figures out the highest-value classification for a hand and
        sets the label attribute accordingly.
        """
        if self.has_straight_flush():
            self.label = 'straight flush'
            return
        if self.has_four_of_a_kind():
            self.label = 'four of a kind'
            return
        if self.has_full_house():
            self.label = 'full house'
            return
        if self.has_flush():
            self.label = 'flush'
            return
        if self.has_straight():
            self.label = 'straight'
            return
        if self.has_three_of_a_kind():
            self.label = 'three of a kind'
            return
        if self.has_twopair():
            self.label = 'two pair'
            return
        if self.has_pair():
            self.label = 'pair'
            return
        self.label = 'no pair'
        return

def main():
    """Estimate the probabilities of the various hands.

    shuffles a deck of cards, divides it into hands, classify the hands and counts the number of times various classifications appear.
    """
    categories = {}
    for i in range(100000):
        deck = Deck()
        deck.shuffle()
        hand = PokerHand()
        deck.move_cards(hand, 5)
        hand.sort()
        hand.classify()
        categories[hand.label] = categories.get(hand.label, 0 ) + 1

    for categorie, freq in categories.iteritems():
        print categorie, 100.0 * freq / 100000.0, '%'


def print_attributes(obj):
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)


if __name__ == '__main__':
    main()
