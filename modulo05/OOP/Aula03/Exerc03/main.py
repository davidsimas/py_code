from conta import Conta

def menu():
    print("-" * 30, "Inicio", "-" * 30)
    conta1 = Conta(input("Informe o titular da conta: "),
                  (input("Informe o número da conta: ")),
                  (input("Informe o saldo da conta: ")),
                  (input("Informe o limite da conta: ")))


    print("-" * 30, "Detalhe", "-" * 29)
    print(f"""

        Marca do veiculo: {conta1.marca}
        Modelo do veiculo: {conta1.modelo}
        Cor do veiculo: {conta1.cor}
        Categoria do veiculo: {conta1.categoria}

    """)

menu()