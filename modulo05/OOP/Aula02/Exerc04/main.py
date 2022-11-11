from animal import Animal

def imprime_dados(animal):

    print("-" * 60)
    print(f"""
    Espécie: {animal.get_especie()}.
    Raça: {animal.get_raca()}.
    Porte: {animal.get_porte()}.
    Cor: {animal.get_cor()}.
    """)


print("-" * 60)
animal1 = Animal(input("Informe a espécie: "),
                (input("Informe a raça: ")),
                (input("Informe o porte: ")),
                (input("Informe a cor: ")))


imprime_dados(animal1)

print("-" * 60)
animal2 = Animal(input("Informe a espécie: "),
                (input("Informe a raça: ")),
                (input("Informe o porte: ")),
                (input("Informe a cor: ")))

imprime_dados(animal2)