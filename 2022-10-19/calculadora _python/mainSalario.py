"""
crie novo documento mainSalario Crie variáveis com tipos predefinidos que suportem a inserção de dados com casas
decimais representando os 4 últimos salários de uma pessoa. crie uma função de impressão de dados para definir o
cabeçalho de uma calculadora, utilizando o conceito de polimorfismo e imprima a palavra, Calculadora no centro da
sua aplicação console. utilizando o conceito de máscara de substituição imprima descritivamente cada salário e a
soma entre os mesmos imprimindo o resultado final. Ex " primeira variável : {} " os dados devem ser apresentados
um em cada linha na sua aplicação console, deve ser utilizado os caracteres especiais de quebra de linha e na
impressão deve apresentar apenas duas casas após a vírgula imprima no final utilizando a variável de soma para
imprimir o resultado final do seu exercício. no documento controller crie uma função para calcular a soma do salario
"""
from controller import somaSalario

def linha():
    label = "Calculadora Salário"
    print("=" * 20 + " {:^} ".format(label) + "=" * 20)


while True:
    try:
        salario01 = float(input("Informe o salário de Outubro: R$"))
        break
    except ValueError:
        print("Você não digitou um número válido.")
while True:
    try:
        salario02 = float(input("Informe o salário de Setembro: R$"))
        break
    except ValueError:
        print("Você não digitou um número válido.")
while True:
    try:
        salario03 = float(input("Informe o salário de Agosto: R$"))
        break
    except ValueError:
        print("Você não digitou um número válido.")
while True:
    try:
        salario04 = float(input("Informe o salário de Julho: R$"))
        break
    except ValueError:
        print("Você não digitou um número válido.")

total = somaSalario(salario01, salario02, salario03, salario04)

linha()

print("\n\t- Outubro R${:.2f} \n\t- Setembro R${:.2f} \n\t- Agosto R${:.2f} \n\t- Julho R${:.2f} \n\tTotal R${:.2f}".format(salario01, salario02, salario03, salario04, total))
