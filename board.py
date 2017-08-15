import numpy as np
import players

class Board:
	X = 1
	O = -1

	def __init__(self,N,players):
		self.symbolsToWin = 3
		self.currentTurn = 0
		self.n = N
		self._win = False
		self.arr = np.zeros(N**2)
		self.players = players

	def xyToIndex(self, x, y):
		return  x + y * self.n

	def indexToXY(self, index):
		return [index % self.n, index // self.n ]

	def legalMove(self, index):
		if index < 0 or index >= len(self.arr):
			return False
		return self.arr[index] == 0

	def setSymbolAtIndex(self, index, value):
		self.arr[ index ] = value

	def setSymbol(self, x, y, value):
		self.arr[ self.xyToIndex(x,y) ] = value

	def isPositionInside(self, posXY):
		if posXY[0] < 0 or posXY[0] >= self.n:
			return False
		if posXY[1] < 0 or posXY[1] >= self.n:
			return False
		return True

	def symbolAt(self, posXY):
		index = self.xyToIndex(posXY[0], posXY[1])
		return self.arr[ index ]

	def currentSymbol(self):
		if self.currentTurn % 2 == 0:
			return Board.X;
		return Board.O;

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


	def symbolsInLine(self, startPoint, dir, symbol):
		startPoint = np.array(startPoint)
		dir = np.array(dir)

		if self.symbolAt(startPoint) != symbol:
			return 0

		suma = 1
		for k in [1,-1]:
			currentDir = dir * k
			point = startPoint
			while True:
				point = point + currentDir
				if not self.isPositionInside(point):
					break
				if self.symbolAt(point) != symbol:
					break
				suma += 1

		return suma

	def isSymbolWinning(self, index):
		point = self.indexToXY(index)
		dirs = [ [1,-1], [1,0], [1,1], [0,1] ]
		symbol = self.symbolAt(point)
		for dir in dirs:
			symbols = self.symbolsInLine(point, dir, symbol)
			if symbols >= self.symbolsToWin:
				return True
		return False

	def win(self):
		return self._win

	def draw(self):
		return self.currentTurn >= len(self.arr) and not self.win()

	def _doTurn(self, player):
		index = player.chooseMove(self)
		if not self.legalMove(index):
			raise ValueError("Illegal move")
		self.setSymbolAtIndex(index, self.currentSymbol())
		self._win = self.isSymbolWinning(index)

	def play(self):
		while True:
			for player in self.players:
				self._doTurn(player)
				if self.win() or self.draw():
					return
				self.currentTurn += 1

b = Board(3, [players.PlayerHuman(), players.PlayerHuman()])
b.play()

#print(b.isSymbolWinning(1))
#print(b.symbolsInLine([0,0], [1,0], Board.X))
