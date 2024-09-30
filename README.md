# Connect-4

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Game Setup](#game-setup)
- [Classes and Methods](#classes-and-methods)
- [Running the Game Demo](#running-the-game-demo)
- [License](#license)

## Introduction
This project implements a Connect Four game in Python, which can be played by two human players or a human player vs an AI. The AI is capable of making strategic decisions using lookahead techniques. The game board is adjustable to any dimensions, though it defaults to the standard 6x7 size. The AI player can be configured to use different tie-breaking strategies and varying levels of lookahead depth to determine the best move.

Connect Four is a classic two-player connection game where players take turns dropping checkers into a vertical board. The objective is to be the first to form a horizontal, vertical, or diagonal line of four checkers.

# Features
Human vs. Human: Play the classic game of Connect Four between two human players.
Human vs. AI: Challenge a computer AI player with adjustable difficulty (based on the depth of lookahead).
Adjustable Board Size: You can create a custom-sized board.
Random Player: An AI player that selects moves randomly.
Strategic AI Player: Uses lookahead and different tie-breaking strategies to choose the optimal moves.

# Game Setup
Board: The game is played on a rectangular grid. The default board size is 6 rows by 7 columns, but the dimensions can be customized during board initialization.

Players: Two players take turns placing their checkers (either 'X' or 'O') into the board's columns. The first player to get four checkers in a row (horizontally, vertically, or diagonally) wins the game.

A few examples of setting up the games will be shown later in the Demo column.

## Classes and Methods

Board Class
Initialization: Creates a game board with the specified height and width.
add_checker: Adds a checker ('X' or 'O') to the specified column.
reset: Resets the board to an empty state.
can_add_to: Checks whether a column can accept more checkers.
is_full: Determines whether the board is full.
is_win_for: Checks if a player has won (either horizontally, vertically, or diagonally).
remove_checker: Removes the top checker from a specified column.

Player Class
Represents a player in the game. Each player has a checker ('X' or 'O').
next_move: Asks the player to input the column for their next move.
opponent_checker: Returns the checker used by the opponent.

RandomPlayer Class
An AI player that selects columns randomly. It checks which columns are available and picks one at random.

AIPlayer Class
A more sophisticated AI that uses lookahead to predict the best move. The AI evaluates possible moves by considering future moves up to a specified depth (lookahead).
Attributes:
checker: The AI's checker ('X' or 'O').
tiebreak: Method used to handle tie scores ('LEFT', 'RIGHT', 'RANDOM').
lookahead: Depth of lookahead to predict moves.
max_score_column: Chooses the best column based on scores. If multiple columns have the same score, it uses the tiebreak strategy to choose one.
scores_for: Returns a score for each column based on the current board state and future moves.
next_move: Returns the best move based on the calculated scores.

## Running the Game Demo

First, create a folder where you can add all 4 of the files and run them on an appropriate Python software (done on Spyder in the demo).

Human vs Human

<img width="139" alt="image" src="https://github.com/user-attachments/assets/8c09555d-483d-431f-9e78-6925f37ce071">

Human vs Random AI

<img width="148" alt="image" src="https://github.com/user-attachments/assets/cc44c26c-2678-4662-b172-70dad9c16576">

Human vs Smart AI (Look Ahead set to 3 in this case and tiebreak strategy set to Random)

<img width="197" alt="image" src="https://github.com/user-attachments/assets/12933f6a-ee02-423d-9b10-af9cd497d137">

Smart AI vs Random AI (We could also do Random AI vs Random AI or Smart AI vs Smart AI)

<img width="205" alt="image" src="https://github.com/user-attachments/assets/2b9f7a06-7716-4a9d-8ccd-8999bff6eb6e">

As expected, the Smart AI wins

<img width="217" alt="image" src="https://github.com/user-attachments/assets/d0802bff-3667-41fa-b923-c581425edf7f">

## License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
