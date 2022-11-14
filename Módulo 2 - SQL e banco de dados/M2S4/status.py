import sqlite3
from query_todo import *

conexao = sqlite3.connect("TODO.sqlite3")
cursor = conexao.cursor()

consulta_todo()
id_tarefa = input("DIGITE O ID DA TAREFA EM QUE DESEJA ATUALIZAR O STATUS: ")
status = input("DIGITE O NOVO STATUS DA TAREFA: ")
valores = [status, id_tarefa]
sql = "UPDATE tarefas SET status = ? WHERE id = ?"
cursor.execute(sql, valores)

conexao.commit()
conexao.close()