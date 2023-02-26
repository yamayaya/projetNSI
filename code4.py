import pyxel, random, time
if __name__ == "__main__":
 # on rajoute random

 # taille de la fenetre 128x128 pixels
 # ne pas modifier
 pyxel.init(128, 128, title="Nuit du c0de")
 t1 = time.time()
 n = 0
 # position initiale du vaisseau
 # (origine des positions : coin haut gauche)
 vaisseau_x = 60
 vaisseau_y = 60

 # vies
 vies = 4

 # initialisation des tirs
 tirs_liste = []

 # initialisation des ennemis
 ennemis_liste = []

 # initialisation des explosions
 explosions_liste = []


 def vaisseau_deplacement(x, y):
  """déplacement avec les touches de directions"""

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


 def tirs_creation(x, y, tirs_liste):
  """création d'un tir avec la barre d'espace"""

  # btnr pour eviter les tirs multiples
  if pyxel.btnr(pyxel.KEY_SPACE):
   tirs_liste.append([x + 4, y - 4])
  return tirs_liste


 def tirs_deplacement(tirs_liste):
  """déplacement des tirs vers le haut et suppression s'ils sortent du cadre"""

  for tir in tirs_liste:
   tir[1] -= 1
   if tir[1] < -8:
    tirs_liste.remove(tir)
  return tirs_liste


 def ennemis_creation(ennemis_liste):
  """création aléatoire des ennemis"""

  # un ennemi par seconde
  if (pyxel.frame_count % 30 == 0):
   ennemis_liste.append([random.randint(0, 120), 0])
  return ennemis_liste


 def ennemis_deplacement(ennemis_liste):
  """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""

  for ennemi in ennemis_liste:
   ennemi[1] += 1
   if ennemi[1] > 128:
    ennemis_liste.remove(ennemi)
  return ennemis_liste


 def vaisseau_suppression(vies):
  """disparition du vaisseau et d'un ennemi si contact"""

  for ennemi in ennemis_liste:
   if ennemi[0] <= vaisseau_x + 8 and ennemi[1] <= vaisseau_y + 8 and ennemi[0] + 8 >= vaisseau_x and ennemi[
    1] + 8 >= vaisseau_y:
    ennemis_liste.remove(ennemi)
    vies -= 1
    # on ajoute l'explosion
    explosions_creation(vaisseau_x, vaisseau_y)
  return vies


 def ennemis_suppression():
  """disparition d'un ennemi et d'un tir si contact"""

  for ennemi in ennemis_liste:
   for tir in tirs_liste:
    if ennemi[0] <= tir[0] + 1 and ennemi[0] + 8 >= tir[0] and ennemi[1] + 8 >= tir[1]:
     ennemis_liste.remove(ennemi)
     tirs_liste.remove(tir)
     # on ajoute l'explosion
     explosions_creation(ennemi[0], ennemi[1])


 def explosions_creation(x, y):
  """explosions aux points de collision entre deux objets"""
  explosions_liste.append([x, y, 0])


 def explosions_animation():
  """animation des explosions"""
  for explosion in explosions_liste:
   explosion[2] += 1
   if explosion[2] == 12:
    explosions_liste.remove(explosion)

    # =========================================================


 # == UPDATE
 # =========================================================
 def update():
  """mise à jour des variables (30 fois par seconde)"""

  global vaisseau_x, vaisseau_y, tirs_liste, ennemis_liste, vies, explosions_liste

  # mise à jour de la position du vaisseau
  vaisseau_x, vaisseau_y = vaisseau_deplacement(vaisseau_x, vaisseau_y)

  # creation des tirs en fonction de la position du vaisseau
  tirs_liste = tirs_creation(vaisseau_x, vaisseau_y, tirs_liste)

  # mise a jour des positions des tirs
  tirs_liste = tirs_deplacement(tirs_liste)

  # creation des ennemis
  ennemis_liste = ennemis_creation(ennemis_liste)

  # mise a jour des positions des ennemis
  ennemis_liste = ennemis_deplacement(ennemis_liste)

  # suppression des ennemis et tirs si contact
  ennemis_suppression()

  # suppression du vaisseau et ennemi si contact
  vies = vaisseau_suppression(vies)

  # evolution de l'animation des explosions
  explosions_animation()

  # =========================================================


 # == DRAW
 # =========================================================
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
    if t2-t1 >= 120 and n == 0:
     pyxel.rect(ennemi[0], ennemi[1], 16, 16, 8)
    
    pyxel.rect(ennemi[0], ennemi[1], 8, 8, 8)

   # explosions (cercles de plus en plus grands)
   for explosion in explosions_liste:
    pyxel.circb(explosion[0] + 4, explosion[1] + 4, 2 * (explosion[2] // 4), 8 + explosion[2] % 3)

    # sinon: GAME OVER
  else:

   pyxel.text(50, 64, 'GAME OVER', 7)


 pyxel.run(update, draw)