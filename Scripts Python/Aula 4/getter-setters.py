# Classe para criar pokemons

class pokemon(object):
    
    #Previne a adição dinamica de atributos na classe pokemon
    __slots__=['name','__hp']


    #Construtor
    def __init__(self,name,hp):
        self.name = name #publico
        self.__hp = hp #privado

    '''#Getter -> Tradicional
    def get_hp(self)
        """Returns pokemon HP"""
        return self.__hp'''

    #Getter -> decorator @property
    @property
    def hp(self):
        """Returns Pokemon HP"""
        return self.__hp
    
    #getter
    ''' def get_hp(self):
        """Returns pokemon HP"""
        return self.__hp'''

    ''' #setter

    def set_hp(self,hp):
        """Sets pokemons Hp"""
        self.__hp = hp'''

    #Setter -> decorator @hp.setter
    @hp.setter
    def hp(self,hp):
        """sets pokemon hp"""
        self.__hp=hp 


def main():

    #Cria um pokemon
    Pikachu = pokemon('Pikachu', 100)

    #Exibe informações do pokemon
    print(f'Nome: {Pikachu.name}')
    print(f'HP: {Pikachu.hp}')
    print()

    #altera o valor do HP do pokemon
    Pikachu.hp=20
    print("Pikachu tomou Rockslide \n")
    print("É super efetivo")
    print()

    #exibe informações do pokemon
    print(f'Nome: {Pikachu.name}')
    print(f'HP: {Pikachu.hp}')
    print()
    
    '''  #Adiciona um novo atributo

    #Pikachu.__hp = 10

    #Exibe informação do pokemon
    print("Pikachu tomou tackle")
    print(f'Nome: {Pikachu.name}')
    print(f'HP: {Pikachu.hp}')
    #print(f'HP: {Pikachu.__hp}')
    print(Pikachu.__slots__)
    print()

    #exibe os atributos do objeto
    #print(Pikachu.__dict__)'''

if __name__ == "__main__":
    main()
