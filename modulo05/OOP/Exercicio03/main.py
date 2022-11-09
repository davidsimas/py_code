"""
EXERCICIO-03 crie um documento instanciando uma classe chamada Pessoa com atributos
nome, cpf, idade. Crie um método str com a variável referência que acessa os atributos
da classe no espaço alocado de memória. insira os atributos na função através da variável
referência padrão, e use f string para adicionar ao return. crie um segundo documento
main com variável referência pessoa 1, pessoa 2, pessoa 3 insira valores diferentes
para cada objeto, imprima no terminal os dados inseridos.
"""

from pessoas import Pessoas

pessoas1 = Pessoas()

pessoas1.nome = "David"
pessoas1.cpf = "Simas"
pessoas1.idade = 41

print(pessoas1)

pessoas2 = Pessoas()

pessoas2.nome = "Ana"
pessoas2.cpf = "Silva"
pessoas2.idade = 25

print(pessoas2)

pessoas3 = Pessoas()

pessoas3.nome = "Oliver"
pessoas3.cpf = "Oliveira"
pessoas3.idade = 34

print(pessoas3)