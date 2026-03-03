from fastapi import FastAPI

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
    }
]

app = FastAPI()

@app.get("/books")
async def first_api():
    return BOOKS