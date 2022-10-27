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

def menu():
    print("""

            [ 1 ] => Fazer Check-In
            [ 2 ] => Relatório Hospedes
            [ 3 ] => Procurar Hospedes
            [ 4 ] => Fazer Check-Out
            [ 5 ] => Finalizar Atendimento

    """)
