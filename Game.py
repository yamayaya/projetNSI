import pyxel, random
from Utilitaire import Utilitaire
import time
class Game:
    t = 0
    # =========================================================
    # == UPDATE
    # =========================================================
    @staticmethod
    def update():
        """mise à jour des variables (30 fois par seconde)"""

        global vaisseau_x, vaisseau_y, tirs_liste, ennemis_liste, vies, explosions_liste

        # mise à jour de la position du vaisseau
        vaisseau_x, vaisseau_y = Utilitaire.vaisseau_deplacement(vaisseau_x, vaisseau_y)

        # creation des tirs en fonction de la position du vaisseau
        tirs_liste = Utilitaire.tirs_creation(vaisseau_x, vaisseau_y, tirs_liste)

        # mise a jour des positions des tirs
        tirs_liste = Utilitaire.tirs_deplacement(tirs_liste)

        # creation des ennemis
        ennemis_liste = Utilitaire.ennemis_creation(ennemis_liste)

        # mise a jour des positions des ennemis
        ennemis_liste = Utilitaire.ennemis_deplacement(ennemis_liste)

        # suppression des ennemis et tirs si contact
        Utilitaire.ennemis_suppression()

        # suppression du vaisseau et ennemi si contact
        vies = Utilitaire.vaisseau_suppression(vies)

        # evolution de l'animation des explosions
        Utilitaire.explosions_animation()


        # =========================================================

    # == DRAW
    # =========================================================
    @staticmethod
    def draw():
        """création des objets (30 fois par seconde)"""

        # vide la fenetre
        pyxel.cls(0)

        # si le vaisseau possede des vies le jeu continue
        if vies > 0:

            # affichage des vies
            pyxel.text(5, 5, 'VIES:' + str(vies), 7)

            # vaisseau (carre 8x8)
            pyxel.rect(vaisseau_x, vaisseau_y, 8, 8, 1)

            # tirs
            for tir in tirs_liste:
                pyxel.rect(tir[0], tir[1], 1, 4, 10)

            # ennemis
            t2 = time.time()
            for ennemi in ennemis_liste:
                if t2-Game.t >=120:
                    pyxel.rect(ennemi[0], ennemi[1], 16, 16, 10)


                pyxel.rect(ennemi[0], ennemi[1], 8, 8, 8)

            # explosions (cercles de plus en plus grands)
            for explosion in explosions_liste:
                pyxel.circb(explosion[0] + 4, explosion[1] + 4, 2 * (explosion[2] // 4), 8 + explosion[2] % 3)

                # sinon: GAME OVER
        else:

            pyxel.text(50, 64, 'GAME OVER', 7)

    @staticmethod
    def run():
        pyxel.run(Game.update, Game.draw)

    @staticmethod
    def init():
        pyxel.init(128, 128, title="Nuit du c0de")
        Game.t = time.time()
