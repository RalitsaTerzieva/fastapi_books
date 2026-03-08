from fastapi import Body, FastAPI

BOOKS = [
    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "category": "Programming"
    },
    {
        "id": 2,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "category": "Software Engineering"
    },
    {
        "id": 3,
        "title": "Atomic Habits",
        "author": "James Clear",
        "category": "Self Development"
    },
    {
        "id": 4,
        "title": "Deep Work",
        "author": "Cal Newport",
        "category": "Productivity"
    },
    {
        "id": 5,
        "title": "Refactoring",
        "author": "Martin Fowler",
        "category": "Programming"
    },
    {
        "id": 6,
        "title": "Design Patterns",
        "author": "Erich Gamma",
        "category": "Software Engineering"
    },
    {
        "id": 7,
        "title": "The Lean Startup",
        "author": "Eric Ries",
        "category": "Business"
    },
    {
        "id": 8,
        "title": "Thinking, Fast and Slow",
        "author": "Daniel Kahneman",
        "category": "Psychology"
    }
]

app = FastAPI()

@app.get("/books")
async def first_api():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str): 
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        return {"message": "Book not found"}


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return



@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body() ):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('id') == updated_book.get('id'):
            BOOKS[i] = updated_book
            return {"message": "Book updated successfully!"}
        

@app.delete("/books/delete_book/{book_id}")
async def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('id') == book_id:
            BOOKS.pop(i)
            return {"message": "Book deleted successfully!"}

