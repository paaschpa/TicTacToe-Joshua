import unittest
import sys
from tictactoe import TicTacToe
from boards.boards import *
from players.players import *

class Test(unittest.TestCase):

	def test_init_creates_a_gameboard_with_ninecells(self):
		tictactoe = TicTacToe()
		self.assertEqual(9, len(tictactoe.gameboard.cells))
	
	def test_init_create_a_gameboard_with_fourcells(self):
		tictactoe = TicTacToe(gameboard=Boards(4))
		self.assertEqual(4, len(tictactoe.gameboard.cells))

	def test_init_when_numberOfPlayers_is_one_PlayerX_is_human(self):
		tictactoe = TicTacToe()
		self.assertEqual("HumanPlayer", tictactoe.PlayerX.__class__.__name__)
		
	def test_init_when_numberOfPlayers_is_two_PlayerX_and_PlayerO_are_human(self):
		tictactoe = TicTacToe(numberOfPlayers=2)
		self.assertEqual("HumanPlayer", tictactoe.PlayerX.__class__.__name__)
		self.assertEqual("HumanPlayer", tictactoe.PlayerO.__class__.__name__)	

if __name__ == "__main__":
	unittest.main()
