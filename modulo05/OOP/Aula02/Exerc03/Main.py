from carro import Carro

def imprime_dados(carro):

    print("-" * 60)
    print(f"""
    Marco do carro: {carro.get_marca()}.
    Modelo do carro: {carro.get_modelo()}.
    Cor do carro: {carro.get_cor()}.
    Categoria do carro: {carro.get_categoria()}.
    """)

print("-" * 60)
carro1 = Carro(input("Informe a marca do carro: "),
              (input("Informe o modelo do carro: ")),
              (input("Informe a cor do carro: ")),
              (input("Informe a categoria do carro: ")))

imprime_dados(carro1)

print("-" * 60)
carro2 = Carro(input("Informe a marca do carro: "),
              (input("Informe o modelo do carro: ")),
              (input("Informe a cor do carro: ")),
              (input("Informe a categoria do carro: ")))

imprime_dados(carro2)