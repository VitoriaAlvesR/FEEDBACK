from flask import Flask, render_templates
import random

app = Flask (__name__)
#Colocando as rotas logo abaixo 👇

@app.route("/")
def pagina_principal ():
    # Toda função tem um retorno
    return "Página principal"
#Colocando o programa funcionar,correr 🏃🏾‍♀️
app.run(debug = True)