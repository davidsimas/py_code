from controller import soma, subtracao, multiplicacao, divisao

def menu():
    print("-" * 20, " Menu ", "-" * 20)

    cond = "sim"
    while cond == "sim":
        while True:
            try:
                n1 = int(input("Número: "))
                n2 = int(input("Número: "))
                break
            except ValueError:
                print("\nVocê não digitou um número válido.")

        print("""\nEscolha um operação aritmética

        [ 1 ] => Somar
        [ 2 ] => Subtrair
        [ 3 ] => Multiplicar
        [ 4 ] => Dividir
        """)
        opcao = str(input("Qual a sua opção: "))
        match opcao:

            case "1":
                resultado = soma(n1, n2)
                print("\nA soma entre os números {} e {} é {:.2f}".format(n1, n2, resultado))
                
            case "2":
                resultado = subtracao(n1, n2)
                print("\nA subtração entre os números {} e {} é {:.2f}".format(n1, n2, resultado))

            case "3":
                resultado = multiplicacao(n1, n2)
                print("\nA multiplicação entre os números {} e {} é {:.2f}".format(n1, n2, resultado))

            case "4":
                resultado = divisao(n1, n2)
                print("\nA divisão entre os números {} e {} é {:.2f}".format(n1, n2, resultado))

            case _:
                print("\nOpção inválida")

        cond = str(input("\nDeseja continuar? [ sim \ não ]\n "))


menu()
