import psycopg2

try:
    # host = "HOST", database = "DATABASE", user="USER", password = "PASSWORD"
    conn = psycopg2.connect(host = "localhost", port = "5433", database = "postgres", user = "david", password = "123456")
    print("Conexão realizado com sucesso")
except:
    print("Conexão não realizada")

if conn is not None:
    print("conexão está estável")

# Referencia para manipular o Banco de Dados.
cursor = conn.cursor()

# Comando SQL - DDL para criar Tabela.
#cursor.execute("CREATE TABLE david (nome VARCHAR(30), sobrenome VARCHAR(30))")

# Comando SQL - DML para inserir dados na Tabela
#nome = input("Digite seu nome: ")
#sobrenome = input("Digite seu sobrenome: ")
#cursor.execute("INSERT INTO david (nome, sobrenome) VALUES(%s, %s)", (nome, sobrenome))

# Comando SQL - DQL para listar dados  
cursor.execute("SELECT * FROM david")
rs = cursor.fetchall()

for row in rs:
    print("Nome = ", row[0])
    print("Sobrenome  = ", row[1], "\n")






conn.commit()
cursor.close()
conn.close()
