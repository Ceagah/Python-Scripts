def fatorial(n):
    #caso base
    if n ==0:
        return 1
    #caso recursivo
    else:
        return (n * fatorial(n-1))
    
if __name__ =="__main__":
    #entrada de dados
    valor=int(input("Informe o valor : "))

    #Chama a função para calcular o fatorial
    print(f'Fatorial de {fatorial(valor)}')
