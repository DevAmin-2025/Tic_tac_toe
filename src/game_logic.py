import random
from typing import Union

from src.utils import print_info, print_lose, print_win


class TicTacToe:
	"""
	A class to represent a Tic Tac Toe game.

	Attributes
	----------
	board: list
		The game board represented as a list.
	__player: str
		The current player ('X' or 'O').
	__ai_player: str
		The AI player ('X' or 'O').

	Methods
	-------
	show_bords()
		Display the current game board.
	get_random_first_player()
		Randomly select which player goes first.
	swap_player_turn()
		Swap the turn between 'X' and 'O'
	fix_spot(cell, player)
		Place the player's marker on the board if the cell is empty.
	filled_board()
		Check if the board is completely filled.
	win_player()
		Check if the current player has won.
	eval_player_input(player_input)
		Validate the player's input.
	get_ai_move()
		Determine the AI's move by selecting a random empty spot.
	Player_turn(player)
		Handle the player's move input.
	one_player_game()
		Run the game in one_player mode against the AI.
	Two_player_game()
		Run the game in two_player mode.
	"""
	def __init__(self):
		self.board = [' '] * 10  # 0th index is not used
		self.__player = self.get_random_first_player()
		self.__ai_player = 'O' if self.__player == 'X' else 'X'

	def show_board(self):
		"""
		Display the current state of the game board.
		"""
		print()
		print(self.board[1], '|', self.board[2], '|', self.board[3])
		print('-' * 10)
		print(self.board[4], '|', self.board[5], '|', self.board[6])
		print('-' * 10)
		print(self.board[7], '|', self.board[8], '|', self.board[9])
		print()

	def get_random_first_player(self) -> str:
		"""
		Randomly select which player goes first.

		:return: 'X' or 'O' indicating the first player.
		"""
		first_player = random.choice(['X', 'O'])
		return first_player

	def swap_player_turn(self):
		"""
		Swap the turn between 'X' and 'O'.
		"""
		self.__player = 'X' if self.__player == 'O' else 'O'

	def fix_spot(self, cell: int, player: str) -> bool:
		"""
		Place the player's marker on the board if the cell is empty.

		:param cell: The cell number (1-9) where the player wants to place their marker.
		:param player: The player's marker ('X' or 'O').
		:return: True if the spot was fixed, False otherwise.
		"""
		if self.board[cell] == ' ':
			self.board[cell] = player
			return True
		return False

	def filled_board(self) -> bool:
		"""
		Check if the board is completely filled.

		:return: True if the board is filled, False otherwise.
		"""
		return False if ' ' in self.board[1:] else True

	def win_player(self, player) -> bool:
		"""
		Check if the current player has won.

		:return: True if the current player has won, False otherwise.
		"""
		win_combinations = [
			[1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
			[1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
			[1, 5, 9], [3, 5, 7]  # Diagonals
		]
		for win_comb in win_combinations:
			if player == self.board[win_comb[0]] == self.board[win_comb[1]] == self.board[win_comb[2]]:
				return True
		return False

	def eval_player_input(self, player_input: str) -> bool:
		"""
		Validate the player's input.

		:param player_input: The player's input.
		:return: True if the input is valid, False otherewise.
		"""
		if not player_input.isdigit() or not (1 <= int(player_input) <= 9):
			return False
		return True

	def get_ai_move(self) -> int:
		"""
		Determine the AI's move by selecting a random empty spot.

		:return: The cell index selected by the AI.
		"""
		available_spots = [index for index, value in enumerate(self.board) if value == ' ' and index != 0]
		return random.choice(available_spots)

	def player_turn(self, player: str) -> Union[bool, None]:
		"""
		Handle the player's move input.

		:param player: The player's marker ('X' or 'O').
		:return: False if the player quits, None if the input is invalid or the spot is taken, True if the move is successful.
		"""
		chosen_spot = input(f'Player {player} enter a number between 1 to 9 (q to quit): ')
		if chosen_spot.lower() == 'q':
			print_info('Goodbye')
			return False
		elif not self.eval_player_input(chosen_spot):
			print_info('\nInvalid input. Enter a number between 1 to 9.\n')
			return None
		chosen_spot = int(chosen_spot)
		state = self.fix_spot(chosen_spot, player)
		if not state:
			print_info('\nAlready occupied. Choose another spot.\n')
			return None
		return True

	def one_player_game(self):
		"""
		Run the game in one-player mode against the AI.
		"""
		while True:
			self.show_board()
			if self.__player == self.__ai_player:
				print_info(f'AI ({self.__ai_player}) is making a move...')
				chosen_spot = self.get_ai_move()
				self.fix_spot(chosen_spot, self.__player)
			else:
				result = self.player_turn(self.__player)
				if result is False:
					break
				elif result is None:
					continue

			if self.win_player(self.__player):
				self.show_board()
				if self.__player == self.__ai_player:
					print_lose('Game Over!')
					break
				print_win(f'\n Congratulations! Player {self.__player} you won. \n')
				break
			elif self.filled_board():
				self.show_board()
				print_info('Draw!')
				break

			self.swap_player_turn()

	def two_player_game(self):
		"""
		Run the game in two-player mode.
		"""
		while True:
			self.show_board()
			result = self.player_turn(self.__player)
			if result is False:
				break
			elif result is None:
				continue

			if self.win_player(self.__player):
				self.show_board()
				print_win(f'\n Congratulations! Player {self.__player} you won. \n')
				break
			elif self.filled_board():
				self.show_board()
				print_info('Draw!\n')
				break

			self.swap_player_turn()
