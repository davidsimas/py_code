# # Importando Classes da Model
from model.pessoaFisica import PessoaFisica

# Função para criação de nova Conta
def create_psf(conta):

    # Abertura do Arquivo.txt em modo escrita
    contas = open("pessoafisica.txt", "a")
    # Escrevento no Arquivo.txt o conteudo do parametro conta
    contas.write(str(conta) + "\n")
    # Fechando Arquivo.txt
    contas.close()


# Função para listar as contas
def read_psf():

    # Criando uma lista vazia
    lista_conta = []
    # Abertura do Arquivo.txt em modo leitura
    contas = open("pessoafisica.txt", "r")
    # Estrutura de repetição FOR para leitura do Arquivo.txt
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
    # Fechando Arquivo.txt
    contas.close()

    return lista_conta


# Função para Atualizar a Conta
def update_psf(conta_update:PessoaFisica):

    # Criando uma lista vazia
    lista_contas = []
    # Abertura do Arquivo.txt em modo leitura
    contas = open("pessoafisica.txt", "r")

    for conta in contas:

        conta_objeto = conta.strip().split("; ")

        if conta_update.cpf == int(conta_objeto[3]):
            lista_contas.append(str(conta_update) + "\n")
        else:
            lista_contas.append(conta)
    # Fechando Arquivo.txt
    contas.close()
    # Abertura do Arquivo.txt mas sobreescrevendo o arquivo
    contas = open("pessoafisica.txt", "w")
    contas.writelines(lista_contas)
    # Fechando Arquivo.txt
    contas.close()


# Função para Deletar uma Conta
def delete_psf(conta_delete:PessoaFisica):

    # Criando uma lista vazia
    lista_contas = []
    # Abertura do Arquivo.txt em modo leitura
    contas = open("pessoafisica.txt", "r")

    for conta in contas:

        conta_objeto = conta.strip().split(";")

        if conta_delete.cpf != int(conta_objeto[3]):
            lista_contas.append(conta)
    # Fechando Arquivo.txt
    contas.close()
    # Abertura do Arquivo.txt mas sobreescrevendo o arquivo
    contas = open("pessoafisica.txt", "w")
    contas.writelines(lista_contas)
    # Fechando Arquivo.txt
    contas.close()