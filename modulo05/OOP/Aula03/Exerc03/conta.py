class Conta:

    # Método Construtor
    def __init__(self, titular, numero, saldo, limite):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite


    # Setter e Getter
    @property
    def titular(self, titular):
        self.__titular = titular
    @titular.getter
    def titular(self):
        return self.__titular

    @property
    def numero(self, numero):
        self.__numero = numero
    @numero.getter
    def numero(self):
        return self.__numero

    @property
    def saldo(self, saldo):
        self.__saldo = saldo
    @saldo.getter
    def saldo(self):
        return self.__saldo

    @property
    def limite(self, limite):
        self.__limite = limite
    @limite.getter
    def limite(self):
        return self.__limite


    # Método ToString
    def __str__(self):
        return f"{self.titular} - {self.numero} - R$ {self.saldo:.2f} - R$ {self._limite:.2f}"