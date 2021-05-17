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
        
print(userPlay())
print(computerPlay())