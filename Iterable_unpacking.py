# ITERABLE UNPACKING

def imprimir_mensaje(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido):
    print(f"""Hola {primer_nombre} 
    {segundo_nombre} 
    {primer_apellido}
    {segundo_apellido}""")

# tupla
estudiante = ('Eduardo', 'Joel', 'Ramírez', 'Martínez')

# imprimir_mensaje(*estudiante)
imprimir_mensaje(*('Eduardo', 'Joel', 'Ramírez', 'Martínez'))

'''
Para pasar argumentos por un iterable el cual se desempaqueta y se asigna a cada parametro de la
funcion debe llevar un '*' antes del iterable, en este caso se guardo en una variable pero se
puede pasar tal cual la tupla(iterable en este caso)
'''

