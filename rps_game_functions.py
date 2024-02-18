# This file defines functions to be used in program for game of Rock-Paper-Scissors
def greet_user():
    print('\n', '*' * 10, "WELCOME to Rock-paper-scissors: User vs Computer", '*' * 10, '\n', '_' * 70)
    user_name = input("\nPlease enter your name here: ")
    print(f"Hello {user_name}, get ready to play!")
    with open("results_register.txt", "a") as file:
        file.write(f"\n{user_name} vs Computer:")
    return user_name

# user defined method to apply rule and find out who wins
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
    if rule_key in ['pr', 'rs', 'sp']:
        print("User wins!")
        victory_user += 1
        # otherwise the result key is among remaining three keys, again inform user and
        # increment computer victory variable victory_comp
    else:
        print("Computer wins!")
        victory_comp += 1
        # return the new count of user and computer wins
    return victory_user, victory_comp


def display_result(u_wins, c_wins, u_name):
    user_name = u_name
    myfile = open("results_register.txt", "a")
    # checks condition id user wins in three games are more than computer wins and prints results accordingly
    if u_wins > c_wins:
        print(f"\nGAME OVER\n*****Best of 3 winner: {user_name}, you won most ({u_wins}) games. Congrats!*****")
        myfile.write(f"\nBest of 3 winner: {user_name}, won {u_wins} games")
    else:
        print(f"\nGAME OVER\n*****Best of 3 winner: Computer won most ({c_wins}) games. Better luck next time!*****")
        myfile.write(f"\nBest of 3 winner: Computer, won {c_wins} games")
    myfile.close()


# using the main trick to test functions
if __name__ == '__main__':
    name = greet_user()
    v_user, v_comp = judge_winner('rs')
    display_result(v_user, v_comp, name)

