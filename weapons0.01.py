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


#armas cuerpo a cuerpo
class Weapons02:
    def __init__(self, name, rateFire, Damage, capacity, reload):
        self.name = name # nombre del arma
        self.rateFire = rateFire # velocidad de ataque
        self.Damage = Damage # daño del arma
        self.capacity = capacity # capasidad del arma
        self.reload = reload # velocidad de recarga

    def __str__(self):
        return f"Arma: {self.name} \ncadencia de tiro: {self.rateFire} \ndaño: {self.Damage} \ncapasidad: {self.capacity} \nvelocidad de recarga: {self.reload}"
    
    print("seleccione un arma para ver sus estadisticas: arco | pistola | cañon | cuchillos arrojadizos")
    
    print(f"hola {bow}")