"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho de uma pessoa
e cadastre-os através de um dicionário em um input , se o número da carteira de trabalho
for diferente de ZERO, o dicionário receberá através de uma condicional também os dados
do primeiro ano de contratação e o salário. ao final do programa imprima os dados
solicitados, esta construção deve ser feita através de funções
"""

import os
from controller import *


def cadastro():

    dados = {}
    dados["nome"] = str(input("Informe o nome completo: "))
    dados["Nascimento"] = str(input("Informe o ano de Nascimento: "))
    dados["Num_car_tra"] = str(input("Informe o número de Carteira de Trabalho: "))
    #print(dados["Num_car_tra"])
    if (dados["Num_car_tra"]) != "0":
        dados["pri_ano_cont"] = str(input("Informe o primeiro ano contratação: "))
        dados["salario"] = str(input("Informe o salário: "))

    salvar(dados)

def menu():
    opcao = "0"
    while opcao != "3":

        print("""

                [ 1 ] => Cadastrar Pessoa
                [ 2 ] => Imprimir Dados Cadastral
                [ 3 ] => Finalizar Atendimento

        """)
        opcao = str(input("Escolha uma opção: "))

        match opcao:
            case "1":
                os.system("cls")
                cadastro()

            case "2":
                os.system("cls")
                listar()

            case "3":
                os.system("cls")
                print("Finalizando o programa")

            case _:
                os.system("cls")
                print("Opção inválida")
                
menu()