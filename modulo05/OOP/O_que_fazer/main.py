from conta import Conta

print("-" * 30, "Inicio menu", "-" * 30)

conta = Conta(input("Digite o seu nome: "),
          int(input("Digite o número da conta: ")),
        float(input("Digite o saldo da conta: ")),
        float(input("Digite o limite da conta: ")))
