from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db.db import Base

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, unique=True)  # ← UNIQUE в БД!
    
    #добавлено каскадное удаление
    books = relationship("Book", back_populates="category", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"Категория: {self.title}"

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    url = Column(String(500))

    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)

    category = relationship("Category", back_populates="books")
    
    def __repr__(self):
        return f"Книга: {self.title} ({self.price} руб.)"