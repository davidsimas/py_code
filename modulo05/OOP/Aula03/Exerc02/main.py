from carro import Carro

def menu():
    print("-" * 30, "Inicio", "-" * 30)
    carro1 = Carro(input("Informe a marca do carro: "),
                (input("Informe o modelo do carro: ")),
                (input("Informe a cor do carro: ")),
                (input("Informe a categoria do carro: ")))


    print("-" * 30, "Detalhe", "-" * 29)
    print(f"""

        Marca do veiculo: {carro1.marca}
        Modelo do veiculo: {carro1.modelo}
        Cor do veiculo: {carro1.cor}
        Categoria do veiculo: {carro1.categoria}

    """)

menu()