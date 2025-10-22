
class Pika:

    tipo = "Electrico"

    def __init__(self, nombre, nivel, salud, voltaje_max, amperaje_max, color):
        self.nombre = nombre
        self.__nivel = nivel
        self.__salud = salud
        self.__voltaje_max = voltaje_max
        self.__amperaje_max = amperaje_max
        self.color = color

    def atacar(self):
        print(f"Pikachu ataca y genera daño de {self.__nivel / 4} ")


    def get_salud(self):
        return self.__salud

    def set_salud(self, salud):
        if salud > 0 and salud < 5000:
            self.__salud = salud
        else:
            print("La salud no puede ser negativa", "La salud no puede ser mayor a 5000")


pikachu_1 = Pika('Pepechu', 700, 100, 6, 2, 'Amarillo')

pikachu_1.atacar()
pikachu_1.set_salud(-200)
pikachu_1.set_salud(500)


# Encapsulamiento consiste en ocultar informacion de implementacion en un objeto y exponer 
# solo la informacion necesaria para poder interactuar con con el esterior 

''' Para evitar acceder a una propiedad de tipo privada podriamos ocupar doble guion bajo '__voltaje_max' 
para poder simular un error como en otro lenguajes de progrmación '''

print(pikachu_1.nombre)
print(pikachu_1.tipo)


# pikachu_1.tipo = "Fuego"  # Esto no se deberia poder realizar

# print(f'El pikachu llamado {pikachu_1.nombre} tiene un nivel de {pikachu_1.nivel} y es de tipo {pikachu_1.tipo} y tiene un voltaje maximo de {pikachu_1.__voltaje_max}')


''' En python podriamos establecer propiedades para estos atibutos prvados y así 
crear y utilizazr los metodos geters y seters como en otros lenguajes de programación '''


print(f'El pikachu llamado {pikachu_1.nombre} tiene un una salud de {pikachu_1.get_salud()}')

