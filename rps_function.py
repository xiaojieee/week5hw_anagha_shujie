import random
# import random for the computer to generate a random number


def computer_choice():
    computer_choice_num = random.randint(0, 2)
    if computer_choice_num == 0:
        return 'Rock'
    elif computer_choice_num == 1:
        return 'Paper'
    elif computer_choice_num == 2:
        return 'Scissors'
# define a computer function to randomly generate number between 0 and 2
# assign the numbers to rock, paper and scissors respectively


def player_choice():
    while True:
        player_choice_input = input("Enter R, P, S:").upper()
        if player_choice_input in ['R', 'P', 'S']:
            if player_choice_input == 'R':
                return 'Rock'
            elif player_choice_input == 'P':
                return 'Paper'
            elif player_choice_input == 'S':
                return 'Scissors'
        else:
            print("Oh no! Not a valid option! Please enter 'R', 'P', 'S' to play!")
# define a player function to play rock paper scissors
# .upper will make the player's choice uppercase even if they enter lowercase
# assign the shorthand to return a full-hand answer
# if player enters anything outside the programmed choices it will prompt them to enter again


def winner(computer, player):
    if computer == player:
        return "It's a tie!"
    elif (computer == 'Rock' and player == 'Scissors') or \
            (computer == 'Paper' and player == 'Rock') or \
            (computer == 'Scissors' and player == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"
# define a winner function to determine who won the game
# there's 2 parameters here, one is the computer and one is the player
# if computer is the same as player, it's a tie
# else if list out the rules to win against computer
# anything 'else' means the computer has won


def playing():
    print("Let's play a game of Rock, Paper, Scissors!")
    while True:
        computer = computer_choice()
        player_choice_input = player_choice()
        print(f"The computer chose {computer}, you chose {player_choice_input}.")
        print(winner(computer, player_choice_input))

        while True:
            play_again = input("Do you want to play again? (Enter y to continue):").lower()
            if play_again == 'y' or play_again == 'n':
                break
            else:
                print("Oh no! Not a valid option! Please enter y or n to continue!")
        if play_again != 'y':
            print("End of game!")
            break
# define a playing function to combine the other functions to create the game
# first prompt the player to enter their choice
# then it will read out a line of what the computer and the player chose
# which then prompts the winner function to declare the winner






if __name__ == "__main__":
    # test the function
    playing()

