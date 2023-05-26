from main import app
from flask import render_template

@app.route('/')
def home():
    estilo_home = 'css/index.css'
    return render_template('index.html', titulo='Home', estilo=estilo_home)
