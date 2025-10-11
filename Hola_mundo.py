import pandas
import this


print("Hola mundo Joram47")

print("Hola Mundo JoramDev98")
print("Mi nombre es Eduardo Joel Ramirez 7")

print("Mi nombre es: \nJoram")

numero = 7
print(numero)
print(type(numero))

numeroDos = 7.40
print(numeroDos)
print(type(numeroDos))

cadena = 'Cadena de texto'
print(cadena)
print(type(cadena))

cadenaDos = 'Estoy "Estudiando"'
print(cadenaDos)
print(type(cadenaDos))

booleanos = True
print(booleanos)
print(type(booleanos))

print("Python respeta las reglas de presedencia en calculos matematicos.")
num1 = 9
num2 = 7.2
valor = num1 + num2 * 4 / 6
valorDos = (num1 + num2) * 4 / 6
print(valor)
print("")
print(valorDos)

print("El resultado es: ", valor)

valor = "Esta variable es una cadena y el valor cambio por que python cuenta con tipado dinamico"
print(valor)

# Estos son los comentarios de una linea
'''
Estos son los 
comentarios 
multilinea
'''

#Operadores aritméticos
num1 = 10
num2 = 3
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
divisionRedondeadaAbajo = num1 // num2
residuo = num1 % num2
exponencial = num1 ** num2

'''
***************************************
Prioridad de los operadores aritméticos
***************************************
Paréntesis dentro afuera ()
Exponenciación **
Multiplicación, División, Módulo *, /, %
Suma y Resta +, -    
'''

formula = 3**3 * (13/5 - (2*4))
print(formula)

#Operadores relacionales
'''
Estos operadores se ejecutan despues 
que los operadores aritméticos debido a menor prioridad

> Mayor que 
< Menor que 
>= Mayor o igual que 
<= Menor o igual que 
!= Diferente que
== Igual que
'''

resultado = 10 < 20
print(resultado)

resultado = 10 > 20
print(resultado)

resultado = 10 == 20
print(resultado)

resultado = 10 != 20
print(resultado)

na = 10
nb = 2
nc = 50

resultado = na**nb + nc - 50 == nc * 2
print(resultado)

#Operadores lógicos
'''
AND (Conjunción) | and
OR (Disyunción) | or
NOT (Negación) | not

AND (como si fuera una multiplicación lógica)
True and True = True
True and False = False
False and True = False
False and False = False

OR (como si fuera una suma lógica)
True or True = True
True or False = True
False or True = True
False or False = False

NOT (Negación)
not (True) = False
not (False) = True

Prioridad de operadores lógicos
not
and
or

'''

#Ejemplo

a = 10
b = 12
c = 13

result = ((a>b) or (a<c)) and ((a==c) or (a>=b))
print("El resultado de la siguiente operación logica \n((a>b) or (a<c)) and ((a==c) or (a>=b)) es: ", result)

'''
Prioridad de todos los operadores en general

1. () Resolver de adentro afuera
2. **
3. *, /, %, not
4. +. -, and
5. >, <, ==, >=, <=, !=, or

'''

#Operadores de Asignación

na = 0

na += 5 # Suma en asignación
na -= 2 # Resta en asignación
na *= 5 # Multiplicación en asignación
na /= 5 # División en asignación
na **= 3 # Potencia en asignación
na %= 5 # Módulo en asignación

print(na)

# Salidas

nombre = "Eduardo Joel"
edad = 27
print("Hola",nombre,"tienes",edad,"años de edad. (Concatencación)")
print("Hola {} tienes {} años de edad (funcion format)".format(nombre, edad))
print(f"Hola {nombre} tienes {edad} años de edad.")

# Entrada de datos
'''
nombre = input("Digite su nombre: ")
print(f"Hola {nombre}.")

numero = int(input("Digite un numero: "))
print(f"El numero entero ingresado mas 1 es : {numero + 1}")

numero = float(input("Digite un numero decimal: "))
print(f"El numero decimal ingresado mas 1 es : {numero + 1}")
'''

# Funciones integradas
n = str(15)
print(n)
n = int("11")
print(n)
n = float("23.47")
print(n)
n = bin(9)
print(n)
n = hex(123)
print(n)
n = int("0b1011", 2)
print(n)
n = int("0xd", 16)
print(n)
n = abs(-9)
print(n)
n = round(14.63)
print(n)
n = len("Joram4798")
print(n)

