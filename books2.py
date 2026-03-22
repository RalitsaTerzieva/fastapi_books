from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
import redis

app = FastAPI()
cache = redis.Redis(host='redis', port=6379)

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id: int, title: str, author: str, description: str, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(description="Id is not needed on create", default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=200)
    rating: int = Field(gt=0, lt=6)



BOOKS = [
    Book(1, "Clean Code", "Robert C. Martin", "A guide to writing clean and maintainable code.", 5),
    Book(2, "The Pragmatic Programmer", "Andrew Hunt", "Best practices and philosophy of software development.", 5),
    Book(3, "Design Patterns", "Erich Gamma", "Classic book about reusable software design patterns.", 5),
    Book(4, "Atomic Habits", "James Clear", "How small habits create big improvements in life.", 4),
    Book(5, "Deep Work", "Cal Newport", "Strategies for focused success in a distracted world.", 4),
    Book(6, "Python Crash Course", "Eric Matthes", "Beginner-friendly introduction to Python programming.", 4),
]

@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create_book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1

    return book.id