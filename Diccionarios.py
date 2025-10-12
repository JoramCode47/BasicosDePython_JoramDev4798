# Diccionarios

# En un diccionario se puede buscar una palabra al igual que el
# concepto más detallado de lo que significa esa palabra
# en otras palabras apartir de una clave se puede acceder al valor 
# con la cual esta relacionada esta clave
# tambien trabaja con hash por lo que una busqueda es rapida


mi_diccionario = {
    'Joram' : [1.4, 2.5, 4.7],
    'Eduardo' : [1.1, 5.5, 3.7],
    'Ramirez' : [2.4, 3.5, 2.7]
}


# Dict

mi_diccionario_1 = dict(
        Joram = [1.4, 2.5, 4.7],
        Eduardo = [1.1, 5.5, 3.7],
        Ramirez = [2.4, 3.5, 2.7]
    )


# Dict Vacio

# mi_diccionario_2 = {} < = Puede ser tambien declarado de esta manera
mi_diccionario_2 = dict()
mi_diccionario_2['JoramCode47'] = [2.5, 4.6, 5.7]
mi_diccionario_2['Joel'] = [2.5, 4.6, 5.7]
mi_diccionario_2['CRonaldo'] = [2.5, 4.6, 5.7]


print(mi_diccionario)
print(mi_diccionario_1)
print(mi_diccionario_2)

print(mi_diccionario_2['JoramCode47'])


# Del
# de esta manera se puede eliminar un elemento de un diccionario

del mi_diccionario_2['Joel']
print(mi_diccionario_2)
print(len(mi_diccionario_2))

print(mi_diccionario.keys())
print(mi_diccionario.values())
print(mi_diccionario.items())


