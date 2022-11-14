import sqlite3

conexao = sqlite3.connect("TODO.sqlite3")
cursor = conexao.cursor()

def consulta_categoria():
    lista = "SELECT * FROM categoria"
    consulta = cursor.execute(lista)
    for i in consulta:
        print(i)

if __name__ == "__main__":
    input("DIGITE QUALQUER TECLA PARA REALIZAR A CONSULTA DAS CATEGORIAS: ")
    consulta_categoria()
    conexao.close()