"""
EXERCICIO-03 crie um documento instanciando uma classe chamada Animal com atributos
espécie, cor, raça. Crie um método str com a variável referência que acessa os
atributos da classe no espaço alocado de memória. insira os atributos na função
através da variável referência padrão, e use f string para adicionar ao return. Crie
um segundo documento main com variável referência animal 1, animal 2, animal 3 e
insira valores diferentes para cada objeto, imprima no terminal os dados inseridos.
"""

from animal import Animal

animal = Animal()

animal.especie = "Canis Lupus Familiaris"
animal.cor = "Branca"
animal.raca = "Akita"

print(animal)

anima2 = Animal()

anima2.especie = "Felis Silvestris Catus"
anima2.cor = "Preta"
anima2.raca = "Siamês"

print(anima2)

anima3 = Animal()

anima3.especie = "Canis Lupus Familiaris"
anima3.cor = "Marrom"
anima3.raca = "Labrador"

print(anima3)