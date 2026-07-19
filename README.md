# 🚀 Task Manager API

A powerful and secure Task Management REST API built with FastAPI that enables users to register, authenticate using JWT tokens, and efficiently manage their daily tasks.

This project demonstrates best practices for building scalable backend applications with FastAPI, including authentication, authorization, CRUD operations, pagination, filtering, and database management.

---

## ✨ Features

- Secure User Registration & Login.
- JWT Authentication & Authorization.
- Password Hashing using Passlib & Bcrypt.
- Complete CRUD Operations for Tasks.
- Task Search & Filtering.
- Pagination Support.
- SQLite Database Integration.
- Interactive Swagger Documentation.
- Protected Endpoints using FastAPI Dependencies.
- Clean and Organized Project Structure.

---

## 🛠 Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Passlib
- Bcrypt
- Pydantic
- Python-dotenv
- Uvicorn

---

## 🔐 Authentication

The API uses JWT (JSON Web Tokens) for secure authentication.

Users can:

- Register an account.
- Login securely.
- Receive an Access Token.
- Access protected endpoints using Bearer Authentication.

---

## 📌 API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and receive JWT Token |

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/tasks/` | Create a new task |
| GET | `/tasks/` | Get all tasks |
| GET | `/tasks/{id}` | Get task by ID |
| PUT | `/tasks/{id}` | Update task |
| DELETE | `/tasks/{id}` | Delete task |

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/TASK_MANAGER_API.git
```

Move to the project directory:

```bash
cd TASK_MANAGER_API
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
uvicorn app.main:app --reload
```

---

## 📖 API Documentation

After running the server, open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI provides complete interactive documentation for all endpoints.

---

## 📂 Project Structure

```text
TASK_MANAGER_API
│
├── app
│   ├── routers
│   │     ├── auth.py
│   │     └── tasks.py
│   │
│   ├── services
│   ├── database.py
│   ├── dependencies.py
│   ├── models.py
│   ├── schemas.py
│   ├── security.py
│   └── main.py
│
├── tests
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## 🎯 What I Learned

- Building REST APIs with FastAPI.
- JWT Authentication & Authorization.
- Database Design with SQLAlchemy.
- Dependency Injection in FastAPI.
- CRUD Operations.
- Pagination & Filtering.
- API Documentation using Swagger.
- Organizing scalable backend projects.

---

## 👨‍💻 Author

### Mohab

Backend Developer | Python & FastAPI Developer

> "Code. Learn. Build. Improve."
