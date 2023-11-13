class Swords: 
    def __init__ (self, daño, velAtak, reguion):
     self.daño = daño
     self.velAtak = velAtak
     self.reguion = reguion
    
    def __stats__(self):
        return f'''daño de la espada: {self.daño} \n
velocidad de ataque: {self.velAtak} \n
reguion de la espada: {self.reguion}'''
    
class SwdIron(Swords):
    def __init__(self, daño, velAtak, reguion, durabilidad):
        Swords.__init__(self, daño, velAtak, reguion)
        self.durabilidad = durabilidad
    
    def __str__(self):
        return f'{super().__stats__()}\n\n durabilidad de la espada: {self.durabilidad}'

ironSword = SwdIron(4, 3, "opalus", 11)
print(ironSword)