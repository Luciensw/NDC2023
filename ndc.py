import pyxel

# Reste à faire :
# Rajouter un knockback de plus en plsu grand quand un joueur attaque l'autre
# Un joueur doit gagner quand l'autre quitte la zone de combat
# Rajouter l'orientation des personnages

class Joueur():
    def __init__(self, x, y, u, v, right_button, left_button, jump_button, sword_button):
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = 10
        self.h = 16
        self.right_button = right_button
        self.left_button = left_button
        self.jump_button = jump_button
        self.sword_button = sword_button
        self.hp = 5
        self.jump = "Ground"
        self.sword = False
        self.orientation = 1
        self.vector = [0,0]
    
    def update(self):
        if pyxel.btn(self.right_button):
            self.x += 1
            self.orientation = 1
        if pyxel.btn(self.left_button):
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
        if self.sword:
            pyxel.blt(self.x+(self.w*self.orientation), self.y, 0, 0, 48, self.w * self.orientation, self.h, 0)

class Plateforme():
    def __init__(self, x, y, length) -> None:
        self.x = x
        self.y = y
        self.u = 16
        self.v = 25
        self.w = 8
        self.h = 6
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



class Jeu():

    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")
        self.joueur_1 = Joueur(15, 55, 3, 0, pyxel.KEY_D, pyxel.KEY_Q, pyxel.KEY_Z, pyxel.KEY_SPACE)
        self.joueur_2 = Joueur(30, 55, 3, 32, pyxel.KEY_RIGHT, pyxel.KEY_LEFT, pyxel.KEY_UP, pyxel.KEY_RETURN)
        self.plateforme_1 = Plateforme(10, 73, 1)
        self.plateforme_2 = Plateforme(30, 73, 5)
        pyxel.load("theme.pyxres")
        pyxel.playm(0, loop = True)
        pyxel.run(self.update, self.draw)


    def update(self):       
        # self.collision_j1()
        self.joueur_1.update()
        self.joueur_2.update()
        self.collision()

    def collision(self):
        if ((self.joueur_1.x < self.joueur_2.x and self.joueur_1.x+self.joueur_1.w > self.joueur_2.x) or (self.joueur_2.x < self.joueur_1.x and self.joueur_2.x+self.joueur_2.w > self.joueur_1.x)):
            print("test")
            print("toto")

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,0,0,0,128,128,0)
        self.plateforme_1.draw()
        self.plateforme_2.draw()
        self.joueur_1.draw()
        self.joueur_2.draw()


Jeu()