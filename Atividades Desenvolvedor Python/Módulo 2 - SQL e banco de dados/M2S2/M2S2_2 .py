import sqlite3
conexao = sqlite3.connect("M2S2_2.sqlite3")
cursor = conexao.cursor()
cursor.execute("CREATE TABLE organizador (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nome TEXT(100),email TEXT(64),cpf TEXT(11) NOT NULL,CONSTRAINT organizador_UN UNIQUE (cpf))")
cursor.execute("CREATE TABLE eventos (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nome TEXT(100),data TEXT(20),local TEXT(100), organizador_id INTEGER NOT NULL,CONSTRAINT eventos_FK FOREIGN KEY (organizador_id) REFERENCES organizador(id))")
conexao.commit()
conexao.close()