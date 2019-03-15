soma = 0
while True:
    numero=int(input("Digite o valor para somar ou 0 para sair :"))
    if numero == 0:
        break
    soma += numero
print("Soma : %d" %soma)