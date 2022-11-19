from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica
from controller.juridico import create_pj, read_pj, update_pj, delete_pj
from controller.fisico import create_psf, read_psf, update_psf, delete_psf

def menu():

    menu = 1

    while menu != 0:

        menu = int(input("""
        [ 0 ] => Sair do Programa
        [ 1 ] => Pessoa Fisica
        [ 2 ] => Pessoa Juridica

        Opção: """))

        match menu:

            case 1:

                menu_inicial = int(input("""
                [ 1 ] => Criar conta Pessoa Física
                [ 2 ] => Lista conta Pessoa Física
                [ 3 ] => Atualizar conta Pessoa Física
                [ 4 ] => Excluir conta Pessoa Física

                Opção: """))

                match menu_inicial:

                    case 1:

                        print("\n Criando uma conta Pessoa Física\n")

                        pessea_fisica = PessoaFisica()

                        pessea_fisica.titular = input("Informe o Titular: ")
                        pessea_fisica.cpf = input("Informe o C.P.F: ")
                        pessea_fisica.saldo_inicial = float(input("Informe o Saldo inicial: R$"))

                        informe = input("\nDeseja informar Segundo Titular? [ S ] / [ N ]: ").upper()
                        if informe == "S":
                            pessea_fisica.segundo_titular = input("Informe o Segundo Titular: ")

                        create_psf(pessea_fisica)

                    case 2:
                        # Listar Pessoa Fisica
                        print("\n Discritivo da conta Pessoa Física\n")

                        lista_psf = read_psf()

                        for c in lista_psf:
                            print(c)

                    case 3:

                        print("\nAtualizar conta Pessoa Física\n")

                        conta_update = PessoaFisica()

                        conta_update.cpf = input("Informe o C.P.F. da conta: ")
                        conta_update.titular = input("Informe o novo Titular: ")
                        conta_update.saldo_inicial = float(input("Informe o novo Saldo: R$"))

                        informe = input("\nDeseja informar Segundo Titular? [ S ] / [ N ]: ").upper()
                        if informe == "S":
                            conta_update.segundo_titular = input("Informe o Segundo Titular: ")

                        update_psf(conta_update)

                    case 4:

                        print("Excluindo conta Pessoa Física")

                        cpf = int(input("Informe o C.P.F. a ser excluido: "))
                        
                        delete_psf(cpf)

                    case _:
                        print("\nOpção Inválida.\n")

            case 2:

                menu_inicial = int(input("""
                [ 1 ] => Criar conta Pessoa Juridica
                [ 2 ] => Lista conta Pessoa Juridica
                [ 3 ] => Atualizar conta Pessoa Juridica
                [ 4 ] => Excluir conta Pessoa Juridica

                Opção: """))

                match menu_inicial:

                    case 1:

                        print("\n Criando uma conta Pessoa Juridica\n")

                        pessea_juridica = PessoaJuridica()

                        pessea_juridica.titular = input("Informe o Titular: ")
                        pessea_juridica.cnpj = int(input("Informe o CNPJ: "))
                        pessea_juridica.saldo_inicial = float(input("Informe o Saldo inicial: R$"))

                        informe = input("\nDeseja informar Segundo Titular? [ S ] / [ N ]: ").upper()
                        if informe == "S":
                            pessea_juridica.segundo_titular = input("Informe o Segundo Titular: ")

                        create_pj(pessea_juridica)

                    case 2:

                        print("\n Discritivo da conta Pessoa Juridica\n")
                        
                        lista_pj = read_pj()

                        for c in lista_pj:
                            print(c)

                    case 3:

                        print("\nAtualizar conta Pessoa Juridica\n")

                        conta_update = PessoaJuridica()

                        conta_update.cnpj = int(input("Informe o CNPJ da conta: "))
                        conta_update.titular = input("Informe o novo Titular: ")
                        conta_update.saldo_inicial = float(input("Informe o novo Saldo: R$"))

                        informe = input("\nDeseja informar Segundo Titular? [ S ] / [ N ]: ").upper()
                        if informe == "S":
                            conta_update.segundo_titular = input("Informe o Segundo Titular: ")

                        update_pj(conta_update)

                    case 4:

                        print("Excluindo conta Pessoa Juridica")

                        cnpj = int(input("Informe o CNPJ a ser excluido: "))
                        
                        delete_pj(cnpj)

                    case _:
                        print("\nOpção Inválida.\n")

            case _:
                print("\nOpção Inválida.\n")
