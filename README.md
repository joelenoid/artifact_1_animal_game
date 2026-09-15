ANIMAL GUESSER
A wordle sort of game played in the terminal where the goal is to guess a randomised animal in 6 tries.
Each animal has attributes that are compared to those of the mystery animal when a guess is input.
These attributes are temperature, habitat, diet and classification/species type.

TERMINAL
The correct format when running the game is as follows "python animal_game.py <difficulty> <username>"
<difficulty> can be easy, medium or hard and the choice will change the pool of animals available.
<username> decides what is displayed on the leaderboard when the game is won.

Example: "python animal_game.py <hard> <joel>"

FEATURES
When a user inputs "list" into the game, a list of available animals is output based on difficulty

A list of high scores logged to board.csv and is produced when the game is complete .

REQUIREMENTS
The tabulate library: pip install tabulate

SKILLS
I have only recently started learning python in my free time over the past month and this is proof of progress.
This project demonstrates exception handling, unit tests, sorting with a custom key, and an external library.
Nested dictionaries, command-line arguments (sys.argv) and  file I/O (reading/writing a CSV-style scoreboard).
This was built as a self-study project alongside CS50P.