import pyxel
from random import randint

# Reste à faire :
# Rajouter un knockback de plus en plus grand quand un joueur attaque l'autre
# Un joueur doit gagner quand l'autre quitte la zone de combat
# Rajouter l'orientation des personnages

class Objet():
    def __init__(self, x, y, u, v, w, h, parent) -> None:
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.parent = parent
    def collision(self, objet):
        if ((self.x < objet.x and self.x+self.w > objet.x) or (objet.x < self.x and objet.x+objet.w > self.x)) and ((self.y < objet.y and self.y+self.h > objet.y) or (objet.y < self.y and objet.y+objet.h > self.y)):
            print("test")
            print("toto")

class Joueur(Objet):
    def __init__(self, x, y, u, v, right_button, left_button, jump_button, sword_button, parent):
        Objet.__init__(self, x, y, u, v, 10, 16, parent)
        self.right_button = right_button
        self.left_button = left_button
        self.jump_button = jump_button
        self.sword_button = sword_button
        self.hp = 5
        self.jump = "Ground"
        self.sword = None
        self.orientation = 1
    
    def update(self):
        if pyxel.btn(self.right_button):
            self.x += 1
            self.orientation = 1
        if pyxel.btn(self.left_button):
            self.x -= 1
            self.orientation = -1


        if pyxel.btnr(self.sword_button) and not self.sword:
            self.sword = Sword(self.x + (self.w * self.orientation), self. y, 0, 48, 16 * self.orientation, 16, self)
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
        if self.sword:
            self.sword.update()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.u, self.v, self.w * self.orientation, self.h, 0)
        if self.sword:
            self.sword.draw()

class Plateforme(Objet):
    def __init__(self, x, y, length, parent) -> None:
        Objet.__init__(self, x, y, 16, 25, 8, 6, parent)
        self.length = length
    def draw(self):
        if self.length == 1:
            pyxel.blt(self.x, self.y, 0, self.u+3*8, self.v, self.w, self.h, 0)
        if self.length == 2:
            pyxel.blt(self.x, self.y, 0, self.u, self.v, self.w, self.h, 0)
            pyxel.blt(self.x+8, self.y, 0, self.u+2*8, self.v, self.w, self.h, 0)
        if self.length >= 3:
            pyxel.blt(self.x, self.y, 0, self.u, self.v, self.w, self.h, 0)
            for i in range(self.length -2):
                pyxel.blt(self.x+((i+1)*8), self.y, 0, self.u+8, self.v, self.w, self.h, 0)
            pyxel.blt(self.x+((self.length-1)*8), self.y, 0, self.u+2*8, self.v, self.w, self.h, 0)

class Sword(Objet):
    def __init__(self, x, y, u, v, w, h, parent) -> None:
        super().__init__(x, y, u, v, w, h, parent)
        self.time = pyxel.frame_count
    def update(self):
        if pyxel.frame_count - self.time >= 3:
            self.parent.sword = None
    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.u, self.v, self.w, self.h, 0)


class Jeu():

    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")
        self.joueur_1 = Joueur(15, 55, 3, 0, pyxel.KEY_D, pyxel.KEY_Q, pyxel.KEY_Z, pyxel.KEY_SPACE, self)
        self.joueur_2 = Joueur(30, 55, 3, 32, pyxel.KEY_RIGHT, pyxel.KEY_LEFT, pyxel.KEY_UP, pyxel.KEY_RETURN, self)
        self.plateforme_1 = Plateforme(10, 73, 1, self)
        self.plateforme_2 = Plateforme(30, 73, 5, self)
        self.score = [0, 0]
        pyxel.load("theme.pyxres")
        pyxel.playm(0, loop = True)
        pyxel.run(self.update, self.draw)


    def update(self):       
        self.joueur_1.update()
        self.joueur_2.update()
        self.joueur_1.collision(self.joueur_2)
        if self.joueur_2.sword:
            if self.joueur_1.collision(self.joueur_2.sword):
                self.joueur_1.hp -= 1
                print(self.joueur_1.hp)

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,0,0,0,128,128,0)
        self.plateforme_1.draw()
        self.plateforme_2.draw()
        self.joueur_1.draw()
        self.joueur_2.draw()
        pyxel.text(2, 2, str(self.score[0]), 0)
        pyxel.text(pyxel.width-5, 2, str(self.score[1]), 0)



Jeu()