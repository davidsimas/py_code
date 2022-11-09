"""
EXERCICIO-01 crie um documento instanciando uma classe chamada conta, crie um método string, com a
variável referência que acessa os atributos da classe no espaço alocado de memória, acessando
diretamente o objeto de conta insira dados internos na função através da variável referência padrão,
e insira atributos recebendo valores internos número, titular, saldo, limite. Através de variáveis.
"""

from conta import Conta
# Objeto da minha classe
conta = Conta()
# Atribuindo valores aos atributos
conta.numero = 123456
conta.titular = 'Lirinha'
conta.saldo = 120
conta.limite = 1200.0

# Imprimindo valores
print(conta)