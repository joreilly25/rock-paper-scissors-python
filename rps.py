import random
playerScore = 0
compScore = 0

def computerPlay():
    compSelections = ["rock", "paper", "scissors"]
    compSelected = random.choice(compSelections)
    return compSelected

print(computerPlay())