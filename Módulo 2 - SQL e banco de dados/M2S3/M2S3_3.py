import sqlite3
conexao = sqlite3.connect("M2S3.sqlite3")
cursor = conexao.cursor()
query = cursor.execute("SELECT * FROM Fornecedor")
for i in query:
    print(i)
conexao.close()