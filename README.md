# Rock, Paper, Scissors Game

This is a simple command-line Rock, Paper, Scissors game where you play against the computer.
The first player to score 5 points wins the game!

## How to Play

1.  Open your terminal or command prompt.
2.  Navigate to the directory where you saved the `rps.py` file.
3.  Run the script using the command: `python rps.py`
4.  The game will prompt you to enter your choice. Type one of the following and press Enter:
    *   `rock`
    *   `paper`
    *   `scissors`
5.  You can also type:
    *   `help` - to see a help message.
    *   `exit` or `close` - to quit the game.

## Game Flow

*   The game starts with both you and the computer at 0 points.
*   In each round:
    *   You will be asked to choose Rock, Paper, or Scissors.
    *   The computer will randomly make its choice.
    *   The choices are compared:
        *   Rock crushes Scissors
        *   Scissors cuts Paper
        *   Paper covers Rock
    *   The winner of the round gets 1 point. If it's a tie, no points are awarded.
*   Your current score and the computer's score are displayed after each round.
*   The first player to reach 5 points wins the game!
*   If you type `help`, instructions will be displayed.
*   If you type `exit` or `close`, the game will end.

## Contributing

Contributions are welcome! If you have any ideas for improvements or find any bugs, feel free to:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes.
4.  Submit a pull request.

## License

This project is released under the MIT License. See the LICENSE file for details (though a LICENSE file is not yet created for this project, it's good practice to mention it).
