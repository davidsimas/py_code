import os
from time import sleep

import controller
import controller_check_in
import controller_relatório

    # Função leitura de dados Check-In

def fazer_check_in():
    nome = str(input("Informe o nome completo: "))
    cpf = str(input("Informe o CPF: "))
    telefone = str(input("Informe o telefone: "))

    return nome, cpf, telefone


    # Saudação

saudacao = controller.saudacao()

print("\n", saudacao[0], "\n")
print("{} Seja bem vindo ao Hotel Enterprise".format(saudacao[1]))

    # Menu do sistema

opcao = "0"
while opcao != "5":

    controller.menu()
    opcao = str(input("Escolha uma opção: "))

    match opcao:
        case "1":
            # Limpar a tela
            os.system("cls")
            #print("\nOpção fazer Check-In\n")
            dados = fazer_check_in()
            controller_check_in.salvar(dados)

        case "2":
            os.system("cls")
            print("\nOpção relatório Hospedes\n")
            print("Lista de nome", controller_relatório.listar())            
            input()

        case "3":
            os.system("cls")
            print("\nOpção procurar Hospedes\n")
            input()
            os.system("cls")

        case "4":
            os.system("cls")
            print("\nOpção fazer Check-Out\n")
            input()

        case "5":
            os.system("cls")
            print("Finalizando o programa")
            input()

        case _:
            os.system("cls")
            print("Opção inválida")
