"""
utilizando o conhecimento adquirido crie um documento com namespace e nome da classe,
conforme orientação de boas práticas.

 - Crie o método construtor recebendo atributos, este método deve conter variável de
   referência de acesso ao objeto, crie os seguintes atributos titular, número, saldo, limite
 - Crie um método encapsulando o extrato de uma conta, o extrato deve imprimir o número
   da conta, o nome do titular e o saldo inicial depositado.
 - Crie um método depositar, utilizando o atributo específico do método (valor), no
   encapsulamento acesse os atributos da classe e utilizando os operadores relacionais
   de incremento receba o atributo do método em questão e retorne o mesmo.
 - Crie um método sacar utilizando o atributo específico do método (valor), no encapsulamento
   acesse os atributos da classe e utilizando operadores relacionais de decremento, retorne
   o atributo do método
 - Crie um método transferir, utilizando os atributos específicos do método valor origem
   e destino. no encapsulamento acesse os atributos do método e atribua as funções sacar
   depositar recebendo o atributo valor.
 - Crie um documento main, faça um cabeçalho com print, logo em seguida a variável recebendo
   o Objeto da classe, atribua descritivamente input solicitando os valores digitados para
   cada atributo específico do nosso construtor. utilize os métodos extrato, depositar e sacar
   Para manipular nosso objeto.
 - Crie uma segunda variável recebendo o Objeto da classe, faça um cabeçalho com print, e
   atribua descritivamente input solicitando os valores digitados para cada atributo
   específico do nosso construtor, utilize os métodos extrato, transferir manipule de
   forma visual as impressões do extrato para visualizar a nossa transferência.
"""

from conta import Conta
 

conta1 = Conta("David", 101, 10000, 15000)

#conta1.titular = "David"
#conta1.numero = 101
#conta1.saldo = 10000.0
#conta1.limite = 15000.0
# Colocar os inputs dentro da instancia
conta2 = Conta("Ana", 201, 1000, 1000)

#conta2.titular = "Ana"
#conta2.numero = 201
#conta2.saldo = 1000.0
#conta2.limite = 1000.0

print("-" * 25 + " Inicio " + "-" * 25)
print(conta1.extrato())
print()

print("-" * 25 + " Deposito " + "-" * 25)
print(conta1.depositar(float(input("Insira o valor do deposito R$"))))
print()
print("-" * 25 + " Extrato " + "-" * 25) 
print(conta1.extrato())
print()

print("-" * 25 + " Sacar " + "-" * 25)
print(conta1.sacar(float(input("Insira o valor do saque R$"))))
print()
print("-" * 25 + " Extrato " + "-" * 25) 
print(conta1.extrato())
print()

conta2.transferir(float(input("Insira o valor a ser transferido R$")), conta2, conta1)

print("-" * 25 + " Extrato " + "-" * 25) 
print(conta1.extrato())
print(conta2.extrato())
print()