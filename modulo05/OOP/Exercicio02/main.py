"""
EXERCICIO-02 crie um documento instanciando uma classe chamada carro com atributos marca,
modelo, valor. Crie um método str com a variável referência que acessa os atributos da
classe no espaço alocado de memória. insira os atributos na função através da variável
referência padrão, e use f string para adicionar ao return. crie um segundo documento main
com variável referência carro 1, carro 2, carro 3, insira valores diferentes para cada
objeto, imprima no terminal os dados inseridos.
"""

from carro import Carro

carro1 = Carro()

carro1.marca = "Fiat"
carro1.modelo = "Ducato"
carro1.valor = 20000.00

print(carro1)

carro2 = Carro()

carro2.marca = "Ford"
carro2.modelo = "Transit"
carro2.valor = 21000.00

print(carro2)

carro3 = Carro()

carro3.marca = "Renault"
carro3.modelo = "Master"
carro3.valor = 18000.00

print(carro3)