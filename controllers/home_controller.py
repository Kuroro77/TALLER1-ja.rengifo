from flask import Blueprint, render_template
from models.usuarios import Usuarios
from config.auth import login_manager

home_blueprint = Blueprint("home", __name__)

@login_manager.user_loader
def load_user(user_id:int):
    return Usuarios.query.get(int(user_id))

@home_blueprint.route('/')
def login():
    return render_template('login.html')