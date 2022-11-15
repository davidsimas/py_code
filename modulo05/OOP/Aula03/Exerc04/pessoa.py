class Pessoas:

    # Método Construtor
    def __init__(self, nome, cpf, idade, altura):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__altura = altura


    # Setter e Getter
    def set_nome(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome

    def set_cpf(self, cpf):
        self.__cpf = cpf
    def get_cpf(self):
        return self.__cpf

    def set_idade(self, idade):
        self.__idade = idade
    def get_idade(self):
        return self.__idade

    def set_altura(self, altura):
        self.__altura = altura
    def get_altura(self):
        return self.__altura


    # Método ToString
    def __str__(self):
        return f"{self.get_nome()} - {self.get_cpf()} - {self.set_idade()} - {self.get_altura():.2f}"