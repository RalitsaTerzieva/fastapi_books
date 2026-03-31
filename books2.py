from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status
import redis


app = FastAPI()
cache = redis.Redis(host='redis', port=6379)

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_data: int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int, published_data: int):
        self.id = id
        self.title = title

        self.author = author
        self.description = description
        self.rating = rating
        self.published_data = published_data



class BookRequest(BaseModel):
    id: Optional[int] = Field(description="Id is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=200)
    rating: int = Field(gt=0, lt=6)
    published_data: Optional[int] = Field(gt=0, lt=2026)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "description": "A classic American novel set in the Jazz Age.",
                "rating": 5,
            }
        }
    }



BOOKS = [
    Book(1, "Clean Code", "Robert C. Martin", "A guide to writing clean and maintainable code.", 5, 2000),
    Book(2, "The Pragmatic Programmer", "Andrew Hunt", "Best practices and philosophy of software development.", 5, 2002),
    Book(3, "Design Patterns", "Erich Gamma", "Classic book about reusable software design patterns.", 5, 2001),
    Book(4, "Atomic Habits", "James Clear", "How small habits create big improvements in life.", 4, 2018),
    Book(5, "Deep Work", "Cal Newport", "Strategies for focused success in a distracted world.", 4, 2017),
    Book(6, "Python Crash Course", "Eric Matthes", "Beginner-friendly introduction to Python programming.", 4, 2019),
]

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def get_book_by_id(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found!")
        

@app.get("/books/", status_code=status.HTTP_200_OK)
async def get_books_by_rating(rating: int = Query(gt=0, lt=6)):
    return [book for book in BOOKS if book.rating == rating]


@app.get("/books/published/", status_code=status.HTTP_200_OK)
async def get_book_by_published_date(published_date: int = Query(gt=0, lt=2040)):
    return [book for book in BOOKS if book.published_data == published_date]


@app.post("/create_book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    find_book_id(new_book)
    BOOKS.append(new_book)

    return {"message": "Book created"}


def find_book_id(book: Book):
    
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    return book.id


@app.put("/books/update_book", status_code=status.HTTP_200_OK)
async def update_book(book: BookRequest):
    book_changed = False
    for index, b in enumerate(BOOKS):
        if b.id == book.id:
            BOOKS[index] = Book(**book.model_dump())
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail="Item not found!")

@app.delete("/books/delete_book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_deleted = False
    for index, b in enumerate(BOOKS):
        if b.id == book_id:
            del BOOKS[index]
            book_deleted = True
    if not book_deleted:
        raise HTTPException(status_code=404, detail="Item not found!")