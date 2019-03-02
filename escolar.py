# Importando bibliotecas
from bd_simulado import *
from flask import Flask, url_for, redirect, request, render_template

# Instanciando a app Flask
app = Flask(__name__)

# Rota para /
@app.route('/')
def principal():
    return render_template('index.html')

# Rota para /login
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        # Verificar a senha
        if (login == get_login()) & (senha == '1'):
            return render_template('oi.html', nome=login)
        else:
            return render_template('index.html',erro="erro")

    else:
        return render_template('index.html',erro='Método incorreto, Use POST!')

# Rodando a app
if __name__ == '__main__':
    app.run(debug=True)