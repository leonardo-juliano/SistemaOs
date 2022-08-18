from models import Servico, Usuario, Cadastro, Produto, Conta

SQL_DELETA_SERVICO = 'delete from servico where id=%s'
SQL_DELETA_USUARIO = 'delete from usuario where id=%s'
SQL_DELETA_PRODUTO = 'delete from produto where ID=%s'
SQL_DELETA_CONTA = 'delete from contas where id=%s'

SQL_CRIA_SERVICO = 'INSERT into servico (cliente, cpf, endereco, cidade, telefone, email, descricao_prod,defeito , observacao) values (%s, %s, %s,%s, %s, %s, %s,%s,%s)'
SQL_CRIA_CLIENTE = 'INSERT into usuario (nome,sobrenome,email,senha,termo) values (%s, %s, %s, %s,%s)'
SQL_CRIA_CONTA  = 'INSERT into contas (clienteR,valorR, equipamentoR, dataV) values (%s, %s, %s, %s)'
SQL_CRIA_PRODUTO = 'INSERT into produto (DESCRICAO,CATEGORIA,VALOR,ESTOQUE) values (%s, %s, %s, %s)'

SQL_ATUALIZA_CONTA = 'UPDATE contas SET clienteR=%s, valorR=%s, equipamentoR=%s, dataV=%s where id=%s'
SQL_ATUALIZA_PRODUTO = 'UPDATE produto SET DESCRICAO=%s, CATEGORIA=%s, VALOR=%s, ESTOQUE=%s where id=%s'
SQL_ATUALIZA_SERVICO = 'UPDATE servico SET cliente=%s, cpf=%s, endereco=%s, cidade=%s, telefone=%s, email=%s,descricao_prod=%s, defeito=%s, observacao=%s where id=%s'
SQL_ATUALIZA_CLIENTE = 'UPDATE usuario SET nome=%s, sobrenome=%s, email=%s, senha=%s where id=%s'

SQL_BUSCA_SERVICO = 'SELECT id, cliente, cpf, endereco, cidade, telefone, email, descricao_prod, defeito,observacao  from servico '
SQL_BUSCA_USUARIO = 'SELECT id,nome, sobrenome, email from usuario '
SQL_BUSCA_PRODUTO = 'SELECT ID,DESCRICAO, CATEGORIA,VALOR, ESTOQUE  from produto '
SQL_BUSCA_CONTA = 'SELECT clienteR,valorR, equipamentoR, dataV from contas '

SQL_PRODUTO_POR_ID = 'SELECT ID,DESCRICAO, CATEGORIA,VALOR, ESTOQUE from produto where id=%s'
SQL_USUARIO_POR_ID = 'SELECT id, nome, sobrenome, email, senha from usuario where id=%s'
SQL_SERVICO_POR_ID = 'SELECT id, cliente, cpf, endereco, cidade, telefone, email, descricao_prod, defeito,observacao from servico where id=%s'


class ContaDao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, contas):
        cursor = self.__db.connection.cursor()
        if(contas._id):
            cursor.execute(SQL_ATUALIZA_CONTA, (contas._cliente, contas._valor, contas._equipamento, contas._data, contas._id))

        else:
            cursor.execute(SQL_CRIA_CONTA,  (contas._clienteR, contas._valorR, contas._equipamentoR, contas._dataV))
            cursor._id= cursor.lastrowid

        self.__db.connection.commit()
        return contas

    def listar_contas(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_CONTA)
        conta = traduz_conta(cursor.fetchall())
        return conta

    def deletar_conta(self,id):
        self.__db.connection.cursor().execute(SQL_DELETA_CONTA,(id,))
        self.__db.connection.commit()

