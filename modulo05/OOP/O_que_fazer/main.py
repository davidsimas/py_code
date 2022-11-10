from conta import Conta

print("-" * 30, "Inicio menu", "-" * 30)


conta = Conta(input("Digite o seu nome: "),
          int(input("Digite o número da conta: ")),
        float(input("Digite o saldo da conta: R$")),
        float(input("Digite o limite da conta: R$")))


print("-" * 30, "Inicio menu", "-" * 30)


print(conta)


"""
conta.set_titular(input("Digite o seu nome: "))
conta.set_numero(int(input("Digite o número da conta: ")))
conta.set_saldo(float(input("Digite o saldo da conta: R$")))
conta.set_limite(float(input("Digite o limite da conta: R$")))
"""