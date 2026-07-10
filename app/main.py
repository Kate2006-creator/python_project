from app.db.db import SessionLocal
from app.db.crud import get_all_categories, get_all_books

def main():
    db = SessionLocal()
    
    try:
        print("\nКАТЕГОРИИ:")
        categories = get_all_categories(db)
        for cat in categories:
            print(f"{cat.title}")
        
        print("\nКНИГИ:")
        books = get_all_books(db)
        for book in books:
            print(f"{book.title}")
            print(f" Цена: {book.price} руб.")
            print(f" Категория: {book.category.title}")
            print(f" Описание: {book.description}")
            print(f" Ссылка: {book.url}")
            print()
        
    except Exception as e:
        print(f"ОШИБКА: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()