
# LISTAS

lista_numeros = [1,2,3]
lista_numeros[2] = 4

print(lista_numeros)

lista_numeros.append(9)

print(lista_numeros)

lista_numeros[3] += 2
print(lista_numeros)

# convertir una tupla en una lista
lista_numeros_2 = list((9,8,7,6,5))
print(lista_numeros_2)

# METODOS DE LISTAS 

number_list = [1,2,3]

# ************* append *************
# agrega al final un nuevo elemento a la lista

number_list.append(4)
number_list.append(5)
number_list.append(9)
number_list.append(9)
print(number_list)

# ************* count *************
# cuenta cuantos elementos iguales se repiten en la lista

print(number_list.count(9))

# ************* extend *************
# nos permite extender la lista con ciertos elementos que se pasen como argumentos

extend_list = [100,101]
number_list.extend(extend_list)
print(number_list)

# ************* index *************
# permite saber si en una lista un elemento existe y si existe retorna el indice

print(number_list.index(9))
print(number_list[5])
# print(number_list.index(1000)) 

'''De esta manera al no encontrar un elemento nos marcara un error 
por lo que se recomienda usar excepciones '''


# ************* insert *************
# nos permite agregar elementos pero en cualquier posicion que nosotros indiquemos

number_list.insert(0, 23)
print(number_list)

''' si la posicion o indice en la cual queremos asignar un valor no se encuentra
lo asigna a una nueva posicion al final de la lista como un (append)'''
number_list.insert(20, 23)
print(number_list)


# ************* pop *************
# este metodo nos permite extraer (✖️quitar) elemento de la lista y retornarlos

print(number_list)
print(number_list.pop())
print(number_list)
# en este caso como no asigne una posicion o indice del elemento que quiero extraer me retorna el ultimo elemento

print(number_list.pop(6))
print(number_list.pop(6))
print(number_list)

# ************* remove *************
''' remove nos permite eliminar elementos de una lista por su valor '''

print(number_list)
number_list.remove(100)
print(number_list)

''' de igual manera se debe tener cuidado y manejar excepciones 
debido a que si se asigna como parametro un valor que no exista en la lista
esto marcara un error '''

# reverse
# este metodo nos permite revertir el orden de la lista

print(number_list)
number_list.reverse()
print(number_list)


# ************* clear *************
# este metodo nos permite nos permite limpiar la lista

print(number_list)
number_list.clear()
print(number_list)


# ************* sort *************
# este metodo nos permite ordenar de menor a mayor la lista

number_list = [1,23,3,45,15,2,0,2]

print(number_list)
number_list.sort()
print(number_list)


