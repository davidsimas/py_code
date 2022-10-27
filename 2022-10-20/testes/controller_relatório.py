def listar():
    names = []
    with open("hospedes.txt", "r") as arquivo:
        for name in arquivo:
            names.append(name)

    return names