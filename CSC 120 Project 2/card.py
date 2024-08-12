"""
The Card module. Contains methods of the Card class related to individual cards.
"""


class Card:
    """
    Creates a card object.
    """

    def __init__(self, rank, suit):
        """
        Creates a card.
        Card is dictionary format, with key and value for rank and suit.
        :param rank: The rank of the card. Can be 2-14.
        :param suit: The suit of the card. Can be S, H, D, or C.
        """
        self.__card = {'rank': rank, 'suit': suit}

    def find_suit(self):
        """
        Returns a string of the suit. (clubs instead of 'C'.)
        :return: One of the four suits, in lowercase specifically.
        """

        value = self.__card['suit']

        if value == 'S':
            return 'spades'
        if value == 'H':
            return 'hearts'
        if value == 'D':
            return 'diamonds'
        if value == 'C':
            return 'clubs'

    def find_rank(self):
        """
        Returns the cards rank, as a str, depending on rank.
        :return: The rank of the card. 11-14 are the jack, queen, king, and ace.
        """
        value = self.__card['rank']

        if value >= 2 and value <= 10:
            return str(value)
        elif value == 11:
            return 'jack'
        elif value == 12:
            return 'queen'
        elif value == 13:
            return 'king'
        elif value == 14:
            return 'ace'

    def __str__(self):
        """
        Returns a plainly stated card, in the form "The (rank) of (suit)"
        :return: The card, in plain english. Specifically a string.
        """

        return str(f'The {self.find_rank()} of {self.find_suit()}')
