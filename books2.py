from fastapi import FastAPI

app = FastAPI()

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
