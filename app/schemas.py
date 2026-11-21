from pydantic import BaseModel, EmailStr, Field

class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(gt=0)
    email: EmailStr

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr