# Program code to play the game of Rock-paper-scissors: user vs computer

# import module for randint function
import random
import rps_game_functions

# Main code
# invoke function greet_user from rps_game_functions module, returned value is stored in user variable
user = rps_game_functions.greet_user()

# lists that store the user and computer points i.e. number of wins from results of three games
user_win = [0, 0, 0]
comp_win = [0, 0, 0]

# tuple defining user choices
user_choices = ('r', 'p', 's')
# dictionary that maps computer's random integer input to corresponding character
comp_val_dict = {0: 'r', 1: 'p', 2: 's'}

# For loop takes inputs thrice to find out best of three
for game in range(0, 3):
    # input values of user and computer are both initialized as ''
    user_val = ''
    comp_val = ''
    got_unique_inputs = False

    # while loop runs following block of code until we obtain unique choices for user and computer
    while not got_unique_inputs:
        # asks for user input
        user_val = input("\nEnter your choice (r/p/s): ")
        # converts to lower case to avoid user value in uppercase
        user_val = user_val.lower()
        # validates the input using user_choices tuple
        if user_val not in user_choices:
            print("Please enter one of r/p/s only.")
            # skip next code and continue to loop condition for next iteration
            continue
        # Computer generates a random integer from 0 to 2 both inclusive
        rand_int = random.randint(0, 2)
        # rand_int is used as key to get corresponding computer input value from dictionary
        comp_val = comp_val_dict.get(rand_int)
        print("Computer's choice:", comp_val)
        # If user choice and computer choice are the same then skip following code and continue to next iteration
        if user_val == comp_val:
            print(f"Draw! No result because of same choices: {user_val} and {comp_val}")
            continue
        # if user choice and computer choice are different then boolean got_unique_inputs is set to True which fails
        # the next while loop iteration and goes out to for loop to execute remaining code in current iteration before
        # the start of next for loop to play another game in a series of 3 games
        else:
            got_unique_inputs = True
    # End of while loop

    # Checking the result is the next part in for loop after while loop ends. It concatenates user and computer values
    # to generate a result key which is passed as argument in judge(result_key) function call
    result_key = user_val + comp_val

    # the function returns two values that have count of user and computer wins respectively. They are
    # stored as list elements in user_win and comp_win lists pertaining to corresponding game
    user_win[game], comp_win[game] = rps_game_functions.judge_winner(result_key)
    # End of for loop.

# best of three decision is taken outside the for loop after three games with unique inputs have been played
# A sum of wins is calculated for both user and computer
user_win_total = sum(user_win)
comp_win_total = sum(comp_win)

# function call to display result of the games and registers a record in file
rps_game_functions.display_result(user_win_total, comp_win_total, user)
# End of program
