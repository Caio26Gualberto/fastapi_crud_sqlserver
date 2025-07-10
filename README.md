# FastAPI SQLAlchemy Mini CRUD - Person

This is a simple CRUD (Create, Read, Update, Delete) example built with **FastAPI** and **SQLAlchemy** using a Microsoft SQL Server database.  
The goal is to demonstrate basic API endpoints for managing `Person` records.

---

## Features

- Create a person
- Read person details
- Update person data
- Delete a person
- Integration with SQL Server using SQLAlchemy ORM

---

## Requirements

- Python 3.10+
- FastAPI
- SQLAlchemy
- pyodbc (for SQL Server driver)
- Microsoft ODBC Driver 17 for SQL Server installed on your system
- A running SQL Server instance accessible to your app

---

## Setup Instructions

1. Clone the repo or copy the code files to your local machine.

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your database connection string in database.py
```python
SQLALCHEMY_DATABASE_URL = (
    "mssql+pyodbc://<server_name>/<database_name>?driver=ODBC+Driver+17+for+SQL+Server"
)
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

OBS: http://127.0.0.1:8000/docs for Swagger
