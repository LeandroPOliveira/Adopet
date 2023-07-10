from main import app, db
from flask import render_template, request, url_for, session, flash, redirect
from helpers import FormularioUsuario, FormularioPerfil, recupera_imagem
from models import Usuarios
from flask_bcrypt import check_password_hash, generate_password_hash
from main import login_manager
from flask_login import login_user, current_user
from PIL import Image


@login_manager.user_loader
def load_user(usuarios_id):
    return Usuarios.query.get(int(usuarios_id))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    estilo_login = 'css/login.css'
    return render_template('login.html', titulo='Login', estilo=estilo_login, form=form, proxima=proxima, visibility='hidden')


@app.route('/autenticar', methods=['GET', 'POST'])
def autenticar():
    form = FormularioUsuario(request.form)  # instanciar a validação do formulario
    usuario = Usuarios.query.filter_by(email=form.email.data).first()  # faz a query no banco de dados
    senha = check_password_hash(usuario.senha, form.senha.data)  # checa se a senha corresponde
    proxima_pagina = request.form['proxima']
    if usuario and senha:  # se usuario e senha estiverem corretos, segue o login
        session['usuario_logado'] = usuario.email
        login_user(usuario)
        flash(usuario.nome + ' logado com sucesso', 'sucesso')
        if proxima_pagina == 'None':
            proxima_pagina = url_for('home')
        return redirect(proxima_pagina)
    else:
        flash('Usuario não encontrado', 'erro')
        return redirect(url_for('login'))


@app.route('/cadastro')
def cadastro():
    # if 'usuario_logado' not in session or session['usuario_logado'] == None:
    #     return redirect(url_for('login', proxima=url_for('novo')))
    form = FormularioUsuario()
    return render_template('cadastro.html', titulo='Novo Usuário', form=form, visibility='hidden')


@app.route('/criar', methods=['POST', ])
def criar():
    form = FormularioUsuario(request.form)
    print(form.email.data)
    print(form.email)
    if not form.validate_on_submit():
        flash('Erro!', 'erro')
        return redirect(url_for('cadastro'))

    email = form.email.data
    nome = form.nome.data
    senha = form.senha.data
    conf_senha = form.conf_senha.data

    usuario = Usuarios.query.filter_by(email=email).first()

    if usuario:
        flash('Email já cadastrado!', 'erro')
        return redirect(url_for('cadastro'))

    if senha != conf_senha:
        flash('As 2 senhas devem ser iguais!', 'erro')
        return redirect(url_for('cadastro'))

    novo_usuario = Usuarios(email=email, nome=nome, senha=generate_password_hash(senha))
    db.session.add(novo_usuario)
    db.session.commit()
    flash('Usuário cadastrado com sucesso!', 'sucesso')

    upload_path = app.config['UPLOAD_PATH']
    arquivo = Image.open(f'{upload_path}/Usuário.png')
    # timestamp = time.time()
    arquivo.save(f'{upload_path}/user{novo_usuario.id}.png')

    return redirect(url_for('home'))


@app.route('/perfil')
def perfil():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('perfil')))
    form = FormularioPerfil()
    usuario = Usuarios.query.filter_by(id=current_user.id).first()
    form.nome.data = usuario.nome
    form.telefone.data = usuario.telefone
    form.cidade.data = usuario.cidade
    form.sobre.data = usuario.sobre
    capa_jogo = recupera_imagem(current_user.id)
    return render_template('perfil.html', titulo='Meu perfil', visibility='visible', form=form, capa_jogo=capa_jogo)


@app.route('/atualizar', methods=['POST', ])
def atualizar():
    form = FormularioPerfil(request.form)

    if form.validate_on_submit():
        perfil = Usuarios.query.filter_by(id=current_user.id).first()
        perfil.nome = form.nome.data
        perfil.telefone = form.telefone.data
        perfil.cidade = form.cidade.data
        perfil.sobre = form.sobre.data

        db.session.add(perfil)
        db.session.commit()

        arquivo = request.files['arquivo']

        if arquivo.filename == '':
            pass
        else:
            upload_path = app.config['UPLOAD_PATH']
            # timestamp = time.time()
            # deleta_arquivo(bike.id)
            arquivo.save(f'{upload_path}/user{perfil.id}.png')
            flash('Perfil atualizado com sucesso!', 'sucesso')

    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!', 'sucesso')
    return redirect(url_for('index'))
