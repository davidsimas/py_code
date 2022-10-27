from datetime import datetime
from time import sleep

listaClientes = []

# Saudação variável

print('''
                                                     _                 _
                                                 ___/|\_______________/|\___
                                                /~^/|||\ ~~ ~~~  ~~ ^/|||\~^\ 
                                               /^~/|||||\~~  ^^~  ^~/|||||\~~\ 
                                         ()   /~~/|||||||\ ~^~_~^~ /|||||||\~~\ 
                                        (()) /~^/| / | \ |\^~/|\~^/| / | \ |\~~\ 
                                        ((()/~~/||_)_|_(_||\/|||\/||_)_|_(_||\~~\ 
                                        )()/~~ ~~^ ^~^~ ~~ /|||||\ ~~ ~^~^ ^~~ ~~\ ()
                                        ()()||||||||||| {} ||||||||| (()
                                        ()))|||||||||||||/|||||||||\|||||||||||||()()
                                        (())|| / | | \ |||| |+|+| |||| / | | \ ||()))
                                        ())(||_)_|_|_(_|||| |+|+| ||||_)_|_|_(_||(())
                                        (())|||||||||||||||_|+|+|_|||||||||||||||())(
                                            @@@ @@@ @@@ @@@|-------|@@@ @@@ @@@ @@@ 
'''.format('HOTEL GUIDOLOOP'))

hora = datetime.today().strftime('%H:%M')
saudacao = ''

if hora > ('06:00') and hora < ('12:00'):
    saudacao = 'Bom dia!'
elif hora > ('12:00') and hora < ('18:00'):
    saudacao = 'Boa tarde!'
else: 
    saudacao = 'Boa noite!' 

print(hora, '\n')

print('{} Seja bem vindo ao hotel Guidoloop!'.format(saudacao))


# Menu
while True:
    opcaoMenu = int(input('''\nMenu:\nEscolha uma das opções abaixo:
1 -> Fazer Check-In
2 -> Relatório Hospedes
3 -> Procurar Hospedes
4 -> Fazer Check-Out
5 -> Finalizar Atendimento
Qual opção: '''))

    # Checkin
    if opcaoMenu == 1:
        novaPessoa = 's'

        print('\nVamos começar seu Check-In:\n')

        while True:
    
            pessoa = []
            nomePessoa = str(input('Qual seu nome completo? '))
            cpfPessoa = int(input('Qual seu cpf? '))
            numeroPessoa = int(input('Qual seu telefone? '))

            # Máscara CPF
            cpfPessoa = str(cpfPessoa)
            if len(cpfPessoa) < 11:
                cpfPessoa = cpfPessoa.zfill(11)
                cpfPessoa = '{}.{}.{}-{}'.format(cpfPessoa[:3], cpfPessoa[3:6], cpfPessoa[6:9], cpfPessoa[9:])

            # Máscara celular
            numeroPessoa = str(numeroPessoa)
            if len(numeroPessoa) <= 11:
                numeroPessoa = '({}) {}-{}'.format(numeroPessoa[:2], numeroPessoa[2:6], numeroPessoa[6:11])

            pessoa.append(nomePessoa)
            pessoa.append(cpfPessoa)
            pessoa.append(numeroPessoa)

            listaClientes.append(pessoa)

            novaPessoa = str(input('\nDeseja realizar o check-in de outra pessoa? \nSim -> S\nNão -> N\n Qual opção: ')).upper().strip()
            if novaPessoa in "Nn":
                break

    # Relatório Hospedes
    if opcaoMenu == 2:
        while True:
            if len(listaClientes) == 0:
                print('Não há hospedes cadastrados')
                sleep(1)
            else:   
                print('-' * 70)
                print('|{:5}|{:20}|{:20}|{:20}|'.format(' Id', ' Nome', ' C.P.F.', ' Telefone'))
                print('-' * 70)
                for i in range(0, len(listaClientes)):
                    print('|{:^5}'.format(i), end='')
                    for j in range(0, len(pessoa)):
                        print('|{:^20}'.format(listaClientes[i][j]), end='')
                    print('|')
                    print('-' * 70)        
            break
    # consulta Hospedes
    if opcaoMenu == 3:
        while True:
            if len(listaClientes) == 0:
                print('Não há hospedes cadastrados')
                sleep(1)
            else:   
                procurarClientes = str(input('\nDigite o nome do hospede para consultar no cadastro ou [S] para sair: ')).strip()
                if procurarClientes in 'Ss':
                    break
                achou = 0
                for c in range(0, len(listaClientes)):
                    if procurarClientes == listaClientes[c][0]:
                        achou += 1
                        indice = c

                if achou > 0:
                    print('-' * 70)
                    print('|{:5}|{:20}|{:20}|{:20}|'.format(' Id', ' Nome', ' C.P.F.', ' Telefone'))
                    print('-' * 70)
                    print('|{:^5}'.format(indice), end='')
                    for x in range(0, len(pessoa)):
                        print('|{:^20}'.format(listaClientes[indice][x]), end='')
                    print('|')
                    print('-' * 70)
                else:
                    print('Hospede não cadastrado.')
            break
    # Check out Hospedes
    if opcaoMenu == 4:
        while True:
            if len(listaClientes) == 0:
                print('Não há hospedes cadastrados')
                sleep(1)
            else:
                procurarClientes = str(input('\nDigite o nome do hospede para fazer o Checkout do cliente ou [S] para sair: ')).strip()
                if procurarClientes == 'S' or procurarClientes == 's':
                    break
                achou = 0
                for c in range(0, len(listaClientes)):
                    if procurarClientes == listaClientes[c][0]:
                        achou += 1
                        indice = c
                
                if achou >= 0:
                    del listaClientes[indice]     
                else:
                    print('\nNão há hospede no hotel.\n')

                print('-' * 70)
                print('|{:5}|{:20}|{:20}|{:20}|'.format(' Id', ' Nome', ' C.P.F.', ' Telefone'))
                print('-' * 70)
                for i in range(0, len(listaClientes)):
                    print('|{:^5}'.format(i), end='')
                    for j in range(0, len(pessoa)):
                        print('|{:^20}'.format(listaClientes[i][j]), end='')
                    print('|')
                    print('-' * 70)
            break
    # Opção Sair do Sistema
    if opcaoMenu == 5:
        break
print('\nObrigado. Volte Sempre!!!')
