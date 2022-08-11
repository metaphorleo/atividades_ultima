import sqlite3
conexao = sqlite3.connect("M2S3.sqlite3")
cursor = conexao.cursor()
cursor.execute("DELETE FROM Fornecedor WHERE id = 1")
conexao.commit()
conexao.close()