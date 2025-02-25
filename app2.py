from flask import Flask,render_template,request,redirect
import datetime
import mysql.connector
# import random

app = Flask(__name__)
#Colocando as rotas logo abaixo 👇🏾

@app.route("/")
def pagina_principal ():
    # Toda função tem um retorno 💪🏾
    return render_template('index.html')

@app.route('/post/comentario', methods = ['POST'])
def post_comentario ():
    # Pegando as informações vinda do formulário do index.html 💪🏾
    pega_usuario = request.form.get('usuario') 
    pega_comentario = request.form.get('comentario')
    dataehora = datetime.datetime.today()

    # Cadastramento das informações no banco de dados, conexao do banco de dados 👇🏾

    conexao = mysql.connector.connect(host = 'localhost',
                                     port = 3306,
                                     user = 'root',
                                     password = 'root',
                                     database = 'db_feedback')
    

    # Responsável pela manipulação do banco de dados 👇🏾
    cursor = conexao.cursor()

    # Comando responsável pela criação do SQL que será executado 👇🏾
    sql = """INSERT INTO tb_comentarios
                (nome, dataehora_comentario, comentario)
              VALUES
                (%s,%s,%s)"""
    
    # Comando para colocar os valores do form nos valores do sql 👇🏾
    valores = (pega_usuario,dataehora,pega_comentario)

    # Comando para a execussão do comando SQL 👇🏾
    cursor.execute(sql,valores)

    # Comando para a conifrmação do comando👇🏾 
    conexao.commit()

    #Comando para o fechamento dconexão com a banco de dados 👇🏾
    cursor.close()
    conexao.close()

    # Esse comando está redirecionando para o index 👇🏾
    return redirect('/')

#Colocando o programa funcionar,correr 🏃🏾‍♀️
app.run(debug = True)