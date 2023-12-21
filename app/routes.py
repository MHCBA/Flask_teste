from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    dado = {'professor': "Cauê Moura", 'Canal': "Desce a Letra", }
    return render_template('index.html', nome = 'Michell', dado = dado)
@app.route('/contato')
def contato():
    return render_template('contato.html')