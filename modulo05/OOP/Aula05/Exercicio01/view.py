from model import Conta
from controller import create, read, update, delete

conta = Conta()


conta.titular = "David" #input() aqui
conta.numero = 1111 #input() aqui
conta.saldo = 80000 #input() aqui

#create(conta)

print("\n ----- Listando -----\n")
lista_contas = read()

for c in lista_contas:
    print(c)

update(conta) #passando o objeto como referencia


print("\n ----- Após o Update -----\n")
lista_contas = read()

for c in lista_contas:
    print(c)


# Funcionando
#delete(2222) # passando o numero da conta como referencia