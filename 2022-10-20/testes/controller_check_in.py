# Fazer as verificações

def salvar(dados):
    with open("hospedes.txt", "a") as arquivo:
        arquivo.write(f"{dados}")