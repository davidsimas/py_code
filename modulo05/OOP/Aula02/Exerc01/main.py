"""
utilizando o conhecimento adquirido crie um documento com namespace conta e nome da classe
Conta, conforme orientação de boas práticas.
Crie o método construtor recebendo atributos, este método deve conter variável de referência
de acesso ao objeto, crie os seguintes atributos titular, número, saldo, limite
Usando __ antes do nome do atributo, torne-os privados sendo assim  os mesmos serão
acessíveis apenas na nossa classe.
 * Crie métodos set e get para cada atributo da classe, lembrando que o método set é (definir),
   e o método get é (pegar), essa condicional é necessária devido os nossos atributos estarem
   privados.
 * Crie um método str recebendo a variável de referência ao objeto, retorne com um f string,
   e atribua os métodos get de cada atributo privado da nossa classe. Crie um Documento com
   namespace Main a partir do documento conta importe a classe Conta.
 * Crie um objeto de conta e solicite ao usuário a atribuição de valores através de input para
   cada atributo do nosso construtor.
 * Crie um print descritivo para nome do titular número da conta e saldo, e usando os métodos
   get imprima os valores inseridos no nosso objeto, com um novo print realize a impressão de
   todos os valores dos nossos atributos. 
 - Crie um novo objeto conta2 e solicite ao usuário a atribuição de valores, através de input
   para cada atributo do nosso construtor.
 - Crie um print descritivo para nome do titular número da conta e saldo, e usando os métodos
   get imprima os valores inseridos no nosso objeto, com um novo print realize a impressão de
   todos os valores dos nossos atributos de conta2
"""

from conta import Conta

print("-" * 30, "Inicio", "-" * 30)

conta = Conta(input("Digite o seu nome: "),
          int(input("Digite o número da conta: ")),
        float(input("Digite o saldo da conta: R$")),
        float(input("Digite o limite da conta: R$")))


print("-" * 30, "Detalhe", "-" * 29)
print(f"""
    O titular {conta.get_titular()} proprietário da conta {conta.get_numero()}
    tem saldo de R$ {conta.get_saldo()} e limite de saldo R$ {conta.get_limite()}
""")

print("-" * 30, "Inicio", "-" * 30)

conta2 = Conta(input("Digite o seu nome: "),
          int(input("Digite o número da conta: ")),
        float(input("Digite o saldo da conta: R$")),
        float(input("Digite o limite da conta: R$")))

print("-" * 30, "Detalhe", "-" * 29)
print(f"""
    O titular {conta.get_titular()} proprietário da conta {conta.get_numero()}
    tem saldo de R$ {conta.get_saldo()} e limite de saldo R$ {conta.get_limite()}
""")