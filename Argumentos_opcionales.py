# OPTIONAL ARGUMENTS

'''
Los argumentos opcionales son útiles cuando se desea proporcionar
un comportamiento predeterminado para una función, pero aún se requiere esa 
flexibilidad para cambiar o requerir ese comportamiento si es necesario.
'''

def calcular_precio(nombre_producto, cantidad, precio_u, descuento = 0):
    precio_final = (cantidad * precio_u) * (1 - descuento)
    print(f'El precio final para {nombre_producto} es de ${precio_final}')

calcular_precio('Camisa', 4, 23)