from app.db.db import engine, SessionLocal
from app.db.models import Base
from app.db.crud import create_category, create_book

def init_database():
    Base.metadata.create_all(bind=engine)
    print("Таблицы созданы!")

    db = SessionLocal()
    
    try:
        cat1 = create_category(db, "Художественная литература")
        print(f"Категория: {cat1.title}")
        
        cat2 = create_category(db, "Научная литература")
        print(f"Категория: {cat2.title}")
        
        books_category1 = [
            ("Война и мир", "Роман Льва Толстого", 450.00, " "),
            ("Преступление и наказание", "Роман Федора Достоевского", 350.00, " "),
            ("Мастер и Маргарита", "Роман Михаила Булгакова", 400.00, " "),
        ]
        
        for title, desc, price, url in books_category1:
            book = create_book(db, title, desc, price, cat1.id, url)
            print(f" Книга: {book.title}")
        
        books_category2 = [
            ("Краткая история времени", "Стивен Хокинг", 550.00, " "),
            ("Будущее разума", "Митио Каку", 500.00, " "),
            ("Структура научных революций", "Томас Кун", 420.00, " "),
        ]
        
        for title, desc, price, url in books_category2:
            book = create_book(db, title, desc, price, cat2.id, url)
            print(f"Книга: {book.title}")
        
        
    except Exception as e:
        print(f"\nОШИБКА: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_database()