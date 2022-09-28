# Rock, Paper, Scissors Game
import random
# Define a function that initiates play

def play():
    player_choice = input("Please choose Rock 'R', Paper 'P' or Scissors 'S': ")
    computer_choice = random.choice(["R", "P", "S"])

    if player_choice == computer_choice:
        print("It's a tie! Play Again...")




play()
