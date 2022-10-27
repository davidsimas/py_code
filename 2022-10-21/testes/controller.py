from datetime import datetime

def saudacao():
    hora = datetime.today().strftime("%H:%M")

    saudacao = " "
    if hora > ("06:00") and hora < ("12:00"):
        saudacao = "Bom dia."
    elif hora > ("12:00") and hora < ("18:00"):
        saudacao = "Boa tarde."
    else: 
        saudacao = "Boa noite."

    return hora, saudacao

def salvar(dados):
    with open("hospedes.txt", "a") as arquivo:
        arquivo.write(f"{dados}\n")

def listar():
    with open('hospedes.txt', 'r') as arquivo:
        print(arquivo.read())

def consultar(consulta):

    lista = []
    dicio = {}

    arquivo = open('hospedes.txt', 'r')

    achou = 0
    for i, c in enumerate(arquivo):
        print(i)
        dicio.update(c)
        lista.append(dicio)
        print(c)

    for i in range(len(lista)):
        print(lista[i])

#        if consulta == eval(c)['nome']:
#            print(c)
#            achou += 1
#
#    if achou == 0:
#        print("Hospede não cadastrado.")

        

"""
       
deletado = 0
    escolha = str(input('\n\033[96mDigite o nome do livro para ser deletado: \033[m'))
    for indLis, campos in enumerate(livraria): 
        if livraria[indLis]['nome'] == escolha:
            del livraria[indLis]
            deletado += 1 
        else:
            acaoDeletar = False



    return
lista = []
dicio = {}

i = 0
while i < 5:
    i += 1
    dicio.update({'Nome': 'David', 'CPF': '03335800958', 'Telefone': '999913988'})
    lista.append(dicio)

for i in range(len(lista)):
    print(lista[i])
"""