from flask import Flask, render_template, request, redirect, session,flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console
        
jogo1= Jogo('Tetris', 'Puzzle', 'Atari')
jogo2= Jogo('Skyrim', 'MMRPG', 'PS3')
jogo3= Jogo('God of War', 'Rack n Slash', 'PS2')
lista = [jogo1, jogo2, jogo3]

class Usuario:
    def __init__(self,nome,nickname,senha):
        self.nome=nome
        self.nickname=nickname
        self.senha=senha

usuario1 = Usuario('Lucas','Lutas','12345')
usuario2 = Usuario('Carlos','Carlão','peneira')
usuario3 = Usuario('José','Zé','caldo')

usuarios ={ usuario1.nickname: usuario1, 
            usuario2.nickname: usuario2, 
            usuario3.nickname: usuario3}

app = Flask(__name__)
app.secret_key = 'candelabro'

@app.route('/')
def index():

    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)



@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' foi logado com sucesso')
            proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Usuario não encontrado')
        return redirect('/login')
    
@app.route('/deslogar')
def deslogar():
    session['usuario_logado'] = None
    flash('Deslogado com sucesso')
    return redirect('/')

    
app.run(debug=True)