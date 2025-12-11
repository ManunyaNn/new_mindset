from app import create_app, db
from app.models import User, Ensemble, Record
from datetime import date
from werkzeug.security import generate_password_hash

def init_database():
    app = create_app()
    
    with app.app_context():
        print("🔄 Начинаем инициализацию базы данных...")
        
        # Удаляем все существующие таблицы
        print("🗑️  Удаляем старые таблицы...")
        db.drop_all()
        
        # Создаем таблицы заново
        print("📦 Создаем новые таблицы...")
        db.create_all()
        
        print("🎵 Добавляем тестовые данные с реальными картинками...")
        # Создаем тестовых пользователей
        users = [
            User(
                username='admin',
                password_hash=generate_password_hash('123456'),
                role='admin'
            ),
            User(
                username='manager',
                password_hash=generate_password_hash('123456'),
                role='manager'
            ),
            User(
                username='user',
                password_hash=generate_password_hash('123456'),
                role='user'
            ),
        ]
        
        for user in users:
            db.session.add(user)
        
        db.session.commit()
        print("✅ Пользователи добавлены!")
        
        print("🎵 Добавляем ансамбли и пластинки...")
        # Ансамбли с реальными URL картинками
        beatles = Ensemble(
            name="The Beatles", 
            type="Рок-группа",
            description="Легендарная британская рок-группа из Ливерпуля, основанная в 1960 году.",
            image_url="https://tv-english.club/wp-content/uploads/2016/02/%D0%B1%D0%B8%D1%82%D0%BB%D0%B72.jpg"
        )
        
        queen = Ensemble(
            name="Queen", 
            type="Рок-группа", 
            description="Британская рок-группа, добившаяся широчайшей известности в середине 1970-х годов.",
            image_url="https://nacion.ru/assets/i/ai/4/7/2/i/3237339.jpg"
        )
        
        pink_floyd = Ensemble(
            name="Pink Floyd", 
            type="Прогрессив-рок",
            description="Британская рок-группа, знаменитая своими философскими текстами и звуковыми экспериментами.",
            image_url="https://upload.wikimedia.org/wikipedia/ru/thumb/1/15/The_Dark_Side_of_the_Moon.png/330px-The_Dark_Side_of_the_Moon.png"
        )
        
        metallica = Ensemble(
            name="Metallica", 
            type="Трэш-метал",
            description="Американская метал-группа, оказавшая значительное влияние на развитие метала.",
            image_url="https://i.ytimg.com/vi/XV1NzsrldC4/maxresdefault.jpg"
        )
        
        orchestra = Ensemble(
            name="Лондонский симфонический оркестр", 
            type="Оркестр",
            description="Один из ведущих симфонических оркестров Великобритании.",
            image_url="https://thecellist.ru/wp-content/uploads/2020/06/Londonskij-simfonicheskij-orkestr.jpg"
        )
        
        acdc = Ensemble(
            name="AC/DC", 
            type="Хард-рок",
            description="Австралийская рок-группа, основанная в 1973 году. Известна энергичными выступлениями и хард-рок саундом.",
            image_url="https://guitarprofi.ru/wp-content/uploads/2015/04/AC-DC-1024x768.jpg"
        )

        # Добавляем все ансамбли
        ensembles = [beatles, queen, pink_floyd, metallica, orchestra, acdc]
        for ensemble in ensembles:
            db.session.add(ensemble)
        
        db.session.commit()
        print("✅ Ансамбли добавлены!")
        
        # Создаем пластинки
        records_data = [
            # The Beatles
            {"catalog": "ABC-001", "title": "Abbey Road", "company": "Apple Records", "price": 2500, "stock": 15, "ensemble": beatles},
            {"catalog": "ABC-002", "title": "The White Album", "company": "Apple Records", "price": 2800, "stock": 10, "ensemble": beatles},
            {"catalog": "ABC-003", "title": "Sgt. Pepper's Lonely Hearts Club Band", "company": "Parlophone", "price": 2700, "stock": 8, "ensemble": beatles},
            
            # Queen
            {"catalog": "QUE-001", "title": "A Night at the Opera", "company": "EMI", "price": 2200, "stock": 8, "ensemble": queen},
            {"catalog": "QUE-002", "title": "News of the World", "company": "EMI", "price": 2100, "stock": 12, "ensemble": queen},
            {"catalog": "QUE-003", "title": "The Game", "company": "EMI", "price": 2300, "stock": 6, "ensemble": queen},
            
            # Pink Floyd
            {"catalog": "PF-001", "title": "The Dark Side of the Moon", "company": "Harvest", "price": 2900, "stock": 20, "ensemble": pink_floyd},
            {"catalog": "PF-002", "title": "The Wall", "company": "Harvest", "price": 3100, "stock": 15, "ensemble": pink_floyd},
            {"catalog": "PF-003", "title": "Wish You Were Here", "company": "Harvest", "price": 2600, "stock": 10, "ensemble": pink_floyd},
            
            # Metallica
            {"catalog": "MET-001", "title": "Master of Puppets", "company": "Elektra", "price": 2400, "stock": 18, "ensemble": metallica},
            {"catalog": "MET-002", "title": "The Black Album", "company": "Elektra", "price": 2200, "stock": 25, "ensemble": metallica},
            {"catalog": "MET-003", "title": "Ride the Lightning", "company": "Megaforce", "price": 2100, "stock": 12, "ensemble": metallica},
            
            # Оркестр
            {"catalog": "LSO-001", "title": "Бетховен: 9 симфоний", "company": "Decca", "price": 3500, "stock": 5, "ensemble": orchestra},
            {"catalog": "LSO-002", "title": "Моцарт: Реквием", "company": "Decca", "price": 1800, "stock": 8, "ensemble": orchestra},
            {"catalog": "LSO-003", "title": "Чайковский: Лебединое озеро", "company": "Decca", "price": 2000, "stock": 10, "ensemble": orchestra},
        
             # AC/DC
            {"catalog": "ACD-001", "title": "Back in Black", "company": "Atlantic", "price": 2300, "stock": 22, "ensemble": acdc},
            {"catalog": "ACD-002", "title": "Highway to Hell", "company": "Atlantic", "price": 2100, "stock": 18, "ensemble": acdc},
            {"catalog": "ACD-003", "title": "High Voltage", "company": "Atlantic", "price": 1900, "stock": 14, "ensemble": acdc},
        ]

        
        for record_data in records_data:
            record = Record(
                catalog_number=record_data["catalog"],
                title=record_data["title"],
                company=record_data["company"],
                release_date=date(2020, 1, 1),
                retail_price=record_data["price"],
                current_stock=record_data["stock"],
                ensemble_id=record_data["ensemble"].id
            )
            db.session.add(record)
        
        db.session.commit()
        print("✅ Пластинки добавлены!")
        print(f"📊 Итоги:")
        print(f"   • Ансамбли: {len(ensembles)}")
        print(f"   • Пластинки: {len(records_data)}")
        print("🎉 База данных успешно инициализирована!")

if __name__ == '__main__':
    init_database()