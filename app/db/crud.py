from sqlalchemy.orm import Session
from app.db import models
from sqlalchemy import and_

def create_category(db: Session, title: str):
    new_category = models.Category(title=title)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_all_categories(db: Session):
    return db.query(models.Category).all()

def get_category_by_id(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_category_by_title(db: Session, title: str):
    return db.query(models.Category).filter(models.Category.title == title).first()

def update_category(db: Session, category_id: int, new_title: str):
    category = get_category_by_id(db, category_id)
    if not category:
        return None
    
    #проверка уникальности названия
    if new_title and new_title != category.title:
        existing = get_category_by_title(db, new_title)
        if existing:
            raise ValueError(f"Category with '{new_title}' exists")
        category.title = new_title
        db.commit()
        db.refresh(category)
    
    return category

def delete_category(db: Session, category_id: int):
    category = get_category_by_id(db, category_id)
    if category:
        db.delete(category)
        db.commit()
    return category


def create_book(db: Session, title: str, description: str, price: float, category_id: int, url: str = None):
    category = get_category_by_id(db, category_id)
    if not category:
        raise ValueError(f"Category {category_id} does not exist")
    
    new_book = models.Book(
        title=title,
        description=description,
        price=price,
        category_id=category_id,
        url=url
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_all_books(db: Session, category_id: int = None):
    query = db.query(models.Book)
    if category_id is not None:
        query = query.filter(models.Book.category_id == category_id)
    return query.all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db: Session, book_id: int, **kwargs):
    book = get_book_by_id(db, book_id)
    if not book:
        return None

    if 'category_id' in kwargs and kwargs['category_id'] is not None:
        category = get_category_by_id(db, kwargs['category_id'])
        if not category:
            raise ValueError(f"Category {kwargs['category_id']} does not exist")
    
    for key, value in kwargs.items():
        if value is not None and hasattr(book, key):
            setattr(book, key, value)
    
    db.commit()
    db.refresh(book)
    return book

def delete_book(db: Session, book_id: int):
    book = get_book_by_id(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book