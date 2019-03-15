import random

def gera_inteiro(a,b):
    return(random.randint(a,b))

print("--- Jogo de Adivinhação --- \n")

numero = gera_inteiro(1,10)

acertou = False

i=0
while i <5:
    chute = int(input("Numero entre 1 e 10 : "))
    if chute == numero:
        acertou = True
        break
    i+=1
if acertou:
    print("Acerto Mizeravi ! O numero gerado foi o %d." %numero)
else:
    print("Seu lixo !  O numero gerado foi o %d." %numero)