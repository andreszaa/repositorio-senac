# Importa o Flask, render template e todos os módulos 0necessários
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# cria uma instancia da aplicacao flask
app = Flask(__name__)

# fazer uma conexao com o bando de dados SQLite
# está funcao sera usada para conectar ao banco de dados
def conectar_banco():
    conn = sqlite3.connect('banco.db') # cria  o arquivo 'banco.db'
    return conn

def criar_tabela():
    conn = conectar_banco()
    cursor = conn.cursor()

    # criar tabela 'contatos' com as colunas necessarias
    cursor.execute('''
    CREATE TABLE IF NOT EXIST contatos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        mensagem TEXT NOT NULL,
        tema TEXT NOT NULL
        )
        ''')
    conn.commit()
    conn.close()
@app.route('/')
def index():
    return render_template('index.html')
    # rota para processar o formulario e salvar os dados no banco de dados
@app.route('/contato', methods=['POST'])
def contato():
    # coletar os dados do formulario
    nome = request.form['nome']
    email = request.form['email']
    mensagem = request.form['mensagem']
    tema = request.form.get('tema')

    # conectar ao banco de dados e inserir os dados informados
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO contatos (nome, email, mensagem, tema)
    VALUES (?, ?, ?, ?)''', (nome, email, mensagem, tema))
    conn.commit()
    conn.close()

    # Redirecionar para uma pagina que mostra os dados salvos
    return redirect(url_for('resultado'))

# Rota para exibir os dados inseridos no banco
@app.route('/resultado')
def resultado():
    #Conectar ao banco de dados e buscar os dados
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('SELECT nome, email, mensagem, tema FROM contatos')
    dados = cursor.fetchall() #Pega todos os dados da tabela 'contatos'
    conn.close

    # Renderizar a pagina de resultado com os dados
    return render_template('resultado.html', contatos = dados)

if __name__ == 'main':
    criar_tabela() # Chama a funcao para criar a tabela, se ela nao existir
    app.run(debug=True)


