# Importação do Flask e dos modulos necessarios do Flask
from flask import Flask, render_template, request

# Criar uma instância da aplicação Flask. O nome '__name__'
# define o nome do módulo atual, essa linha informa ao Flask
# onde encontrar os arquivos como templates e estáticos.
app = Flask(__name__)

# Definir a rota principal da aplicação. Essa função é chamada 
# quando acessamos a URL raiz '/'
@app.route('/')
def index():
    return render_template('index.html')

# definir a rota para o processamento do formulario
@app.route('/contato', methods=['POST'])
def contato():
    nome = request.form['nome'] 
    email = request.form['email']
    mensagem = request.form['mensagem']
    tema = request.form['tema']

    return f'''
    <h1>Obrigado, {nome}</h1>
    <p>Recebemos sua mensagem:</p>
    <p><strong>E-mail:</strong>{email}</p>
    <p><strong>Mensagem:</strong>{mensagem}</p>
    <p><strong>Tema:</strong>{tema}</p>
    '''

if __name__=='__main__':
    app.run(debug=True)
    