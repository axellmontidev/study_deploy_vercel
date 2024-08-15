from flask import Flask, render_template

app = Flask(__name__)

#criar a primeira página do site
#route -> o que vem depois do domínio ex.: sitealeatorio.com/contatos o contatos é a route
#função -> o que queremos exibir na página
#template
@app.route("/") #quando é somente a / ele direciona para a home
def homepage():
    return render_template("home_page.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)
#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True) #faz com que fique atualizando automaticamente

#servidor Heroku

