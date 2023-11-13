import tkinter as tk
from tkinter import ttk

class Personaje:
    def __init__(self, type, speedMov, atacDamage, atacSpeed, energy, resistence, abilityPowe):
        self.type = type
        self.speedMov = speedMov
        self.atacDamage = atacDamage
        self.atacSpeed = atacSpeed
        self.energy = energy
        self.resistence = resistence
        self.abilityPowe = abilityPowe

    def __str__(self):
        return f"tipo: {self.type} velocidad de movimiento: {self.speedMov} velocidad de ataque: {self.atacSpeed} Daño de ataque: {self.atacDamage} Energía: {self.energy} Resistencia: {self.resistence}"

human = Personaje("humano", 3, 3, 3, 3, 3, 0)
mage = Personaje("mago", 3, 1, 2, 5, 1, 5)
berserk = Personaje("Berserker", 3, 5, 3, 4, 5, 0)


#print("mago vs berserker")

#magovs = mage.atacDamage + mage.resistence
#print(f'stats Mago: {magovs}')

#bersvs = berserk.atacDamage + berserk.resistence
#print(f'stats de Berserker: {bersvs}')

#if magovs < bersvs:
#   print("berserker win")

#elif  bersvs < magovs:
  #  print("mago win")

#else:
   # print("empatan\n\n\n\n")

#prueba de botones

#armas no magicas y a distancia
class Weapons01:
    def __init__(self, name, rateFire, Damage, capacity, reload):
        self.name = name # nombre del arma
        self.rateFire = rateFire # cadencia de disparo
        self.Damage = Damage # daño del arma
        self.capacity = capacity # capasidad del arma
        self.reload = reload # velocidad de recarga

    def __str__(self):
        return f"Arma: {self.name} | cadencia de tiro: {self.rateFire} | daño: {self.Damage} | capasidad: {self.capacity} | velocidad de recarga: {self.reload}"

bow = Weapons01("arco", 3, 2.5, 5, 3) # humano
pistol = Weapons01("pistola", 2, 3, 7, 4)# humano
canon = Weapons01("cañon", 5, 5, 1, 5)# Berserker
knife = Weapons01("cuchillos arrojadizos", 2, 2, 8, 1) # humano


# test

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
        Swords.__init__(self.daño, self.velAtak, self.reguion)
        self.durabilidad = durabilidad
    
    def __str__(self):
        return f'{self.__stats__()}\n durabilidad de la espada: {self.durabilidad}'

ironSword = SwdIron(4, 3, "opalus", 11)

print(ironSword)
 