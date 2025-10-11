'''
#EJERCICIO 1
Hacer un programa que pida 2 números y se de cuenta cuál de ellos es par,
o si ambos lo son.
'''

num1 = int(input("Ingrese primer número: "))
num2 = int(input("Ingrese segundo número: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos numeros son par")
elif num1 % 2 == 0:
    print(f"El numero {num1} es par")
elif(num2 % 2 == 0):
    print(f"El numero {num2} es par")
else:
    print("Numgun numero ingresado es par")

