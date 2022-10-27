def salvar(nome):
    with open('pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome}\n')


def listar():
    names = []
    with open('pessoas.txt', 'r') as arquivo:
        for name in arquivo:
            name = name.strip()
            names.append(name)

    return names

#salvar('David')
print("Lista de nome", listar())