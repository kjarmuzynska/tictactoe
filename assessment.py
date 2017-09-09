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
				self.assessments[x]=-100
		index=np.argmax(self.assessments)
		self.dev=np.std(self.assessments)
		self.average = np.average(self.assessments)
		return index



if __name__ == "__main__":
	player = PlayerRandomAssessment()
	g = Game(3, 3, [player])
	player.chooseMove(g)
