#!/usr/bin/python

"""
__version__ = "$Revision: 1.3 $"
__date__ = "$Date: 2004/04/14 02:38:47 $"
"""
import sys
from PythonCard import model
from tictactoe import TicTacToe

class MyBackground(model.Background):

	def on_initialize(self, event):
		self.playfieldButtons = []
		for i in range(9):
			self.playfieldButtons.append(self.components["btn" + str(i)])
		self.tictactoe = TicTacToe()
		self.currentPlayer = self.tictactoe.PlayerX
		self.x_or_o = "player_x"
		self.doComputerMove()

	def on_btnYes_mouseClick(self, event):
		for i in range(0,9):
			button = self.components["btn" + str(i)]
			button.visible = True

	def isplayfieldButton(self, button):
		if button in self.playfieldButtons:
			return True
		else:
			return False
	
	def on_mouseUp(self, event):
		if self.isplayfieldButton(event.target):
			button = event.target
			self.makeMove(button)
			event.skip()
		else:
			event.skip()

	def makeMove(self,button):
		self.tictactoe.gameboard.takeCell(self.x_or_o, self.getPlayerMove(self.x_or_o, button.name))
		button.label = self.x_or_o
		self.switchPlayers()
		self.doComputerMove()

	def getPlayerMove(self, x_or_o, buttonName=""):
		if buttonName != "":
			return self.currentPlayer.getMove(x_or_o, self.tictactoe.gameboard, buttonName)
		return self.currentPlayer.getMove(x_or_o, self.tictactoe.gameboard)
	
	def switchPlayers(self):
		if self.currentPlayer == self.tictactoe.PlayerX:
			self.currentPlayer = self.tictactoe.PlayerO
			self.x_or_o = "player_o"
		else:
			self.currentPlayer = self.tictactoe.PlayerX
			self.x_or_o = "player_x"

	def doComputerMove(self):
		if self.currentPlayer.__class__.__name__.__contains__("Computer"):
			cell = self.currentPlayer.getMove(self.x_or_o, self.tictactoe.gameboard)
			print "computer is ", cell
			self.makeMove(self.components["btn" + str(cell)])

if __name__ == '__main__':
	app = model.Application(MyBackground)
	app.MainLoop()
