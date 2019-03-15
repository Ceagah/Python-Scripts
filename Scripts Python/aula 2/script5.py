# Função que retorna o maior , o menor e a media dos valores de uma lista

def analise_lista(lista):
    maior=max(lista)
    menor=min(lista)
    media=sum(lista)/len(lista)
    return (maior, menor, media)

valores=[1,4,4,6,2,7,8]

maior,menor,media=analise_lista(valores)

print("Maior = %.2f" %maior)
print("Menor = %.2f" %menor)
print("Média = %.2f" %media)