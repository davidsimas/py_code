from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

"""
- Crie uma variável de referência ao objeto de PessoaFisica e insira valores
  nos atributos do construtor.
- Faça um print utilizando interpolação e faça um cabeçalho Menu PessoaFisica Inicial
- Faça um print deste objeto,
- logo em seguida insira valores utilizando o set do segundo_titular e atribua um
  dado ao mesmo.
- Faça um print utilizando interpolação e faça um cabeçalho Menu PessoaFisica alterações.
- Realize a impressão novamente deste objeto para visualizar as alterações após inserir
  segundo titular.
"""


pessoa1 = PessoaFisica("David Simas", "111444", 1000)
print("-" * 15, "Menu", "-" * 15)
print(pessoa1)
pessoa1.segundo_titular = "Ana"
print("-" * 15, "Menu", "-" * 15)
print(pessoa1)

pessoa2 = PessoaJuridica("Felipe", "111444", 2547)
print("-" * 15, "Menu", "-" * 15)
print(pessoa2)
pessoa2.segundo_titular = "Maria"
print("-" * 15, "Menu", "-" * 15)
print(pessoa2)