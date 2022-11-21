from model.pessoaJuridica import PessoaJuridica

def create_pj(conta):

    contas = open("pessoaJuridica.txt", "a")
    contas.write(str(conta) + "\n")

    contas.close()


def read_pj():

    lista_conta = []

    contas = open("pessoaJuridica.txt", "r")

    for conta in contas:
        conta = conta.strip()
        conta_objeto = conta.split(";")

        conta = PessoaJuridica()

        conta.agencia = conta_objeto[0]
        conta.numero_agencia = conta_objeto[1]
        conta.titular = conta_objeto[2]
        conta.cnpj = conta_objeto[3]
        conta.saldo_inicial = conta_objeto[4]
        conta.segundo_titular = conta_objeto[5]

        lista_conta.append(conta)

    contas.close()

    return lista_conta


def update_pj(conta_update:PessoaJuridica):

    lista_contas = []

    contas = open("pessoaJuridica.txt", "r")

    for conta in contas:

        conta_objeto = conta.strip().split(";")

        if conta_update.cnpj == int(conta_objeto[3]):
            lista_contas.append(str(conta_update) + "\n")
        else:
            lista_contas.append(conta)

    contas.close()

    contas = open("pessoaJuridica.txt", "w")
    contas.writelines(lista_contas)
    contas.close()


def delete_pj(conta_delete:PessoaJuridica):

    lista_contas = []

    contas = open("pessoaJuridica.txt", "r")

    for conta in contas:

        conta_objeto = conta.strip().split(";")

        if conta_delete.cnpj != int(conta_objeto[3]):
            lista_contas.append(conta)

    contas.close()

    contas = open("pessoaJuridica.txt", "w")
    contas.writelines(lista_contas)
    contas.close()