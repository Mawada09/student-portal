from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    name: str
    email: str
    course: str

class StudentUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    course: str | None = None

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    course: str

    class Config:
        from_attributes = True
