-- Схема таблицы Ансамблей
CREATE TABLE IF NOT EXISTS ensemble (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50),
    description TEXT,
    image_url VARCHAR(200)
);

-- Схема таблицы Пластинок
CREATE TABLE IF NOT EXISTS record (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    catalog_number VARCHAR(50) NOT NULL UNIQUE,
    title VARCHAR(200) NOT NULL,
    company VARCHAR(100),
    release_date DATE,
    retail_price FLOAT,
    current_stock INTEGER DEFAULT 0,
    ensemble_id INTEGER NOT NULL,
    FOREIGN KEY (ensemble_id) REFERENCES ensemble (id)
);

-- Схема таблицы Пользователей
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(80) NOT NULL UNIQUE,
    password_hash VARCHAR(128) NOT NULL
);
