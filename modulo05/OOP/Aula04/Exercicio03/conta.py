class Conta:

    def __init__(self, numero, agencia, tipo):
        self.__numero = numero
        self.__agencia = agencia
        self.__tipo = tipo
        print("Passando pelo Construtor Conta")

    def __str__(self):
        return f"Número de Conta: {self.numero}\nNome da Agência {self.agencia}\nTipo de Conta: {self.tipo}"

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def tipo(self, numero):
        self.__numero = numero

    @property
    def agencia(self):
        return self.__agencia
    @agencia.setter
    def agencia(self, agencia):
        self.__titular = agencia

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo