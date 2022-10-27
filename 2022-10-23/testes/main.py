import os
from controller import *

hora = datetime.today().strftime("%H:%M")

print("\n", hora, "\n")
print("{} Seja bem vindo ao Hotel Enterprise".format(saudacao(hora)))

def menu():
    opcao = "0"
    while opcao != "5":

        print("""

                [ 1 ] => Fazer Check-In
                [ 2 ] => Relatório Hospedes
                [ 3 ] => Procurar Hospedes
                [ 4 ] => Fazer Check-Out
                [ 5 ] => Finalizar Atendimento

        """)
        opcao = str(input("Escolha uma opção: "))

        match opcao:
            case "1":
                os.system("cls")
                dados = {}
                dados["nome"] = str(input("Informe o nome completo: "))
                dados["cpf"] = str(input("Informe o CPF: "))
                dados["telefone"] = str(input("Informe o telefone: "))
                salvar(dados)

            case "2":
                os.system("cls")        
                listar()

            case "3":
                os.system("cls")
                consulta = str(input("Informe o nome do hospede para consulta: "))
                consultar(consulta)

            case "4":
                os.system("cls")
                check_out = str(input("Informe o nome do hospede para Check Out: "))
                fazer_check_out(check_out)

            case "5":
                os.system("cls")
                print("Finalizando o programa")

            case _:
                os.system("cls")
                print("Opção inválida")

menu()
