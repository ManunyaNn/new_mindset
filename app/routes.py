from flask import render_template, request, flash, redirect, url_for, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from app import db
from app.models import User, Ensemble, Record

main = Blueprint('main', __name__)

# Главная страница - доступна всем
@main.route('/')
def index():
    ensembles = Ensemble.query.all()
    return render_template('index.html', ensembles=ensembles)

# Страница входа
@main.route('/login', methods=['GET', 'POST'])
def login():
    # Если пользователь уже авторизован, перенаправляем на главную
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Ищем пользователя в базе
        user = User.query.filter_by(username=username).first()
        
        # Проверяем пароль
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash(f'Добро пожаловать, {username}!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.index'))
        else:
            flash('Неверное имя пользователя или пароль', 'danger')
    
    return render_template('login.html')

# Выход из системы
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из системы', 'info')
    return redirect(url_for('main.index'))

# Защищенная страница (пример)
@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

# Страница ансамбля - доступна всем
@main.route('/ensemble/<int:ensemble_id>')
def ensemble_detail(ensemble_id):
    ensemble = Ensemble.query.get_or_404(ensemble_id)
    records = Record.query.filter_by(ensemble_id=ensemble_id).all()
    return render_template('ensemble_detail.html', ensemble=ensemble, records=records)