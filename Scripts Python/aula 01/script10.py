import math
numero = int(input("Informe o numero :"))

try:
    raiz=math.sqrt(numero)
    print("A raiz quadrada de %d é %.2f"%(numero,raiz))
except Exception as E:
    print("Erro ao calcular a raiz quadrada de %d: '%s'"%(numero,E))
finally:
    print("Fim do programa")