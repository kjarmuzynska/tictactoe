#
# cocos2d
# http://cocos2d.org
#
# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from primitives import Circle, Line
from board import Board


import cocos

class TBoard(cocos.layer.Layer):
	is_event_handler = True

	def __init__(self, game):
		super( TBoard, self ).__init__()
		self.schedule( self.step )
		self.board = game.board
		self.cell_size = 60
		self._listeners = []
		self._drawers = []
		self.frameWidth = 2
		self.colorFrame = (0.85, 0.84, 0.89, 0.5)
		self.colorX = (0.18, 0.73, 0.76, 1)
		self.colorO = (0.28, 0.2, 1.0, 1)

		for p in game.players:
			if hasattr(p, 'onClicked'):
				self.addListener(p)

		for p in game.players:
			if hasattr(p, 'drawCell'):
				self._drawers.append(p)

	def addListener(self, listener):
		self._listeners.append(listener)

	def step(self,dt):
		pass

	def boardPositionToPixelCenter(self, posXY):
		x, y=posXY[0], self.board.n-1-posXY[1]
		x_pixels=(0.5+x)*self.cell_size
		y_pixels=(0.5+y)*self.cell_size
		return [x_pixels, y_pixels]

	def drawX(self, posXY):
		[px, py]=self.boardPositionToPixelCenter(posXY)
		for x in [-1, 1]:
			for y in [-1, 1]:
				L=self.cell_size/2*0.8
				line=Line(a=(px+x*L, py+y*L), b=(px,py), z=1, color=self.colorX, stroke=5)
				line.render()


	def drawO(self, posXY):
		[px, py]=self.boardPositionToPixelCenter(posXY)
		circle = Circle(x=px, y=py, z=1, width=self.cell_size*0.9, color=self.colorO, stroke=5)
		circle.render()


	def drawBoard(self):
		n = self.board.n
		for i in range(n-1):
			x=(i+1)*(self.cell_size)
			y=n*(self.cell_size)
			liney = Line(a=(x, 0), b=(x,y), z=1, color=self.colorFrame, stroke=self.frameWidth)
			liney.render()

			linex = Line(a=(0, x), b=(y,x), z=1, color=self.colorFrame, stroke=self.frameWidth)
			linex.render()

	def drawCell(self, x, y):
		posXY=[x, y]
		for drawer in self._drawers:
			drawer.drawCell(posXY, self.boardPositionToPixelCenter(posXY), self.cell_size)

		if self.board.symbolAt(posXY) == self.board.O:
			self.drawO(posXY)
		elif self.board.symbolAt(posXY) == self.board.X:
			self.drawX(posXY)

	def draw( self ):
		self.drawBoard()
		for x in range(self.board.n):
			for y in range(self.board.n):
				self.drawCell(x, y)


	def onClicked(self, posXY):
		for listener in self._listeners:
			listener.onClicked(posXY)
		#board.setSymbol(posXY, Board.O)


	def on_mouse_press (self, x, y, buttons, modifiers):
		posXY = self.Pixels_to_matrix(x, y)
		if self.board.isPositionInside(posXY) and self.board.legalMove(self.board.xyToIndex(posXY)):
			self.onClicked(posXY)
		else:
			print('be')

	def Pixels_to_matrix(self, x, y):
		pos_x=x//self.cell_size
		pos_y=self.board.n-1-y//self.cell_size
		return [pos_x, pos_y]



if __name__ == "__main__":
	# director init takes the same arguments as pyglet.window
	cocos.director.director.init()

	# We create a new layer, an instance of HelloWorld
	board = Board(3)
	board.setSymbol([1,1], Board.O)
	board.setSymbol([2,2], Board.X)

	hello_layer = TBoard(board)

	# A scene that contains the layer hello_layer
	main_scene = cocos.scene.Scene(hello_layer)

	# And now, start the application, starting with main_scene
	cocos.director.director.run(main_scene)

	# or you could have written, without so many comments:
#	  director.run( cocos.scene.Scene( HelloWorld() ) )
