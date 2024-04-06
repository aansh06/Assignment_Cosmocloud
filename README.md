# Assignment_Cosmocloud  -Library Management System

## Description
This project is a Library Management System developed using FastAPI and MongoDB. It allows users to manage students' records, including creating, updating, deleting, and listing students.

## Features
- **Create Student**: Add a new student record to the database.
- **Update Student**: Modify existing student records with new information.
- **Delete Student**: Remove a student record from the database.
- **List Students**: Retrieve a list of students with optional filtering by country and age.

## Technologies Used
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **MongoDB**: A NoSQL database used to store student records.
- **Pydantic**: Data validation and settings management using Python type annotations.

## Getting Started
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Set up your MongoDB instance and configure the connection URI in `database/connection.py`.
4. Run the FastAPI application using `uvicorn main:app --reload`.

## Basic Routes
- **Create Student**: `POST /students`
  - Create a new student record.
- **Update Student**: `PATCH /students/{student_id}`
  - Update an existing student record with the specified ID.
- **Delete Student**: `DELETE /students/{student_id}`
  - Delete the student record with the specified ID.
- **List Students**: `GET /students`
  - Retrieve a list of students. Optional query parameters (`country`, `age`) can be used for filtering.
