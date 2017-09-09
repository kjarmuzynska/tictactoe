from board import Board
from players import Player
import random
from game import Game
import numpy as np
from primitives import Circle, Line

class PlayerAssessment(Player):
	def __init__(self):
		self.dev, self.average= 0, 0

	def activate(self, game):
		self.board = game.board
		self.assessments = np.copy(self.board.arr)
		super().activate(game)

	def decision_assessment(self):
		index=np.argmax(self.assessments)
		self.dev=np.std(self.assessments)
		self.average = np.average(self.assessments)
		return index


	def drawCell(self, posXY, pixelCenter, cell_size):
		x=self.board.xyToIndex(posXY)
		v=self.assessments[x]
		if v<=-100:
			return
		if not self.dev:
			return
		stand=(v-self.average)/self.dev
		circle = Circle(x=pixelCenter[0], y=pixelCenter[1], z=1, width=cell_size*0.5, color=(stand, 0, 0, 0.98*stand), stroke=5)
		circle.render()



class PlayerRandomAssessment(PlayerAssessment):

	def chooseMove(self, game):
		for x in range(len(self.assessments)):
			if game.board.legalMove(x):
				los=random.random()
				self.assessments[x]+=los
			else:
				self.assessments[x]=0
		return self.decision_assessment()



class PlayerAssessmentRank(PlayerAssessment):

	def chooseMove(self, game):
		self.my_symbol = game.currentSymbol()
		self.last_moves(game)
		return self.decision_assessment()

	def last_moves(self, game):
		try:
			self.add_rank_line(self.game.story[-1], 1)
			self.add_rank_line(self.game.story[-2], 0)
		except:
			pass






	def add_rank_line(self, move, enemy):
		#linia, legalny, odpowiednia odleglosc
		self.last_moves(game)
		point = self.board.indexToXY(index)
		dirs = [ [1,-1], [1,0], [1,1], [0,1] ]
		new_dirs=[]
		for dir in dirs:
			for i in [2, 3, 4, 5]:
				new_dirs.append(np.array(dir)*i)

		symbol = self.board.symbolAt(point)
		for dir in dirs:
			symbol = self.symbolsInLine(point, dir, symbol)

		pass



if __name__ == "__main__":
	player = PlayerRandomAssessment()
	g = Game(3, 3, [player])
	player.chooseMove(g)
