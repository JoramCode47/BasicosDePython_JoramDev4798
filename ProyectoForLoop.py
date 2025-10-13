# PROYECTO 1 FOR LOOP

import turtle

ventana = turtle.Screen()
ventana.bgcolor = (6,7,9)
tortuga = turtle.Turtle()
tortuga.speed(2)


# Dibujar cuadrado


# tortuga.forward(100)
# tortuga.right(90)

# tortuga.forward(100)
# tortuga.right(90)

# tortuga.forward(100)
# tortuga.right(90)

# tortuga.forward(100)
# tortuga.right(90)

for _ in range(4):
    tortuga.forward(100)
    tortuga.right(90)


ventana.exitonclick()