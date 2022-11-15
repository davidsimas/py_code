from conta import Conta

class PessoaJuridica(Conta):

    __segundo_titular = ""
    
    def __init__(self, titular, cnpj, saldo_inicial):
        super().__init__("101", "Juridica")
        self.titular = titular
        self.cnpj = cnpj
        self.saldo_inicial = saldo_inicial
        print("Passando pelo construtor da classe Pessoa Jurudica")


    @property
    def segundo_titular(self):
        return self.__segundo_titular
    @segundo_titular.setter
    def segundo_titular(self,segundo_titular):
        self.__segundo_titular = segundo_titular


    def __str__(self):
        return f"{super().__str__()} - {self.titular}\n - {self.cnpj}\n - {self.saldo_inicial}\n - {self.segundo_titular}"