def fib(n):
    if n == 0:
        return 0
    if n==1:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

#entrada de dados
n = int(input("Informe o tamanho da sequencia : "))
print (f'O numero gerado foi : {fib(n)}')
