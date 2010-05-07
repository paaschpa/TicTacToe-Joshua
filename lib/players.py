import time
import random
class HumanPlayer:
	"""HumanPlayer"""
	
	def getMove(self, x_or_o, gameboard, buttonName=""):
		"""PlayerMove""" 
		if buttonName == "":
			cell = self.getraw_input(x_or_o, gameboard.getEmptyCells())
		else:
			cell = buttonName[3:]
		return cell

	def getraw_input(self, x_or_o, availablemoves=[]):
		input = raw_input(x_or_o + " enter your move (%s): " % ", ".join([str(cell) for cell in availablemoves]))
		return int(input)

class ComputerPlayerDifficult:
	
	def getMove(self, x_or_o, gameboard, buttonName=""):
		if buttonName !="":
			return buttonName[3:]

		t0 = time.time()
    		opponent = { "player_o" : "player_x", "player_x" : "player_o" }
    		
		def judge(winner):
			print winner
        		if winner == x_or_o:
            			return +1
        		if winner == None:
            			return 0
        		return -1

    		def evaluateMove(move, player=x_or_o):
        		try:
				gameboard.takeCell(player, move)
				if gameboard.gameOver():
                			return judge(gameboard.winner())
				outcomes = (evaluateMove(next_move, opponent[player]) for next_move in gameboard.getEmptyCells())

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
				gameboard.takeCell("empty", move)

    		moves = [(move, evaluateMove(move)) for move in gameboard.getEmptyCells()]
    		random.shuffle(moves)
    		moves.sort(key = lambda (move, winner): winner)
    		#print "computer move: %0.3f ms" % ((time.time()-t0)*1000)
    		print moves
    		return moves[-1][0]
	

class ComputerPlayerEasy:
	def getMove(self,x_or_o, gameboard, buttonName=""):
		if buttonName != "":
			return buttonName[3:]
		cells = gameboard.getEmptyCells()
		random.shuffle(cells)
		return cells[0]

