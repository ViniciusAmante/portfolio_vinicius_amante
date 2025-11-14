from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/curriculo')
def curriculo():
    return render_template('curriculo.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/habilidades')
def habilidades():
    return render_template('habilidades.html')

@app.route('/documentos')
def documentos():
    return render_template('docs.html')

@app.route('/certificacoes')
def certificacoes():
    return render_template('certificados.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)