from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import crud
from app import schemas

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=List[schemas.BookResponse])
def get_books(
    category_id: Optional[int] = Query(None, description="Фильтр по категории"),
    db: Session = Depends(get_db)
):
    if category_id:
        return crud.get_books_by_category(db, category_id)
    return crud.get_all_books(db)

@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Получить книгу по ID"""
    book = crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category_by_id(db, book.category_id)
    if not category:
        raise HTTPException(status_code=400, detail="Category not found")
    return crud.create_book(
        db,
        title=book.title,
        description=book.description,
        price=book.price,
        category_id=book.category_id,
        url=book.url
    )

@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_id(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book.category_id:
        category = crud.get_category_by_id(db, book.category_id)
        if not category:
            raise HTTPException(status_code=400, detail="Category not found")
    
    update_data = book.model_dump(exclude_unset=True)
    return crud.update_book(db, book_id, **update_data)

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    crud.delete_book(db, book_id)
    return None