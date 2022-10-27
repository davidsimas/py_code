"""
Utilizando os conhecimentos adquiridos nas aulas anteriores onde foram feitos códigos estruturados,
estamos incrementando o Python funcional. crie um projeto com o nome Calculadora python, depois crie
um documento chamado controller dentro deste documento deve conter 4 funções com as operações básicas
matemáticas. crie um outro documento chamado main, este documento deve estar importando as 4 operações
matemáticas. crie uma função print solicitando dados ao usuário esta funcao deve ser com tipo predefinido
tipo flutuante. deve ser utilizado o conceito de interpolação para criar um cabeçalho de um menu, dentro
deste menu deve conter a possibilidade de fazer a impressão dos dados inseridos pelo usuário, permitindo
assim o usuário escolher uma das 4 operações matemáticas importadas, consequentemente imprimindo assim o
resultado desejado dos dados inseridos.
"""
import controller

while True:
    try:
        num01 = float(input("Digite o primeiro numero: "))
        num02 = float(input("Digite o segundo numero: "))
        break
    except ValueError:
        print("\nVocê não digitou um número válido.")
 
try:
    opcao = "0"
    while opcao != "5":
    
        print("\nOs números digitados formam {:.2f} e {:.2f}".format(num01, num02))
        print("""\nEscolha um operação aritmética

        [ 1 ] => Somar
        [ 2 ] => Subtrair
        [ 3 ] => Multiplicar
        [ 4 ] => Dividir
        [ 5 ] => Sair...
        """)
        opcao = str(input("Qual a sua opção: "))

        match opcao:

            case "1":
                resultado = controller.soma(num01, num02)
                print("\nO resultado da soma foi: {:.2f}".format(resultado))

            case "2":
                resultado = controller.subtracao(num01, num02)
                print("\nO resultado da subtração foi: {:.2f}".format(resultado))

            case "3":
                resultado = controller.multiplicacao(num01, num02)
                print("\nO resultado da multiplicação foi: {:.2f}".format(resultado))

            case "4":
                resultado = controller.divisao(num01, num02)
                print("\nO resultado da divisão foi: {:.2f}".format(resultado))

            case "5":
                print("\nVocê saiu do programa")

            case _:
                print("\nOpção inválida")

    print("\nFim do programa.")

except ValueError:
    print("\nOops! Esse não é um número válido. Tente novamente...")
