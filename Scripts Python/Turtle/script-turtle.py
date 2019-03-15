import turtle
# cria uma janela grafica
screen = turtle.Screen()
# Cria uma tartaruga chamada reliquia
reliquia = turtle.Turtle()
# define a forma do cursor
reliquia.shape('turtle')
# Define a cor e a espessura do traço
reliquia.color('blue')
reliquia.pensize(1)
# Move a tartaruga 150 unidades para frente
reliquia.forward(150)
# gira a tartaruga 90º para a esquerda
reliquia.left(90)
# move a tartarua 75 unidades para frente
reliquia.forward(75)
# gira a tartaruga 90º para a esquerda
reliquia.left(90)
# Move a tartaruga 150 unidades para frente
reliquia.forward(150)
# gira a tartaruga 90º para a esquerda
reliquia.left(90)
# move a tartarua 75 unidades para frente
reliquia.forward(75)
# fecha a janela
screen.exitonclick()