"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas
pessoas foram cadastradas; B) A média de idade do grupo; C) Uma lista com todas as mulheres;
D) Uma lista com todas as pessoas com idade acima da média.
"""
import os
from controller import *


def cadastro():

    dados = {}
    lista = []

    dados["nome"] = str(input("Informe o nome completo: "))
    dados["Sexo"] = str(input("Informe o sexo: "))
    dados["Idade"] = str(input("Informe a sua idade: "))
    lista.append(dados)
    salvar1(lista)

def menu():
    opcao = "0"
    while opcao != "6":

        print("""

                [ 1 ] => Cadastrar pessoa
                [ 2 ] => Quantas pessoas foram cadastradas
                [ 3 ] => A média de idade do grupo
                [ 4 ] => Uma lista com todas as mulheres
                [ 5 ] => Uma lista com todas as pessoas com idade acima da média
                [ 6 ] => Finalizar Atendimento

        """)
        opcao = str(input("Escolha uma opção: "))

        match opcao:
            case "1":
                os.system("cls")
                cadastro()

            case "2":
                os.system("cls")

            case "3":
                os.system("cls")

            case "4":
                os.system("cls")

            case "5":
                os.system("cls")

            case "6":
                os.system("cls")
                print("Finalizando o programa")

            case _:
                os.system("cls")
                print("Opção inválida")
                
menu()