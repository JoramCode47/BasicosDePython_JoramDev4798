# EJERCICIO ARGS AND KWARGS

def calcular_precio_total(*args, **kwargs):
    #*args => es uan tupla los valores que contiene
    precio_total = sum(args)
    #kwargs => todo lo que se que el usuario ingrese con una llave y un valor sera almacenado en un diccionario
    descuento = kwargs.get('descuento', 0)
    impuesto = kwargs.get('impuesto', 0)

    precio_total -= precio_total * descuento
    precio_total += precio_total * impuesto

    return precio_total
# en este caso el orden si importa siempre irian los *args y despues los **kwargs


#Forma de pasar argumentos 1
# total = calcular_precio_total(110, 75, 23, descuento = 0.2, impuesto = 0.01 )

#lista
lista_productos = [100, 75, 25]
#diccionario
opcionales = { 'descuento' : 0.2, 'impuesto' : 0.01 }

opcionales_2 = { 'descuento' : 0.2 }

#Forma de pasar argumentos 2
total = calcular_precio_total(*lista_productos, **opcionales)
print(f'El precio final con descuento e impuesto es: ${total:.2f}')

total = calcular_precio_total(*lista_productos, **opcionales_2)
print(f'El precio final solo con descuento es: ${total:.2f}')





