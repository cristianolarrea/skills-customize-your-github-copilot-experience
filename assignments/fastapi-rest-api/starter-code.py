from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
    {"id": 2, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "year": 1999},
    {"id": 3, "title": "Designing Data-Intensive Applications", "author": "Martin Kleppmann", "year": 2017},
]


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", status_code=201)
def create_book(payload: BookCreate):
    new_id = max((book["id"] for book in books), default=0) + 1
    new_book = {"id": new_id, **payload.model_dump()}
    books.append(new_book)
    return new_book


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            deleted = books.pop(index)
            return {"message": "Book removed", "book": deleted}
    raise HTTPException(status_code=404, detail="Book not found")
