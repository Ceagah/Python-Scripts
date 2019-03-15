import turtle

def desenha_quadrado(tartaruga,tamanho,cor):
    tartaruga.color(cor)

    for i in range(200):
        tartaruga.forward(tamanho)
        tartaruga.left(100)
        for i in range(200):
            tartaruga.color('black')
            tartaruga.forward(tamanho)
            tartaruga.right(50)



screen = turtle.Screen()

reliquia=turtle.Turtle()
reliquia.shape('turtle')

desenha_quadrado(reliquia,1,'red')

screen.exitonclick()