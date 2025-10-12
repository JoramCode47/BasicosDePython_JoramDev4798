
# SETS
'''
En los sets sus datos no pueden ser ordenados podrian estar ordenados pero no siempre
se debe fiar de que esto los respetara en el orden
adicionalmente los objetos que almacenen los 
sets deben ser hasheables'''

my_set = {1,2,3,4,5}

print(my_set)

my_set_empty = set()
my_set_empty.add(1)
my_set_empty.add(2)
my_set_empty.add(3)
my_set_empty.add(4)
my_set_empty.add(2)
my_set_empty.add(4)
print(my_set_empty)

'''
los sets no se miestran los elementos duplicados'''
# es una forma de eliminar los elementos duplicados en una lista por ejemplo

lista = [1,2,3,4,5,5,6,7,9]

my_new_set = set(lista)

print(my_new_set)

pertenece = 7 in my_new_set
print(pertenece)

'''En los sets seria mas rapidoutilizar esta busqueda debido a que ocupa
informacion hasheada es decir que cada elemento de esta tiene un 
identificador hash p.ej

hash('manzana') tiene un identificador => 1100689786902494064
y esto para cada uno de los elementos del set 
hash('pera') tiene un identificador => -267935935992215713

'''

frutas = {'manzana',
        'pera',
        'durazno', 
        'banana',
        'uva'}

print(hash('manzana'))
print(hash('pera'))


# FROZENSETS
'''
Estos no pueden ser modificados'''

mi_frozenset_de_set = frozenset(my_new_set)
mi_frozenset_de_lista = frozenset(lista)
print(mi_frozenset_de_set)



