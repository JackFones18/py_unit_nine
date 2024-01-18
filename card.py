# card.py

import random


class CardDeck:
    def __init__(self):
        self.suits = ["♣️", "♦️", "♥️", "♠️"]                                               # This defines the suits that can be used. They are organized from the least powerful suit to most powerful.
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]     # This defines the values that can be used. They are organized from the least powerful value to most powerful.
        self.deck = self.create_deck()

    def create_deck(self):
        """
        This function creates the deck, using a nested loop to make every possible combination of values and suit.
        :return: returns the list with every possible card.
        """
        return [
            (value, suit)                           # This nested loop will make a list with every card.
            for value in self.values                # This is a nested loop that iterates over each value
            for suit in self.suits                  # This is the second part of the nested loop that iterates over each suit.
        ]

    def shuffle_deck(self):                                                                 # These five lines are the fisher-yates shuffle method, given to me by ChatGPT

        n = len(self.deck)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]

    def deal_cards(self, num_cards):        # I wasn't exactly sure how to deal the cards; I kept getting error messages, so I asked ChatGPT for help.
        """
        Deals the cards to the players. Given by ChatGPT.
        :param num_cards:
        :return: returns the cards which have been dealt to each player.
        """
        return self.deck[:num_cards]        # self.deck refers to the deck of cards created earlier.
                                            # num_cards gives the top card from the deck.
                                            # These lines essentially simulate taking the top card off of the pile and dealing it to the player.
