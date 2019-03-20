# Define a classe TV
class TV(object):
    """Class to represent a TV set."""

    # Contrutor
    def __init__(self):
        
        print('A TV está sendo ligada...\n')
        
        self.ligado = True
        self.__canal = 1
        self.__volume = 1
        self._polegadas = None

    # Destrutor
    def __del__(self):
        print('Desligando a TV...\n')

    # Método para setar o valor do canal
    def set_canal(self, c):
        """Set TV channel value."""

        if not self.ligado:
            print("Ligue a TV primeiro!\n")
        else:
            self.__canal = c

    #Método para setar o valor do volume
    def set_volume(self,v):
        """SET TV VOLUME VALUE"""
        if not self.ligado:
            print("Bora ligar essa Tv ai ?\n")
        else:
            self.__volume = v

    #Método para recuperar o valor do canal
    def get_canal(self):
        """Returns TV channels value."""
        return self.__canal
    #Método para recuperar o valor do volume
    def get_volume(self):
        """Returns Tv volume value"""
        return self.__volume
    
    #Função Principal
def main():

    #Instanciamento do objeto
    tv = TV()

    #Exibe o canal e volume da TV
    print("Dados da minha Tv...")
    print(f'Canal: {tv.get_canal()}')
    print(f'Volume : {tv.get_volume()}')
    print(f'Status : {tv.ligado} da {tv.ligado}')

    #Desliga a Tv

    tv.ligado = False
    # Seta o canal e volume da Tv
    tv.set_canal(10)
    tv.set_volume(10)

    #Exibe o canal e volume da Tv
    print('Dados da minha Tv...')
    print(f'Canal : {tv.get_canal()}')
    print(f'Volume : {tv.get_volume()}')
    print(f'Status : {tv.ligado}')

    #Liga a Tv
    tv.ligado = True
    #Seta o canal e volume da Tv
    tv.set_canal(10)
    tv.set_volume(10)

    #exibe o canale  o volume da Tv
    print('Dados da minha Tv...')
    print(f'Canal : {tv.get_canal()}')
    print(f'Volume : {tv.get_volume()}')
    print(f'Status : {tv.ligado}')

    #Executa o trecho com o codigo principal do programa
if __name__ == "__main__":
    main()