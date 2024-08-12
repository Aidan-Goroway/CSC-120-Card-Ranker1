"""
The poker_hand module. Contains methods of the PokerHand class, related to a poker hand (typically 5 cards).
"""

from deck import *
MAX_CARDS_IN_HAND = 5


class PokerHand:
    """
    A class based around a hand for Poker. Poker uses hands of 5 cards, from a deck of 52 cards.
    There are 13 differently ranked cards for each of the 4 suits.
    """

    def __init__(self, list_of_cards):
        """
        Creates a hand of cards, suing the parameter list_of_cards.
        :param: list_of_cards: A list of cards used to create a hand.
        """

        self.__hand = list_of_cards.copy()

    def add_card(self, card_object):
        """
        Appends a card to a hand.
        :param: card_object: The card that will be appended to a hand.
        """
        self.__hand.append(card_object)

    def get_ith_card(self, index):
        """
        A method to grab a card from a list, chosen by its index.
        :param index: The index/card of a list/hand.
        :return: Returns an index of the list "__hand", or None if the index is invalid.
        """
        if (index < 0) or (index > MAX_CARDS_IN_HAND):
            return None
        else:
            return self.__hand[index]

    def __str__(self):
        """
        Represents the hand as 5 easily readable cards.
        :return: Returns a variable 'to_return' that is continuously updated
        with a new easily understandable card throughout the for loop.
        Starts with header 'HAND CONTENTS' and goes through a loop of the hand.
        When the end of the loop is reached, the resulting print is the header
        above every card from the hand, each placed neatly on a line.
        """
        to_return = "HAND CONTENTS:\n"
        for index in range(0, MAX_CARDS_IN_HAND):
            card = self.get_ith_card(index)
            to_return += str(card) + "\n"
        return to_return

    def list_hands_ranks(self):
        """
        Takes obfuscated card data and turns it into the easily understandable ranks of a 5-card hand.
        :return: An easily readable list of 5 cards' ranks.
        """
        rank_list = []
        for i in range(0,MAX_CARDS_IN_HAND):
            card_index = self.get_ith_card(i)
            card = card_index.find_rank()

            rank_list.append(card)
        return rank_list

    def determine_flush(self):
        """
        A function that categorizes a card hand as a flush.
        :return: Returns True if the hand is a flush, False otherwise.
        """

        card = self.get_ith_card(0)
        card_suit = card.find_suit()

        for index in range(0, MAX_CARDS_IN_HAND):
            if card_suit != self.get_ith_card(index).find_suit():
                return False
        return True

    def rank_of_flush(self):
        """
        This function will only go off when comparing flushes.
        :return: Returns the highest rank of a flush, to be compared against
        another flush.
        """

        flush = self.__hand
        for rank in reversed(STRING_RANKS):
            for card in flush:
                cards_rank = card.find_rank()#
                if cards_rank == rank:
                    return rank


    def determine_pair(self):
        """
        A function that categorizes the card hand as a pair.
        :return: Returns True if the hand is a pair, False otherwise.
        """

        for i in range(0, (MAX_CARDS_IN_HAND - 1)):
            for j in range(i+1,MAX_CARDS_IN_HAND):
                if self.list_hands_ranks()[i] == self.list_hands_ranks()[j]:
                    return True
        return False

    def rank_of_pair(self):
        """
        This function will only go off when comparing pairs.
        :return: Returns the highest rank of a pair, to be compared against
        another pair, or None, in case of an unpredictable bug.
        """
        for i in range(0,(MAX_CARDS_IN_HAND - 1)):
            for j in range(i+1,MAX_CARDS_IN_HAND):
                if self.list_hands_ranks()[i] == self.list_hands_ranks()[j]:
                    rank = self.list_hands_ranks()[i]
                    return rank
        return None

    def break_tie_pair(self):
        """
        This function will only go off when comparing tied pairs.
        :return: Returns the highest "chaser rank" of a pair, to be compared against
        another pair's chaser. Currently Unfinished.
        """
        pass

    def determine_two_pair(self):
        """
        A function that categorizes the card hand as a two_pair.
        :param: hand: A hand of 5 random cards.
        :return: Returns True if the hand is a two_pair, False otherwise.
        """

        matching_card_1 = 0
        matching_card_2 = 0
        x = False
        hand = self.list_hands_ranks()

        for i in range(0, MAX_CARDS_IN_HAND - 1):
            for j in range((i + 1), MAX_CARDS_IN_HAND):
                if self.list_hands_ranks()[i] == self.list_hands_ranks()[j]:
                    matching_card_1 = hand[i]
                    matching_card_2 = hand[j]
                    x = True
        if x:
            hand.remove(matching_card_1)
            hand.remove(matching_card_2)
        else:
            return False

        for i in range(0, 2):
            for j in range((i + 1), 3):
                if hand[i] == hand[j]:
                    hand.append(matching_card_1)
                    hand.append(matching_card_2)
                    return True
        hand.append(matching_card_1)
        hand.append(matching_card_2)
        return False

    def rank_of_two_pair(self):
        """
        This function will only go off when comparing two_pairs.
        :return: Returns the highest rank of a two_pair, to be compared against
        another two_pair.
        """
        matching_card_1 = 0
        matching_card_2 = 0
        rank_1 = None
        rank_2 = None
        two_pair_hand = self.list_hands_ranks()

        for i in range(0, MAX_CARDS_IN_HAND - 1):
            for j in range((i + 1), MAX_CARDS_IN_HAND):
                if self.list_hands_ranks()[i] == self.list_hands_ranks()[j]:
                    matching_card_1 = two_pair_hand[i]
                    matching_card_2 = two_pair_hand[j]
                    rank_1 = matching_card_1

        two_pair_hand.remove(matching_card_1)
        two_pair_hand.remove(matching_card_2)

        for i in range(0, 2):
            for j in range((i + 1), 3):
                if two_pair_hand[i] == two_pair_hand[j]:
                    rank_2 = two_pair_hand[i]

        if rank_1 > rank_2:
            return rank_1
        elif rank_1 < rank_2:
            return rank_2
        else:
            return rank_1 # in cases of 4_of_a_kind scenarios

    def determine_high_card(self):
        """
        A function that categorizes the card hand as a high_card. This funtion
        will always return True if run.
        :return: Returns True if the hand is a high_card. The return value will
        always be True, because every hand that is not a flush,pair, or two_pair
        must be a high_card.
        """
        return True

    def rank_of_high_card(self):
        """
        Only to be used when ranking high_cards.
        :return: Returns the rank of the high card.
        """

        hand = self.__hand

        for rank in reversed(STRING_RANKS):
            for card in hand:
                cards_rank = card.find_rank()
                if cards_rank == rank:
                    return rank

    def determine_hand(self):
        """
        A method to determine what type a hand is.
        :return: returns a string representing what the hand is.
        """
        if self.determine_flush():
            return 'flush'
        elif self.determine_two_pair():
            return 'two_pair'
        elif self.determine_pair():
            return 'pair'
        else:
            self.determine_high_card()
            return 'high_card'


    def compare_to(self, other_hand):
        """
        Determines which of two poker hands is worth more. Returns an int
        which is either positive, negative, or zero depending on the comparison.
        :param: self: The first hand to compare
        :param: other_hand: The second hand to compare
        :return: a negative number if self is worth LESS than other_hand,
        zero if they are worth the SAME (a tie), and a positive number if
        self is worth MORE than other_hand
        """

        # This definitely needs a fix

        if self.__hand > other_hand:
            return 1
        elif self.__hand < other_hand:
            return -1
        else:
            return 0

# debug_list_1 = []
#
# c1 = Card(2,'S')
# c2 = Card(11,'C')
# c3 = Card(3,'H')
# c4 = Card(3,'C')
# c5 = Card(11,'H')
# debug_list_1.append(c1)
# debug_list_1.append(c2)
# debug_list_1.append(c3)
# debug_list_1.append(c4)
# debug_list_1.append(c5)
#
# debug_list_2 = []
#
# d1 = Card(2,'D')
# d2 = Card(11,'H')
# d3 = Card(3,'S')
# d4 = Card(3,'S')
# d5 = Card(11,'C')
# debug_list_2.append(c1)
# debug_list_2.append(c2)
# debug_list_2.append(c3)
# debug_list_2.append(c4)
# debug_list_2.append(c5)

# h = PokerHand(debug_list)
# print(PokerHand.list_hands_ranks(h))

#m = PokerHand(debug_list_1)
#print(PokerHand.determine_two_pair(m))

#print(PokerHand.rank_of_two_pair(m))
#print(PokerHand.determine_two_pair(m))