#First way to Do
import random
from types import WrapperDescriptorType

def get_choices():
    options = ["rock", "paper", "scissors"]

    player_choice = input("Enter a choice (rock, paper, scissors): ").lower()

    while player_choice not in options:
        print("Invalid choice! Please choose only from rock, paper, or scissors.")
        player_choice = input("Enter again (rock, paper, scissors): ").lower()

    computer_choice = random.choice(options)

    return {"player": player_choice, "computer_choice": computer_choice}

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer_choice"])
print(result)

#Second with more Easy way
#import random

#def play():
    #user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    #computer = random.choice(['r', 'p', 's'])

    #if user == computer:
        ##return 'It\'s a tie'

    # r > s, s > p, p > r
    #if is_win(user, computer):
        #return 'You won!'

    #return 'You lost!'

#def is_win(player, opponent):
    # return true if player wins
    #if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        #or (player == 'p' and opponent == 'r'):
        #return True

#print(play())

