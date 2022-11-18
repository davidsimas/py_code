"""
 - Na pasta view crie um documento com namespace main.py e realize as importacoes.
   * from model.pessoaFisica import PessoaFisica
   * from model.pessoaJuridica import PessoaJuridica
   * from controller.juridico import create_pj, read_pj
   * from controller.fisico import create_psf, read_psf
 - Crie uma funcao menu().
 - Dentro da função menu() crie uma variável com nome de menu recebendo valor 1.
 - Crie um while, abrindo parênteses atribua à variável menu diferente de zero.
 - Crie um print descritivo solicitando ao usuário para digitar a opção desejada.
 - Crie uma variável menu_inicial recebendo um int() e dentro do int um input 
   solicitando ao usuário opção 1 ou opção 2, estas opções devem ser relacionadas
   à pessoa física e pessoa jurídica.
"""

from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica
from controller.juridico import create_pj, read_pj
from controller.fisico import create_psf, read_psf

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

                Opção: """))
                match menu_inicial:
                    case 1:
                        pessea_fisica = PessoaFisica()

                        pessea_fisica.titular = input("Informe o Titular: ")
                        pessea_fisica.cpf = input("Informe o C.P.F: ")
                        pessea_fisica.saldo_inicial = float(input("informe o Saldo inicial: R$"))

                        informe = input("\nDeseja informar Segundo Titular? [ S ] / [ N ]: ").upper()
                        if informe == "S":
                            pessea_fisica.segundo_titular = input("Informe o Segundo Titular: ")

                        create_psf(pessea_fisica)

                    case 2:
                        # Listar Pessoa Fisica
                        print("\n Discritivo da conta Pessoa Fisica\n")

                        lista_psf = read_psf()

                        for c in lista_psf:
                            print(c)


            case 2:
                menu_inicial = int(input("""
                [ 1 ] => Criar conta Pessoa Juridica
                [ 2 ] => Lista conta Pessoa Juridica

                Opção: """))
                match menu_inicial:
                    case 1:
                        pessea_juridica = PessoaJuridica()

                        pessea_juridica.titular = input("Informe o Titular: ")
                        pessea_juridica.cnpj = input("Informe o CNPJ: ")
                        pessea_juridica.saldo_inicial = float(input("informe o Saldo inicial: R$"))

                        informe = input("\nDeseja informar Segundo Titular? [ S ] / [ N ]: ").upper()
                        if informe == "S":
                            pessea_juridica.segundo_titular = input("Informe o Segundo Titular: ")
                        create_pj(pessea_fisica)

                    case 2:
                        # Listar Pessoa Fisica
                        print("\n Discritivo da conta Pessoa Juridica\n")
                        lista_pj = read_pj()

                        for c in lista_pj:
                            print(c)
