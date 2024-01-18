# compare_game.py

from card import CardDeck


class CompareGame:

    def __init__(self):

        self.player_count = 2                                       # Sets the player count to two, so you can have more players if you want and the amount of players isn't hard-coded.
        self.player_hands = [[] for _ in range(self.player_count)]  # Makes two empty lists, which will later have the player's hand added to it.
        self.round_winner = None                                    # Keeps track of the current round winner, currently set to none as there is no active round.
        self.round_number = 0                                       # Keeps track of what round it is, starting at 0.
        self.deck = None                                            # Brings the deck in, but is currently an empty deck.
        self.rounds_won = [0] * self.player_count                   # A list to keep track of how many rounds each player has won

    def start_game(self, num_cards):
        """
        This is the first function that will be called. It starts the game by making, shuffling, and dealing the deck.
        :param num_cards: this parameter represent the number of cards that each player will receive.
        :return:N/A
        """
        self.deck = CardDeck()                                      # This line creates a new deck.
        self.deck.shuffle_deck()                                    # This line shuffles said deck.

        print("Dealer deals", num_cards, "cards to each player...")
        cards = self.deck.deal_cards(num_cards * self.player_count) # Calculates the total number of cards needed for both players
        for i in range(self.player_count):
            self.player_hands[i] = cards[i::self.player_count]      # This and the previous line were a suggestion from ChatGPT, as I couldn't figure out how to equally deal the cards to each player.
                                                                    # It essentially takes every other card from the deck and assigns it to each player, to simulate a fair deal and make sure everyone gets different cards and the same amount.
        self.show_player_hands()                                    # Prints the hand of each player

    def show_player_hands(self):
        """
        This function shows the player's hands. It comes entirely from ChatGPT, as I forgot how to print a list without the weird commas and stuff.
        :return: N/A
        """
        for i, hand in enumerate(self.player_hands, start=1):                                   # As previously mentioned, these lines come from ChatGpt. The enumerate function is used to iterate over each player's hand (self.player_hands). It returns pairs of the form (index, hand), where index is the position of the hand in self.player_hands. The start=1 argument specifies that indexing should start from 1 instead of the default 0.
            print(f"Player {i} Hand:", ", ".join(f"{value} {suit}" for value, suit in hand))    # Joins the values and suits of each card in the player's hand into a comma-separated string. The generator expression (f"{value} {suit}" for value, suit in hand) creates a string for each card, and ", ".join(...) concatenates these strings with commas in between.

    def play_round(self):
        """
        Plays through a round, adding a tally to the round total, Printing each user's card, finding the winner, and printing the winner.
        :return: N/A
        """
        self.round_number += 1                                                              # Adds a tally to the amount of rounds
        print("Round", self.round_number, ":")                                              # Prints which round it is

        for i in range(self.player_count):
            print("Player", i + 1, ":", self.player_hands[i][self.round_number - 1][0],     # Accesses the value of the card that the player has in their hand for the current round. subtracts one from the round number because of indexing
                  self.player_hands[i][self.round_number - 1][1])                           # Accesses the suit of the card that the player has in their hand for the current round.

        self.determine_round_winner()                                                       # Finds the winner of the round
        self.rounds_won[self.round_winner] += 1                                             # Adds a tally to the amount of rounds the winner has won.
        print("Player", self.round_winner + 1, "wins this round!")                          # Prints the winner

    def determine_round_winner(self):
        """
        compares the cards to find the winner of the round.
        :return: N/A
        """
        round_values = [hand[self.round_number - 1][0] for hand in self.player_hands]       # Creates a list containing the values of the cards that each player has played in the current round.
        max_value = max(round_values)                                                       # Finds the highest value in the list, using the command max. I googled how to find this. https://realpython.com/python-min-and-max/#:~:text=Use%20Python%27s%20min()%20and,()%20with%20strings%20and%20dictionaries
        self.round_winner = round_values.index(max_value)                                   # Sets self.round_winner to the index of the player whose card has the maximum value in the current round. I couldn't figure out how to give the suits a value, so if there are multiple players with the same maximum value, it chooses the first occurrence.

    def get_winner(self):
        """
        Finds the overall winner, based on who won the most rounds.
        :return: returns the winner and how many rounds they won.
        """
        max_rounds = max(self.rounds_won)                       # Finds the max rounds won by a single player, again using the max method found at https://realpython.com/python-min-and-max/#:~:text=Use%20Python%27s%20min()%20and,()%20with%20strings%20and%20dictionaries

        if self.rounds_won.count(max_rounds) == 1:              # Checks if there is only one person with the most wins
            winner = self.rounds_won.index(max_rounds) + 1      # If there is only one, that player's number is assigned to winner.
            return [winner], max_rounds                         # Returns the winner and how many rounds they won
        else:
            return [], max_rounds                               # If there are multiple winners, a blank value is returned with how many rounds were won.

