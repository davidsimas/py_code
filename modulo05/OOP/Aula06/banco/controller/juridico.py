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
        # agencia, numero_agencia, titular, cpf e saldo_incial
        conta.agencia = conta_objeto[0]
        conta.numero_agencia = conta_objeto[1]
        conta.titular = conta_objeto[2]
        conta.cnpj = conta_objeto[3]
        conta.saldo_inicial = conta_objeto[4]
        conta.segundo_titular = conta_objeto[5]

        lista_conta.append(conta)

    contas.close()

    return lista_conta