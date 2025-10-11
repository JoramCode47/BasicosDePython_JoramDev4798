# EJERCICIO 4
'''
*******************************
Hacer un programa para ingrear el radio de un circulo y
se reporte su área y la longitud de la circunferencia.
*******************************
'''

import math

radio = float(input("Ingrese el radio de un circulo: "))

PI = 3.1416

area = PI * radio ** 2
longitud = 2 * PI * radio

area = math.pi * radio ** 2
longitud = 2 * math.pi * radio

print(f"El área del circilo es: {area:.2f} y si longitud de la circunferencia es: {longitud:.3f}")
