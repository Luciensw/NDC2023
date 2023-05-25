import pyxel

# Reste à faire :
# Rajouter un knockback de plus en plsu grand quand un joueur attaque l'autre
# Un joueur doit gagner quand l'autre quitte la zone de combat
# Rajouter l'orientation des personnages

class Joueur():
    def __init__(self, x, y, u, v, w, h, right, left, jump_button, sword_button):
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.right = right
        self.left = left
        self.jump_button = jump_button
        self.sword_button = sword_button
        self.hp = 5
        self.jump = "Ground"
        self.sword = False
        self.orientation = 1
        self.vector = [0,0]
    
    def update(self):
        if pyxel.btn(self.right):
            self.x += 1
            self.orientation = 1
        if pyxel.btn(self.left):
            self.x -= 1
            self.orientation = -1


        if pyxel.btnr(self.sword_button):
            self.sword = not self.sword
            print("sword")

        if pyxel.btn(self.jump_button) and self.jump == "Ground":
            self.jump = "Jump"
        if self.jump == "Jump":
            self.y -= 2
        if self.y < 30:
            self.jump = "Fall"
        if self.jump == "Fall":
            self.y += 2
        if self.y >= 60:
            self.jump = "Ground"

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.u, self.v, self.w * self.orientation, self.h, 0)




class Jeu():

    '''
    Voici notre jeu : Spartacus bros brawl super ultra ultimate !!!!
    Ce jeu est un smash bros like qui se joue à 2 joueurs.
    LES JOUEURS NE SONT PAS DES OISEAUX.
    Le joueur 1 utilise les touches ZQSD pour se déplacer et la barre espace pour attaquer.
    Le joueur 2 utilise les flèches du clavier pour se déplacer et la touche entrée pour attaquer.
    '''



    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")
        self.joueur_1 = Joueur(15, 60, 2, 0, 6, 8, pyxel.KEY_D, pyxel.KEY_Q, pyxel.KEY_Z, pyxel.KEY_SPACE)
        self.joueur_2 = Joueur(30, 60, 2, 8, 6, 8, pyxel.KEY_RIGHT, pyxel.KEY_LEFT, pyxel.KEY_UP, pyxel.KEY_RETURN)
        pyxel.load("theme.pyxres")
        pyxel.playm(0, loop = True)
        pyxel.run(self.update, self.draw)


    def update(self):       
        # self.collision_j1()
        self.joueur_1.update()
        self.joueur_2.update()
        self.collision()

    def collision(self):
        if (self.joueur_1.x < self.joueur_2.x and self.joueur_1.x+self.joueur_1.w > self.joueur_2.x) or (self.joueur_2.x < self.joueur_1.x and self.joueur_2.x+self.joueur_2.w > self.joueur_1.x):
            print("test")
            print("toto")

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,0,0,0,128,128,0)
        self.joueur_1.draw()
        self.joueur_2.draw()
        # if self.j1sword:
        #     pyxel.blt(self.j1x+5, self.j1y, 0, 8, 24, 5, 8, 0)
        # if self.j2sword:
        #     pyxel.blt(self.j2x-4, self.j2y, 0, 8, 24, -5, 8, 0)







Jeu()