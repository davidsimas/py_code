livraria = []

cadastro = "S"
while cadastro == "S":
    nome = str(input("Informe o Nome do livro: "))
    editora = str(input("Informe a Editora do livro: "))
    autor = str(input("Informe o Autor do livro: "))
    genero = str(input("Informe o Gênero do livro: "))
    ano = str(input("Informe o Ano de lançamento do livro: "))
    isbn = str(input("Informe o ISBN do livro: "))

    livro = {'Nome': nome,
          'Editora': editora,
          'Autor': autor,
          'Genero': genero,
          'Ano': ano,
          'ISBN': isbn}

    livraria.append(livro)

    cadastro = str(input("Deseja cadastrar outro livro? [ S ] ou [ N ]. ")).upper().strip()

# Calcula o tamanho de cada campo da tabela
tamanhoCampo = [8, 8, 8, 8, 8, 8]
espacoCampo = [8, 8, 8, 8, 8, 8]

for x, y in enumerate(livraria):
    cont = 0
    for i in y.values():
        if len(i) <= 8:
            tamanhoCampo[cont] = 6
            espacoCampo[cont] = 6
        elif (len(i) > 8) and (len(i) < 30):
            tamanhoCampo[cont] = len(i)
            espacoCampo[cont] = len(i)
        elif len(i) >= 30:
            tamanhoCampo[cont] = 30
            espacoCampo[cont] = 30
        cont += 1       

linha ="-" * (sum(tamanhoCampo) + 7 + 12)
print(linha)
cont = 0
for label in livro:
    print(f"| {label[0:espacoCampo[cont]]:^{tamanhoCampo[cont]}} ", end="")
    cont += 1
print("|")
print(linha)

for indLis, campos in enumerate(livraria):
    cont = 0
    for indDic in campos.values():
        print(f"| {indDic[0:espacoCampo[cont]]:{tamanhoCampo[cont]}} ", end="")
        cont +=1
    print("|")
print(linha)