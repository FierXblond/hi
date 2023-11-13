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
        return f"tipo: {self.type} \nvelocidad de movimiento: {self.speedMov} \nvelocidad de ataque: {self.atacSpeed} \nDaño de ataque: {self.atacDamage} \nEnergía: {self.energy} \nResistencia: {self.resistence}"

human = Personaje("humano", 3, 3, 3, 3, 3, 0)
mage = Personaje("mago", 3, 1, 2, 5, 1, 5)
berserk = Personaje("Berserker", 3, 5, 3, 4, 5, 0)

x = input()

if x == 1:
    print(human)