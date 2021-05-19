import random
playerScore = 0
compScore = 0

def computerPlay():
    compSelections = ["rock", "paper", "scissors"]
    compSelection = random.choice(compSelections)
    return "rock"

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

def playRound(playerSelection, compSelection):
    global playerScore
    global compScore
    if playerSelection == "rock" and compSelection == "scissors":
        playerScore += 1
        return print("You Win! Rock beats Scissors!")
    elif playerSelection == "scissors" and compSelection == "rock":
        compScore += 1
        return print("You Lose! Rock beats Scissors!")
        
playRound(userPlay(), computerPlay())
print("Your Score: " + str(playerScore))
print("Comp Score: " + str(compScore))