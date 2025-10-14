# EJERCICIO PRACTICO FUNCIONES

def suma (num_1, num_2):
    return int(num_1) + int(num_2)

def resta (num_1, num_2):
    return int(num_1) - int(num_2)

def multiplicacion (num_1, num_2):
    return int(num_1) * int(num_2)

def division (num_1, num_2):
    return int(num_1) / int(num_2)


def imprimir_menu():
    print("")
    print("**************** Menu de operaciónes *************")
    print("1 ........................................... Suma")
    print("2 .......................................... Resta")
    print("3 ................................. Multiplicacion")
    print("4 ....................................... Division")
    print("")


continuar = True

while continuar:
    imprimir_menu()
    operacion = int(input("Por favor ingrese la operacion a realizar: "))
    resultado = 0

    if(operacion == 1):
        num_1 = int(input("Por favor ingrese primer numero: "))
        num_2 = int(input("Por favor ingrese segundo numero: "))
        resultado = suma(num_1 = num_1, num_2 = num_2)
        print(f"el resultado de la suma es: {resultado}")
    elif(operacion == 2):
        num_1 = int(input("Por favor ingrese primer numero: "))
        num_2 = int(input("Por favor ingrese segundo numero: "))
        resultado = resta(num_1 = num_1, num_2 = num_2)
        print(f"el resultado de la resta es: {resultado}")
    elif(operacion == 3):
        num_1 = int(input("Por favor ingrese primer numero: "))
        num_2 = int(input("Por favor ingrese segundo numero: "))
        resultado = multiplicacion(num_1 = num_1, num_2 = num_2)
        print(f"el resultado de la multiplicación es: {resultado}")
    elif(operacion == 4):
        num_1 = int(input("Por favor ingrese primer numero: "))
        num_2 = int(input("Por favor ingrese segundo numero: "))
        resultado = division(num_1 = num_1, num_2 = num_2)
        print(f"el resultado de la division es: {resultado}")
    elif(operacion == 5):
        print("Saliendo!")
        break
    else:
        print("La operacion que elegiste no es valida, por favor ingrese otra operación")
        continue

    pregunta = input("¿Desea ejecutar otra operación? \n Yes => Y | No => N: ")
    if pregunta != "Y":
        continuar = False


    



    
