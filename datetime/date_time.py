"""
 * Documentação oficial

https://docs.python.org/pt-br/3/library/datetime.html
"""

# Importar o módulo e suas classes.
from datetime import date, time, datetime, timedelta

# Mostrar data e hora atuais.
data_hora = datetime.now()
print(data_hora)

"""
 - Método strftime()

Método para formatação de objetos de data em string legíveis. Recebe
como parâmetro uma diretiva que será usada para formatar a string.

 * Diretivas aqui
https://docs.python.org/pt-br/3/library/datetime.html#strftime-and-strptime-behavior
"""
# Mostra o nome do mês de uma data.
data_hora = datetime(2022, 11, 15)
print(data_hora.strftime("%B"))

# Mostra data e hora atuais com métodos today() e now().
hoje = date.today().strftime("%d/%m/%Y")
agora = datetime.now().strftime("%d/%m/%Y %H:%M")
print("Dia de hoje: ", hoje)
print("Data e hora atuais: ", agora)

# Mostrar data e hora formatadas.
data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
print(data_hora)

# Mostrar o ano atual e o nome do dia da semana.
data_hora = datetime.now()
print(data_hora)
print(data_hora.strftime("%A"))

# Criar um objeto de data.
data_hora = datetime(2022, 7, 16)
print(data_hora)

# Criar um objeto de hora.
hora = time(hour = 12, minute = 15, second = 20)
print(hora)

# Transformar string em data, método strptime.
data_texto = "25/12/2022"
data_hora = datetime.strptime(data_texto, "%d/%m/%Y")
print(data_hora)

# Mostrar hora UTC.
datetime.utcnow().strftime("%H:%M")

# Quantos dias faltam para meu aniversário?
meu_aniversario = datetime(year = 2023, month = 2, day = 28, hour = 20)
contagem = meu_aniversario - datetime.now()
print(f"Faltam {contagem.days} dias para meu aniversário.")

# Criar objeto data a partir de uma string com método fromisoformat().
data = date.fromisoformat("2022-07-15")
print(data.strftime("%d/%m/%Y"))

"""
Com timedelta é possível adicionar ou subtrair dias, horas, minutos e segundos.
"""

# Adicionar dias a uma data, que dia será daqui a 10 dias?
data_futura = datetime.today() + timedelta(days = 109)
print(data_futura.strftime("%d/%m/%Y"))

"""
 - Módulo dateutil

Fornece extensões úteis para o datetime. Por exemplo, com relativedelta podemos
adicionar ou subtrair outros períodos como meses ou anos.
"""

# Que dia será daqui a 3 anos, 2 meses e 10 dias?

from dateutil.relativedelta import relativedelta

data_atual = datetime.today()
delta = relativedelta(year =+ 3, months =+ 2, days =+ 10)
data_futura = data_atual + delta
print(data_futura.strftime("%d/%m/%Y"))

# Que dia era há 180 dias?
data_passada = datetime.today() + timedelta(days =- 180)
print(data_passada.strftime("%d/%m/%Y"))