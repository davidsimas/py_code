from model import Conta

def create(conta):
    #print(f"aqui na função create {conta}")
    conta = open("Aula05\conta1.txt", "a")
    conta.write(str(conta) + "\n")
    conta.close


def read():
    lista_conta = []
    contas = open("Aula05\conta.txt", "r")

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