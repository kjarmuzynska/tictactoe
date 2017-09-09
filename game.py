import numpy as np
from board import Board
import players

class Game:
	def __init__(self,N,W,players):
		self.symbolsToWin = W
		self.currentTurn = 0
		self._win = False
		self.players = players
		self.board=Board(N)
		self.story=[]
		for i in self.players:
			i.activate(self)

		self.currentPlayer = 0

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

		if index == -1: #jeśli gracz zwrócił -1, znaczy, że nie jest gotowy teraz żeby podjąć decyzję, i zrobi to później
			return False
		if not self.board.legalMove(index):
			raise ValueError("Illegal move")
		symbol = self.currentSymbol()
		self.board.setSymbolAtIndex(index, symbol)
		self.story.append((index, symbol))
		self._win = self.isSymbolWinning(index)
		return True

	def play(self):
		while True:
			player = self.players[self.currentPlayer]

			if not self._doTurn(player):
				return #jeśli doTUrn zwróciło false, znaczy że gracz się namyśla, i gra jest wstrzymana aż nie wybierze ruchu
			if self.win() or self.draw():
				return
			self.currentTurn += 1
			self.currentPlayer = (self.currentPlayer + 1) % len(self.players)

if __name__ == "__main__":
	g = Game(3, 3, [players.PlayerHuman(), players.PlayerHuman()])
	g.play()


#print(b.isSymbolWinning(1))
#print(b.symbolsInLine([0,0], [1,0], Board.X))
