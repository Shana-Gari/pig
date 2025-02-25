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

score =0

# for loop to iterate through each player's turn
for player_index in range(players):
    print("Player", player_index+1, "turn")

    # while loop to allow the player to roll multiple times in a single turn until they choose to stop or roll a 1
    while True:

        roll_dice=input("Do you want to roll? (y/n): ")

        if roll_dice.lower()=='y':
            roll_value=roll()
            print("You rolled:", roll_value)
            if roll_value==1:
                print("You rolled a 1. No points added.")
                score=0
                break   #breaks out of the loop
            else:
                score+=roll_value
                print("Your current round score is:", score)
        elif roll_dice.lower()=='n':
            player_scores[player_index]+=score
            print("Your total score is:", player_scores[player_index])
            break  #breaks out of the loop
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
   
        