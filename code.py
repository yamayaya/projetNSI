import pyxel, random, time
from Utilitaire import Utilitaire
from Game import Game

if __name__ == "__main__":
 pyxel.init(128, 128, title="Nuit du c0de")
 pyxel.run(Game.update, Game.draw)