from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import books, categories
from app.db.db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book API",
    description="API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router)
app.include_router(categories.router)

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok", "message": "Service is running"}

@app.get("/", tags=["root"])
def root():
    return {
        "message": "Welcome to Book Library API",
        "docs": "/docs",
        "health": "/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)