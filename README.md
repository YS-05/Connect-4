# Connect-4

This project implements a Connect 4 game that can be played by two players: a human player, a random AI player, or a smart AI player with configurable depth. The game supports a simple board setup, allows interaction through a command-line interface, and includes multiple playing modes.

Features:
Two-player gameplay: Either two human players or a human player versus AI can play the game.
Random AI: A basic AI that chooses a random legal move.
Smart AI: A configurable AI that looks ahead by a set number of moves (depth) and tries to pick the best possible move based on this foresight.
Tiebreak mechanisms: The smart AI can use different strategies to resolve ties between equally good moves: choosing the leftmost, rightmost, or randomly selecting.
Board management: The game includes the ability to add, remove, and check for winning moves on the board.

Game modes:
Human vs Human: Two human players take turns entering their moves via the console.
Human vs Random AI: A human player competes against an AI that chooses moves at random.
Human vs Smart AI: A human player competes against an AI that uses lookahead to choose its moves, with a configurable depth level.

Upon starting the game, the board is displayed and players alternate turns.
The game will ask the players (or the AI) to input the column in which they want to drop their checker.
The game continues until one player wins by connecting four checkers in a row or until the board is full (tie).
