"""
Faça um programa que solicite o nome de um aluno solicite também a inserção das últimas três
notas este cálculo deve realizar a média desse aluno e através desta condição deve ser impresso
o nome do aluno, as três notas digitadas e a média final, e deve ser impresso se o aluno
foi aprovado ou nao!
"""
import os

dados = {}

def cadastro():        

        dados["Nome"] = str(input("Informe o nome do Aluno: "))
        dados["Nota_01"] = float(input("Informe a primeira nota: "))
        dados["Nota_02"] = float(input("Informe a segunda nota: "))
        dados["Nota_03"] = float(input("Informe a terceira nota: "))

def media():

    soma = 0
    for indice in dados:
        if dados[indice] != dados["Nome"]:
            soma += dados[indice]
    dados["Media"] = media = soma  / 3

    if media >= 7:
        dados["Situacao"] = ("Aprovado")
    else:
        dados["Situacao"] = ("Reprovado")
        
def relatorio():

    print(dados)


cadastro()
media()
relatorio()
