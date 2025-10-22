'''
En este caso __init__ => podria ser como un constructor
y self que se envia a todos los metodos que cree en la clase
es como el this, como ejemplo, this.nombre => self.nombre
el cual al usar algun metodo y utilizar self seguido de alguna
propiedad este usara la informacion con la que previamente creamos
o construimos nuestro objeto.


'''

class Pikachu:
    tipo = "Electrico"

    # def __init__(self):
    #     self.nombre = 'pepe'
    #     self.nivel = 750
    #     self.salud = 500

    def __init__(self, nombre, nivel, salud):
        self.nombre = nombre
        self.nivel = nivel
        self.salud = salud


    def atacar(self):
        print(f"Pikachu ataca y genera {self.nivel / 4} de daño")


# pikachu_1 = Pikachu()

# print(pikachu_1.nombre)
# print(pikachu_1.tipo)
# print(pikachu_1.nivel)
# print(pikachu_1.salud)


pikachu_2 = Pikachu('pepe', 100, 200)
pikachu_3 = Pikachu('Roco', 200, 500)

print(pikachu_2.nombre)
print(pikachu_2.nivel)
print(pikachu_2.tipo)
print(f'El pikachu 2 llamado {pikachu_2.nombre} ataca.')
pikachu_2.atacar()
print("")
print(pikachu_3.nombre)
print(pikachu_3.nivel)
print(pikachu_3.tipo)
print(f'El pikachu 3 llamado {pikachu_3.nombre} ataca.')
pikachu_3.atacar()











