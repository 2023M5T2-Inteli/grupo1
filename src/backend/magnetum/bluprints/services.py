# CRUD

from magnetum.extentions import db
import sqlite3

cursor = db.connect()

def service():
    cursor.execute("INSERT INTO cliente (nome_nome, numero_projetos) VALUES ('João', 1);")



