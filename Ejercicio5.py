# EJERCICIO 5

'''
***************************
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
cuánto deberá pagar finalmente por su compra
***************************
'''

total_compra = float(input("Ingrese el totoal de la compra: "))
descuento = 0.15
total_compra -= descuento * total_compra
print(f"El total a pagar es de: ${total_compra:.2f}")





