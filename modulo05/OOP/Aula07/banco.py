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
#cursor.execute("CREATE TABLE david (id int primary key generated always as identity, nome VARCHAR(30), sobrenome VARCHAR(30))")

# Comando SQL - DML para inserir dados na Tabela
#nome = input("Digite seu nome: ")
#sobrenome = input("Digite seu sobrenome: ")
#cursor.execute("INSERT INTO david (nome, sobrenome) VALUES(%s, %s)", (nome, sobrenome))

# Comando SQL - DQL para listar dados  
cursor.execute("SELECT * FROM david")
rs = cursor.fetchall()

for row in rs:
    print("ID = ", row [0])
    print("Nome = ", row[1])
    print("Sobrenome  = ", row[2], "\n")

# Comando SQL - DML para update dados na Tabela
#idd = int(input("Digite o ID: "))
#nome = input("Digite novo nome: ")
#sobrenome = input("Digite novo sobrenome: ")

#cursor.execute("UPDATE david SET nome = %s, sobrenome = %s WHERE id = %s", (nome, sobrenome, idd))

# Comando SQL - DML para Excluir dados na Tabela

idd = (input("Digite o ID: "))

cursor.execute("DELETE FROM david WHERE id = %s", idd)

count = cursor.rowcount
print(count, "Dados deletado com sucesso")

conn.commit()
cursor.close()
conn.close()


"""
https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/



http://www.dsc.ufcg.edu.br/~jacques/cursos/map/
html/uml/diagramas/diagramas.htm
"""