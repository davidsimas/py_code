class Conta:

    def __init__(self, titular, numero, saldo, limite):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite


    # Setter
    def difinir_titular(self, titular):
        self.__titular = titular
    # Getter
    def pegar_titular(self, titular):
        return self.__titular

    def difinir_numero(self, numero):
        self.__numero = numero
    # Getter
    def pegar_numero(self, numero):
        return self.__numero

    def difinir_saldo(self, saldo):
        self.__saldo = saldo
    # Getter
    def pegar_saldo(self, saldo):
        return self.__saldo

    def difinir_limite(self, limite):
        self.__limite = limite
    # Getter
    def pegar_limite(self, limite):
        return self.__limite


    def __str__(self):
        return f"{self.pegar_titular()} - {self.__numero() - {self.pegar_saldo()} - {self.pegar_limite()}}"
        