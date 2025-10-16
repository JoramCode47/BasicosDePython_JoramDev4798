# DICTIONARY UNPACKING

def imprimir_mensaje(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido):
    print(f"""Hola {primer_nombre} 
    {segundo_nombre} 
    {primer_apellido}
    {segundo_apellido}""")

# diccionario
diccionario = {
    'segundo_nombre' : 'Joel',
    'primer_apellido' : 'Ramírez',
    'primer_nombre' : 'Eduardo',
    'segundo_apellido' : 'Martínez'
 }

# imprimir_mensaje(*estudiante)
imprimir_mensaje(**diccionario)

'''
Para pasar argumentos por un iterable mediante un diccionario es posible sin
respetar el orden de los parametros, sin embargo deben coincidir las keys del 
diccionario que pasaremos como argumentos con
el nombre de los parametros de la función

adicionarl a diferencia de pasarlos mediante una tupla en este caso 
se debe asignar dos '**' antes del diccionario para que asi entienda que estamos apsando argumentos 
en un iterable y que al des empaquetar debe coincidir las key con el parametro
'''
