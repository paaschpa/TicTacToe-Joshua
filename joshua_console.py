import time, random

class TicTacToe:

	def __init__(self, numberOfPlayers=1):
		self.emptyGameboard()
		self.Player_X = self.askPlayer
		self.Player_O = self.computerPlayer

		if numberOfPlayers == 0:
			self.Player_X = self.computerPlayer
		if numberOfPlayers == 2:
			self.Player_O = self.askPlayer 

		self.difficultyselection = "2"

	def emptyGameboard(self):
		self.gameboard = ["empty"]*9

	#printGameboard and addspaces are my 
	#attempt at UI/Graphic Design.
	#It's testable. That is all.
	def printGameboard(self, board):
		print " " 
		print self.addspaces(board[0]),"||",self.addspaces(board[1]),"||",self.addspaces(board[2])
		print "-" * 34
		print self.addspaces(board[3]),"||",self.addspaces(board[4]),"||",self.addspaces(board[5])
		print "-" * 34
		print self.addspaces(board[6]),"||",self.addspaces(board[7]),"||",self.addspaces(board[8])
		print " "

	def addspaces(self, cell):
		times = 0
		if len(cell) < 10:
			times = 10-len(cell)
		spaces = " " * times
		return cell + spaces	

	def takesCell(self, player, space):
		self.gameboard[space] = player
	
	def askPlayer(self, x_or_o):
		cell = self.getraw_input(x_or_o)
    		while cell not in self.possibleMoves():
        		print "Sorry, '%s' is not a valid move. Please try again." % cell
        		cell = self.getraw_input(x_or_o) 
    		self.takesCell(x_or_o, int(cell))
	
	def getraw_input(self, x_or_o):
		input = raw_input(x_or_o + " enter your move (%s): " % ", ".join([str(cell) for cell in self.possibleMoves()]))
		return int(input)

	#I totally lifted this from http://en.literateprograms.org/Tic_Tac_Toe_(Python)
	#I added a little functionality --checkForWinningMove--
	#I'm going to attempt to write some tests and refactor it. At minimum, I need to verify it always wins
	#but I'm not sure how to go about it...math and thinking are hard.
	def computerPlayer(self, x_or_o):
		if self.difficultyselection == "1":
			moves = self.possibleMoves()
			random.shuffle(moves)
			self.takesCell(x_or_o, moves[0])
			return

		winningMove = self.checkForWinningMove(x_or_o)
		if winningMove != None:
			self.takesCell(x_or_o, winningMove)
			return
		
		t0 = time.time()
    		opponent = { "player_o" : "player_x", "player_x" : "player_o" }
    		
		def judge(winner):
        		if winner == x_or_o:
            			return +1
        		if winner == None:
            			return 0
        		return -1

    		def evaluateMove(move, player=x_or_o):
        		try:
				self.takesCell(player, move)
				if self.gameOver():
                			return judge(self.winner())
				outcomes = (evaluateMove(next_move, opponent[player]) for next_move in self.possibleMoves())

				if player == x_or_o:
                			#return min(outcomes)
               			 	min_element = 1
                			for o in outcomes:
                    				if o == -1:
                        				return o
	                    			min_element = min(o,min_element)
               				return min_element
            			else:
                			#return max(outcomes)
                				max_element = -1
                				for o in outcomes:
                    					if o == +1:
                        					return o
                    					max_element = max(o,max_element)
                				return max_element

		        finally:
				self.takesCell("empty",move)

    		moves = [(move, evaluateMove(move)) for move in self.possibleMoves()]
    		random.shuffle(moves)
    		moves.sort(key = lambda (move, winner): winner)
    		print "computer move: %0.3f ms" % ((time.time()-t0)*1000)
    		print moves
    		self.takesCell(x_or_o, moves[-1][0])
	
	def possibleMoves(self):
		return [i for i in range(0, len(self.gameboard))
	            if self.gameboard[i] == "empty"]
	
	def checkForWinningMove(self, x_or_o):
		for move in self.possibleMoves():
			self.takesCell(x_or_o, move)
			if self.winner():
				return move
			self.takesCell("empty",move)
		return None

	
    	def winner(self):
        	winningLists = [[0,1,2],[3,4,5],[6,7,8], # vertical
                	        [0,3,6],[1,4,7],[2,5,8], # horizontal
                        	[0,4,8],[2,4,6]]         # diagonal
        	for winningList in winningLists:
			if self.gameboard[winningList[0]] != "empty" and self.winningCombination([self.gameboard[cell] for cell in winningList]):
                		return self.gameboard[winningList[0]]

	def winningCombination(self, list):
		return list[0] == list[1] == list [2]
	
	def gameOver(self):
		if len(self.possibleMoves()) == 0:
			return True
		if self.winner():
			return True
		return False

def startGame():

	print "Greetings Professor Falken"
	print "Shall we play a game?"
	print "1: Tic Tac Toe"
	print "2: Chess"
	print "3: Global Thermonuclear War"
	print " "
	
	gameselection = raw_input("Make a selection: (1,2,3)")
	while gameselection != str(1):
		if gameselection ==  str(3):
			print "Sorry Matthew Broderick and Ally Sheedy are not available to save the world at this time." 
		print "Wouldn't you prefer a nice game of tic tac toe?"
		gameselection = raw_input("Make a selection: (1,2,3)")	

	playerselection = raw_input("How many human players? (0,1,2)")
	while int(playerselection) not in range(0,3):
		playerselection = raw_input("How many human players? (1,2)")
		
	difficultyselection = "2"
	if playerselection == "1":
		difficultyselection = raw_input("Would you like Easy or Hard? (1,2)")
		while int(difficultyselection) not in range(1,3):
			difficultyselection = raw_input("Would you like Easy or Hard (1,2)")

	
	tictactoe = TicTacToe(int(playerselection))
    	tictactoe.printGameboard(tictactoe.gameboard)
	tictactoe.difficultyselection = difficultyselection

	turn = 1
   	while True:
       		print "%i. turn" % turn
		
		tictactoe.Player_X("player_x")
		tictactoe.printGameboard(tictactoe.gameboard)
		
		if endingMove(tictactoe): 
       			break
       		
		tictactoe.Player_O("player_o")	
		tictactoe.printGameboard(tictactoe.gameboard)
       		if endingMove(tictactoe): 
       			break
       		turn += 1
		
	tictactoe.printGameboard(tictactoe.gameboard)

	if tictactoe.winner():
       		print tictactoe.winner() + " my primary goal is to win!" 
	else:    
       		print "A strange game. The only winning move is not to play. How about a nice game of chess?"

def endingMove(tictactoe):
	if tictactoe.gameOver():
		return True
	if tictactoe.winner() != None:
		return True
	return False
		

if __name__ == "__main__":
	startGame()
