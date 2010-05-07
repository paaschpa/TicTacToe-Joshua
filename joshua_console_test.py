import unittest
import sys
from joshua import TicTacToe
import joshua
from cStringIO import StringIO

class Test(unittest.TestCase):

	def setUp(self):
        	self.tictactoeGame = TicTacToe()
		self.gameboard = self.tictactoeGame.gameboard
		self.held, sys.stdout = sys.stdout, StringIO()
	
	def test_A_new_tictactoeGame_gameboard_has_nine_cells_filled_with_empty(self):
		self.assertEqual(9,len(self.gameboard))
		for i in range(0,9):
			self.assertEqual("empty",self.gameboard[i])

	def test_addspaces_adds_blanks_to_make_the_cell_length_equal_to_10(self):
		self.assertEqual(10, len(self.tictactoeGame.addspaces("empty")))
		
	def test_addspaces_returns_a_cell_with_length_of_ten_when_given_text_less_then_10(self):
		self.assertEqual(10, len(self.tictactoeGame.addspaces("player_x")))
	
#       My google-fu was weak and I didn't find a simple way to test stdout...
#	there are other things to be done and I'm making the decision to skip this 
#	test as I should be able to easily see any issues. As I proceed, I'm hoping 
#	I stumble across a way to test stdout as well as $1 million and the always elusive
#	unicorn.  
# 	I take the above back...I found a way to capture stdout, but I don't like the test
#	And I still haven't found a unicorn
	def test_print_gameboard_prints_empty_top_row_to_screen(self):
		self.tictactoeGame.printGameboard(self.tictactoeGame.gameboard)
		capture = sys.stdout.getvalue()
		self.assertEqual(True,capture.__contains__("empty     "))

	def test_player_x_is_in_cell_0(self):
		self.gameboard[0] = "player_x"
		self.assertEqual(self.gameboard[0], "player_x")

	def test_player_x_is_in_cell_0__player_o_is_in_cell_1(self):
		self.gameboard[0] = "player_x"
		self.gameboard[1] = "player_o"
		self.assertEqual(self.gameboard[0], "player_x")
		self.assertEqual(self.gameboard[1], "player_o")

	def test_player_x_takes_cell_0(self):
		self.tictactoeGame.takesCell("player_x", 0)	
		self.assertEqual("player_x", self.gameboard[0]) 
	
	def test_player_x_takes_cell_2__player_o_takes_cell_1(self):
		self.tictactoeGame.takesCell("player_x", 0)
		self.tictactoeGame.takesCell("player_o", 1)
		self.assertEqual("player_x", self.gameboard[0])
		self.assertEqual("player_o", self.gameboard[1])
	
	#Need to mock out the getraw_input method with 
	#the local raw_inputMock method
	def test_humanPlayer_places_x_in_cell0(self):
		def raw_inputMock(arg):
			return 0

		self.tictactoeGame.getraw_input = raw_inputMock

		self.tictactoeGame.askPlayer("player_x")
		self.assertEqual("player_x", self.tictactoeGame.gameboard[0])

	def test_possibleMoves_returns_all_cell_numbers_for_a_new_gameboard(self):
		self.assertEqual([0,1,2,3,4,5,6,7,8], self.tictactoeGame.possibleMoves())
	
	def test_possibleMoves_returns_cells1to8_when_cell_0_isNotEmpty(self):
		self.gameboard[0] = "player_x"
		self.assertEqual([1,2,3,4,5,6,7,8], self.tictactoeGame.possibleMoves()) 
	
	def test_possibleMoves_returns_cells_marked_as_empty(self):
		self.gameboard[2]="player_x"
		self.gameboard[4]="player_y"
		self.gameboard[6]="player_x"
		self.assertEqual([0,1,3,5,7,8], self.tictactoeGame.possibleMoves())

	def test_gameOver_isTrue_when_all_cells_are_filled(self):
		for i in range(0,9):
			self.gameboard[i]="player_x"
		self.assertEqual(True, self.tictactoeGame.gameOver())
	
	def test_gameOver_isFalse_when_AtLeastOne_cell_contains_empty_and_there_is_not_a_winner(self):
		for i in range(1,9):
			self.gameboard[i]="player_x"
		self.gameboard[4]="player_o"
		self.gameboard[8]="player_o"
		self.assertEqual(False, self.tictactoeGame.gameOver())
	
	def test_winner_returns_player_x_when_player_x_has_won_in_column_one(self):
		self.tictactoeGame.gameboard = ["player_o","player_o","player_x","player_x","player_x","player_x","player_x","player_o","player_o",]
		self.assertEqual("player_x",self.tictactoeGame.winner())

	def test_winner_returns_player_x_when_player_x_has_won_in_column_two(self):
		self.tictactoeGame.gameboard = ["player_o","player_x","player_o","player_x","player_x","player_o","player_o","player_x","player_x",]
		self.assertEqual("player_x",self.tictactoeGame.winner())

	def test_winner_returns_player_x_when_player_x_has_won_in_column_three(self):
		self.tictactoeGame.gameboard = ["player_o","player_x","player_x","player_o","player_o","player_x","player_x","player_o","player_x",]
		self.assertEqual("player_x",self.tictactoeGame.winner())
	
	def test_winner_returns_player_o_when_player_o_has_won_in_middle_row(self):
		self.tictactoeGame.gameboard = ["player_o","player_x","player_x","player_o","player_o","player_o","player_x","player_o","player_x",]
		self.assertEqual("player_o",self.tictactoeGame.winner())

	def test_winner_returns_player_o_when_player_o_has_won_diagnol(self):
		self.tictactoeGame.gameboard = ["player_o","player_x","player_x","player_x","player_o","player_o","player_o","player_x","player_o",]
		self.assertEqual("player_o",self.tictactoeGame.winner())

	def test_winningCombination_returns_true_when_all_items_areEqual(self):
		winningList = ["player_x", "player_x", "player_x"]
		self.assertEqual(True, self.tictactoeGame.winningCombination(winningList))

	def test_winningCombinatino_returns_false_when_one_item_isNotEqual_to_other_items(self):
		nonwinningList = ["player_x","player_y","player_x"]
		self.assertEqual(False, self.tictactoeGame.winningCombination(nonwinningList))

	def test_winningCombination_returns_false_when_one_item_isEmpty(self):
		nonwinningList = ["player_x","player_x","empty"]
		self.assertEqual(False, self.tictactoeGame.winningCombination(nonwinningList))

	def test_winner_returns_player_x_when_player_x_has_a_winning_combination(self):
		self.tictactoeGame.gameboard = ["player_x","player_x","player_x","player_o","player_o","player_x","player_x","player_o","player_o",]
		self.assertEqual("player_x",self.tictactoeGame.winner())

	def test_endingMove_returns_false_with_no_winner_and_empty_gameboard(self):
		self.assertEqual(False, joshua.endingMove(self.tictactoeGame))

	def test_endingMove_returns_true_with_a_winner(self):
		self.tictactoeGame.gameboard = ["player_x","player_x","player_x","player_o","player_o","player_x","player_x","player_o","player_o",]
		self.assertEqual(True, joshua.endingMove(self.tictactoeGame))

	def test_checkForWinningMove_finds_winningCell_when_available(self):
		self.tictactoeGame.gameboard = ["player_o","player_o","empty","player_x","player_x","empty","empty","empty","empty"]
		self.tictactoeGame.checkForWinningMove("player_o")
		self.assertEqual("player_o", self.tictactoeGame.gameboard[2])
	
	def test_checkForWinningMove_finds_returns_None_when_no_winningCell_is_found(self):
		self.tictactoeGame.gameboard = ["player_o","empty","empty","player_x","player_x","empty","empty","empty","empty"]
		self.assertEqual(None,self.tictactoeGame.checkForWinningMove("player_o"))

	def test_computerPlayer_makes_winning_move_when_available(self):
		self.tictactoeGame.gameboard = ["player_o","player_o","empty","player_x","player_x","empty","empty","empty","empty"]
		self.tictactoeGame.computerPlayer("player_o")
		self.assertEqual("player_o", self.tictactoeGame.gameboard[2])
			
if __name__ == "__main__":
	unittest.main()
