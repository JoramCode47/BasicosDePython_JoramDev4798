
edad = 19

print(edad)


edad = "11"

print(edad)


# ENTEROS int

sueldo = 23

# BOOLEANOS bool
es_domingo = False

print(type(es_domingo))

# FLOTANTE float

salario = float("128.8034")
print(type(salario))

print(f"El salario es de {salario:.2f}")


# STRINGS

cadena_1 = 'cadena  1'
cadena_2 = "cadena  2"
cadena_multilinea = """cadena de mas 
de una linea de codigo 
es decir realiza saltos de linea implicitos en esta.
"""

print(cadena_1)
print(cadena_2)
print(cadena_multilinea)

print(len(cadena_1))
print(len(cadena_2))
print(len(cadena_multilinea))


# REMOVER PREFIJOS Y SUFIJOS DE CADENAS

producto_1 = "0001 - Manzana"
producto_2 = "Manzana - 0002"


print(producto_1.removeprefix('0001 - '))
print(producto_2.removesuffix(' - 0002'))


# INDEXING (permite obtener o acceder a caracteres especificos de uan cadena)

cadena = "Hola, mundo!"

print(cadena[0])
print(cadena[-1])

# SLICING (permite obtener o acceder a cadenas mas grandes de una cadena principal)

print(cadena[0:4])
print(cadena[6:11])
''' esto se define en la primer posicion desde que posicion 
voy a partir o empezar a obtener y el segundo numero es la posicion en la que voy a cortar la cadena mas 1
o bien el length de la cadena

si no se especifica el indice o posicion de partida este se toma como posicion 0
y en caso de que ninguna posicion se establezca se usa obtiene toda la cena de texto
'''

print(cadena[:4])
print(cadena[:])


'''
    Se puede obtener tambien una cadena por saltos por ejmplo en la cadena
    'Hola, mundo!' si nosotros aplicamos los saltos de dos en dos obtendriamos lo siguiente
    'Hl,mno'
'''

print(cadena[::2])


#Ejercicio 

telefono = "4-5-6-7-3-2-4-7-9"

print(telefono[::2])
print(telefono[0:13:2])

telefono_2 = "-5-6-7-3-2-4-7-9"
print(telefono_2[1:12:2])

# telefono_2[(indice desde el inicio):(indice +1 donde parto la cadena):(saltos que ire dando 2 en 2 o 5 -5 etc)]

# se puede hacer SLICING NEGATIVO

print(cadena[-6:-1])
print(cadena[-6:-1:1])
print(cadena[-6:-1:2])

'''
    Se puede hacer un reverse de cadena o invertir el orden de las palabras
'''

print(cadena[::-1])
''' cadena[
 (no se especifica entonces parte desde 0): 
 (no se especifica asi que toma toda la cadena o el length total de la cadena): 
 (va ir obteniendo de menos uno -1 en menos uno -1)
]'''



# MUTABILIDAD E INMUTABILIDAD


'''

 Inmutables: no pueden ser cambiados despues de haber sido creados
    - Numeros
    - Cadenas
    - Booleans
    - Tuplas

    por ejemplo si se declara una variable y se vuelve a signar 
    otro valor este por detras es replasado con el mismo nombre de 
    variable es deceir que cuenta con otro identificador

    por ejemplo 

    edad = 20 
    y si se imprimer su id de esta variable p.ej
    seria : 140729280132616

    pero al asignarle un nuevo valor el id es uno nuevo debido a que es como
    una nueva instancia de la clase 'int' y el objeto anterior lo elimina 
 
    edad = 27
    su id es : 140729280132840

    edad = 20
    print(id(edad))

    edad = 27
    print(id(edad))

 Mutables ; si pueden cambiar despues de ser creados
    - Listas
    - Sets
    - Diccionarios

    las listas por ejemplo no cambian su id de la variable(objeto) cuando
    se modifica su contenido es decir que se pueden agregar elementos o quitar y seguira siendo
    el mismo identificador

    lista = [1,2,3,4,5,6,7]
    print(id(lista)) => 2781566521216


    la lista sera la siguiente [1,2,3,4,5,6,7,9]
    y su id el mismo
    print(id(lista)) => 2781566521216


    En caso de que se declare una lista nueva y se asigne 
    el valor de la lista actual esta seguira apuntando 
    a la misma lista por ejemplo:

    lista = [1,2,3,4,5,6,7]
    lista_nueva = lista

    lista nueva.append(23)

    [1,2,3,4,5,6,7,23] ys is imprimo la lista original seria lo mismo
    [1,2,3,4,5,6,7,23] ya que apuntan al mismo identificador debido a que 
    una lista es un objeto mutable.


'''

# lista = [1,2,3,4,5,6,7]
# lista.append(9)  
# print(id(lista))


# edad = 20
# print(id(edad))

# edad = 27
# print(id(edad))

