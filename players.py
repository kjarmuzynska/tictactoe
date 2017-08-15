import numpy as np
import random as rnd

class Player:
	def chooseMove(self, board):
		return 0

class PlayerHuman(Player):
	def chooseMove(self, board):
		while True:
			board.printBoard()
			x = int(input())
			y = int(input())
			index = board.xyToIndex(x, y)
			if board.legalMove(index):
				return index
			print("Chosen  move is illegal, chose again")

class PlayerRandomAI(Player):
	def chooseMove(self, board):
		maxRange = len(board.arr) - board.currentTurn
		randomField = rnd.randrange(maxRange)

		for i in range(len(board.arr)):
			if not board.legalMove(i):
				continue
			if randomField == 0:
				return i
			randomField -= 1
