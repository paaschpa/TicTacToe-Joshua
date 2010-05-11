import sys
import unittest
import boards
from boards import *

class BoardsTest(unittest.TestCase):
	
	def test_init_creates_a_list_with_nine_emptycells(self):
		board = Boards()
		self.assertEqual(9, len(board.cells))
		for i in board.cells:
			self.assertEqual("empty", i)

	def test_init_instance_creates_a_list_with_sixteen_emptycells(self):
		board = Boards(16)
		self.assertEqual(16, len(board.cells))
		for i in board.cells:
			self.assertEqual("empty", i)
			
	def test_winner_returns_none_when_there_is_no_winning_combination(self):
		board = Boards(9)
		self.assertEqual(None, board.winner())

	def test_winner_returns_player_x_when_x_has_a_winning_combination(self):
		board = Boards(9)
		board.cells[0] = "player_x"
		board.cells[1] = "player_x"
		board.cells[2] = "player_x"
		self.assertEqual("player_x", board.winner())

	def test_winner_returns_player_y_when_y_has_a_winning_combination(self):
		board = Boards(9)
		board.cells[2] = "player_y"
		board.cells[5] = "player_y"
		board.cells[8] = "player_y"
		self.assertEqual("player_y", board.winner())

	def test_winner_returns_player_with_diagonal_win(self):
		board = Boards(9)
		board.cells[0] = "player_y"
		board.cells[4] = "player_y"
		board.cells[8] = "player_y"
		self.assertEqual("player_y", board.winner())

	def test_takeCell_places_player_x_in_cell_four(self):
		board = Boards(9)
		board.takeCell("player_x", 4)
		self.assertEqual("player_x", board.cells[4])

	def test_takeCell_places_takes_number_as_string(self):
		board = Boards(9)
		board.takeCell("player_x", "5")
		self.assertEqual("player_x", board.cells[5])

	def test_takeCell_raises_CellNotAvailableError_when_cell_is_taken(self):
		board = Boards(9)
		board.takeCell("player_y", 5)
		self.assertRaises(boards.CellNotAvailableError, board.takeCell, "player_x",5)

	def test_getEmptyCells_returns_all_cells(self):
		self.board = Boards(9)
		self.assertEqual([0,1,2,3,4,5,6,7,8], self.board.getEmptyCells())

	def test_getEmptyCells_returns_1to8_when_zero_isNotEmpty(self):
		self.board = Boards(9)
		self.board.cells[0] = "filled"
		self.assertEqual([1,2,3,4,5,6,7,8], self.board.getEmptyCells())
	
	def test_winningCombination_returns_true_when_all_items_areEqual(self):
		winningList = ["player_x", "player_x", "player_x"]
		self.board = Boards()
		self.assertEqual(True, self.board.winningCombination(winningList))

	def test_winningCombinatino_returns_false_when_one_item_isNotEqual_to_other_items(self):
		nonwinningList = ["player_x","player_y","player_x"]
		self.board = Boards()
		self.assertEqual(False, self.board.winningCombination(nonwinningList))

	def test_winningCombination_returns_false_when_one_item_isEmpty(self):
		nonwinningList = ["player_x","player_x","empty"]
		self.board = Boards()
		self.assertEqual(False, self.board.winningCombination(nonwinningList))
	
	def test_winningCombination_returns_false_on_three_empties(self):
		nonwinningList = ["empty","empty","empty"]
		self.board = Boards()
		self.assertEqual(False, self.board.winningCombination(nonwinningList))
	
	def test_gameOver_returns_false_with_no_winner_and_emtpy_cells(self):
		board = Boards()
		self.assertEqual(False, board.gameOver())

	def test_gameOver_returns_true_when_all_cells_are_not_empty(self):
		board = Boards()
		for i in range(0, len(board.cells)):
			board.cells[i] = "filled"
		self.assertEqual(True, board.gameOver())
	
	def test_gameOver_returns_true_when_there_is_a_winner(self):
		board = Boards()
		board.cells[0]="player_x"
		board.cells[1]="player_x"
		board.cells[2]="player_x"
		self.assertEqual(True, board.gameOver())


if __name__ == "__main__":
	unittest.main()
