# Rock, Paper, Scissors with the computer

import random

i = True
while i is True:
    def play():
        while True:
            rps = ['r', 'p', 's']
            user_choice = input("Choose 'r' for rock, 'p' for paper, or 's' for scissors: ").lower()
            com_choice = random.choice(rps)
            if user_choice not in 'rps' or len(user_choice) > 1:
                print("Error: Incorrect Input")
            elif user_choice == com_choice:
                print("Tie! Pick Again!")
            else:
                return com_choice, user_choice
    results = play()
    print(f"You chose {results[1]} and the computer chose {results[0]}.")

    def who_wins(results):
        if results[1] == 'r' and results[0] == 's':
            print("You win!")
        elif results[1] == 'r' and results[0] == 'p':
            print("You lose!")
        elif results[1] == 'p' and results[0] == 'r':
            print("You win!")
        elif results[1] == 'p' and results[0] == 's':
            print("You lose!")
        elif results[1] == 's' and results[0] == 'p':
            print("You win!")
        elif results[1] == 's' and results[0] == 'r':
            print("You lose!")

    who_wins(results)

    def play_again():
        play_again = input("Play again (y/n)? ").lower()
        if play_again not in "yn" or len(play_again) > 1:
            print("Error: Incorrect Input")
        elif play_again == 'y':
            return True
        else:
            print("Thanks for playing...")
            return False

    i = bool(play_again())




