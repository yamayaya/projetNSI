import pyxel, random

class Utilitaire:
    vaisseau_x = 60
    vaisseau_y = 60

    vies = 4

    tirs_liste = []

    ennemis_liste = []

    explosions_liste = []

    @staticmethod
    def vaisseau_deplacement(x, y):
        if pyxel.btn(pyxel.KEY_RIGHT):
            if (x < 120):
                x = x + 1
        if pyxel.btn(pyxel.KEY_LEFT):
            if (x > 0):
                x = x - 1
        if pyxel.btn(pyxel.KEY_DOWN):
            if (y < 120):
                y = y + 1
        if pyxel.btn(pyxel.KEY_UP):
            if (y > 0):
                y = y - 1
        return x, y

    @staticmethod
    def tirs_creation(x, y, tirs_liste):
        if pyxel.btnr(pyxel.KEY_SPACE):
            tirs_liste.append([x + 4, y - 4])
        return tirs_liste

    @staticmethod
    def tirs_deplacement(tirs_liste):
        for tir in tirs_liste:
            tir[1] -= 1
            if tir[1] < -8:
                tirs_liste.remove(tir)
        return tirs_liste

    @staticmethod
    def ennemis_creation(ennemis_liste):
        if (pyxel.frame_count % 30 == 0):
            ennemis_liste.append([random.randint(0, 120), 0])
        return ennemis_liste

    @staticmethod
    def ennemis_deplacement(ennemis_liste):
        for ennemi in ennemis_liste:
            ennemi[1] += 1
            if ennemi[1] > 128:
                ennemis_liste.remove(ennemi)
        return ennemis_liste

    @staticmethod
    def vaisseau_suppression(vies):
        for ennemi in Utilitaire.ennemis_liste:
            if ennemi[0] <= Utilitaire.vaisseau_x + 8 and ennemi[1] <= Utilitaire.vaisseau_y + 8 and ennemi[0] + 8 >= Utilitaire.vaisseau_x and ennemi[1] + 8 >= Utilitaire.vaisseau_y:
                Utilitaire.ennemis_liste.remove(ennemi)
                vies -= 1
                Utilitaire.explosions_creation(Utilitaire.vaisseau_x, Utilitaire.vaisseau_y)
        return vies

    @staticmethod
    def ennemis_suppression():
        """disparition d'un ennemi et d'un tir si contact"""

        for ennemi in Utilitaire.ennemis_liste:
            for tir in Utilitaire.tirs_liste:
                if ennemi[0] <= tir[0] + 1 and ennemi[0] + 8 >= tir[0] and ennemi[1] + 8 >= tir[1]:
                    Utilitaire.ennemis_liste.remove(ennemi)
                    Utilitaire.tirs_liste.remove(tir)
                    # on ajoute l'explosion
                    Utilitaire.explosions_creation(ennemi[0], ennemi[1])

    @staticmethod
    def explosions_creation(x, y):
        """explosions aux points de collision entre deux objets"""
        Utilitaire.explosions_liste.append([x, y, 0])

    @staticmethod
    def explosions_animation():
        """animation des explosions"""
        for explosion in Utilitaire.explosions_liste:
            explosion[2] += 1
            if explosion[2] == 12:
                Utilitaire.explosions_liste.remove(explosion)