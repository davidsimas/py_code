from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

pessoa1 = PessoaFisica("David Simas", "111444", 1000)
print("-" * 25, "Menu", "-" * 25)
print(pessoa1)
pessoa1.segundo_titular = "Ana"
print("-" * 25, "Menu", "-" * 25)
print(pessoa1)

pessoa2 = PessoaJuridica("Felipe", "111444", 2547)
print("-" * 25, "Menu", "-" * 25)
print(pessoa2)
pessoa2.segundo_titular = "Maria"
print("-" * 25, "Menu", "-" * 25)
print(pessoa2)