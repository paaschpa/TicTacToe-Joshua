import time, random
from lib.boards import *
from lib.players import *

class TicTacToe:

	def __init__(self, numberOfPlayers=1, gameboard=None, difficulty="Hard"):
		if gameboard is None:
			self.gameboard = Boards(9)
		else:
			self.gameboard = gameboard

		self.PlayerX = HumanPlayer()
		self.PlayerO = self.getComputerPlayer(difficulty)
		
		if numberOfPlayers == 2:
			self.PlayerO = HumanPlayer()
		if numberOfPlayers == 0:
			self.PlayerX = self.getComputerPlayer(difficulty)

	def getComputerPlayer(self, difficulty):
		if difficulty == "Hard":
			return ComputerPlayerDifficult()
		elif difficulty =="2":
			return ComputerPlayerDifficult()

		return ComputerPlayerEasy()
