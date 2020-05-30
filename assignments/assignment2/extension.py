"""
File: extension.py : Extension of Game of Nimm - 'AI version'
------------------
A simple version of computer player that can always wins in a game of Nimm!
"""

TOTAL_STONES = 20
NUM_PLAYERS = 2


def main():
    game_of_nimm_ai()


def input_is_invalid(user_input, num_of_stones):
    if (num_of_stones == 1) and (user_input == 2):
        print("Not enough stones to remove!")
        return True
    elif (user_input == 1) or (user_input == 2):
        return False
    else:
        return True


def game_of_nimm():
    print("Welcome to the game of Nimm!")

    player_1 = input("Player 1's name (Press Enter to skip): ")
    player_2 = input("Player 2's name (Press Enter to skip): ")
    if player_1 == "":
        player_1 = "Player 1"
    if player_2 == "":
        player_2 = "Player 2"

    num_of_stones = TOTAL_STONES
    player_turn = 1
    print("There are " + str(num_of_stones) + " stones left")

    while num_of_stones > 0:
        if player_turn == 1:
            user_input = int(input(player_1 + " would you like to remove 1 or 2 stones? "))
        elif player_turn == 2:
            user_input = int(input(player_2 + " would you like to remove 1 or 2 stones? "))

        while input_is_invalid(user_input, num_of_stones):
            user_input = int(input("Please enter 1 or 2: "))

        num_of_stones -= user_input
        player_turn = (player_turn % NUM_PLAYERS) + 1
        if num_of_stones != 0:
            print("\nThere are " + str(num_of_stones) + " stones left")

    print("\nPlayer " + str(player_turn) + " wins!")


def game_of_nimm_ai():
    print("Welcome to the game of Nimm!\nPlay with the Computer!")

    player_1 = input("Enter your name (Press Enter to skip): ")
    player_2 = "Computer"
    if player_1 == "":
        player_1 = "Player 1"

    num_of_stones = TOTAL_STONES
    print("There are " + str(num_of_stones) + " stones left\n")

    num_of_stones -= 1
    print(player_2 + " starts the game\n" + player_2 + " picked 1 stone")
    print("There are " + str(num_of_stones) + " stones left\n")
    player_turn = 1

    while num_of_stones > 0:
        if player_turn == 1:
            user_input = int(input(player_1 + " would you like to remove 1 or 2 stones? "))

            while input_is_invalid(user_input, num_of_stones):
                user_input = int(input("Please enter 1 or 2: "))

            num_of_stones -= user_input

        elif player_turn == 2:
            num_of_stones -= (user_input % 2) + 1
            print(player_2 + " picked " + str((user_input % 2) + 1) + " stone(s)")

        player_turn = (player_turn % NUM_PLAYERS) + 1
        if num_of_stones != 0:
            print("\nThere are " + str(num_of_stones) + " stones left")

    if player_turn == 1:
        print("\n" + player_1 + " wins!")
    elif player_turn == 2:
        print("\n" + player_2 + " wins!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
