from flask import render_template, Blueprint
from app import db
from app.models import Ensemble, Record

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # Получаем все ансамбли для главной страницы
    ensembles = Ensemble.query.all()
    return render_template('index.html', ensembles=ensembles)

@main.route('/ensemble/<int:ensemble_id>')
def ensemble_detail(ensemble_id):
    # Страница конкретного ансамбля с его пластинками
    ensemble = Ensemble.query.get_or_404(ensemble_id)
    records = Record.query.filter_by(ensemble_id=ensemble_id).all()
    return render_template('ensemble_detail.html', ensemble=ensemble, records=records)