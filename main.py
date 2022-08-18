from flask import Flask, render_template, request, redirect, session, flash, send_from_directory

from dao import ServicoDao, UsuarioDao, ProdutoDao, ContaDao
from flask_mysqldb import  MySQL

from models import Servico,Usuario, Cadastro,Produto, Conta


app = Flask(__name__)
app.secret_key = 'OS'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@Fy45jkloaz'
app.config['MYSQL_DB'] = 'ferramenta'
app.config['MYSQL_PORT'] = 3306
db = MySQL(app)
Servico_dao= ServicoDao(db)
usuario_dao= UsuarioDao(db)
produto_dao = ProdutoDao(db)
contaR_dao = ContaDao(db)

@app.route('/')
def index():
    return render_template('index.html', titulo="Concertos S.A")

@app.route('/lista_servico')
def lista_servico():
    lista = Servico_dao.listar()
    return render_template('lista.html', titulo="Ordens de Serviço",servicos=lista)

@app.route('/lista_contas')
def lista_contas():
    lista = contaR_dao.listar_contas()
    return render_template('contas_receber.html', titulo="Contas Receber",conta=lista)

@app.route('/lista_usuario')
def listar_usuario():
    listar = usuario_dao.listar_usuario()
    return render_template('listar_usuario.html', titulo="Listas de Usuarios",usuarios=listar)

@app.route('/lista_produtos')
def listar_produtos():
    listar = produto_dao.listar_produtos()
    return render_template('produto.html', titulo="Listas de Produtos",produtos=listar)


@app.route('/novo')
def novo():

    return render_template('novo.html', titulo='Cadastrando novos Serviços')

@app.route('/cadastra_produto')
def cadastra_produto():

    return render_template('cadastrar_produto.html', titulo='Cadastrando novos Produtos')

@app.route('/cadastra_conta')
def cadastra_conta():

    return render_template('cadastrar_conta.html', titulo='Cadastrar uma conta a Receber')

@app.route('/produto')
def produto():

    return render_template('produto.html', titulo='PRODUTOS')

@app.route('/criar', methods=['POST',])
def criar():
    cliente = request.form['cliente']
    cpf = request.form['cpf']
    endereco = request.form['endereco']
    cidade = request.form['cidade']
    telefone= request.form['telefone']
    email = request.form['email']
    descricao_prod = request.form['descricao_prod']
    defeito= request.form['defeito']
    observacao = request.form['observacao']

    servico = Servico(cliente, cpf, endereco, cidade, telefone, email, defeito, descricao_prod, observacao)

    #lista.append(servico)
    Servico_dao.salvar(servico)
    return redirect('/lista_servico')

@app.route('/criar_produto', methods=['POST',])
def criar_produto():
    descricao = request.form['descricao']
    categoria = request.form['categoria']
    valor = request.form['valor']
    estoque = request.form['estoque']

    produto = Produto(descricao,categoria,valor,estoque)

    #lista.append(servico)
    produto_dao.salvar(produto)
    return redirect('/lista_produtos')

@app.route('/criar_contasR', methods=['POST',])
def criar_contaR():
    cliente = request.form['cliente']
    valor = request.form['valor']
    equipamento = request.form['equipamento']
    data = request.form['data']
    id = request.form['id']

    contas = Conta(cliente,valor,equipamento,data,id)


    contaR_dao.salvar(contas)
    return redirect('/contas_receber')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima=''
    return render_template('login.html', proxima = proxima)
#-------------------------------------------------------------------------------
#REGISTRO DE USUARIO

@app.route('/registro')
def registro():
    proxima2= request.args.get('proxima2')
    return render_template('sem_cadastro.html', Usuario=proxima2)

@app.route('/salvarUsuario', methods=['POST',])
def salvarUsuario():
    nome = request.form['name']
    sobrenome = request.form['lastname']
    email = request.form['email']
    senha = request.form['password']
    if request.form.get('agree-term') == 0:
        termo = 0
    else:
        termo =1
    cadastro = Cadastro(nome, sobrenome, email, senha, termo)

    usuario_dao.salvar(cadastro)
    return redirect('/login')

#------------------------------------------------------------------------------------------------------------
@app.route('/trabalhe_conosco')
def trabalhe_conosco():
    return render_template('index.html', titulo="Trabalhe conosco")

#------------------------------------------------------------------------------------------------------------
@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario=usuario_dao.busca_por_id(request.form['usuario'])
    if usuario:
        if usuario._senha == request.form['senha']:
            session['usuario_logado']=request.form['usuario']
            flash(request.form['usuario'] + ' logou com sucesso!')
            proxima_pagina= request.form['proxima']
            if proxima_pagina == 'None':
                return redirect ('/')
            else:
                return redirect ('/{}'.format(proxima_pagina))

    flash('logado com sucesso')
    return redirect('/')
#------------------------------------------------------------------------------------------------------------
#Limpar sessão
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuario logado')
    return redirect('/login')
#------------------------------------------------------------------------------------------------------------
@app.route('/editar/<int:id>')
def editar(id):

    servico = Servico_dao.busca_por_id(id)
    return render_template('editar.html', titulo='Editando o Serviço', servico=servico)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    cliente = request.form['cliente']
    cpf = request.form['cpf']
    endereco = request.form['endereco']
    cidade = request.form['cidade']
    telefone= request.form['telefone']
    email = request.form['email']
    descricao_prod = request.form['descricao_prod']
    defeito= request.form['defeito']
    observacao = request.form['observacao']
    id = request.form['id']

    print(id)
    servico = Servico(cliente, cpf, endereco, cidade, telefone, email, defeito, descricao_prod, observacao,id)

   # lista.append(servico)
    Servico_dao.salvar(servico)
    return redirect('/lista_servico')
#------------------------------------------------------------------------------------------------------------
@app.route('/deletar/<int:id>')
def deletar(id):
    Servico_dao.deletar(id)
    return redirect('/lista_servico')

@app.route('/deletar_produto/<int:id>')
def deletar_produto(id):
    produto_dao.deletar(id)
    return redirect('/lista_produtos')

@app.route('/deletar_conta/<int:id>')
def deletar_conta(id):
    contaR_dao.deletar_conta(id)
    return redirect('/lista_contas')

@app.route('/deletar_usuario/<int:id>') #para entender que esta pegando o id como referencia
def deletar_usuario(id):
    usuario_dao.deletar_usuario(id)
    return redirect('/listar_usuario')


#------------------------------------------------------------------------------------------------------------
@app.route('/img/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('img', nome_arquivo)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/deletar/<int:id>')
def deletar(id):
    print(str(id))
    usuario_dao.deletar(str(id))
    return redirect('/')


@app.route('/editar_produto/<int:id>')
def editar(id):

    produto = produto_dao.busca_por_id(id)
    return render_template('editar.html', titulo='Editando o Serviço', produto=produto)


@app.route('/atualizar_produto', methods=['POST',])
def atualizar_produto():
    descricao = request.form['descricao']
    categoria = request.form['categoria']
    valor = request.form['valor']
    estoque = request.form['estoque']
    id= request.id['id']

    print(id)
    produto = Produto(descricao,categoria,valor,estoque,id)

    produto_dao.salvar(produto)
    return redirect('/')






