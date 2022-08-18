class Servico:
    def __init__(self, cliente, cpf, endereco,cidade, telefone, email,descricao_prod, observacao,defeito, id=None):
        self._id=id
        self._cliente= cliente
        self._cpf = cpf
        self._endereco = endereco
        self._cidade = cidade
        self._telefone = telefone
        self._email = email
        self._descricao_prod = descricao_prod
        self._defeito = defeito
        self._observacao = observacao


class Usuario:
    def __init__(self, id, nome, senha):
        self._id = id
        self._nome = nome
        self._senha = senha

class Cadastro:
    def __init__(self, nome, sobrenome, email, senha, termo,id=None):
        self._id = id
        self._nome = nome
        self._sobrenome = sobrenome
        self._email = email
        self._senha = senha
        self._termo = termo

class Produto:
    def __init__(self, descricao,categoria, valor,estoque,id=None):
        self._id = id
        self._descricao = descricao
        self._categoria = categoria
        self._valor = valor
        self._estoque = estoque

class Conta:
    def __init__(self, cliente,valor, equipamento,data,id=None):
        self._id = id
        self._cliente = cliente
        self._valor = valor
        self._equipamento = equipamento
        self._data = data

