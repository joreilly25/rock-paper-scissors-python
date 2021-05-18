import random
playerScore = 0
compScore = 0

def computerPlay():
    compSelections = ["rock", "paper", "scissors"]
    compSelected = random.choice(compSelections)
    return compSelected

def userPlay():
    while True:
        playerSelection = input("Please enter Rock, Paper, or Scissors: ").lower()
        if playerSelection == "rock" or playerSelection == "paper" or playerSelection == "scissors":
            return playerSelection
            break
        elif playerSelection == "exit" or playerSelection == "close":
            break
        elif playerSelection == "help":
            print("Typing exit or close will stop program. if you want to play, please select rock paper or scissors.")
        
print(userPlay())
print(computerPlay())