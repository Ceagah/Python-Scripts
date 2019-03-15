#Importando Função Sleep
from time import sleep

h=float(input("Entre com a sua altura em metros :"))
s=str(input("Entre com o seu sexo : ")).strip().upper()[0]
p=float(input("Entre com o seu peso em Kilogramas : "))

# .strip tira desconsidera os espaços. .upper coloca todas as entradas em Uppercase . [0] usa somente a primeira letra entrada como a variavel.
if s in 'M':
    print('Calculando . . . ')
    sleep(4)
    pesoidealm=((72.7*h)-58)
    print(f'Seu peso ideal é  : {(72.7*h)-58:.2f}Kg\n')
    if p>pesoidealm:
        print("Voce está acima do peso")
    else:
        print("Voces está em seu peso ideal! Parabens ! ")
elif s in 'F':
    print('Calculando . . . ')
    sleep(4)
    pesoidealf=((62.1*h)-44.7)
    print(f'Seu peso ideal é :{(62.1*h)-44.7:.2f}Kb\n')
    if p>pesoidealf:
        print("Voce está acima do peso")
    else:
        print("Voces está em seu peso ideal! Parabens ! ")
