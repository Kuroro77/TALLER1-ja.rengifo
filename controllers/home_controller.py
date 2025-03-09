from flask import Blueprint, render_template, request
from flask_login import login_user, current_user

from models.usuarios import Usuarios
from config.auth import login_manager

home_blueprint = Blueprint("home", __name__)

@login_manager.user_loader
def load_user(user_id:int):
    return Usuarios.query.get(int(user_id))

@home_blueprint.route('/')
def login():
    return render_template('login.html')

@home_blueprint.route('/auth')
def auth():
    username = request.args.get("username")
    password = request.args.get("password")

    user = Usuarios.query.filter_by(username=username, password=password).first()

    if user:
        login_user(user)
        return render_template('bienvenida.html', current_user= current_user)
    else:
        return render_template('404.html')