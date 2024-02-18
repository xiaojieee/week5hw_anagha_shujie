import random
import time
# import random for the computer to generate a random number
# import time to delay the code from showing after each round, so it's not overwhelming for the player


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
        time.sleep(0.5)
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
# using the time.sleep function to delay the message showing up by 0.5 seconds
# this will also delay it each round
# .upper will make the player's choice uppercase even if they enter lowercase
# assign the shorthand to return a full-hand answer
# if player enters anything outside the programmed choices it will prompt them to enter again


def winner(computer, player):
    if computer == player:
        return "It's a tie this round!"
    elif (computer == 'Rock' and player == 'Scissors') or \
            (computer == 'Paper' and player == 'Rock') or \
            (computer == 'Scissors' and player == 'Paper'):
        return "Computer win this round!"
    else:
        return "You win this round!"
# define a winner function to determine who won the game
# there's 2 parameters here, one is the computer and one is the player
# if computer is the same as player, it's a tie
# else if list out the rules to win against computer
# anything 'else' means the computer has won


def play_game():
    random.seed()
    print("Let's play a game of Rock, Paper, Scissors!\nRules: Best of 3 win")
    while True:
        computer_score = 0
        player_score = 0
        for _ in range(3):
            computer = computer_choice()
            player_choice_input = player_choice()
            print(f"The computer chose {computer}, you chose {player_choice_input}.")
            time.sleep(1)
            results = winner(computer, player_choice_input)
            print(results)

            if results == "You win this round!":
                player_score += 1
            elif results == "Computer win this round!":
                computer_score += 1
            print(f"Computer's score: {computer_score}. Your score {player_score}.")

        if player_score > computer_score:
            print("Congratulations! You win!")
        elif player_score < computer_score:
            print("Sorry! The computer win!")
        else:
            print("It's a tie! No one win!")

        while True:
            time.sleep(2)
            play_again = input("Do you want to play again? (Enter 'y' to continue, or 'n' to exit):").lower()
            if play_again == 'y' or play_again == 'n':
                break
            else:
                print("Oh no! Not a valid option! Please enter 'y' or 'n' to continue!")
        if play_again != 'y':
            print("End of game, thank you for playing!")
            break
# define a play game function to combine the other functions to create the game
# the random module generates pseudo-random numbers, using the .seed() method will set a different seed each time
# the .seed() will generate numbers with an equal distribution
# first prompt the player to enter their choice
# initialise both scores to zero first to be able to keep track of the scores
# then it will read out a line of what the computer and the player chose
# which then prompts the winner function to declare the winner of the round
# after the game have gone through 3 rounds it will print a new message declaring the game winner
# using the .sleep method again to wait to prompt the player if they want to play the game again
# depending on their choice either play again, which loops through the code again
# if they chose to not play, it will end the code


if __name__ == "__main__":
    # test the function
    print(computer_choice())
    print(player_choice())
    play_game()

