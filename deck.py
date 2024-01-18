# card_deck.py

import random

class CardDeck:
    def __init__(self):
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.deck = self.create_deck()

    def create_deck(self):
        return [(value, suit) for value in self.values for suit in self.suits]

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_cards(self, num_cards):
        return self.deck[:num_cards]

# For testing the card deck
if __name__ == "__main__":
    deck = CardDeck()
    deck.shuffle_deck()
    print(deck.deal_cards(5))


