# import mysql.connector
# from mysql.connector import errorcode
#
# print("Conectando...")
# try:
#       conn = mysql.connector.connect(
#             host='127.0.0.1',
#             user='root',
#             password='admin'
#       )
# except mysql.connector.Error as err:
#       if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print('Existe algo errado no nome de usuário ou senha')
#       else:
#             print(err)
#
import sqlite3

conn = sqlite3.connect('adopet')

cursor = conn.cursor()

# cursor.execute("DROP DATABASE IF EXISTS `bikeswap`;")

# cursor.execute("CREATE DATABASE `bikeswap`;")
#
# cursor.execute("USE `bikeswap`;")

# criando tabelas
TABLES = {}
TABLES['Pets'] = ('''
      CREATE TABLE 'pets' (
      'id' integer PRIMARY KEY AUTOINCREMENT,
      'nome' varchar(50) NOT NULL,
      'idade' varchar(20) NOT NULL,
      'porte' varchar(30) NOT NULL,
      'descricao' varchar(40) NOT NULL,
      'localidade' varchar(40) NOT NULL);''')

TABLES['Usuarios'] = ('''
      CREATE TABLE 'usuarios' (
      `usuario` varchar(20) PRIMARY KEY,
      `senha` varchar(100) NOT NULL
      );''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]

    cursor.execute(tabela_sql)


# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (usuario, senha) VALUES (?, ?)'
usuarios = [
      ("admin", "123456"),
      ("leandro", "teste"),
      ("erika", "bagual")
]

cursor.executemany(usuario_sql, usuarios)

# cursor.execute('select * from adopet.usuarios')
# print(' -------------  Usuários:  -------------')
# for user in cursor.fetchall():
#     print(user[1])

# inserindo jogos
pets_sql = 'INSERT INTO pets (nome, idade, porte, descricao, localidade) VALUES (?, ?, ?, ?, ?)'
pets = [
      ('Dunga', '2 anos', 'Porte pequeno', 'Calmo e educado', 'Rio de Janeiro (RJ)'),
      ('Felícia', '3 meses', 'Porte pequeno', 'Ativa e carinhosa', 'Nova Iguaçu (RJ)'),
      ('Sirius', '6 meses', 'Porte Grande', 'Ativo e educado', 'Duque de Caxias (RJ)'),
]
cursor.executemany(pets_sql, pets)

# cursor.execute('select * from adopet.pets')
# print(' -------------  Pets:  -------------')
# for bike in cursor.fetchall():
#     print(bike[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()