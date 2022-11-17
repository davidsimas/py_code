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
        print(f"Aqui Conta Objeto {conta_objeto}")

        conta = Conta()
        conta.titular = conta_objeto[0]
        conta.numero = conta_objeto[1]
        conta.saldo = conta_objeto[2]

        lista_conta.append(conta)

    contas.close

    return lista_conta