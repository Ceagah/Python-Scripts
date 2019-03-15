from time import sleep

#Entrada de Dados
mt2=float(input('Entre com o tamanho [em metros quadrados] da area a ser pintada :'))

#1 litro de tinta pinta 3 metros²
litro=(mt2/3)

if litro%18==0:
#1 lata contem 18 litros
    lata=(litro/18)
elif litro%18!=0: