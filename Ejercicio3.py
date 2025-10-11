# EJERCICIO 3
# invertir el valor de dos variables

a = float(input("Ingrese valor de a: "))
b = float(input("Ingrese valor de b: "))

aux = a
a = b
b = aux

print(f"El valor de a = {a} y el valor de b = {b}")

''' *********** Resolución ********** '''

a, b = b, a
print(f'El nuevo valor de a = {a} y el valor de b = {b}')

