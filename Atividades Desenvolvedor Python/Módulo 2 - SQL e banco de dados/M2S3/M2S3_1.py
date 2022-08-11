import sqlite3
conexao = sqlite3.connect("M2S3.sqlite3")
cursor = conexao.cursor()
dados = [("Padaria do Pão", "Rua dos Pães, 12"), ("Marcenaria Martelo", "Rua das Madeiras, 15")]
cursor.executemany("INSERT INTO Fornecedor (nome, endereco) VALUES (?, ?)", dados)
conexao.commit()
conexao.close()
