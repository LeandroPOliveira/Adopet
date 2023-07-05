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
from flask_bcrypt import generate_password_hash

conn = sqlite3.connect('adopet')

cursor = conn.cursor()

# cursor.execute("DROP DATABASE IF EXISTS `bikeswap`;")

# cursor.execute("CREATE DATABASE `bikeswap`;")
#
# cursor.execute("USE `bikeswap`;")

# criando tabelas
TABLES = {}
TABLES['pets'] = ('''
      CREATE TABLE 'pets' (
      'id' integer PRIMARY KEY AUTOINCREMENT,
      'nome' varchar(50) NOT NULL,
      'idade' varchar(10) NOT NULL,
      'porte' varchar(30) NOT NULL,
      'descricao' varchar(50) NOT NULL,
      'localidade' varchar(40) NOT NULL);''')

TABLES['usuarios'] = ('''
      CREATE TABLE 'usuarios' (
      'id' integer PRIMARY KEY AUTOINCREMENT,
      'email' varchar(50),
      'senha' varchar(100) NOT NULL,
      'nome' varchar(40),
      'telefone' varchar(20),
      'cidade' varchar(40),
      'sobre' varchar(200)
      );''')

for tabela_nome in TABLES:
    tabela_sql = TABLES[tabela_nome]

    cursor.execute(tabela_sql)


# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (email, senha, nome, telefone, cidade, sobre) VALUES (?, ?, ?, ?, ?, ?)'
usuarios = [
      ('admin@email.com', generate_password_hash("admin321"), "Admin", '169999-0000', 'Batatais',
       'Administrador do site'),
      ('user1@hotmail.com', generate_password_hash("user123"), "Usuario1", '169999-1111', 'Araraquara',
       'Lorem ipsum quos atque1'),
      ('user2@hotmail.com', generate_password_hash("user213"), "Usuario2", '169999-2222', 'Batatais',
       'Lorem ipsum quos atque2'),

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
      ('Sirius', '6 meses', 'Porte grande', 'Ativo e educado', 'Duque de Caxias (RJ)'),
      ('Fiona', '3 anos', 'Porte pequeno', 'Calma e carinhosa', 'São Gonçalo (RJ)'),
      ('Sid', '8 meses', 'Porte médio/grande', 'Brincalhão e amável', 'Rio de Janeiro (RJ)'),
('Yoda', '1 ano', 'Porte médio', 'Ativo e carinhoso', 'Nova Iguaçu (RJ)'),
('Lua', '6 meses', 'Porte médio', 'Ativa e carinhosa', 'Duque de Caxias (RJ)'),
('Amora', '45 dias', 'Porte grande', 'Calma e carinhosa', 'São Gonçalo (RJ)'),
('Zelda', '5 meses', 'Porte médio', 'Ativa e amável', 'Rio de Janeiro (RJ)'),
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