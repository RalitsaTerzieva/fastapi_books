# 📚 FastAPI Learning Project

This is a simple FastAPI project created for learning purposes.  
It includes basic API routes and demonstrates how to build and run a FastAPI application.

---

## 🚀 Features

- FastAPI setup
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

---

## 🐳 Running the Project with Docker

This project can also be run using **Docker**, which allows the application to run inside a containerized environment.  
Containerization ensures that the application runs consistently across different machines without dependency or Python version conflicts.

Docker builds an **image** from a `Dockerfile`, and that image is used to start a **container** that runs the application.

---

### 📄 Step 1: Create a Dockerfile

Create a file named:

```
Dockerfile
```

Add the following content:

```dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Explanation of the Dockerfile steps:

| Instruction | Description |
|-------------|-------------|
| `FROM python:3.11` | Uses an official Python base image |
| `WORKDIR /app` | Sets the working directory inside the container |
| `COPY requirements.txt .` | Copies dependency file into the container |
| `RUN pip install --no-cache-dir -r requirements.txt` | Installs project dependencies without caching to reduce image size |
| `COPY . .` | Copies the project source code |
| `CMD` | Starts the FastAPI application using Uvicorn |


### 🔨 Step 2: Build the Docker Image

Run the following command in the project root directory:

```bash
docker build -t fastapi-books .
```

This command creates a Docker image named:

```
fastapi-books
```

---

### ▶️ Step 3: Run the Docker Container

Start the application inside a Docker container:

```bash
docker run -p 8000:8000 fastapi-books
```

Explanation of the port mapping:

```
-p 8000:8000
```

- The first `8000` is the port on your local machine.
- The second `8000` is the port inside the container where the application is running.

---

### 🌐 Step 4: Access the API

Open your browser and go to:

```
http://localhost:8000/docs
```

This will display the automatically generated interactive API documentation from FastAPI.

---

### 💡 Why Use Docker?

Using Docker provides several advantages:

- Consistent development environment
- No dependency conflicts
- Easy deployment to cloud environments
- Simplified application distribution
- Faster onboarding for new developers

---