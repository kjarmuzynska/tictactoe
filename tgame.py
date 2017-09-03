import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from primitives import Circle, Line

from game import Game
from board import Board
import players
from tboard import TBoard

import cocos


class PlayerHumanT(players.Player):
	def __init__(self):
		self.selectedPosition = None

	def chooseMove(self, game):
		self.game = game
		if not self.selectedPosition:
			return -1
		index = game.board.xyToIndex(self.selectedPosition)
		self.selectedPosition = None
		return index


	def onClicked(self, posXY):
		print("Player wants to move %s %s " %(posXY[0], posXY[1]) )
		if not self.game:
			return
		self.selectedPosition = posXY
		self.game.play()
		self.game = None

if __name__ == "__main__":
	# director init takes the same arguments as pyglet.window
	cocos.director.director.init()

	# We create a new layer, an instance of HelloWorld
	player1 = PlayerHumanT()
	player2 = PlayerHumanT()
	#game = Game(3, [players.PlayerRandomAI(), player1])
	game = Game(3, [player1, player2])
	game.play()

	tboard = TBoard(game.board)
	tboard.addListener(player1)
	tboard.addListener(player2)

	# A scene that contains the layer hello_layer
	main_scene = cocos.scene.Scene(tboard)

	# And now, start the application, starting with main_scene
	cocos.director.director.run(main_scene)
