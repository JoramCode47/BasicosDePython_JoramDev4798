# WHILE

nombre = ""
correo = ""
mensaje = ""

condicion_salida = "CONTINUE"


while condicion_salida == "CONTINUE":
    nombre = input("Por favor ingrese su nombre: ")
    correo = input("Por favor ingrese su correo: ")
    mensaje = input("Por favor ingrese su mensaje: ")

    print(f"""
        mensaje enviado a {nombre}

        destinatario: {correo}

        mensaje a enviar es: {mensaje}
    
    """)

    condicion_salida = input('Si desea enviar otro pensaje por favor ingrese "CONTINUE"')






