import sqlite3

conexao = sqlite3.connect("TODO.sqlite3")
cursor = conexao.cursor()

data = input("DIGITE A DATA QUE DESEJA CONSULTAR (aaaa-mm-dd): ")
valor = [data]
sql = "SELECT t.id, t.tarefa, c.nome as categoria, t.data, t.status FROM tarefas as t, categoria as c WHERE t.categoria_id = c.id AND t.data = ?"
consulta = cursor.execute(sql, valor)
for i in consulta:
    print(i)

conexao.close()