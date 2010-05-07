import unittest
import sys
from joshua_console import *
from cStringIO import StringIO

class Test(unittest.TestCase):

	def setUp(self):
		self.console = JoshuaConsole()
		self.held, sys.stdout = sys.stdout, StringIO()
	
	def test_new_tictactoeGame_gameboard_has_nine_cells_filled_with_empty(self):
		self.assertEqual(9,len(self.console.tictactoe.gameboard.cells))
		for i in range(0,9):
			self.assertEqual("empty",self.console.tictactoe.gameboard.cells[i])
	def test_new_tictactoe_game_has_nine_empty_cells_PlayerX_isHuman_Player_isComputerHard(self):
		pass

	def test_addspaces_adds_blanks_to_make_the_cell_length_equal_to_10(self):
		self.assertEqual(10, len(self.console.addspaces("empty")))
	
	def test_addspaces_returns_a_cell_with_length_of_ten_when_given_text_less_then_10(self):
		self.assertEqual(10, len(self.console.addspaces("player_x")))
	
#       My google-fu was weak and I didn't find a simple way to test stdout...
#	there are other things to be done and I'm making the decision to skip this 
#	test as I should be able to easily see any issues. As I proceed, I'm hoping 
#	I stumble across a way to test stdout as well as $1 million and the always elusive
#	unicorn.  
# 	I take the above back...I found a way to capture stdout, but I don't like the test
#	And I still haven't found a unicorn
	def test_print_gameboard_prints_empty_top_row_to_screen(self):
		self.console.printGameboard(self.tictactoeGame.gameboard)
		capture = sys.stdout.getvalue()
		self.assertEqual(True,capture.__contains__("empty     "))

	def test_player_x_is_in_cell_0(self):
		self.console.tictactoe.gameboard.cells[0] = "player_x"
		self.assertEqual(self.console.tictactoe.gameboard.cells[0], "player_x")

	def test_player_x_is_in_cell_0__player_o_is_in_cell_1(self):
		self.console.tictactoe.gameboard.cells[0] = "player_x"
		self.console.tictactoe.gameboard.cells[1] = "player_o"
		self.assertEqual(self.console.tictactoe.gameboard.cells[0], "player_x")
		self.assertEqual(self.console.tictactoe.gameboard.cells[1], "player_o")

	def test_makeMove_player_x_to_cell_0(self):
		def getMoveMock(arg1, arg2, arg3):
			return 0
		
		self.console.currentPlayer.getMove = getMoveMock
		self.console.makeMove()	
		self.assertEqual("player_x", self.console.tictactoe.gameboard.cells[0]) 
	
	def test_switchPlayers_changes_currentPlayerX_tocurrent_PlayerO(self):
		self.assertEqual(self.console.tictactoe.PlayerX, self.console.currentPlayer)
		self.console.switchPlayers()
		self.assertEqual(self.console.tictactoe.PlayerO, self.console.currentPlayer)

	def test_switchPlayers_changes_currentPlayerO_tocurrentPlayerX(self):
		self.console.currentPlayer = self.console.tictactoe.PlayerO
		self.assertEqual(self.console.tictactoe.PlayerO, self.console.currentPlayer)
		self.console.switchPlayers()
		self.assertEqual(self.console.tictactoe.PlayerX, self.console.currentPlayer)

	
	#def test_player_x_makeMove_to_cell_2__player_o_makeMove_to_cell_1(self):
		#self.console.makeMove()
		#self.tictactoeGame.takesCell("player_o", 1)
		#self.assertEqual("player_x", self.gameboard[0])
		#self.assertEqual("player_o", self.gameboard[1])
	
			
if __name__ == "__main__":
	unittest.main()
