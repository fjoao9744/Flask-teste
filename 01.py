#vou colocar esse site no ar

from flask import Flask, render_template 
app = Flask(__name__) 


@app.route("/") 
def pagina_inicial(): 
    return render_template("pagina-inicial.html") 

@app.route("/alunos")
def alunos():
    return render_template("alunos.html") 

@app.route("/alunos/<nome_aluno>") 
def usuarios(nome_aluno): 
    return render_template("aluno.html", nome = nome_aluno) #coloca o parametro para mandar para o html


if __name__ == '__main__':
    app.run(debug = True) 