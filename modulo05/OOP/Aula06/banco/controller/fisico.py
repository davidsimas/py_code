from model.pessoaFisica import PessoaFisica

def create_psf(conta):

    contas = open("pessoafisica.txt", "a")
    contas.write(str(conta) + "\n")

    contas.close()


def read_psf():

    lista_conta = []

    contas = open("pessoafisica.txt", "r")

    for conta in contas:
        conta = conta.strip()
        conta_objeto = conta.split(";")

        conta = PessoaFisica()

        conta.agencia = conta_objeto[0]
        conta.numero_agencia = conta_objeto[1]
        conta.titular = conta_objeto[2]
        conta.cpf = conta_objeto[3]
        conta.saldo_inicial = conta_objeto[4]
        conta.segundo_titular = conta_objeto[5]

        lista_conta.append(conta)

    contas.close()

    return lista_conta


def update_psf(conta_update:PessoaFisica):

    lista_contas = []

    contas = open("pessoafisica.txt", "r")

    for conta in contas:

        conta_objeto = conta.strip().split("; ")

        if conta_update.cpf == conta_objeto[3]:
            lista_contas.append(str(conta_update) + "\n")
        else:
            lista_contas.append(conta)

    contas.close()

    contas = open("pessoafisica.txt", "w")
    contas.writelines(lista_contas)
    contas.close()


def delete_psf(numero_cpf):

    lista_contas = []

    contas = open("pessoafisica.txt", "r")

    for conta in contas:

        conta_objeto = conta.strip().split(";")

        if numero_cpf != int(conta_objeto[3]):
            lista_contas.append(conta)

    contas.close()

    contas = open("pessoafisica.txt", "w")
    contas.writelines(lista_contas)
    contas.close()