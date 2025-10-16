# MULTIPLE RETURN

'''
En python se puede retornar mas de un solo valor espesificando por 
comas ',' que valores va a retornar una función

cuando retornamos más de un valor lo que retornamos es una tupla,
por lo que es posible desestructurar una tupla en variables 
siguiendo el orden que llevan sus valores

se desempaqueta en una tupla ya que es un tipo de dato inmutable por lo que
no se puede modificar, adicional se usa para almacenar dator heterogeneos
es decir que no son similares entre si


'''

def calcular_precio(nombre_producto, cantidad, precio_u, descuento = 0):
    precio_final = (cantidad * precio_u) * (1 - descuento)
    return nombre_producto, cantidad, precio_final


compra_final = calcular_precio('Short', 3, 22.50)

print(compra_final)

nombre_p, cantidad, precio_final = calcular_precio('Short', 3, 22.50)

print(f'nombre del producto: {nombre_p}')
print(f'cantidad: {cantidad}')
print(f'precio final: ${precio_final:.2f}')

