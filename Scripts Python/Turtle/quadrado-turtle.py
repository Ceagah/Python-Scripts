import turtle

#função que desenha um quadrado em espiral
def quadrado_espiral(tartaruga,tamanho):
    if tamanho > 0:
        tartaruga.forward(tamanho)
        tartaruga.right(90)
        quadrado_espiral(tartaruga,tamanho-5)
    
#função principal

if __name__ == "__main__":

    #cria uma janela grafica
    screen=turtle.Screen()

    #cria a tartaruga
    t=turtle.Turtle()

    #Define a forma do cursor
    t.shape('turtle')

    #desenha o quadrado em espiral

    quadrado_espiral(t,300)

    #Fecha a janela
    screen.exitonclick()