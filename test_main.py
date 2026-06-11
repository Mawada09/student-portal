from fastapi.testclient import TestClient
from main import app
 
client = TestClient(app)
 
 
# Test 1: Root endpoint
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Student Portal API is running!"}
 
 
# Test 2: Create a new student
def test_create_student():
    response = client.post("/students", json={
        "name": "Test Student",
        "email": "teststudent@test.com",
        "course": "Computer Science"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Student"
    assert data["email"] == "teststudent@test.com"
    assert data["course"] == "Computer Science"
    assert "id" in data
 
 
# Test 3: Cannot create student with duplicate email
def test_create_duplicate_student():
    # First creation
    client.post("/students", json={
        "name": "Duplicate Student",
        "email": "duplicate@test.com",
        "course": "Engineering"
    })
    # Second creation with same email
    response = client.post("/students", json={
        "name": "Duplicate Student",
        "email": "duplicate@test.com",
        "course": "Engineering"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"
 
 
# Test 4: Get all students
def test_get_all_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
 
 
# Test 5: Get a single student by ID
def test_get_student_by_id():
    # Create a student first
    create_response = client.post("/students", json={
        "name": "Single Student",
        "email": "single@test.com",
        "course": "Mathematics"
    })
    student_id = create_response.json()["id"]
 
    # Now get that student
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["id"] == student_id
 
 
# Test 6: Get a student that does not exist
def test_get_nonexistent_student():
    response = client.get("/students/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"
 
 
# Test 7: Update a student
def test_update_student():
    # Create a student first
    create_response = client.post("/students", json={
        "name": "Old Name",
        "email": "update@test.com",
        "course": "Physics"
    })
    student_id = create_response.json()["id"]
 
    # Update the student
    response = client.put(f"/students/{student_id}", json={
        "name": "New Name"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "New Name"
 
 
# Test 8: Delete a student
def test_delete_student():
    # Create a student first
    create_response = client.post("/students", json={
        "name": "To Be Deleted",
        "email": "delete@test.com",
        "course": "Chemistry"
    })
    student_id = create_response.json()["id"]
 
    # Delete the student
    response = client.delete(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["message"] == f"Student {student_id} deleted successfully"
 
    # Confirm student is gone
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 404