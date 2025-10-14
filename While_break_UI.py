import turtle
import random

meta = 750

ventana = turtle.Screen()
ventana.title("Carrera de caracoles")
ventana.bgcolor(0,0,0)
ventana.setup(width=900, height=600)

caracol_1 = turtle.Turtle()
caracol_1.shape('turtle')
caracol_1.color('red')
# simula que el lapiz o puntero se levanta para no escribir y pendown lo baja para comenzar a escribir
caracol_1.penup()
# nos ayuda a fijar unas cordenadas a las cuales se puede desplazar el puntero 
caracol_1.goto(-400, 100)

caracol_2 = turtle.Turtle()
caracol_2.shape('turtle')
caracol_2.color('blue')
caracol_2.penup()
caracol_2.goto(-400, -50)

pasos_caracol_1 = 0
pasos_caracol_2 = 0


while True:

    avance_caracol_1 = random.randint(1, 20)
    avance_caracol_2 = random.randint(1, 20)

    if ((avance_caracol_1 % 2 == 0) or (avance_caracol_2 % 2 == 0)):
        continue

    pasos_caracol_1 += avance_caracol_1
    pasos_caracol_2 += avance_caracol_2

    caracol_1.forward(avance_caracol_1)
    caracol_2.forward(avance_caracol_2)

    if pasos_caracol_1 >= meta or pasos_caracol_2 >= meta:
        break

if pasos_caracol_1 > pasos_caracol_2:
    print("Gana Caracol 1!!")
elif pasos_caracol_2 > pasos_caracol_1:
    print("Gana Caracol 2!!")
else:
    print("Empate!!")

ventana.exitonclick()
