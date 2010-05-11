import unittest
import sys
from tictactoe import TicTacToe
from lib.boards import *
from lib.players import *

class Test(unittest.TestCase):

	def test_init_creates_a_gameboard_with_ninecells(self):
		tictactoe = TicTacToe()
		self.assertEqual(9, len(tictactoe.gameboard.cells))
	
	def test_init_creates_a_gameboard_with_ninecells_all_set_to_empty(self):
		tictactoe = TicTacToe()
		for i in range(0,9):
			self.assertEqual("empty", tictactoe.gameboard.cells[i])

	def test_init_create_a_gameboard_with_sixteenCells(self):
		tictactoe = TicTacToe(gameboard=Boards(16))
		self.assertEqual(16, len(tictactoe.gameboard.cells))

	def test_init_when_numberOfPlayers_is_one_PlayerX_is_human(self):
		tictactoe = TicTacToe(numberOfPlayers=1)
		self.assertEqual("HumanPlayer", tictactoe.PlayerX.__class__.__name__)
		
	def test_init_when_numberOfPlayers_is_two_PlayerX_and_PlayerO_are_human(self):
		tictactoe = TicTacToe(numberOfPlayers=2)
		self.assertEqual("HumanPlayer", tictactoe.PlayerX.__class__.__name__)
		self.assertEqual("HumanPlayer", tictactoe.PlayerO.__class__.__name__)	
	
	def test_getComputerPlayer_returns_ComputerPlayerDifficult_when_passed_difficult(self):
		tictactoe = TicTacToe()
		player = tictactoe.getComputerPlayer("Hard")
		self.assertEqual("ComputerPlayerDifficult", player.__class__.__name__)

	def test_getComputerPlayer_returns_ComputerPlayerEasy(self):
		tictactoe = TicTacToe()
		player = tictactoe.getComputerPlayer("Test")
		self.assertEqual("ComputerPlayerEasy", player.__class__.__name__)


if __name__ == "__main__":
	unittest.main()
