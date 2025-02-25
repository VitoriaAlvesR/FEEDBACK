# Documento criado apenas para testes 👍🏾

from flask import Flask,render_template,form,request,redirect,datetime
# import random

app = Flask(__name__)
#Colocando as rotas logo abaixo 👇🏾

@app.route("/")
def pagina_principal ():
    # Toda função tem um retorno 💪🏾
    return render_template('index.html')

@app.route('/post/comentario', methods = ['POST'])
def post_comentario ():
    # Pegando as informações vinda do formulário do index.html
    pega_usuario = request.form.get('usuario') 
    pega_comentario = request.form.get('comentario')
    dataehora = datetime.datetime.today

    # Cadastramento das informações no banco de dados 👇🏾

    # Esse comando está redirecionando para o index 👇🏾
    return redirect('/index.html')
#Colocando o programa funcionar,correr 🏃🏾‍♀️
app.run(debug = True)