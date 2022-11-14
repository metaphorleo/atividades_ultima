import sqlite3

conexao = sqlite3.connect("TODO.sqlite3")
cursor = conexao.cursor()

def consulta_todo():
    lista = "SELECT t.id, t.tarefa, c.nome as categoria, t.data, t.status FROM tarefas as t, categoria as c WHERE t.categoria_id = c.id"
    consulta = cursor.execute(lista)
    for i in consulta:
        print(i)

if __name__ == "__main__":
    consulta_todo()
    conexao.close()