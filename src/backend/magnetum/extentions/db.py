# Configurações do nosso database
import sqlite3

try:
    banco = sqlite3.connect("teste.db") # Cria um banco de dados
    print("Banco de daos iniciado!")
    cursor = banco.cursor() # Permite as operações do banco

    # Operações do banco de dados
    # cursor.execute() -> Esse comando recebe instruções em squilite

    cursor.execute('CREATE TABLE cliente (	cliente_id integer PRIMARY KEY,	nome_nome text NOT NULL, numero_projetos integer NOT NULL);')

    cursor.execute("CREATE TABLE projetos (	projeto_id integer PRIMARY KEY, cliente_id,nome_projeto text NOT NULL);")

    cursor.execute("CREATE TABLE ciclo (	ciclo_id integer PRIMARY KEY, numero_ciclo INTEGER, massa_ciclo REAL NOT NULL);")

    cursor.execute("CREATE TABLE ensaio (	ensaio_id integer PRIMARY KEY, cliente_id,data text NOT NULL, hora REAL NOT NULL, operador text NOT NULL, duracao REAL NOT NULL, massa_solido REAL NOT NULL, massa_agua REAL NOT NULL, campo REAL NOT NULL, ciclo_id);")




except sqlite3.Error as erro:
    print(erro)

