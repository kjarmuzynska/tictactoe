import numpy as np
from board import Board
import players

class Game:
	def __init__(self,N,players):
		self.symbolsToWin = 3
		self.currentTurn = 0
		self._win = False
		self.players = players
		self.board=Board(3)

	def currentSymbol(self):
		if self.currentTurn % 2 == 0:
			return self.board.X;
		return self.board.O;

	def symbolsInLine(self, startPoint, dir, symbol):
		startPoint = np.array(startPoint)
		dir = np.array(dir)

		if self.board.symbolAt(startPoint) != symbol:
			return 0

		suma = 1
		for k in [1,-1]:
			currentDir = dir * k
			point = startPoint
			while True:
				point = point + currentDir
				if not self.board.isPositionInside(point):
					break
				if self.board.symbolAt(point) != symbol:
					break
				suma += 1
		return suma

	def isSymbolWinning(self, index):
		point = self.board.indexToXY(index)
		dirs = [ [1,-1], [1,0], [1,1], [0,1] ]
		symbol = self.board.symbolAt(point)
		for dir in dirs:
			symbols = self.symbolsInLine(point, dir, symbol)
			if symbols >= self.symbolsToWin:
				return True
		return False

	def win(self):
		return self._win

	def draw(self):
		return self.currentTurn >= len(self.board.arr) and not self.win()

	def _doTurn(self, player):
		index = player.chooseMove(self)
		if not self.board.legalMove(index):
			raise ValueError("Illegal move")
		self.board.setSymbolAtIndex(index, self.currentSymbol())
		self._win = self.isSymbolWinning(index)

	def play(self):
		while True:
			for player in self.players:
				self._doTurn(player)
				if self.win() or self.draw():
					return
				self.currentTurn += 1

g = Game(3, [players.PlayerHuman(), players.PlayerHuman()])
g.play()

#print(b.isSymbolWinning(1))
#print(b.symbolsInLine([0,0], [1,0], Board.X))
