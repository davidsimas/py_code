from arquivo import salvar, listar # Trocar o nome arquivo para Controller

def menu():
    print("-" * 20, " Menu ", "-" * 20)

    cond = "sim"
    while cond == "sim":
        nome = salvar(input("digite o seu nome: "))
        cond = str(input("Deseja contiunar \n sim \n nao \n :> "))

menu()

print("A lista de nomes inseridos\n", listar())
