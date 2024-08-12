"""
This Module contains the main function, which plays a game. You are given two different card hands and asked to rank
them. If you do so successfully, you earn a point. If you fail once, you receive a game over. You win the game if
you can correctly rank each card until there are not enough cards in the deck to draw another hand.
Due to a shortage of time and knowledge, and the frank reality that I don't know what I am doing,
the main() function is very obviously incomplete.
"""
"""
Help received from CS Help Desk, Loudi (from class), and Eric Zhao.
"""
"""
I affirm that I have carried out the attached academic endeavors with full academic honesty, in
accordance with the Union College Honor Code and the course syllabus.
"""

from poker_hand import *

def main():
    """
    The main function that plays the game. See module doc_string above.
    Many of the lines here would have been replaced with functions, given more time.
    """

    deck = Deck()
    deck.shuffle()

    list_1 = []
    list_2 = []
    for card in range(0,MAX_CARDS_IN_HAND):
        list_1.append(deck.deal_one())
        list_2.append(deck.deal_one())


    if deck.remaining_cards_in_deck() > MAX_CARDS_IN_HAND:

        # present player with 2 hands
        hand_1 = PokerHand(list_1)
        hand_2 = PokerHand(list_2)
        hand_type_1 = 0
        hand_type_2 = 0
        points = 0
        print(hand_1.__str__())
        print(hand_2.__str__())

        # GUTS GO HERE \/\/\/

        if hand_1.determine_hand() == 'flush':
            hand_type_1 = 'flush'
            hand_1 = hand_1.rank_of_flush()
        elif hand_1.determine_hand() == 'two_pair':
            hand_type_1 = 'two_pair'
            hand_1 = hand_1.rank_of_two_pair()
        elif hand_1.determine_hand() == 'pair':
            hand_type_1 = 'pair'
            hand_1 = hand_1.rank_of_pair()
        else: # high_card
            hand_1.determine_high_card()
            hand_type_1 = 'high_card'
            hand_1 = hand_1.rank_of_high_card()

        if hand_2.determine_hand() == 'flush':
            hand_type_2 = 'flush'
            hand_2 = hand_2.rank_of_flush()
        elif hand_2.determine_hand() == 'two_pair':
            hand_type_2 = 'two_pair'
            hand_2 = hand_2.rank_of_two_pair()
        elif hand_2.determine_hand() == 'pair':
            hand_type_2 = 'pair'
            hand_2 = hand_2.rank_of_pair()
        else: # high_card
            hand_2.determine_high_card()
            hand_type_2 = 'high_card'
            hand_2 = hand_2.rank_of_high_card()

        if hand_type_1 == hand_type_2: #both hands are flushes or pairs or ect.

            if hand_1 == 'jack':
                hand_1 = str(11)
            if hand_1 == 'queen':
                hand_1 = str(12)
            if hand_1 == 'king':
                hand_1 = str(13)
            if hand_1 == 'ace':
                hand_1 = str(14)

            if hand_2 == 'jack':
                hand_2 = str(11)
            if hand_2 == 'queen':
                hand_2 = str(12)
            if hand_2 == 'king':
                hand_2 = str(13)
            if hand_1 == 'ace':
                hand_2 = str(14)

            if hand_1 > hand_2:
                answer = hand_1
            elif hand_1 < hand_2:
                answer = hand_2
            else:
                pass

        else: pass


        print(hand_1)
        print(hand_2)
        # GUTS GO HERE /\/\/\

        # have input to see if guess matches answer
        guess = input("Which hand has a greater value? Answer 1 or 2\n")
        if guess == 2:
            guess = -1


        # if they match, add a point
        if (hand_1.compare_to(hand_2) == 1 and guess == 1) or (hand_1.compare_to(hand_2) == -1 and guess == -1):
            points += 1
        else:
            print(f'Game over, you scored {points} points.')
            return None


        # if its not a match, end the game

        # game ends when loop closes (too little cards)

        pass #PASS for debugging
    else:
        print('Game over! There are not enough cards in the deck to play another round')



main()
