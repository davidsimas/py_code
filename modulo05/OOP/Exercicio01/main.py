"""
EXERCICIO-01 crie um documento instanciando uma classe chamada Conta com atributos
número, titular, saldo, limite crie um método str com a variável referência que acessa
o objeto no espaço alocado de memória, acessando diretamente o objeto de conta. insira
os atributos na função através da variável referência padrão, e use f string para adicionar
ao return.
"""


from conta import Conta
# Objeto da minha classe
conta = Conta()
# Atribuindo valores aos atributos
conta.numero = 123456
conta.titular = "David"
conta.saldo = 120
conta.limite = 1200.0

# Imprimindo valores
print(conta)