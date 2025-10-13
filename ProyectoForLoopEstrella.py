
# PROYECTO 2 FOR LOOP 
# ESTRELLLA 


import turtle

ventana = turtle.Screen()
ventana = turtle.bgcolor(0,0,0)

turtle_point = turtle.Turtle()
turtle_point.speed(2)
turtle_point.color('white')


for _ in range(5):
    turtle_point.forward(250)
    turtle_point.right(144)


ventana.exitonclick()