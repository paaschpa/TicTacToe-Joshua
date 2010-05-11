class BoardError(Exception): pass
class CellNotAvailableError(BoardError): pass

class Boards:
	
	def __init__(self, cells=None):
		if cells is None:
			cells = 9
		self.cells = ["empty"]*cells

	def winner(self):
        	winningLists = [[0,1,2],[3,4,5],[6,7,8], # vertical
                	        [0,3,6],[1,4,7],[2,5,8], # horizontal
                        	[0,4,8],[2,4,6]]         # diagonal
        
		for winningList in winningLists:
			if self.cells[winningList[0]] != "empty" and self.winningCombination([self.cells[cell] for cell in winningList]):
                		return self.cells[winningList[0]]

	def takeCell(self, x_or_o, cell):
		if int(cell) not in self.getEmptyCells():
			if x_or_o != "empty":
				raise CellNotAvailableError, "Cell is already taken"
		self.cells[int(cell)] = x_or_o

	def getEmptyCells(self):
		return [i for i in range(0, len(self.cells)) if self.cells[i] == "empty"]

	def winningCombination(self, list):
		for i in range(0, len(list)):
			if list[i] == "empty":
				return False

			if i+1 < len(list):
				if list[i] != list[i+1]:
					return False
		return True

	def gameOver(self):
		if len(self.getEmptyCells()) == 0:
			return True
		if self.winner():
			return True
		return False

