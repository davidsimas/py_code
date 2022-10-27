"""
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: inicio, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
 - A) De 1 até 10, de 1 em 1
 - B) De 10 até 0, de 2 em 2
 - C) Uma contagem personalizada 
"""

from time import sleep

def contador(inicio, fim, passo):
    print()
    print("-" * 50)

    if inicio < fim:
        for cont in range(inicio, fim, passo):
            sleep(0.3)
            print(cont, end=" ")

    elif inicio > fim:
        for cont in range(inicio, fim, - passo):
            sleep(0.3)
            print(cont, end=" ")

contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
contador(int(input("Inicio: ")), int(input("Fim: ")), int(input("Passo: ")))