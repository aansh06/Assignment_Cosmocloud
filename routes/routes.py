import bson
from fastapi import APIRouter, Path, HTTPException, status, Query
from models.models import StudentCreate, Address,StudentResponse
from database.connection import students_collection
from typing import Optional
from bson import ObjectId


router = APIRouter()

# Create student
@router.post("/students", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_student(student: StudentCreate):
    # Insert new student document into MongoDB
    result = students_collection.insert_one(student.dict())
    # Fetch the inserted student document ID
    print(type(result.inserted_id))
    print(result.inserted_id)
    inserted_id = str(result.inserted_id)
    # Return the ID of the newly created student
    return {"id": inserted_id}

# List students
@router.get("/students", response_model=dict)
async def list_students(
    country: Optional[str] = Query(None, description="Filter students by country"),
    age: Optional[int] = Query(None, description="Filter students by minimum age")
):
    query = {}
    # Apply country filter if provided
    if country:
        query["address.country"] = country
    # Apply age filter if provided
    if age is not None:
        query["age"] = {"$gte": age}

    # Fetch students matching the query from MongoDB
    students = list(students_collection.find(query))

    # Prepare response according to specification
    student_response_list = []
    for student in students:
        student_response_list.append({
            "name": student["name"],
            "age": student["age"]
        })

    return {"data": student_response_list}

# Get student by ID
@router.get("/students/{id}", response_model=StudentResponse)
async def get_student(student_id: str = Path(..., description="The ID of the student previously created.")):
    student_id_obj = ObjectId(student_id)
    student_data = students_collection.find_one({"_id": student_id_obj})
    if student_data is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # Create student object from fetched data
    student_responses = StudentResponse(
            id=str(student_data["_id"]),
            name=student_data["name"],
            age=student_data["age"],
            address=Address(**student_data["address"])  # Convert address dict to Address object
        )

    return student_responses


# Update student by ID

@router.patch("/students/{student_id}")
async def update_student(student_id: str = Path(..., description="The ID of the student to update"),
                         student_update: dict = {}):
    # Fetch student from the database
    student_id_obj = ObjectId(student_id)
    student = students_collection.find_one({"_id": student_id_obj})
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    # Update student fields based on provided data
    update_data = {key: value for key, value in student_update.items() if value is not None}
    if update_data:
        students_collection.update_one({"_id": student_id}, {"$set": update_data})

    # Return success response
    return {}



# Delete student by ID

@router.delete("/students/{student_id}")
async def delete_student(student_id: str = Path(..., description="The ID of the student to delete")):
    # Delete student by ID from MongoDB
    student_id_obj = ObjectId(student_id)

    result = students_collection.delete_one({"_id":student_id_obj})

    # If no student deleted, raise HTTPException with status code 404 (Not Found)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")

    # Return success response
    return {}