"""
 - Na pasta model crie um segundo documento com namespace pessoaFisica.py.
 - Realize a importação da classe conta from model.conta import Conta.
 - Dentro deste documento crie uma classe PessoaFisica, faça a herança da classe
   conta esta classe deve conter quatro atributos privados:
     * segundo_titular
     * titular
     * cpf
     * saldo_inicial
   inseridos diretamente na classe, todos os atributos devem estar vazios, sem dados fixos.
 - Crie anotações de @property e @setter para cada atributo privado da nossa classe.
 - Chame o método __str__ e retorne o método super().__str__() e acessando os atributos
   através das anotações de @property e @setter de titular, cpf e saldo_inicial e
   segundo_titular,  coloque ( ; ) na divisão entre  os atributos.
"""

from model.conta import Conta

class PessoaFisica(Conta):

    __segundo_titular = ""
    __titular = ""
    __cpf = ""
    __saldo_inicial = 0.0

    @property
    def segundo_titular(self):
        return self.__segundo_titular
    @segundo_titular.setter
    def segundo_titular(self, segundo_titular):
        self.__segundo_titular = segundo_titular
    

    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    
    @property
    def saldo_inicial(self):
        return self.__saldo_inicial
    @saldo_inicial.setter
    def saldo_inicial(self, saldo_inicial):
        self.__saldo_inicial = saldo_inicial

    
    def __str__(self):
        return f"{super().__str__()}; {self.titular}; {self.cpf}; {self.saldo_inicial}; {self.segundo_titular}"