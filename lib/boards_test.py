import sys
import unittest
from boards import *

class NinecellsTest(unittest.TestCase):
	
	def test_init_ninecells_instance_creates_a_list_with_nine_emptycells(self):
		self.board = Boards(9)
		self.assertEqual(9, len(self.board.cells))

	def test_init_fourcells_instance_creates_a_list_with_four_emptycels(self):
		self.board = Boards(4)
		self.assertEqual(4, len(self.board.cells))
	
	def test_winner_returns_player_x_when_x_has_a_winning_combination(self):
		pass

	def test_winner_returns_player_y_when_y_has_a_winning_combination(self):
		pass

	def test_winner_returns_when_there_is_no_winning_combination(self):
		pass

	def test_takeCell_places_player_x_in_cell_one(self):
		pass

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
	
	def test_gameOver_returns_true_when_all_cells_are_not_empty(self):
		pass
	
	def test_gameOver_returns_true_when_there_is_a_winner(self):
		pass

	def test_gameOver_returns_false_with_no_winner_and_emtpy_cells(self):
		pass


if __name__ == "__main__":
	unittest.main()
