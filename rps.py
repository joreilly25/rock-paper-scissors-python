"""
A simple command-line Rock, Paper, Scissors game.
The user plays against the computer. The first to score 5 points wins.
The user can type 'help' for instructions or 'exit'/'close' to quit.
"""
import random


def computerPlay():
    """Randomly selects Rock, Paper, or Scissors for the computer.

    Returns:
        str: The computer's choice ('rock', 'paper', or 'scissors').
    """
    compSelections = ["rock", "paper", "scissors"]
    compSelection = random.choice(compSelections)
    return compSelection


def userPlay():
    """Prompts the user for their choice (Rock, Paper, Scissors, Help, Exit, Close).

    Handles user input for game choices, help requests, or exiting the game.
    Input is case-insensitive.

    Returns:
        str: The player's valid game choice ('rock', 'paper', 'scissors'),
             or 'quit' if the player chooses to exit.
    """
    while True:  # Loop indefinitely until a valid choice or exit command is given
        playerSelection = input("Please enter Rock, Paper, or Scissors: ").lower()
        if (
            playerSelection == "rock"
            or playerSelection == "paper"
            or playerSelection == "scissors"
        ):
            return playerSelection
        elif playerSelection == "exit" or playerSelection == "close":
            return "quit"
        elif playerSelection == "help":
            print(
                "Typing exit or close will stop program. if you want to play, please select rock paper or scissors."
            )


def playRound(playerSelection, compSelection):
    """Determines the winner of a single round of Rock, Paper, Scissors.

    Args:
        playerSelection (str): The player's choice ('rock', 'paper', 'scissors').
        compSelection (str): The computer's choice ('rock', 'paper', 'scissors').

    Returns:
        str: "player_wins" if the player wins,
             "computer_wins" if the computer wins,
             "draw" if it's a tie.
    """
    wins_against = {  # Defines the winning condition for each choice
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    if playerSelection == compSelection:
        return "draw"
    elif wins_against[playerSelection] == compSelection:
        return "player_wins"
    else:
        return "computer_wins"


def game():
    """Manages the main game flow for Rock, Paper, Scissors.

    Initializes scores, then loops through rounds of play until one player
    reaches 5 points or the user quits. It handles user input,
    determines round outcomes, updates scores, and prints relevant messages.
    """
    playerScore = 0  # Initialize player's score for the game
    compScore = 0  # Initialize computer's score for the game

    while True:  # Main game loop, continues until a win condition or quit
        user_selection = userPlay()

        if user_selection == "quit":
            print("Thanks for playing!")
            break

        comp_selection = computerPlay()
        outcome = playRound(user_selection, comp_selection)

        if outcome == "player_wins":
            print(f"You win this round! {user_selection.capitalize()} beats {comp_selection}.")
            playerScore += 1
        elif outcome == "computer_wins":
            print(f"Computer wins this round! {comp_selection.capitalize()} beats {user_selection}.")
            compScore += 1
        else:  # outcome == "draw"
            print(f"This round is a draw! Both chose {user_selection}.")

        print(f"Your Score: {playerScore}")
        print(f"Computer Score: {compScore}")

        if playerScore >= 5:
            print("Congrats You Win!")
            break
        elif compScore >= 5:
            print("Oh no! Try again!")
            break


if __name__ == "__main__":
    # Ensures game() is called only when the script is executed directly
    game()

# playRound(userPlay(), computerPlay())
