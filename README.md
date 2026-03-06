# FastAPI Mini Resume Management API

## Overview

This project is a RESTful API built using **FastAPI** to manage candidate resumes and related information.
The API allows uploading candidate resumes, storing candidate metadata, filtering candidates based on skills and experience, and performing CRUD operations.

This project demonstrates backend API development using **FastAPI, SQLAlchemy, and SQLite**.

---

## Features

* Upload candidate resume (PDF / DOC / DOCX)
* Store candidate metadata in database
* List all candidates
* Filter candidates by:

  * Skill
  * Minimum experience
  * Graduation year
* Retrieve candidate by ID
* Delete candidate
* Health check endpoint

---

## Tech Stack

* Python 3.13
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

---

## Project Structure

```
project/
│
├── main.py
├── database.py
├── models.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <repository-folder>
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the FastAPI server

```bash
uvicorn main:app --reload
```

---

## API Documentation

Once the server is running, interactive API documentation is available at:

Swagger UI
http://127.0.0.1:8000/docs

ReDoc
http://127.0.0.1:8000/redoc

These interfaces allow you to explore and test the API endpoints directly from your browser.

---

## Database

The application uses **SQLite** as the database and **SQLAlchemy ORM** for database interactions.

Candidate information and resume metadata are stored persistently in the database.

---

## Example Endpoints

| Method | Endpoint                   | Description      |
| ------ | -------------------------- | ---------------- |
| GET    | /health                    | Health check     |
| POST   | /candidates                | Create candidate |
| GET    | /candidates                | List candidates  |
| GET    | /candidates/{candidate_id} | Get candidate    |
| DELETE | /candidates/{candidate_id} | Delete candidate |

---

## Author

Jephy Joseph
B.Tech Computer Science
