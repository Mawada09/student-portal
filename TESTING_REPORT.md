# Week 2 Testing Report - Student Portal API

**Student:** David Mawada (Mawada09)  
**Date:** June 11, 2026  
**Project:** Student Portal API  
**Repository:** https://github.com/Mawada09/student-portal

---

## 1. Unit Tests (PyTest)

### Tools Used
- PyTest 9.0.3
- HTTPX 0.28.1
- FastAPI TestClient

### Test Results
All 8 tests passed successfully.

```
========================= test session starts =========================
platform win32 -- Python 3.14.5, pytest-9.0.3
collected 8 items

test_main.py::test_root PASSED
test_main.py::test_create_student PASSED
test_main.py::test_create_duplicate_student PASSED
test_main.py::test_get_all_students PASSED
test_main.py::test_get_student_by_id PASSED
test_main.py::test_get_nonexistent_student PASSED
test_main.py::test_update_student PASSED
test_main.py::test_delete_student PASSED

================== 8 passed, 9 warnings in 1.07s ==================
```

### Tests Written

| Test | Description | Expected Result | Status |
|------|-------------|-----------------|--------|
| test_root | Root endpoint returns correct message | 200 OK | ✅ PASSED |
| test_create_student | Creates a new student record | 201 Created | ✅ PASSED |
| test_create_duplicate_student | Blocks duplicate email registration | 400 Bad Request | ✅ PASSED |
| test_get_all_students | Returns list of all students | 200 OK | ✅ PASSED |
| test_get_student_by_id | Returns a single student by ID | 200 OK | ✅ PASSED |
| test_get_nonexistent_student | Returns 404 for missing student | 404 Not Found | ✅ PASSED |
| test_update_student | Updates student name and course | 200 OK | ✅ PASSED |
| test_delete_student | Deletes student and confirms removal | 200 OK | ✅ PASSED |

---

## 2. API Testing (Postman)

### Collection: Student Records API

| Request | Method | URL | Response Code | Status |
|---------|--------|-----|---------------|--------|
| Create Student | POST | /students | 201 Created | ✅ PASSED |
| Get All Students | GET | /students | 200 OK | ✅ PASSED |
| Update Student | PUT | /students/1 | 200 OK | ✅ PASSED |
| Delete Student | DELETE | /students/2 | 200 OK | ✅ PASSED |

### Sample Responses
- **POST /students:** Created Alice Wanjiru with id:8, name, email, course returned
- **GET /students:** Returned full list of 7 students from database
- **PUT /students/1:** Updated name to "David Mawada Updated", course to "Software Engineering"
- **DELETE /students/2:** Response: "Student 2 deleted successfully"

---

## 3. GitHub Actions (CI/CD)

### Workflow File
`.github/workflows/tests.yml`

### Configuration
- Trigger: On every push and pull request to main branch
- Runner: ubuntu-latest
- Database: PostgreSQL 17 (service container)
- Python: 3.13

### Result
✅ Workflow run #2 passed successfully  
All 8 tests passed automatically in the cloud on every push.

---

## 4. Code Quality (Flake8)

### Tool Used
Flake8 7.3.0

### Command
```
python -m flake8 . --max-line-length=100 --exclude=__pycache__,.pytest_cache
```

### Findings

| Code | Type | Description | File |
|------|------|-------------|------|
| W293 | Warning | Blank line contains whitespace | test_main.py |
| E302 | Warning | Expected 2 blank lines between functions | database.py, models.py, schemas.py |
| E501 | Warning | Line too long (104 > 100 characters) | database.py |
| F401 | Warning | Unused import (EmailStr) | schemas.py |

### Summary
No critical errors found. All issues are minor style warnings that do not affect functionality. These will be addressed in future refactoring.

---

## 5. Summary

| Activity | Result |
|----------|--------|
| Unit tests written | 8 tests |
| Unit tests passed | 8/8 (100%) |
| API endpoints tested in Postman | 4/4 |
| GitHub Actions workflow | ✅ Passing |
| Code quality check | ✅ Complete (minor warnings only) |

**Week 2 Deliverable Status: COMPLETE ✅**
