# Importando Classes da Model
from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica
# Importando Funções da Controller
from controller.juridico import create_pj, read_pj, update_pj, delete_pj
from controller.fisico import create_psf, read_psf, update_psf, delete_psf

# Função para construção do Menu
def menu():
    # Variável de referência para a estrutura de repetição While
    menu = 1
    # Estrutura de repetição While
    while menu != 0:
        # Variável de referência recebe o valor digitado pelo usuário
        # e impressão do Menu Primário
        menu = int(input("""
        [ 0 ] => Sair do Programa
        [ 1 ] => Pessoa Fisica
        [ 2 ] => Pessoa Juridica

        Opção: """))
        # Estrutura de condição Match Case com a variável de referência menu
        match menu:
            # Caso variável de referência seja igual a 1
            case 1:
                # Variável de referência recebe o valor digitado pelo usuário
                # e impressão do Menu Secundário
                menu_inicial = int(input("""
                [ 1 ] => Criar conta Pessoa Física
                [ 2 ] => Lista conta Pessoa Física
                [ 3 ] => Atualizar conta Pessoa Física
                [ 4 ] => Excluir conta Pessoa Física

                Opção: """))
                # Estrutura de condição Match Case com a variável de referência menu_inicial
                match menu_inicial:
                    # Caso variável de referência menu_inicial seja igual a 1
                    case 1:
                        # Impressão do descritivo da opção 1
                        print("\n Criando uma conta Pessoa Física\n")
                        # Instância de novo Objeto
                        pessea_fisica = PessoaFisica()
                        # Atribui valores digitado pelo usuário ao Objeto
                        pessea_fisica.titular = input("Informe o Titular: ")
                        pessea_fisica.cpf = input("Informe o C.P.F: ")
                        pessea_fisica.saldo_inicial = float(input("Informe o Saldo inicial: R$"))
                        # Variável de referência para a estrutura de condição IF
                        informe = input("\nDeseja informar Segundo Titular? [ S ] / [ N ]: ").upper()
                        # Estrutura de condição IF
                        if informe == "S":
                            pessea_fisica.segundo_titular = input("Informe o Segundo Titular: ")
                        # Chamada de função passando o Objeto como parametro
                        create_psf(pessea_fisica)
                    # Caso variável de referência menu_inicial seja igual a 2
                    case 2:
                        # Impressão do descritivo da opção 2
                        print("\n Discritivo da conta Pessoa Física\n")
                        # Variável para receber o retorno da função
                        lista_psf = read_psf()
                        # Estrutura de repetição para impressão da lista de contas
                        for c in lista_psf:
                            print(c)
                    # Caso variável de referência menu_inicial seja igual a 3
                    case 3:
                        # Impressão do descritivo da opção 3
                        print("\nAtualizar conta Pessoa Física\n")
                        # Instância de novo Objeto
                        conta_update = PessoaFisica()
                        # Atribui valores digitado pelo usuário ao Objeto
                        conta_update.cpf = int(input("Informe o C.P.F. da conta: "))
                        conta_update.titular = input("Informe o novo Titular: ")
                        conta_update.saldo_inicial = float(input("Informe o novo Saldo: R$"))
                        # Variável de referência para a estrutura de condição IF
                        informe = input("\nDeseja informar Segundo Titular? [ S ] / [ N ]: ").upper()
                        # Estrutura de condição IF
                        if informe == "S":
                            conta_update.segundo_titular = input("Informe o Segundo Titular: ")
                        # Chamada de função passando o Objeto como parametro
                        update_psf(conta_update)
                    # Caso variável de referência menu_inicial seja igual a 4
                    case 4:
                        # Impressão do descritivo da opção 4
                        print("Excluindo conta Pessoa Física")
                        # Instância de novo Objeto
                        conta_delete = PessoaFisica()
                        # Atribui valores digitado pelo usuário ao Objeto
                        conta_delete.cpf = int(input("Informe o C.P.F. a ser excluido: "))
                        # Chamada de função passando o Objeto como parametro
                        delete_psf(conta_delete)
                    # Caso variável de referência esteja fora dos valores.
                    case _:
                        print("\nOpção Inválida.\n")
            # Caso variável de referência menu seja igual a 2
            case 2:

                menu_inicial = int(input("""
                [ 1 ] => Criar conta Pessoa Juridica
                [ 2 ] => Lista conta Pessoa Juridica
                [ 3 ] => Atualizar conta Pessoa Juridica
                [ 4 ] => Excluir conta Pessoa Juridica

                Opção: """))

                match menu_inicial:
                    # Caso variável de referência menu_inicial seja igual a 1
                    case 1:
                        # Impressão do descritivo da opção 1
                        print("\n Criando uma conta Pessoa Juridica\n")
                        # Instância de novo Objeto
                        pessea_juridica = PessoaJuridica()
                        # Atribui valores digitado pelo usuário ao Objeto
                        pessea_juridica.titular = input("Informe o Titular: ")
                        pessea_juridica.cnpj = int(input("Informe o CNPJ: "))
                        pessea_juridica.saldo_inicial = float(input("Informe o Saldo inicial: R$"))
                        # Variável de referência para a estrutura de condição IF
                        informe = input("\nDeseja informar Segundo Titular? [ S ] / [ N ]: ").upper()
                        # Estrutura de condição IF
                        if informe == "S":
                            pessea_juridica.segundo_titular = input("Informe o Segundo Titular: ")
                        # Chamada de função passando o Objeto como parametro
                        create_pj(pessea_juridica)
                    # Caso variável de referência menu_inicial seja igual a 2
                    case 2:
                        # Impressão do descritivo da opção 2
                        print("\n Discritivo da conta Pessoa Juridica\n")
                        # Variável para receber o retorno da função
                        lista_pj = read_pj()
                        # Estrutura de repetição para impressão da lista de contas
                        for c in lista_pj:
                            print(c)
                    # Caso variável de referência menu_inicial seja igual a 3
                    case 3:
                        # Impressão do descritivo da opção 3
                        print("\nAtualizar conta Pessoa Juridica\n")
                        # Instância de novo Objeto
                        conta_update = PessoaJuridica()
                        # Atribui valores digitado pelo usuário ao Objeto
                        conta_update.cnpj = int(input("Informe o CNPJ da conta: "))
                        conta_update.titular = input("Informe o novo Titular: ")
                        conta_update.saldo_inicial = float(input("Informe o novo Saldo: R$"))
                        # Variável de referência para a estrutura de condição IF
                        informe = input("\nDeseja informar Segundo Titular? [ S ] / [ N ]: ").upper()
                        # Estrutura de condição IF
                        if informe == "S":
                            conta_update.segundo_titular = input("Informe o Segundo Titular: ")
                        # Chamada de função passando o Objeto como parametro
                        update_pj(conta_update)
                    # Caso variável de referência menu_inicial seja igual a 4
                    case 4:
                        # Impressão do descritivo da opção 4
                        print("Excluindo conta Pessoa Juridica")
                        # Instância de novo Objeto
                        conta_delete = PessoaJuridica()
                        # Atribui valores digitado pelo usuário ao Objeto
                        conta_delete.cnpj = int(input("Informe o CNPJ a ser excluido: "))
                        # Chamada de função passando o Objeto como parametro
                        delete_pj(conta_delete)
                    # Caso variável de referência esteja fora dos valores.
                    case _:
                        print("\nOpção Inválida.\n")
            # Caso variável de referência esteja fora dos valores.
            case _:
                print("\nOpção Inválida.\n")
