from abc import ABC, abstractmethod
import math

class ColorMixin:
    def __init__(self, couleur="blanc"):
        self.couleur = couleur

    def afficher_couleur(self):
        print(f"[{self.couleur}] {self}")

class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} (aire = {self.aire():.2f})"


class Cercle(ColorMixin,Forme):
    def __init__(self, rayon , couleur = "rouge"):
        ColorMixin.__init__(self,couleur)
        self.rayon = rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)


class Rectangle( ColorMixin,Forme):
    def __init__(self, largeur, hauteur , couleur = " bleu "):
        ColorMixin.__init__(self, couleur)
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Carre(Rectangle):
    def __init__(self,cote,couleur="vert"):
        super().__init__(cote, cote , couleur)
        if self.largeur != self.hauteur:
            raise ValueError("Un carré doit avoir des côtés égaux.")


class Triangle(ColorMixin,Forme):
    def __init__(self, base, hauteur, couleur="jaune"):
        ColorMixin.__init__(self, couleur)
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return (self.base * self.hauteur) / 2


if __name__ == "__main__":
    formes = [
        Cercle(5,"rouge"),
        Rectangle(4, 6,"bleu"),
        Triangle(3, 8,"jaune"),
        Cercle(2.5,"cyan"),
        Carre(2,"vert")
    ]

    for f in formes:
        f.afficher_couleur()

   