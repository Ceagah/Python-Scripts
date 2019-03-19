# --------------------------------------------------------
# Programa exemplo para a criação de classes com heranças
# --------------------------------------------------------

# Define a classe Base
class Animal:

    def __init__(self):
        print('Construindo a classe base: Animal')


class Mamifero(Animal):

    def __init__(self):
        super().__init__()
        print('Construindo a classe derivada: Mamífero')


class Cachorro(Mamifero):

    def __init__(self):
        super().__init__()
        print('Construindo a classe derivada: Cachorro')


# Código principal do programa
if __name__ == "__main__":

    # Cria um mamífero
    macaco = Mamifero()

    print()

    # Cria um cachorro
    miranda = Cachorro()
