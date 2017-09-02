import numpy as np
import random as rnd

class Player:
	def chooseMove(self, game):
		return 0

class PlayerHuman(Player):
	def chooseMove(self, game):
		while True:
			game.board.printBoard()
			x = int(input())
			y = int(input())
			index = game.board.xyToIndex([x, y])
			if game.board.legalMove(index):
				return index
			print("Chosen  move is illegal, chose again")

class PlayerRandomAI(Player):
	def chooseMove(self, game):
		maxRange = len(game.board.arr) - game.board.currentTurn
		randomField = rnd.randrange(maxRange)

		for i in range(len(game.board.arr)):
			if not game.board.legalMove(i):
				continue
			if randomField == 0:
				return i
			randomField -= 1
