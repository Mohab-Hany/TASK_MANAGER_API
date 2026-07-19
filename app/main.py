from fastapi import FastAPI

from .database import Base
from .database import engine

from .routers import auth
from .routers import tasks


#===================
# CREATE TABLES
#===================

Base.metadata.create_all(
    bind=engine
)


#===================
# FASTAPI
#===================

app = FastAPI(

    title="Task Manager API",

    description="""
    Task Manager API Project

    Features:

    - Authentication
    - JWT Token
    - CRUD Operations
    - Search
    - Filter
    - Pagination
    - SQLite Database
    """,

    version="1.0.0"
)


#===================
# ROUTERS
#===================

app.include_router(
    auth.router
)

app.include_router(
    tasks.router
)


#===================
# HOME PAGE
#===================

@app.get("/")
def home():

    return {

        "message":
        "Welcome To Task Manager API"

    }