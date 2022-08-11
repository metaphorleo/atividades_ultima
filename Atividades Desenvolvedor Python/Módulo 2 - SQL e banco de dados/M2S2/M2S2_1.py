import sqlite3
conexao = sqlite3.connect("M2S2_1.sqlite3")
cursor = conexao.cursor()
cursor.execute("CREATE TABLE categorias (id INTEGER NOT NULL,nome TEXT(100),CONSTRAINT categorias_PK PRIMARY KEY (id))")
cursor.execute("CREATE TABLE tarefas (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nome TEXT(100),data TEXT(20),categoria_id INTEGER NOT NULL,status TEXT(20),CONSTRAINT tarefas_FK FOREIGN KEY (categoria_id) REFERENCES categorias(id))")
conexao.commit()
conexao.close()