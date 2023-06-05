from main import app, db
from flask import render_template, request, url_for, session, flash, redirect
from helpers import FormularioUsuario
from models import Usuarios
from flask_bcrypt import check_password_hash, generate_password_hash


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    estilo_login = 'css/login.css'
    return render_template('login.html', titulo='Login', estilo=estilo_login, form=form, proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    form = FormularioUsuario(request.form)  # instanciar a validação do formulario
    usuario = Usuarios.query.filter_by(nome=form.nome.data).first()  # faz a query no banco de dados
    senha = check_password_hash(usuario.senha, form.senha.data)  # checa se a senha corresponde
    proxima_pagina = request.form['proxima']
    if usuario and senha:  # se usuario e senha estiverem corretos, segue o login
        session['usuario_logado'] = usuario.nome
        flash(usuario.nome + 'logado com sucesso')
        if proxima_pagina == 'None':
            proxima_pagina = url_for('home')
        return redirect(proxima_pagina)
    else:
        flash('Usuario não encontrado')
        return redirect(url_for('login'))


@app.route('/cadastro')
def cadastro():
    # if 'usuario_logado' not in session or session['usuario_logado'] == None:
    #     return redirect(url_for('login', proxima=url_for('novo')))
    form = FormularioUsuario()
    return render_template('cadastro.html', titulo='Novo Usuário', form=form)


@app.route('/criar', methods=['POST', ])
def criar():
    form = FormularioUsuario(request.form)
    print(form.email.data)
    print(form.email)
    if not form.validate_on_submit():
        flash('Erro!')
        return redirect(url_for('cadastro'))

    email = form.email.data
    nome = form.nome.data
    senha = form.senha.data
    conf_senha = form.conf_senha.data

    usuario = Usuarios.query.filter_by(email=email).first()

    if usuario:
        flash('Email já cadastrado!')
        return redirect(url_for('cadastro'))

    if senha != conf_senha:
        flash('As 2 senhas devem ser iguais!')
        return redirect(url_for('cadastro'))

    novo_usuario = Usuarios(email=email, nome=nome, senha=generate_password_hash(senha))
    db.session.add(novo_usuario)
    db.session.commit()

    # arquivo = request.files['arquivo']
    # upload_path = app.config['UPLOAD_PATH']
    # timestamp = time.time()
    # arquivo.save(f'{upload_path}/capa{nova_bike.id}-{timestamp}.jpg')

    return redirect(url_for('home'))