# main.py

from testing_card import CompareGame


def get_cards_per_player():
    """
    asks the user how many cards and therefore rounds there should be.
    :return: returns the amount of cards to deal each player, which will also determine the amount of rounds.
    """
    while True:                                                                                                     # Creates a loop that doesn't end until a valid input is received.
        try:
            num_cards = int(input("How many cards should each player get? Enter a number between 1 and 26: "))
            if 1 <= num_cards <= 26:                                                                               # Tests to make sure the user enters a number between 1 and 26, as that is how many rounds can be played (assuming there are 2 players.)
                return num_cards
            else:
                print("Please enter a number between 1 and 26.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 26.")


def main():
    print("Welcome to the game of Compare. You will decide how many cards we get, and then we'll play them one by one.")
    print("Whoever has the higher card wins that round. Whoever wins the most rounds wins the game.")

    num_cards = get_cards_per_player()

    game = CompareGame()
    game.start_game(num_cards)                      # This will pass the user entered integer to the function in the testing_cards file.

    while game.round_number < num_cards:            # Keeps playing rounds until there has been a round played for every card.
        game.play_round()

    print("Game Over!")

    winners, max_rounds = game.get_winner()         # Retrieves the list of winners and how many rounds they won from testing_card
                                                                                         # I saw ChatGPT use enumerate earlier, so I googled it to see how it works. https://www.simplilearn.com/tutorials/python-tutorial/enumerate-in-python
    for i, rounds in enumerate(game.rounds_won, start=1):                                # The enumerate function is used to iterate over game.rounds_won, and start=1 indicates that the index should start from 1.
        print("Player", i, "wins", rounds, "rounds.")                                    # Prints how many rounds each player won.
    value = len(winners)                                                                 # Chose a random name to assign the length of the list of winners, so it can be tested.
    if value == 1:                                                                       # Tests if there is only one winner.
        print("Player", *winners, "wins the game with:", max_rounds, "round(s).")        # The asterisk is so that when the winner is printed, there are no brackets. https://www.javatpoint.com/how-to-print-a-list-without-brackets-in-python
    else:
        print("It's a tie!")                                                             # Halfway into coding this I realized if you change the amount of players so there are more than 2 this whole thing breaks, but I don't have time to fix it.


if __name__ == "__main__":
    main()
