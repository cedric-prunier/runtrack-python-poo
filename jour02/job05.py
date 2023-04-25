from math import *


class Forme:
    def aire(self):
        return 0


class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return self.radius * self.radius * pi


rectangle = Forme()
print(rectangle.aire())

cercle = Cercle(13)
print(cercle.aire())
