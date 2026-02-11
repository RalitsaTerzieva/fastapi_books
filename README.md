# 📚 FastAPI Learning Project

This is a simple FastAPI project created for learning purposes.  
It includes basic API routes and demonstrates how to build and run a FastAPI application.

---

## 🚀 Features

- FastAPI setup
- 3 basic API routes
- Simple in-memory data (BOOKS list)
- Automatic Swagger documentation

---

## 📦 Requirements

- Python 3.9+
- pip

---

## 🔧 Installation

1. Clone the repository:

```bash
git https://github.com/RalitsaTerzieva/fastapi_books
cd fastapi_books
```

2. Create virtual environment:

```
python -m venv venv
```

3. Activate virtual environment:

```
source venv/bin/activate
```

4. Install dependencies:

```
pip install "fastapi[standard]"
```

▶️ Run the Application

```
fastapi dev main.py
```

Or using uvicorn:

```
uvicorn main:app --reload
```