# Função que retorna a media dos valores de uma lista
def media_lista(lista):
    media=sum(lista)/len(lista)
    return media

# Define uma lista de valores
valores=[1,4,4,6,2,7,8]

# Utiliza a função "Media_lista"
media=media_lista(valores)
# Exibe o resultado
print("Média = %.2f" %media)