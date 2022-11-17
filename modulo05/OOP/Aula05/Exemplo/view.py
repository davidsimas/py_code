from model import Conta
from controller import create, read

conta = Conta()

conta.titular = "David Simas" #input() aqui
conta.numero = 1111 #input() aqui
conta.saldo = 10000 #input() aqui

#print(f"Aqui na VIEW {conta.titular}")
#print(f"Aqui na VIEW {conta.numero}")
#print(f"Aqui na VIEW {conta.saldo}")

create(conta)

lista_contas = read()

#print(lista_contas)

for c in lista_contas:
    print(c)