class ProdutoDao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, produto):
        cursor = self.__db.connection.cursor()
        if(produto._id):
            cursor.execute(SQL_ATUALIZA_PRODUTO, (produto._descricao, produto._categoria, produto._valor, produto._estoque, produto._id))

        else:
            cursor.execute(SQL_CRIA_PRODUTO, (produto._descricao, produto._categoria, produto._valor, produto._estoque))
            cursor._id= cursor.lastrowid

        self.__db.connection.commit()
        return produto

    def listar_produtos(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_PRODUTO)
        produtos = traduz_produtos(cursor.fetchall())
        return produtos

    def deletar(self,id):
        self.__db.connection.cursor().execute(SQL_DELETA_PRODUTO,(id,))
        self.__db.connection.commit()

    def busca_por_id(self,id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_PRODUTO_POR_ID,(id,))
        tupla = cursor.fetchone()
        return Produto(tupla[1],tupla[2],tupla[3], tupla[4],id=tupla[0])


class ServicoDao:
    def __init__(self, db):
        self.__db=db

    def salvar(self,servico):
        cursor = self.__db.connection.cursor()

        if(servico._id):
            cursor.execute(SQL_ATUALIZA_SERVICO, (servico._cliente, servico._cpf, servico._endereco,servico._cidade, servico._telefone,servico._email,servico._descricao_prod,servico._defeito,servico._observacao,servico._id))
        else:
            cursor.execute(SQL_CRIA_SERVICO, (servico._cliente, servico._cpf, servico._endereco,servico._cidade, servico._telefone,servico._email,servico._descricao_prod,servico._defeito,servico._observacao))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return servico

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_SERVICO)
        servicos = traduz_servicos(cursor.fetchall())
        return servicos

    def busca_por_id(self,id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SERVICO_POR_ID,(id,))
        tupla = cursor.fetchone()
        return Servico(tupla[1],tupla[2],tupla[3], tupla[4],tupla[5],tupla[6],tupla[7],tupla[8],tupla[9],id=tupla[0])

    def deletar(self,id):
        self.__db.connection.cursor().execute(SQL_DELETA_SERVICO,(id,))
        self.__db.connection.commit()

def traduz_servicos(servicos):
    def cria_servico_com_tupla(tupla):
        return(Servico(tupla[1],tupla[2],tupla[3],tupla[4],tupla[5],tupla[6],tupla[7],tupla[8],tupla[9],id=tupla[0]))
    return list(map(cria_servico_com_tupla,servicos))

def traduz_produtos(produtos):
    def cria_produto_com_tupla(tupla):
        return(Produto(tupla[1],tupla[2],tupla[3],tupla[3],tupla[0]))
    return list(map(cria_produto_com_tupla,produtos))

def traduz_conta(contas):
    def cria_conta_com_tupla(tupla):
        return(Conta(tupla[1],tupla[2],tupla[3],tupla[3],tupla[0]))
    return list(map(cria_conta_com_tupla,contas))

def traduz_usuario(tupla):
    return Usuario(tupla[0],tupla[3],tupla[4])


class UsuarioDao:
    def __init__(self,db):
        self.__db=db

    def salvar(self,usuario):
        cursor = self.__db.connection.cursor()

        if(usuario._id):
            cursor.execute(SQL_ATUALIZA_CLIENTE,(usuario._nome,usuario._sobrenome,usuario._email,usuario._senha, usuario._termo,usuario._id))
        else:
             cursor.execute(SQL_CRIA_CLIENTE,(usuario._nome,usuario._sobrenome,usuario._email,usuario._senha, usuario._termo))
             cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return usuario


    def deletar_usuario(self,id):
        self.__db.connection.cursor().execute(SQL_DELETA_USUARIO,(id,))
        self.__db.connection.commit()


    def busca_por_id(self,email):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID,(email,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario

    def listar_usuario(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_USUARIO)
        usuarios = traduz_usuario2(cursor.fetchall())
        return usuarios

def traduz_usuario2(usuarios):
    def cria_usuario_com_tupla(tupla):
        return Usuario(tupla[1],tupla[2],tupla[3],)
    return list(map(cria_usuario_com_tupla,usuarios))



