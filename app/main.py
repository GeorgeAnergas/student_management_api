from fastapi import FastAPI, HTTPException
from .schemas import StudentCreate, StudentResponse
from .database import get_connection
from psycopg.rows import dict_row

app = FastAPI(
    title="Student Management API", 
    description="An API for managing students",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}


@app.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate):
    conn = get_connection()
    cursor = conn.cursor(row_factory=dict_row)
    try:
        cursor.execute("SELECT * FROM students WHERE email = %s", (student.email,))
        existing_student = cursor.fetchone()
        if existing_student is not None:
            raise HTTPException(status_code=409, detail="A student with this email already exists")
        cursor.execute(
            "INSERT INTO students (name, age, email) VALUES (%s, %s, %s) RETURNING *",
            (student.name, student.age, student.email)
        )
        new_student = cursor.fetchone()
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()

    return new_student

@app.get("/students", response_model=list[StudentResponse])
def get_students():
    conn = get_connection()
    cursor = conn.cursor(row_factory=dict_row)
    try:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return students

@app.get("/students/{student_id}", response_model=StudentResponse)
def find_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor(row_factory=dict_row)
    try:
        cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        student = cursor.fetchone()
    finally:
        cursor.close()
        conn.close()
    if student is None:
        raise HTTPException(status_code=404, detail="Student Not Found")
    return student


@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentCreate):
    conn = get_connection()
    cursor = conn.cursor(row_factory=dict_row)
    try:
        cursor.execute("UPDATE students SET name = %s, age = %s, email = %s "
        "WHERE id = %s RETURNING *",
        (student.name, student.age, student.email, student_id))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Student Not Found")
        updated_student = cursor.fetchone()
        conn.commit()
    except HTTPException:
        raise
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()

    return updated_student

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Student Not Found")
        conn.commit()
    except HTTPException:
        raise
    except Exception:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()
    return {"message": "Student deleted successfully"}


