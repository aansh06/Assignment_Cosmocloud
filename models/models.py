from pydantic import BaseModel

class Address(BaseModel):
    city: str
    country: str

class StudentCreate(BaseModel):
    name: str
    age: int
    address: Address

class StudentResponse(BaseModel):
    id: str
    name: str
    age: int
    address: Address

    class Config:
        arbitrary_types_allowed = True
