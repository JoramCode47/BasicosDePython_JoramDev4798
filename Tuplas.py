
# TUPLAS

mi_tupla = (1, False, 'Eduardo Joel', 0.147)

def funcion_retorna_tupla():
    return 2, True, "Información", 2.128

tupla_informacion = funcion_retorna_tupla()

print(tupla_informacion)


def info_estudiante():
    return "Eduardo Joel Ramírez Martínez", 27, 9.8

nombre_estudiante, edad_estudiante, promedio_estudiante = info_estudiante()

print(nombre_estudiante)
print(edad_estudiante)
print(promedio_estudiante)



# ONE-LINE SwAPPING

variable_1 = 1.0
variable_2 = 2.0

print(f"variable_1 = {variable_1}")
print(f"variable_2 = {variable_2}")

variable_1, variable_2 = variable_2, variable_1

print(f"variable_1 = {variable_1}")
print(f"variable_2 = {variable_2}")




