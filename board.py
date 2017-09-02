import numpy as np

class Board:
	X = 1
	O = -1

	def __init__(self,N):
		self.n = N
		self.arr = np.zeros(N**2)


	def xyToIndex(self, posXY):
		return  posXY[0] + posXY[1] * self.n

	def indexToXY(self, index):
		return [index % self.n, index // self.n ]

	def legalMove(self, index):
		if index < 0 or index >= len(self.arr):
			return False
		return self.arr[index] == 0

	def setSymbolAtIndex(self, index, value):
		self.arr[ index ] = value

	def setSymbol(self, posXY, value):
		self.arr[ self.xyToIndex(posXY) ] = value

	def isPositionInside(self, posXY):
		if posXY[0] < 0 or posXY[0] >= self.n:
			return False
		if posXY[1] < 0 or posXY[1] >= self.n:
			return False
		return True

	def symbolAt(self, posXY):
		index = self.xyToIndex(posXY)
		return self.arr[ index ]

	def printSymbol(self, value):
		if value == Board.O:
			return ' O '
		elif value == Board.X:
			return ' X '
		return '[ ]'

	def printBoard(self):
		i = 0
		for value in self.arr:
			print(self.printSymbol(value), end='')
			i+=1
			if i%self.n == 0:
				print('')

#b = Board(3, [players.PlayerHuman(), players.PlayerHuman()])
#b.play()

#print(b.isSymbolWinning(1))
#print(b.symbolsInLine([0,0], [1,0], Board.X))
