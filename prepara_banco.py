import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='@Fy45jkloaz', host='127.0.0.1', port=3306, charset='utf8')

# Descomente se quiser desfazer o banco...
'''conn.cursor().execute("DROP DATABASE `ferramenta`;")
conn.commit()'''

'''CREATE DATABASE `ferramenta`  DEFAULT CHARSET=utf8;'''
'''CREATE TABLE `servico` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cliente` varchar(45) NOT NULL,
  `cpf` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `endereco` varchar(45) DEFAULT NULL,
  `cidade` varchar(45) DEFAULT NULL,
  `telefone` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `descricao_prod` varchar(45) NOT NULL,
  `observacao` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cpf_UNIQUE` (`cpf`)
) ENGINE=InnoDB;'''
criar_tabelas = '''SET NAMES utf8;
    USE `ferramenta`;
    CREATE TABLE `usuario` (
      `id` int(11) NOT NULL,
      `nome` varchar(20) NOT NULL,
      'sobrenome' varchar(20) NOT NULL,
      'email' varchar(50) NOT NULL,
      `senha` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB;'''
'''CREATE TABLE `produto` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `DESCRICAO` varchar(45) DEFAULT NULL,
  `ESTOQUE` varchar(45) DEFAULT NULL,
  `CATEGORIA` varchar(45) DEFAULT NULL,
  `VALOR` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) '''
'''CREATE TABLE `contas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `clienteR` varchar(45) DEFAULT NULL,
  `dataV` varchar(45) DEFAULT NULL,
  `valorR` varchar(45) DEFAULT NULL,
  `equipamentoR` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
)'''
conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO ferramenta.usuario (nome, sobrenome,email, senha) VALUES (%s, %s,%s, $s)',
      [
            ('Vinicius', 'Ribeiro', 'vinicius@gmail.com', '1234' ),
            ('Leonardo','Henrique','leonardo@gmail.com','2424'),
            ('Leonardo','juliano','leonardooooo@gmail.com','2424'),

      ])

cursor.execute('select * from ferramenta.usuario')
print(' -------------  Usu??rios:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo servi??os
cursor.executemany(
      'INSERT INTO ferramenta.servico (cliente, equipamento, defeito) VALUES (%s, %s, %s)',
      [
            ('Jo??o', 'PC', 'Formata????o'),
            ('Marina', 'Notebook', 'atualiza????o do anti-v??rus'),
            ('Jos??', 'Tablet', 'Pouca mem??ria'),
            ('Vinicius', 'Notebook', 'Placa de v??deo'),
            ('Caique', 'Smartphone', 'Pouca mem??ria'),
            ('Caio', 'PC', 'Processador lento'),
      ])

cursor.execute('select * from ferramenta.servico')
print(' -------------  Servi??os:  -------------')
for servico in cursor.fetchall():
    print(servico[1])

# commitando sen??o nada tem efeito
conn.commit()
cursor.close()