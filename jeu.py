import pyxel
class Jeu():
    def __init__(self):
        pyxel.init(128, 128, title="NDC 2023")
        pyxel.run(self.update, self.draw)
    def update(self):
        pass
    def draw(self):
        pass