"""
The Deck module. Contains methods of the Deck class related to a deck of cards.
"""
import random

from card import *

SUITS = ['H', 'D', 'S', 'C']
RANKS = [
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
    ]
STRING_RANKS = [
    str(2), str(3), str(4), str(5), str(6), str(7), str(8),
    str(9), str(10), 'jack', 'queen', 'king', 'ace'
]


class Deck:
    """
    Models a deck of cards. Will hold no more than 52 elements.
    """

    def __init__(self):
        """
        Creates the deck.
        Specifically, a list of 52 dictionaries.
        """
        self.__deck = []
        for rank in RANKS:
            for suit in SUITS:
                self.__deck.append(Card(rank, suit))

    def shuffle(self):
        """
        Shuffles the deck in random order.
        """
        random.shuffle(self.__deck)

    def deal_one(self):
        """
        As long as there are cards remaining in the deck, a card is drawn.
        :return: card: If there is at least one card in the deck, this
        card is returned.
        :return: None: If the deck is empty, with no more cards remaining,
        returns keyword None.
        """
        if Deck.remaining_cards_in_deck(self) != 0:
            card = self.__deck[0]
            self.__deck.pop(0)
            return card
        else:
            return None

    def remaining_cards_in_deck(self):
        """
        Returns the amount of cards remaining in the deck.
        Used in Deck function deal_one.
        :return: A number representing the amount of cards in the deck.
        """
        return len(self.__deck)

    def __str__(self):
        """
        Prints the entire deck, line by line.
        :return: Returns a variable 'to_return' that is continuously updated
        with a new card from the deck throughout the for loop.
        Starts with header 'DECK CONTENTS' and goes through a loop of the deck.
        When the end of the loop is reached, the resulting print is the header
        above every card from the deck, each placed neatly on a line.
        """
        to_return = "DECK CONTENTS:\n"
        for index in range(0, self.remaining_cards_in_deck()):
            card = self.__deck[index]
            to_return += str(card) + "\n"
        return to_return

    def return_deck(self):
        """
        Passes down the deck for suture usage.
        :return: The deck, a list initiated with 52 cards.
        """
        return self.__deck
