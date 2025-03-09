from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user

from models.usuarios import Usuarios
from models.perros import Perros
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
        es_admin = user.es_admin

        if es_admin:
            perros = Perros.query.all()

            return render_template('listado.html', perros=perros, current_user=current_user)
        else:
            return render_template('bienvenida.html', current_user=current_user)
    else:
        return render_template('404.html')

@home_blueprint.route('/logout')
def logout():
    logout_user()
    return render_template('login.html')
