import sys
import unittest
from players import *
from boards import *

class PlayersTest(unittest.TestCase):
	#Need to mock out the getraw_input method with 
	#the local raw_inputMock method
	def test_HumanPlayer_getPlayerMove_equals_zero(self):
		def raw_inputMock(arg1, arg2):
			return 0
		board = Boards(9)
		self.human = HumanPlayer()
		self.human.getraw_input = raw_inputMock
		self.assertEqual(0, self.human.getMove("", board))
		


	def test_ComputerPlayerDifficult_getPlayerMove_takes_last_cell(self):
		computer = ComputerPlayerDifficult()
		board = Boards(9)
		for i in range(0,8):
			board.cells[i]="x"
		move = computer.getMove("x", board) 
		self.assertEqual(8, move)
	
	def test_ComputerPlayerDifficult_getPlayerMove_can_take_one_of_two_cells(self):
		computer = ComputerPlayerDifficult()
		board = Boards(9)
		for i in range(0,7):
			board.cells[i]="x"
		move = computer.getMove("x", board) 
		self.assertTrue([7,8].__contains__(move))
	
	def test_ComputerPlayerDifficult_getPlayerMove_can_take_one_of_three_cells(self):
		computer = ComputerPlayerDifficult()
		board = Boards(9)
		for i in range(0,6):
			board.cells[i]="player_x"
		move = computer.getMove("player_x", board) 
		self.assertTrue([6,7,8].__contains__(move))

	def test_ComputerPlayerDifficult_getPlayerMove_can_take_one_of_four_cells(self):
		computer = ComputerPlayerDifficult()
		board = Boards(9)
		for i in range(0,5):
			board.cells[i]="x"
		move = computer.getMove("x", board) 
		print move
		self.assertTrue([5,6,7,8].__contains__(move))

	def test_ComputerPlayerDifficult_getPlayerMove_can_take_one_of_five_cells(self):
		computer = ComputerPlayerDifficult()
		board = Boards(9)
		for i in range(0,4):
			board.cells[i]="x"
		move = computer.getMove("x", board) 
		print move
		self.assertTrue([4,5,6,7,8].__contains__(move))

	def test_ComputerPlayerDifficult_getPlayerMove_can_take_one_of_six_cells(self):
		computer = ComputerPlayerDifficult()
		board = Boards(9)
		for i in range(0,3):
			board.cells[i]="x"
		move = computer.getMove("x", board) 
		print move
		self.assertTrue([3,4,5,6,7,8].__contains__(move))

	def test_ComputerPlayerDifficult_getPlayerMove_can_take_one_of_seven_cells(self):
		computer = ComputerPlayerDifficult()
		board = Boards(9)
		for i in range(0,2):
			board.cells[i]="player_x"
		move = computer.getMove("player_x", board) 
		print move
		self.assertTrue([2,3,4,5,6,7,8].__contains__(move))

if __name__ == "__main__":
	unittest.main()
