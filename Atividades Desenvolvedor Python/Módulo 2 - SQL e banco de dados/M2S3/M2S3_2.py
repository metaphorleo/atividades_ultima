import sqlite3
conexao = sqlite3.connect("M2S3.sqlite3")
cursor = conexao.cursor()
cursor.execute("UPDATE Fornecedor SET endereco = 'Rua dos Peixes, 26' WHERE id = 2")
conexao.commit()
conexao.close()