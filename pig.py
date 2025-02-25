import random

def roll():
    min_value=1
    max_value=6
    roll= random.randint(min_value,max_value)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("Invalid input. Please enter a number between 2 and 4.")
    else:
        print("Invalid input. Please enter a number between 2 and 4.")

max_score=50
player_scores=[0 for _ in range(players)]  #list comprehension to create a list of 0s for each player score. The _ is used as a throwaway variable, meaning we don't care about the value of the variable.

print(player_scores)