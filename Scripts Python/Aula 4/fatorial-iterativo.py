#entrada de dados
n= int(input("Digite o numero que você quer fatorar: "))

fatorial = 1
while(n>0):
    fatorial=fatorial*n
    n-=1
print(f'O valor de {n} fatorial é : {fatorial}')