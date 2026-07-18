from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Optional

#добавила ограничения
class CategoryBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Название категории")
    
    @field_validator('title')
    def title_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Название категории не может быть пустым')
        return v.strip()

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100, description="Новое название категории")
    
    @field_validator('title')
    def title_not_empty(cls, v):
        if v is not None and not v.strip():
            raise ValueError('Название категории не может быть пустым')
        return v.strip() if v else v

class CategoryResponse(CategoryBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="Название книги")
    description: Optional[str] = Field(None, max_length=1000, description="Описание книги")
    price: float = Field(..., gt=0, description="Цена книги (должна быть больше 0)")
    url: Optional[str] = Field(None, max_length=500, description="Ссылка на книгу")
    category_id: int = Field(..., gt=0, description="ID категории")
    
    @field_validator('title')
    def title_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Название книги не может быть пустым')
        return v.strip()
    
    @field_validator('price')
    def price_positive(cls, v):
        if v <= 0:
            raise ValueError('Цена должна быть больше 0')
        return v

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    price: Optional[float] = Field(None, gt=0)
    url: Optional[str] = Field(None, max_length=500)
    category_id: Optional[int] = Field(None, gt=0)
    
    @field_validator('title')
    def title_not_empty(cls, v):
        if v is not None and not v.strip():
            raise ValueError('Название книги не может быть пустым')
        return v.strip() if v else v
    
    @field_validator('price')
    def price_positive(cls, v):
        if v is not None and v <= 0:
            raise ValueError('Цена должна быть больше 0')
        return v

class BookResponse(BookBase):
    id: int
    category: Optional[CategoryResponse] = None
    model_config = ConfigDict(from_attributes=True)