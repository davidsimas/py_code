from animal import Animal
import os

lista_animal = []

def cadastrar_animal():

    animal = Animal(input("Informe a espécie: "),
                   (input("Informe a raça: ")),
                   (input("Informe o porte: ")),
                   (input("Informe a cor: ")))
    return animal


def imprime_dados(animal):

    print(f"""
    Espécie: {animal.especie}.
    Raça: {animal.raca}.
    Porte: {animal.porte}.
    Cor: {animal.cor}.
    """)


def menu():
    opcao = "0"
    while opcao != "3":

        print("""

                [ 1 ] => Cadastrar Pessoa
                [ 2 ] => Imprimir Dados Cadastral
                [ 3 ] => Finalizar

        """)
        opcao = str(input("Escolha uma opção: "))

        match opcao:
            case "1":
                os.system("cls")
                lista_animal.append(cadastrar_animal())

            case "2":
                os.system("cls")
                for objeto in lista_animal:
                    imprime_dados(objeto)

            case "3":
                os.system("cls")
                print("Finalizando o programa")

            case _:
                os.system("cls")
                print("Opção inválida")

menu()