# LAMBDA

# *************************
# Funcion normal
# def retornar_nota(estudiante):
#     return estudiante[1]
# *************************
# Funcion lambda
# lambda x : X[1]
# *************************


lista_estudiantes = [
    ('Eduardo', 9.5),
    ('Joel', 6.3),
    ('Sergio Ramos', 5.2),
    ('Cristiano Ronaldo', 9.2)
    ]


print(lista_estudiantes)

# lista_ordenada = sorted(lista_estudiantes, key=retornar_nota, reverse=True)
lista_ordenada = sorted(lista_estudiantes, key=lambda x : x[1], reverse=True)

print(lista_ordenada)


# EJEMPLO 2

lista = [1,2,3,4]

retorno = lambda x:x[3]

# de esta manera podemos almacenar esta funcion en una variable
# para poder usarla despues en otro momento del codigo

print(retorno(lista))


# EJERCICIO

print("********** EJRCICIO 1 ***********")

sumatoria = lambda n1, n2 : n1 + n2

resultado = sumatoria(25,20)

print(resultado)





