from model import Conta
from controller import create, read

conta = Conta()

conta.titular = "David Simas" #input() aqui
conta.numero = 1111 #input() aqui
conta.saldo = 10000 #input() aqui

create(conta)

lista_contas = read()

for c in lista_contas:
    print(c)
