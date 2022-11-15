from conta import Conta

class PessoaJuridica(Conta):

    __segundo_titular = ""
    
    def __init__(self, titular, cnpj, saldo_inicial):
        # numero, agencia, tipo
        super().__init__("101", "Bradesco", "Juridica")
        self.__titular = titular
        self.__cnpj = cnpj
        self.__saldo_inicial = saldo_inicial
        print("Passando pelo construtor da classe Pessoa Jurudica")


    @property
    def segundo_titular(self):
        return self.__segundo_titular
    @segundo_titular.setter
    def segundo_titular(self,segundo_titular):
        self.__segundo_titular = segundo_titular


    def __str__(self):
        return f"{super().__str__()}Titular: {self.__titular}\nCNPJ: {self.__cnpj}\nSaldo Inicial: {self.__saldo_inicial}\nSegondo Titular: {self.segundo_titular}"