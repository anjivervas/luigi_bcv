from flask import Blueprint, render_template

main_bp = Blueprint('main',__name__)

@main_bp.route ('/')
def index():
    print('Estoy en la ruta principal')
    return render_template('index.html')

@main_bp.route('/acerca-de')
def about():
    return render_template('about.html')