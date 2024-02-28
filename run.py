# Your code goes here.
import random

print("Welcome to Game Box!")

player = input("Do you want to play Rock, Paper, Scissors Game?")
print()

if player.lower() != "yes":
    quit()
else:
    print("Here is the rules")
choose = ("rock", "paper", "scissors")
player = None
computer = random.choice(choose)

player = input("Make a choice (rock, paper, scissors): ")

print(f"Player: {player}")
print(f"Computer: {computer}")