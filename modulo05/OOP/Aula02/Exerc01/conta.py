class Conta:

    # Método Construtor
    def __init__(self, titular, numero, saldo, limite):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite


    # Setter e Getter
    def set_titular(self, titular):
        self.__titular = titular
    def get_titular(self):
        return self.__titular

    def set_numero(self, numero):
        self.__numero = numero
    def get_numero(self):
        return self.__numero

    def set_saldo(self, saldo):
        self.__saldo = saldo
    def get_saldo(self):
        return self.__saldo

    def set_limite(self, limite):
        self.__limite = limite
    def get_limite(self):
        return self.__limite


    # Método ToString
    def __str__(self):
        return f"{self.get_titular()} - {self.get_numero()} - R$ {self.get_saldo():.2f} - R$ {self.get_limite():.2f}"