from game import Game
from assessment import *
import tgame



if __name__ == "__main__":
	# director init takes the same arguments as pyglet.window
	p1 = PlayerAssessmentMateusz()
	#p1 = tgame.PlayerHumanT()
	p2 = PlayerAssessmentMateusz([41, 40], 2.0)
	game = Game(10, 5,  [p1, p2])
	game.play()
	tgame.LaunchGame(game)
