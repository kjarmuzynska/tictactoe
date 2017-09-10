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



	def add_rank_line(self, move, enemy):
		#linia, legalny, odpowiednia odleglosc
		#jhak gdzie zagra to wywalamy wage?

		self.last_moves(game)
		point = self.board.indexToXY(move)
		dirs = [ [1,-1], [1,0], [1,1], [0,1] ]
		new_dirs=[]
		for dir in dirs:
			for i in [2, 3, 4, 5]:
				new_dirs.append(np.array(dir)*i)

		symbol = self.board.symbolAt(point)
		for n_dir in new_dirs:
			symbol = self.symbolsInLine(point, n_dir, symbol)

		pass


class PlayerAssessmentMateusz(PlayerAssessment):
	def __init__(self):
		super().__init__()
		#self.symbolsWeights = [2.1, 2]
		#self.emptyWeight = 1.1
		self.symbolsWeights = [4.1, 4]
		self.emptyWeight = 1.1

	def chooseMove(self, game):
		self.my_symbol = game.currentSymbol()
		self.enemy_symbol = game.currentOppositeSymbol()

		for i in range(len(self.board.arr)):
			v = self.board.arr[i]
			if v != 0:
				self.assessments[i] = 0
				continue
			xy = self.board.indexToXY(i)
			self.assessments[i] = self.assessField(i, xy, v)

		return self.decision_assessment()


	def assessField(self, index, posXY, value):
		dirs = [ [1,-1], [1,0], [1,1], [0,1] ]

		value = 0
		for dir in dirs:
			v1 = self.assessAxis(posXY, dir, self.my_symbol, 0)
			v2 = self.assessAxis(posXY, dir, self.enemy_symbol, 1)
			value += max(v1, v2) #TODO

		return value

	def assessAxis(self, start, dir, symbol, enemy):
		start = np.array([int(x) for x in start])
		dir = np.array(dir)

		value = self.emptyWeight
		for k in [1,-1]:
			currentDir = dir * k
			point = start
			while True:
				point = point + currentDir
				if not self.board.isPositionInside(point):
					break

				symbol_at = self.board.symbolAt(point)
				if symbol_at == symbol:
					value *= self.symbolsWeights[enemy]
				elif symbol_at == 0:
					value *= self.emptyWeight
				else:
					break

		return value


if __name__ == "__main__":
	player = PlayerRandomAssessment()
	g = Game(3, 3, [player])
	player.chooseMove(g)
