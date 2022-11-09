"""
EXERCICIO-04 crie um documento instanciando uma classe chamada animal, crie a um método string,
com a variável referência que acessa os atributos da classe no espaço alocado de memória.
Defina os atributos diretamente no retorno, raca, cor, idade. crie um segundo documento main com
variável referência animal 1, animal 2, animal 3, insira valores diferentes para cada atributo
através das variáveis de objeto, e imprima no terminal os dados inseridos.
"""

from animal import Animal

animal = Animal()

animal.raca = "Pastor Alemão"
animal.cor = "Marrom"
animal.idade = 4

print(animal)