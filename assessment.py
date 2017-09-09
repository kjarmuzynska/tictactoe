from board import Board
from players import Player
import random
from game import Game
import numpy as np

class PlayerAssessment(Player):
	def activate(self, game):
		self.board = game.board
		self.assessments = np.copy(self.board.arr)
		super().activate(game)


class PlayerRandomAssessment(PlayerAssessment):

	def chooseMove(self, game):
		for x in range(len(self.assessments)):
			if game.board.legalMove(x):
				los=random.random()
				self.assessments[x]+=los
			else:
				self.assessments[x]=-100
		index=np.argmax(self.assessments)
		return index



if __name__ == "__main__":
	player = PlayerRandomAssessment()
	g = Game(3, 3, [player])
	player.chooseMove(g)
