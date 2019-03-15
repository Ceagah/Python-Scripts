# Importando a função sleep
from time import sleep

# Entrada de dados
n1I=int(input("Entre com um numero INTEIRO :"))
n2I=int(input("Entre outro numero INTEIRO :"))
nr=float(input("Entre com um numero REAL :"))

sleep(2)
print("Buscando os resultados . . . ")
# Entretendo o usuário
sleep(2)

# Operações
print("O Produto do primeiro numero com a metade do segundo : ")
# Entretendo de novo
sleep(3)
print(n1I*(n2I/2))
print()

#Operação
print("A soma do triplo do primeiro numero com o terceiro")
# Entretendo de novo
sleep(3)
print((3*n1I)+nr)
print()
# Entretendo de novo
sleep(2)
print("O terceiro numero elevado ao cubo")
# Entretendo de novo
sleep(3)
print(pow(nr,3))
