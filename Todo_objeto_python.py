

nombre = "Joram"
edad = 27

print(f"Hola mi nombre es {nombre} y tengo {edad}")

# Todo en python es un objeto por lo que si tenemos 
# una variable esta es una instancia de una clase es decir una variable es como un objeto

print(type(edad))
# Esto imprimme class 'int'

print(type(nombre))
# Esto imprime class 'str'

# podemos acceder a su valor de cada variable(objeto)
# con id(nombre_variable) para obtener su identificador unico de esta variable
# con repr(nombre_variable) para obtener su valor o la representacion de esta varible

print(id(nombre))
print(repr(nombre))

print(id(edad))
print(repr(edad))

