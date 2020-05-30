"""
File: nimm.py
-------------------------
Nimm is an ancient game of strategy that where Players alternate
taking stones until there are zero left.

The game of Nimm goes as follows:
1. The game starts with a pile of 20 stones between the players
2. The two players alternate turns
3. On a given turn, a player may take either 1 or 2 stone from the center pile
4. The two players continue until the center pile has run out of stones.
The last player to take a stone loses.
"""
TOTAL_STONES = 20
NUM_PLAYERS = 2

def main():
    game_of_nimm()


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
    num_of_stones = TOTAL_STONES
    player_turn = 1
    print("There are " + str(num_of_stones) + " stones left")
    while num_of_stones > 0:
        user_input = int(input("Player " + str(player_turn) + " would you like to remove 1 or 2 stones? "))
        while input_is_invalid(user_input, num_of_stones):
            user_input = int(input("Please enter 1 or 2: "))

        num_of_stones -= user_input
        player_turn = (player_turn % NUM_PLAYERS) + 1
        if num_of_stones !=0:
            print("\nThere are " + str(num_of_stones) + " stones left")
    print("\nPlayer " + str(player_turn) + " wins!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
