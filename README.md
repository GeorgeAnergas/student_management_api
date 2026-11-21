## Student Management API
A REST API for managing student records, built with Python, FastAPI and PostgreSQL.
The API allows users to create, retrieve, update and delete student records.


## Technologies
- Python
- FastAPI
- PostgreSQL
- Psycopg
- Pydantic
- Uvicorn


## API ENDPOINTS
Method              Endpoints                       Description                    
GET                 /                               Welcome Message
POST                /students                       Create a new student
GET                 /students                       Get all students
GET                 /students/{student_id}          Get a student by ID
PUT                 /students/{student_id}          Update a student
DELETE              /students/{student_id}          Delete a student



## Installation and Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project folder:

   ```bash
   cd student_management_api
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment (Windows):

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

5. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```




## Database Configuration

1. Create a PostgreSQL database named `student_management`.

2. Create a `.env` file in the project root directory with the following settings:

   ```env
   DB_name=student_management
   DB_user=postgres
   DB_pass=your_password
   DB_host=localhost
   DB_port=5432
   ```

   Replace `your_password` with your PostgreSQL password.

3. Create the `students` table:

   ```sql
   CREATE TABLE students (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       age INTEGER NOT NULL,
       email VARCHAR(150) NOT NULL UNIQUE
   );
   ```




## Running the Application

Start the development server with:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

http://127.0.0.1:8000

You can access the interactive API documentation at:

http://127.0.0.1:8000/docs
