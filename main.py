from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Sample book model
class Book(BaseModel):
    title: str
    author: str
    description: str

# In-memory database to store books
books_db = {
    1: Book(title="The Catcher in the Rye", author="J.D. Salinger", description="A story about teenage rebellion."),
    2: Book(title="To Kill a Mockingbird", author="Harper Lee", description="A novel about racial inequality."),
    3: Book(title="1984", author="George Orwell", description="A dystopian novel about a totalitarian regime."),
}

# POST /books - Create a new book
@app.post("/books")
async def create_book(book: Book):
    book_id = max(books_db.keys()) + 1 if books_db else 1  # Generate new book ID
    books_db[book_id] = book
    return {"id": book_id, "book": book}

# GET /books - Get a list of all books
@app.get("/books")
async def get_books():
    return books_db

# GET /books/{id} - Get a specific book by ID
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[book_id]

# PUT /books/{id} - Update a specific book by ID
@app.put("/books/{book_id}")
async def update_book(book_id: int, book: Book):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    books_db[book_id] = book
    return {"id": book_id, "book": book}

# DELETE /books/{id} - Delete a specific book by ID
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    del books_db[book_id]
    return {"message": "Book deleted successfully"}

