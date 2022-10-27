def salvar(dados):
    with open("dados_cadastral_ex02.txt", "a") as arquivo:
        arquivo.write(f"{dados}\n")

def total_pessoas():
    with open("dados_cadastral_ex02.txt", "r") as arquivo:
        total = 0
        for linha in arquivo:
            #print(type(eval(linha)))
            total += 1

    return total

def media_idade():
    total = total_pessoas()
    with open("dados_cadastral_ex02.txt", "r") as arquivo:
        idade = 0
        # Percorre as linhas do arquivo
        for linha in arquivo:
            # Transforma cada linha em uma Lista
            lista = eval(linha)
            # Percorre a lista
            for c in lista:
                # Converte "Idade" de String em Inteiro e soma as idades
                idade += int(c["Idade"])

        return idade / total

def lista_feminina():
    with open("dados_cadastral_ex02.txt", "r") as arquivo:
        for linha in arquivo:
            lista = eval(linha)
            for c in lista:
                if (c["Sexo"]) == "F":
                    print(c)

def pessoas_acima_media():
    media = media_idade()
    with open("dados_cadastral_ex02.txt", "r") as arquivo:
        for linha in arquivo:
            lista = eval(linha)
            for c in lista:
                if (c["Idade"]) > str(media):
                    print(c)



"""
Teste de codigos........
Somente DELETAR

def media_idade():
    total = total_pessoas()
    with open("dados_cadastral_ex02.txt", "r") as arquivo:
        idade = 0
        # Percorre o arquivo
        for linha in arquivo:
            # Transforma cada linha em uma Lista
            list = eval(linha)
            # Percorre a lista
            for c in list:
                # Converte "Idade" de String em Inteiro e soma as idades
                idade += int(c["Idade"])

        return idade / total

            for c in list:
                print(c["Idade"])
                idade = int(c["Idade"])
                print(type(idade))


y = eval("[{'nome': 'Da', 'Sexo': 'M', 'Idade': '40'}]")

for x in y:
    print(x)
    print(x['nome'])
    input()
    for linha in arquivo:
        dicio = eval(linha)
        lista.append(dicio)

    for i, c in enumerate(lista):
        print(i)
        print(c.keys())
        print(c.values())
"""