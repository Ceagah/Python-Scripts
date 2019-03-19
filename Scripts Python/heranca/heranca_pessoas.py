# coding: utf-8
# Define a classe base -> Pessoa
class Pessoa:
    """Class to represent people"""

    # Cria uma pessoa generica
    def __init__(self, nome, endereco):
        """Creates a new person"""

        self.nome = nome
        self.endereco = endereco

    # Retorna informações da pessoa generica
    def get_info(self):
        """Returns person info"""

        info = f'    Nome: {self.nome}'
        info += f'    Endereço: {self.endereco}'
        return info

    # ---------------------------------------------------------------
    # Implementa o metodo __str__, para exibir informações da pessoa
    # Esse metodo será utilizado pelas demais classes derivadas de
    # Pessoa, através do conceito de polimorfismo.
    # ---------------------------------------------------------------
    def __str__(self):
        return self.get_info()

#Define a classe Pessoa fisica - > derivada  da classe pessoa

class PessoaFisica(Pessoa):
    """Class to represent fisical people."""
    
    #Cria uma pessoa fisica
    def __init__(self, nome, endereco, cpf):
        """Create a fisical people"""
        #O super() permite que o construtor da classe PessoaFisica encontra a superclasse Pessoa, e utilize o construtor
        #dela para inicializar o valor dos atributos 'nome' e ' endereço'
        
        super().__init__(nome,endereco)

        #Inicializa o valor do atributo 'cpf', presente somente na classe PessoaFisica
        self.cpf=cpf

    #Retorna informações da pessoa fisica
    def get_info(self):
        """Return person info"""

        #O Super() permite que se utilize o metodo get_info(), definido na super classe Pessoa
        info= super().get_info()
        info+= "\n    CPF: %s."%(self.cpf)
        return info

#Método para validar o CPF

    def valida_cpf(self):
        """Validates CPF"""

        #TO-DO
        print("Validando o CPF do %s..." %(self.nome))

class PessoaJuridica(Pessoa):
    """Class to represent legal people."""
    
    #Cria uma pessoa juridica
    def __init__(self, nome, endereco, cnpj):
        """Create a new legal people"""
        #O super() permite que o construtor da classe PessoaJuridica encontra a superclasse Pessoa, e utilize o construtor
        #dela para inicializar o valor dos atributos 'nome' e ' endereço'
        
        super().__init__(nome,endereco)

        #Inicializa o valor do atributo 'cnpj', presente somente na classe PessoaJuridica
        self.cnpj=cnpj

    #Retorna informações da pessoa Juridica
    def get_info(self):
        """Return person info"""

         #O Super() permite que se utilize o metodo get_info(), definido na super classe Pessoa
        info= super().get_info()
        info+= "\n    CNPJ: %s."%(self.cnpj)
        return info

#Método para validar o CNPJ

def valida_cnpj(self):
    """Validates CNPJ"""

    #TO-DO
    print("Validando o CNPJ do %s..." %(self.nome))

#Trecho com o Codigo principal do programa

def main():

    print('-' * 55)
    print('Demonstração de herança e polimorfismo')
    print('-' * 55)
    print()

    # Cria e exibe informações de uma pessoa genérica
    ze = Pessoa('Zé Ruela', 'Rua sem nome e sem numero')

    print('Exibindo informações da pessoa genérica:\n')
    print(ze)

    print()
    print('-' * 55)
    print()
    #Cria e exibe informações de uma pessoa fisica
    joao = PessoaFisica('João Carlos', 'Rua do João', '111.222.333.45')

    print("Exibindo informações da pessoa fisica:\n")
    print(joao)
    print()

    #Chama o metodo para validar o CPF do João
    joao.valida_cpf()

    print()
    print("-"*55)
    print()


# Executa o trecho com o código principal
if __name__ == "__main__":
    main()