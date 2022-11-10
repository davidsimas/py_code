class Conta:

    def __init__(self, titular, numero, saldo, limite):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    
    def extrato(self):
        return f"O titular {self.titular} da conta {self.numero} tem saldo de R${self.saldo:.2f}"


    def depositar(self, valor):
        self.saldo += valor
        return f"Valor depositado R${valor:.2f}."


    def sacar(self, valor):
        self.saldo -= valor
        return f"Valor sacado R${valor:.2f}."


    def transferir(self, valor, origem, destino):
        origem.sacar(valor)
        destino.depositar(valor)
