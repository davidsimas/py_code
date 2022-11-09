"""
EXERCICIO-03 crie um documento instanciando uma classe chamada pessoa, crie a um método string, com
a variável referência que acessa os atributos da classe no espaço alocado de memória. Defina os
atributos diretamente no retorno, marca, modelo, valor. crie um segundo documento main com variável
referência pessoa 1, pessoa 2, pessoa 3, insira valores diferentes para cada atributo através das
variáveis de objeto, e imprima no terminal os dados inseridos
"""

from pessoas import Pessoas

pessoas = Pessoas()

pessoas.nome = "David"
pessoas.sobrenome = "Simas"
pessoas.idade = 41
pessoas.data_nascimento = "28/02/1981"

print(pessoas)