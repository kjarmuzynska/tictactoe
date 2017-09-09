from game import Game
from assessment import *
import tgame



if __name__ == "__main__":
	# director init takes the same arguments as pyglet.window
	game = Game(10, 5,  [tgame.PlayerHumanT(), PlayerRandomAssessment()])
	game.play()
	tgame.LaunchGame(game)
