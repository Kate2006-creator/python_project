# API для библиотеки книг

## Описание проекта
API позволяет:
- Создавать, читать, обновлять и удалять книги
- Создавать, читать, обновлять и удалять категории
- Фильтровать книги по категории
- Получать детальную информацию о книгах и категориях

## Технологии

- FastAPI— современный фреймворк для Python
- SQLAlchemy —  для работы с базами данных
- PostgreSQL —  база данных
- Pydantic — валидация данных
- Uvicorn — сервер

## Установка и запуск

### Клонирование репозитория
git clone <your-url>
cd python_project

### Настройка виртуального окружения
- python3 -m venv venv
- source venv/bin/activate  # Linux/WSL
# или
- venv\Scripts\activate     # Windows

## Установка зависимостей
pip install -r requirements.txt

## Настройка базы данных, создание пользователя и базы данных
sudo -u postgres psql
CREATE USER octagon WITH PASSWORD '12345';
CREATE DATABASE octagon_db OWNER octagon;
GRANT ALL PRIVILEGES ON DATABASE octagon_db TO octagon;

## Настройка переменных окружения
Создать файл .env в корне проекта:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345

## Инициализация базы данных
python3 -m app.init_db

## Запуск сервера
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

## API Документация
После запуска сервера документация доступна по адресам:

- Swagger UI: http://127.0.0.1:8000/docs

- ReDoc: http://127.0.0.1:8000/redoc

- Health Check: http://127.0.0.1:8000/health