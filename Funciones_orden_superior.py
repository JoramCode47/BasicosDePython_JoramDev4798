# Funciones de orden superior
'''
Es cualquier funcion que acepta otras funciones como argumentos, por ejemplo
 una funcion que acepte otra funcion y esa funcion se aplica a cada uno de los 
items del iterable que le pasemos
'''


print("*************************** map *************************")

# map

'''
map se utiliza para aplicar una funcion a todos los elementos de una o mas secuencias
como las listas, tuplas o iterables similares. Toma dos argumentos principales:
- funcion que se aplica
- una o mas secuencias de datos sobre los que se aplicara la funcion.
'''

print("")
print(" ************* Ejemplo 1 *************************")
# ejemplo map 1

lista_nombre = ['maria', 'carlos', 'pepe']

''' En este ejemplo la funcion es map a la cual recibe como primer argumento una funcion la cual es ipper
la cual es un metodo interno de la clase str, por ultimo esta se parsea a una lista ya que queremos que esto es lo
que queremos que nos devuelva '''
lista_nombre_mayus = list(map(str.upper,lista_nombre))

print(lista_nombre_mayus)  # => ['MARIA', 'CARLOS', 'PEPE']


# ejemplo map 2
print(" ************* Ejemplo 2 *************************")

sufix = '_fruta'

def agregar_sufix(fruta):
    return fruta+sufix

lista_frutas = ['platano', 'pera', 'manzana', 'uva']

lista_frutas_modificada = list(map(agregar_sufix, lista_frutas))

print(lista_frutas_modificada) # => ['platano_fruta', 'pera_fruta', 'manzana_fruta', 'uva_fruta']


lista_frutas_modificada = list(map(lambda x : f"{x}{sufix}", lista_frutas))

print(lista_frutas_modificada) # => ['platano_fruta', 'pera_fruta', 'manzana_fruta', 'uva_fruta']


print("")
print("*************************** filter *************************")

# filter 

''' Esta se utiliza para filtrar los elementos de un iterable como una lista, tupla, 
o culaquier otro iterable, pero basandose en una funcion condicional que se proporciona. '''

print(" ************* Ejemplo 1 *************************")

numbers = [1,2,3,4,5,6,7,8,9,10,11]

numbers_list = list(filter(lambda x : x % 2 == 0, numbers)) 

print(numbers_list) # => [2, 4, 6, 8, 10]


print(" ************* Ejemplo 2 *************************")

names = ['Alicea', 'bob', 'Anna', 'David', 'Amelia', 'Charlie']

lista_nombres = list(filter(lambda x : x[0].upper() == 'A', names))

print(lista_nombres) # => ['Alicea', 'Anna', 'Amelia']


print("")
print("*************************** sorted *************************")

# sorted
'''
La funcion sorted toma como minimo un iterable (por ejemplo una lista) y devuelve una nueva lista
que contiene los elementos ordenados.
'''

estudiantes = [
    ('Juana', 22, 95, '555-1234'),
    ('Pedro', 18, 89, '555-5678'),
    ('Laura', 25, 94, '555-9876')
]


# en la lista de estudiantes  se ordenara con 'sorted' mediante una llave 
# que le pasemos, que en este caso es cada estudiante que es una tupla 
# en la posiscion 1 el cual representa la edad
# en caso que quisieramos ordenar por notas (calificaciones) seria
# en la posicion 2  

lista_estudiantes = list(sorted(estudiantes, key= lambda x : x[1], reverse=True))

print(lista_estudiantes)

lista_estudiantes = list(sorted(estudiantes, key= lambda x : x[2], reverse=True))
print(lista_estudiantes)

print("")
print("*************************** sorted *************************")

# reduce

'''
Se utiliza para aplicar una funcion de manera acumulativa a los elementos de un iterable 
reduciendolos a un solo valor 

esta funcion si se importa de un paquete 'functools' y se importa 'reduce'
'''

from functools import reduce

numeros = [1,2,3,4,5]

total = reduce(lambda x, y : (x + y) * 2, numeros)

print(total)




