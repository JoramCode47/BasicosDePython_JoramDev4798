
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura: "))


if 0 < edad < 100:
    if edad >= 18:
        if altura > 1.70:
            print(f'La persona si puede participar ya que tiene {edad} años y mide {altura:.2f}.')
        elif edad > 25 and altura > 1.65:
            print(f'La persona si puede participar ya que mide {altura:.2f} pero tiene {edad} años.')
        else:
            print("no puede acceder debido a que no cumple con el requerimiento de edad y altura.")
    else:
        print("Usted no cuenta con la mayoria de edad!")
else:
    print("Edad incorrecta!")
    
