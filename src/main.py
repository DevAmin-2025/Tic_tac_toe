"""
This script initializes and starts the Tic Tac Toe game. It allows the user to choose between
A one-player game against an AI opponent or a two_player game.
"""
from src.game_logic import TicTacToe
from src.utils import print_info

if __name__ == '__main__':
	game = TicTacToe()
	print_info('\n Welcome to Tic Tac Toe game \n')
	print('1. One player game')
	print('2. Two player game\n')
	user_choice_game = input('Please choose an option: ')
	if user_choice_game == '1':
		game.one_player_game()
	elif user_choice_game == '2':
		game.two_player_game()
	else:
		print_info('Invalid input.')
		print_info('Exiting the app...')
