from model import Conta

def create(conta):

    contas = open("conta.txt", "a")
    contas.write(str(conta) + "\n")

    contas.close()


def read():

    lista_conta = []

    contas = open("conta.txt", "r")

    for contar in contas:
        contar = contar.strip()
        conta_objeto = contar.split(";")
        #print(f"Aqui Conta Objeto {conta_objeto}")

        conta = Conta()
        conta.titular = conta_objeto[0]
        conta.numero = conta_objeto[1]
        conta.saldo = conta_objeto[2]

        lista_conta.append(conta)

    contas.close

    return lista_conta


def update(conta_update:Conta):

    lista_contas = []

    contas = open("conta.txt", "r")

    for conta in contas:
        conta_limpa = conta.strip()
        conta_objeto = conta_limpa.split(";")

        if conta_update.numero == int(conta_objeto[1]):
            lista_contas.append(str(conta_update) + "\n")
        else:
            lista_contas.append(conta)

    contas.close()

    contas = open("conta.txt", "w")
    contas.writelines(lista_contas)
    contas.close()


def delete(numero_conta):

    lista_contas = []

    contas = open("conta.txt", "r")

    for conta in contas:

        conta_limpa = conta.strip()
        conta_objeto = conta_limpa.split(";")

        if numero_conta != int(conta_objeto[1]):
            lista_contas.append(conta)

    contas.close()

    contas = open("conta.txt", "w")
    contas.writelines(lista_contas)
    contas.close()

"""
David;1111;10000
Joao;2222;10000
Anas;3333;10000
Vitoria;4444;10000
Neo;5555;10000
"""