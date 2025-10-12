
'''
    Desarrolla un Script que pida la edad y altura del usuario 
    Si la persona es mayor de edad puede participar
    Pero la persona debe medir mas de 1.70 
    Si la persona no mide 1.70 pero es mayor a 25 años
    y la altura es mayor a 1.65
'''


edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura: "))


if 0 < edad < 100:
    if edad >= 18:
        if (altura >= 1.70) or (edad >= 25 and altura > 1.65):
            print(f'La persona si puede participar ya que tiene {edad} años y mide {altura:.2f}.')
        else:
            print("no puede acceder debido a que no cumple con el requerimiento de edad y altura.")
    else:
        print("Usted no cuenta con la mayoria de edad!")
else:
    print("Edad incorrecta!")
    
