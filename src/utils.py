"""
Provide ways to have colorful prints.
"""
from termcolor import colored


def print_info(text: str):
	print(colored(text, 'white', attrs=['reverse']))


def print_win(text: str):
	print(colored(text, 'green', attrs=['reverse', 'blink']))


def print_lose(text: str):
	print(colored(text, 'red', attrs=['reverse', 'blink']))
