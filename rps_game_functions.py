# Week 5 homework Ex 14.
# This file defines functions to be used in program for game of Rock-Paper-Scissors

# 1. Following function asks for name of the user-player and greets them, also makes an entry in register with a
# timestamp that is provided as the argument by main program
def greet_user(date_time):
    print(f"{'~'*70}\n{'*' * 10} WELCOME to Rock-paper-scissors: User vs Computer {'*' * 10}\n{'~' * 70}")
    user_name = input("\nPlease enter your name here: ")
    print(f"Hello {user_name}, get ready to play!")
    # open file in append mode and write username as well as time and date of game being played in the file
    with open("results_register.txt", "a") as file:
        file.write(f"\n{user_name} vs Computer: {date_time}")
    # Return the name of the user-player to main program
    return user_name


# 2. user defined function to apply relevant rule and find out who wins
def judge_winner(rule_key):
    # Rules dictionary to lookup for deciding results
    rules_dict = {
        'pr': 'Paper covers rock',
        'rs': 'Rock crushes scissors',
        'sp': 'Scissors cut paper',
        'rp': 'Paper covers rock',
        'sr': 'Rock crushes scissors',
        'ps': 'Scissors cut paper'
    }
    # variables to track wins of user and computer are initialised as 0.
    victory_user = 0
    victory_comp = 0
    # prints the value corresponding to the key received in the rules dictionary rules_dict
    print(rules_dict[rule_key])
    # if result key is one of the three dictionary keys corresponding to users win,
    # inform user and increment user victory variable victory_user
    if rule_key in ['rp', 'rs', 'sp']:
        print("User wins!")
        victory_user += 1
        # otherwise the result key is among remaining three keys, again inform user and
        # increment computer victory variable victory_comp
    else:
        print("Computer wins!")
        victory_comp += 1
        # return the new count of user and computer wins
    return victory_user, victory_comp


# 3. Function takes user-name and counts of computer and user victories in series of games as arguments and
# displays result on screen as well as makes entry in file
def display_result(u_wins, c_wins, u_name):
    user_name = u_name
    # opens file in append mode to avoid overwriting previous content
    myfile = open("results_register.txt", "a")
    # checks condition id user wins in three games are more than computer wins and prints results accordingly
    if u_wins > c_wins:
        print(f"\nGAME OVER\n*****!Best of 3 winner: {user_name}, you won most ({u_wins}) games. Congrats!*****")
        myfile.write(f"\nBest of 3 winner: {user_name}, won {u_wins} games")
    else:
        print(f"\nGAME OVER\n*****!Best of 3 winner: Computer won most ({c_wins}) games. Better luck next time!*****")
        myfile.write(f"\nBest of 3 winner: Computer, won {c_wins} games")
    # close the file results_register.txt
    myfile.close()


# 4. Following function reads history from file and calculates the percentage of games computer and user have won
def win_percentage():
    with open("results_register.txt", 'r') as file:
        lines = file.read()
        # counts the number of times string 'computer,' appears in results register that is the no. of times it has won
        comp_wins = lines.count('Computer,')
        file.seek(0)
        # There are two lines added per game hence total entries are actually half the number of lines
        total_entries = len(file.readlines())//2
        # Calculate percentage wins for computer and user
        comp_win_percent = (comp_wins/total_entries)*100
        user_win_percent = 100 - comp_win_percent
        # print it out on screen
        print(f"\n{'%'*100}\nTRIVIA: So far, Users have won {user_win_percent:.2f} % of the games while computer has "
              f"won {comp_win_percent:.2f} % of the games!\n{'%'*100}")


# using the main trick to test functions
# if __name__ == '__main__':
#     name = greet_user('2024:02:18')
#     v_user, v_comp = judge_winner('rs')
#     display_result(v_user, v_comp, name)
#     win_percentage()
