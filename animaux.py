class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
       raise NotImplementedError("Cette méthode doit être redéfinie")



class Chien(Animal):
    def parler(self):
        return f"\n Le chien  {self.nom} dit : Woof !"


class Chat(Animal):
    def parler(self):
        return f"\n Le chat {self.nom} dit : Miaou !"

class Vache(Animal):
    def parler(self):
        return f"\n La vache {self.nom} dit : Meuh !"
    
def faire_parler(animal):
    print(animal.parler())

def faire_parler_tous(animaux):
    for animal in animaux :
        faire_parler(animal)


if __name__ == "__main__":
    animaux = [
        Chien("Rex"),
        Chat("Minou"),
        Chien("Max"),
        Vache("Marguerite"),
        
    ]

    faire_parler_tous(animaux)