def salvar1(dados):
    with open("dados_cadastral_ex02.txt", "a") as arquivo:
        arquivo.write(f"{dados}\n")