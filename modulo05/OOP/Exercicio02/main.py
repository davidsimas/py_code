"""
EXERCICIO-02 crie um documento instanciando uma classe chamada carro, crie a um método string, com a
variável referência que acessa os atributos da classe no espaço alocado de memória. Defina os atributos
diretamente no retorno, marca, modelo, valor. crie um segundo documento main com variável referência
carro 1, carro 2, carro 3, insira valores diferentes para cada atributo através das variáveis de objeto
e imprima no terminal os dados inseridos.
"""

from carro import Carro
# Objeto da minha classe
carro = Carro()
# Atribuindo valores aos atributos
carro.marca = "Fiat"
carro.modelo = "Ducato"
carro.valor = 2000.00

# Imprimindo valores
print(carro)