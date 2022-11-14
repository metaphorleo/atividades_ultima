import sqlite3
from query_categoria import *

conexao = sqlite3.connect("TODO.sqlite3")
cursor = conexao.cursor()

def criar():
    criar_categoria = input("DIGITE O NOME DA CATEGORIA QUE DESEJA CRIAR: ")
    valor = [criar_categoria]
    sql = "INSERT INTO categoria (nome) VALUES (?)"
    cursor.execute(sql, valor)

def atualizar():
    consulta_categoria()
    id_categoria = input("DIGITE O ID DA CATEGORIA QUE DESEJA ATUALIZAR: ")
    nome_categoria = input("DIGITE O NOVO NOME DA CATEGORIA: ")
    valores = [nome_categoria, id_categoria]
    sql = "UPDATE categoria SET nome = ? WHERE id = ?"
    cursor.execute(sql, valores)

def excluir():
    consulta_categoria()
    id_excluir = input("DIGITE O ID DA CATEGORIA QUE DESEJA EXCLUIR: ")
    valor = [id_excluir]
    sql = "DELETE FROM categoria WHERE id = ?"
    cursor.execute(sql, valor)

print("1. CRIAR CATEGORIA\n2. ATUALIZAR CATEGORIA\n3. EXCLUIR CATEGORIA")
numero = int(input("DIGITE O NÚMERO DO QUE DESEJA FAZER: "))

if numero == 1:
    criar()
if numero == 2:
    atualizar()
if numero == 3:
    excluir()

conexao.commit()
conexao.close()