import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

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
		index = self.game.board.xyToIndex(posXY)
		#głupie rozwiązanie, poprawić
		if not self.game.board.legalMove(index):
			return

		self.selectedPosition = posXY

		self.game.play()
		self.game = None

def LaunchGame(game):
	# director init takes the same arguments as pyglet.window
	cocos.director.director.init(width=1024, height=768)
	tboard = TBoard(game)
	# A scene that contains the layer hello_layer
	main_scene = cocos.scene.Scene(tboard)
	# And now, start the application, starting with main_scene
	cocos.director.director.run(main_scene)

if __name__ == "__main__":
	#game = Game(3, [players.PlayerRandomAI(), player1])
	game = Game(15, 5,  [PlayerHumanT(), PlayerHumanT()])
	game.play()
	LaunchGame(game)
