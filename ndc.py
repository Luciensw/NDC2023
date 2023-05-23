import pyxel
class Jeu():
    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")
        self.j1x = 15
        self.j1y = 60
        self.j2x = 30
        self.j2y = 60
        pyxel.run(self.update, self.draw)
    def update(self):
        # Déplacement joueur 1
        j1x = 0
        if pyxel.btn(pyxel.KEY_D):
            j1x += 1
        if pyxel.btn(pyxel.KEY_Q):
            j1x -= 1
        self.j1x += j1x
        # Déplacement joueur 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.j2x += 1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.j2x -= 1
        # Saut et gravité
        j2y = 0
        if pyxel.btn(pyxel.KEY_SPACE):
            j2y = 1
        if self.j2y < 128:
            self.j2y += j2y
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.j1x,self.j1y,8,8,8)
        pyxel.rect(self.j2x,self.j2y,8,8,5)
Jeu()