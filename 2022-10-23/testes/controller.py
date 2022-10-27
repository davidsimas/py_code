from datetime import datetime

def saudacao(hora):

    saudacao = " "
    if hora > ("06:00") and hora < ("12:00"):
        saudacao = "Bom dia."
    elif hora > ("12:00") and hora < ("18:00"):
        saudacao = "Boa tarde."
    else: 
        saudacao = "Boa noite."

    return saudacao

def salvar(dados):
    with open("hospedes.txt", "a") as arquivo:
        arquivo.write(f"{dados}\n")

def listar():
    with open("hospedes.txt", "r") as arquivo:
        print(arquivo.read())

def consultar(consulta):

    achou = 0
    with open("hospedes.txt", "r") as arquivo:
        for linha in arquivo:
            if consulta == eval(linha)["nome"]:
                print(linha)
                achou += 1

def fazer_check_out(check_out):

    lista = []
    dicio = {}

    with open("hospedes.txt", "r") as arquivo:
        for linha in arquivo:
            if check_out != eval(linha)["nome"]:
                dicio = eval(linha)
                lista.append(dicio)

    with open("hospedes.txt", "w") as arquivo:
        for i, dados in enumerate(lista):
            arquivo.write(f"{dados}\n")
    print("Check-Out realizado...")
    