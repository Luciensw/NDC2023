import pyxel




class Jeu():




    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")
        self.j1x = 15
        self.j1y = 60
        self.j2x = 30
        self.j2y = 60
        self.jumpj1 = "Ground"
        self.jumpj2 = "Ground"
        self.j1hp = 5
        self.j2hp = 5
        self.j1sword = False
        self.j2sword = False
        pyxel.load("theme.pyxres")
        pyxel.music(0)
        pyxel.run(self.update, self.draw)






    def update(self):


        # Déplacement joueur 1
        if pyxel.btn(pyxel.KEY_D):
            self.j1x += 1
        if pyxel.btn(pyxel.KEY_Q):
            self.j1x -= 1
        if pyxel.btn(pyxel.KEY_SPACE):
            not self.j1sword


        # Déplacement joueur 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.j2x += 1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.j2x -= 1
        if pyxel.btn(pyxel.KEY_RETURN):
            not self.j2sword


        # Saut et gravité
        if pyxel.btn(pyxel.KEY_UP) and self.jumpj2 == "Ground":
            self.jumpj2 = "Jump"
        if self.jumpj2 == "Jump":
            self.j2y -= 2
        if self.j2y < 30:
            self.jumpj2 = "Fall"
        if self.jumpj2 == "Fall":
            self.j2y += 2
        if self.j2y >= 60:
            self.jumpj2 = "Ground"

        if pyxel.btn(pyxel.KEY_Z) and self.jumpj1 == "Ground":
            self.jumpj1 = "Jump"
        if self.jumpj1 == "Jump":
            self.j1y -= 2
        if self.j1y < 30:
            self.jumpj1 = "Fall"
        if self.jumpj1 == "Fall":
            self.j1y += 2
        if self.j1y >= 60:
            self.jumpj1 = "Ground"


    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.j1x, self.j1y, 0, 0, 0, 8, 8, 0)
        pyxel.blt(self.j2x, self.j2y, 0, 0, 8, -8, 8, 0)







Jeu()