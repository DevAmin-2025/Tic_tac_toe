# Tic Tac Toe Game

## Introduction
Welcome to the Tic Tac Toe game project! This project implements the classic Tic Tac Toe game in Python. Whether you want to play against an AI opponent or challenge a friend in two-player mode, this game has you covered. The game features colorful prints to enhance the user experience and provide clear feedback during gameplay.

## Features
- One-player mode: Play against an AI opponent.
- Two-player mode: Play against another human player.
- Colorful prints for game information, win, and lose messages.

## Modules
1. **`game_logic.py`**: This module contains the `TicTacToe` class, which implements the game logic.
### Methods:
- `show_board()`: Display the current game board.
- `get_random_first_player() -> str`: Randomly select which player goes first.
- `swap_player_turn()`: Swap the turn between 'X' and 'O'.
- `fix_spot(cell: int, player: str) -> bool`: Place the player's marker on the board if the cell is empty.
- `filled_board() -> bool`: Check if the board is completely filled.
- `win_player() -> bool`: Check if the current player has won.
- `eval_player_input(player_input: str) -> bool`: Validate the player's input.
- `get_ai_move() -> int`: Determine the AI's move by selecting a random empty spot.
- `player_turn(player: str) -> Union[bool, None]`: Handle the player's move input.
- `one_player_game()`: Run the game in one-player mode against the AI.
- `two_player_game()`: Run the game in two-player mode.

2. **`main.py`**: This module initializes and starts the Tic Tac Toe game. It allows the user to choose between a one-player game against an AI opponent or a two-player game.

3. **`utils.py`**: This module provides utility functions for colorful prints.
    ### Functions:
    - `print_info(text: str)`: Print game information in white color.
    - `print_win(text: str)`: Print win message in green color.
    - `print_lose(text: str)`: Print lose message in red color.

## How to Run
1. **Clone the Repository**: Open your terminal and run the following command to clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
```
Replace your-username and your-repo with the actual GitHub username and repository name.

2. Navigate to the main project directory, add the current directory to the `PYTHONPATH` and run the `main.py` script.
```bash
cd Tic_tac_toe
export PYTHONPATH=$PYTHONPATH:$(pwd)
python src/main.py
```
3. Install any necessary requirement.
```bash
pip install -r requirements.txt
```
