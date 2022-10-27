def salvar(dados):
    with open("dados_cadastral_ex01.txt", "a") as arquivo:
        arquivo.write(f"{dados}\n")

def listar():
    with open("dados_cadastral_ex01.txt", "r") as arquivo:
        print(arquivo.read())