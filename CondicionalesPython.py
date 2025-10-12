# CONDICIONALES

edad = 116

if 0 < edad < 100:
    print("Edad Correcta \n")
    if edad >= 18:
        print("Eres mayor de edad")
    elif edad == 17:
        print("Ya casi eres mayor de edad")
    else:
        print("Eres menor de edad")
else:
    print("Edad Incorrecta")