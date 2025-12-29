import pytest
from app import create_app, db
from app.models import Ensemble, Record, User
from datetime import date

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:", # Используем БД в памяти для тестов
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

# --- Юнит-тесты моделей ---

def test_create_ensemble(app):
    """Тестирование создания ансамбля (аналог test_create_patient)"""
    with app.app_context():
        ens = Ensemble(name="The Beatles", type="Рок-группа")
        db.session.add(ens)
        db.session.commit()
        assert ens.id is not None [cite: 36, 37]
        assert ens.name == "The Beatles"

def test_unique_record_catalog(app):
    """Тестирование уникальности номера каталога (аналог test_unique_medicine_name)"""
    with app.app_context():
        ens = Ensemble(name="Test")
        db.session.add(ens)
        db.session.commit()
        
        r1 = Record(catalog_number="ABC-123", title="Album 1", ensemble_id=ens.id)
        db.session.add(r1)
        db.session.commit() [cite: 42]
        
        r2 = Record(catalog_number="ABC-123", title="Album 2", ensemble_id=ens.id)
        db.session.add(r2)
        with pytest.raises(Exception): # Ожидаем ошибку из-за unique=True
            db.session.commit() [cite: 43]

# --- Интеграционные тесты (эндпоинты) ---

def test_health_check(client):
    """Проверка доступности (аналог test_health_check)"""
    # Если у вас нет /health, можно тестировать главную страницу
    response = client.get('/')
    assert response.status_code == 200 [cite: 66, 67]

def test_add_ensemble_route(client, app):
    """Проверка добавления через POST (аналог test_add_patient)"""
    # Предполагается наличие маршрута /add-ensemble в app.routes
    response = client.post('/add-ensemble', data={
        'name': 'Queen',
        'type': 'Rock'
    }, follow_redirects=True)
    
    with app.app_context():
        assert Ensemble.query.filter_by(name='Queen').first() is not None [cite: 72, 73]
