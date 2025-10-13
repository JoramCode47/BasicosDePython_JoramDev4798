# FOR LOOP 
# (OBJETOS ITERABLES)
'''
Los iterables son objetos que tienen la capacidad de retornar uno a uno sus elementos
a medida que se los pidamos ''' 

lista_nombre = ['Joel', 'Ronaldo', 'Ramos']
tuplas_notas = ('Eduardo', 50, 4.5)
set_departamentos = {'ventas', 'compras', 'roles', 'it'}

print("********* Iterando en listas *********")

for nombre in lista_nombre:
    print(nombre)

print("********* Iterando en tuplas *********")

for nota in tuplas_notas:
    print(nota)


print("********* Iterando en sets *********")
'''
En este caso no se imprimen los datos como los ingresamos en el set 
debido a que los sets usan un didentificador o una posicion basandose en una tabla hash 
por lo que le orden puede que no sea el original al que se ingresaron '''
for departamento in set_departamentos:
    print(departamento)

# FOR LOOP - RANGE
# (SOBRE RANGOS ESTABLECIDOS)

# for i in range(0, 4, 1):
# for i in range(4):

print("********* Ejemplo de for loop con range *********")

for _ in range(4):
    print("Desde origen avanzar 10 pasos.")
    print("Girar 90 grados.")


# FOR LOOP ENUMERATE
# al usar enumerate por cada iteracion me retornara una tupla por lo que puedo acceder a indice, valor
print("********* Ejemplo de for loop con enumerate *********")

lista_nombres = ['Eduardo', 'Joel', 'Ramirez', 'Martinez']

for index, nombre in enumerate(lista_nombre):
    print(index, nombre)





