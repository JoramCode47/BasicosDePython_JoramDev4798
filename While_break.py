# WHILE BREAK

import random

pasos_caracol_1 = 0
pasos_caracol_2 = 0

while True:
    avance_caracol_1 = random.randint(1, 4) 
    avance_caracol_2 = random.randint(1, 4) 

    pasos_caracol_1 += avance_caracol_1
    pasos_caracol_2 += avance_caracol_2

    print(f"El caracol 1 avanza {avance_caracol_1} pasos y comula un lleva un total de {pasos_caracol_1}")
    print(f"El caracol 2 avanza {avance_caracol_2} pasos y comula un lleva un total de {pasos_caracol_2}")
    print("****************************************************************")

    if pasos_caracol_1 >= 20 or pasos_caracol_2 >= 20:
        break


if pasos_caracol_1 > pasos_caracol_2:
    print("El caracol 1 es el ganador")
elif pasos_caracol_2 > pasos_caracol_1:
    print("El caracol 2 es el ganador")
else:
    print("Hay un empate!!")