from pessoa import Pessoas

def imprime_dados(pessoas):
    print("-" * 60)
    print(f"""
        {pessoas.get_nome()} com o CPF {pessoas.get_cpf()}
        {pessoas.get_nome()} com a idade de {pessoas.get_idade()} anos
        {pessoas.get_nome()} com altura de {pessoas.get_altura():.2f} Metros
    """)

print("-" * 60)
pessoas1 = Pessoas(input("Digite o seu nome: "),
                 (input("Digite o sue C.P.F: ")),
              int(input("Digite a sua idade: ")),
            float(input("Digite a sua altura : ")))

imprime_dados(pessoas1)

print("-" * 60)
pessoas2 = Pessoas(input("Digite o seu nome: "),
                 (input("Digite o sue C.P.F: ")),
              int(input("Digite a sua idade: ")),
            float(input("Digite a sua altura : ")))

imprime_dados(pessoas2)
