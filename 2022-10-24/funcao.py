from time import sleep

def contador(inicio, fim, passo):
    print("-" * 50)
    passo = abs(passo) if passo != 0 else 1 # define passo com o valor absoluto (deixa sinal positivo), e caso seja zero, recebe 1
    print(f"contagem de {inicio} até {fim}, de {passo} em {passo}") # print usando interpolação
    #sleep(0.5)

    if inicio < fim:
        for cont in range(inicio, fim, passo):
            print(cont, end=" ")
            #sleep(0.3)
    
    elif inicio > fim:
        for cont in range(inicio, fim, - passo):
            print(cont, end=" ")
            #sleep(0.3)
        print("\nFuncionando")

contador(10, 30, 2)
print()
print("-" * 15, "Personalize seu For", "-" * 15)

contador(int(input("Inicio: ")), int(input("Fim: ")), int(input("Passo: ")))