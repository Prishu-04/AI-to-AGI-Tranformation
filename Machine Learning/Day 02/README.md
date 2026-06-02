# Day 2 — Python Advanced + OOP Student Data Pipeline

## 🚀 Overview

This repository contains my **Day 2 AI/ML learning project**, focused on **Python Advanced Concepts and Object-Oriented Programming (OOP)**.

In this project, I converted a basic function-based student data processing script into a **reusable object-oriented Python pipeline**. The pipeline validates student records, removes invalid data, generates rule-based performance predictions, exports clean data into a CSV file, and creates a JSON summary report.

This project is part of my AI/ML roadmap where I am building strong foundations in Python, data processing, debugging, and production-style coding practices.

---

## 📌 Day 2 Learning Focus

### Topics Covered

- Python advanced programming
    
- Object-Oriented Programming basics
    
- Classes and objects
    
- Attributes and methods
    
- `self` and `__init__()`
    
- Instance-level data handling
    
- Separation of responsibility
    
- File handling using CSV and JSON
    
- Folder and path handling using `pathlib`
    
- Debugging OOP and file-related errors
    
- Git and GitHub commit workflow
    

---

## 🧠 Key Concepts Learned

### 1. Class

A class is a blueprint for creating objects.

```python
class StudentRecord:
    pass
```

In this project, `StudentRecord` acts as a blueprint for one student.

---

### 2. Object

An object is a real instance created from a class.

```python
student = StudentRecord("Rahul", 85, 90, 5.5)
```

Here, `student` is an object of the `StudentRecord` class.

---

### 3. Attributes

Attributes store data inside an object.

```python
self.name = name
self.marks = marks
self.attendance = attendance
self.study_hours = study_hours
```

---

### 4. Methods

Methods are functions inside a class.

```python
def is_valid(self):
    ...
```

Examples used in this project:

```python
student.is_valid()
student.predict_performance()
student.to_dictionary()
```

---

### 5. `self`

`self` represents the current object. It allows each object to store and access its own data.

---

### 6. `__init__()`

`__init__()` is a constructor method that runs automatically when an object is created.

```python
def __init__(self, name, marks, attendance, study_hours):
    self.name = name
    self.marks = marks
    self.attendance = attendance
    self.study_hours = study_hours
```

---

## 🏗️ Project Architecture

The project follows a simple but professional OOP structure.

```text
day2_student_pipeline/
│
├── main.py
├── data/
│   └── clean_students.csv
│
└── reports/
    └── summary_report.json
```

---

## 🧩 Classes Used

### 1. `StudentRecord`

The `StudentRecord` class represents a single student record.

#### Responsibilities

- Store student details
    
- Validate marks, attendance, and study hours
    
- Predict student performance
    
- Convert object data into dictionary format
    

#### Attributes

```python
name
marks
attendance
study_hours
```

#### Methods

```python
is_valid()
predict_performance()
to_dictionary()
```

---

### 2. `StudentPipeline`

The `StudentPipeline` class processes multiple student records.

#### Responsibilities

- Store raw student objects
    
- Separate valid and invalid students
    
- Count prediction categories
    
- Save clean data to CSV
    
- Save summary report to JSON
    
- Display summary in terminal
    

#### Attributes

```python
students
clean_students
invalid_students
```

#### Methods

```python
clean_data()
count_predictions()
save_clean_data()
save_report()
show_summary()
```

---

## ⚙️ Project Features

- Creates multiple student objects using OOP
    
- Validates each student record
    
- Removes invalid student data
    
- Predicts student performance using rule-based logic
    
- Saves clean student data into CSV format
    
- Saves summary report into JSON format
    
- Automatically creates `data/` and `reports/` folders
    
- Uses clean and reusable class-based structure
    
- Demonstrates debugging of OOP and file-handling errors
    

---

## 📊 Prediction Rules

The project predicts student performance using the following rules:

```text
Excellent:
marks >= 80 and attendance >= 85 and study_hours >= 5

Good:
marks >= 50 and attendance >= 75

Needs Improvement:
otherwise
```

---

## ❌ Invalid Data Rules

A student record is considered invalid if:

```text
marks < 0 or marks > 100
attendance < 0 or attendance > 100
study_hours < 0
```

Invalid records are not saved in the clean CSV file.

---

## 🧾 Complete Code

Create a file named:

```text
main.py
```

Paste the following code:

```python
import csv
import json
from pathlib import Path


class StudentRecord:
    def __init__(self, name, marks, attendance, study_hours):
        self.name = name
        self.marks = marks
        self.attendance = attendance
        self.study_hours = study_hours

    def is_valid(self):
        if self.marks < 0 or self.marks > 100:
            return False

        if self.attendance < 0 or self.attendance > 100:
            return False

        if self.study_hours < 0:
            return False

        return True

    def predict_performance(self):
        if self.marks >= 80 and self.attendance >= 85 and self.study_hours >= 5:
            return "Excellent"
        elif self.marks >= 50 and self.attendance >= 75:
            return "Good"
        else:
            return "Needs Improvement"

    def to_dictionary(self):
        return {
            "name": self.name,
            "marks": self.marks,
            "attendance": self.attendance,
            "study_hours": self.study_hours,
            "prediction": self.predict_performance()
        }


class StudentPipeline:
    def __init__(self, students):
        self.students = students
        self.clean_students = []
        self.invalid_students = []

    def clean_data(self):
        for student in self.students:
            if student.is_valid():
                self.clean_students.append(student)
            else:
                self.invalid_students.append(student)

    def count_predictions(self):
        counts = {
            "Excellent": 0,
            "Good": 0,
            "Needs Improvement": 0
        }

        for student in self.clean_students:
            prediction = student.predict_performance()
            counts[prediction] += 1

        return counts

    def save_clean_data(self, filename):
        fieldnames = ["name", "marks", "attendance", "study_hours", "prediction"]

        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for student in self.clean_students:
                writer.writerow(student.to_dictionary())

    def get_invalid_student_names(self):
        names = []

        for student in self.invalid_students:
            names.append(student.name)

        return names

    def save_report(self, filename):
        report = {
            "project_name": "Reusable OOP Student Pipeline",
            "total_students": len(self.students),
            "valid_students": len(self.clean_students),
            "invalid_students": len(self.invalid_students),
            "invalid_student_names": self.get_invalid_student_names(),
            "prediction_counts": self.count_predictions()
        }

        with open(filename, "w") as file:
            json.dump(report, file, indent=4)

    def show_summary(self):
        print("Student Pipeline Summary")
        print(f"Total students: {len(self.students)}")
        print(f"Valid students: {len(self.clean_students)}")
        print(f"Invalid students: {len(self.invalid_students)}")
        print(f"Invalid student names: {self.get_invalid_student_names()}")
        print(f"Prediction counts: {self.count_predictions()}")


def main():
    data_folder = Path("data")
    reports_folder = Path("reports")

    data_folder.mkdir(exist_ok=True)
    reports_folder.mkdir(exist_ok=True)

    students = [
        StudentRecord("Rahul", 85, 90, 5.5),
        StudentRecord("Aman", 45, 70, 3),
        StudentRecord("Priya", 72, 80, 4),
        StudentRecord("Sneha", 92, 95, 6),
        StudentRecord("Rohit", 120, 80, 4),
        StudentRecord("Neha", 66, -10, 3.5),
        StudentRecord("Karan", 58, 78, 2.5),
        StudentRecord("Anjali", 91, 89, 5.2)
    ]

    pipeline = StudentPipeline(students)

    pipeline.clean_data()
    pipeline.save_clean_data(data_folder / "clean_students.csv")
    pipeline.save_report(reports_folder / "summary_report.json")
    pipeline.show_summary()


if __name__ == "__main__":
    main()
```

---

## ▶️ How to Run

Open terminal inside the project folder and run:

```bash
python main.py
```

---

## ✅ Expected Terminal Output

```text
Student Pipeline Summary
Total students: 8
Valid students: 6
Invalid students: 2
Invalid student names: ['Rohit', 'Neha']
Prediction counts: {'Excellent': 3, 'Good': 2, 'Needs Improvement': 1}
```

---

## 📁 Output Files Generated

After running the program, two output files are generated.

### 1. Clean CSV File

Path:

```text
data/clean_students.csv
```

Expected content:

```csv
name,marks,attendance,study_hours,prediction
Rahul,85,90,5.5,Excellent
Aman,45,70,3,Needs Improvement
Priya,72,80,4,Good
Sneha,92,95,6,Excellent
Karan,58,78,2.5,Good
Anjali,91,89,5.2,Excellent
```

---

### 2. JSON Summary Report

Path:

```text
reports/summary_report.json
```

Expected content:

```json
{
    "project_name": "Reusable OOP Student Pipeline",
    "total_students": 8,
    "valid_students": 6,
    "invalid_students": 2,
    "invalid_student_names": [
        "Rohit",
        "Neha"
    ],
    "prediction_counts": {
        "Excellent": 3,
        "Good": 2,
        "Needs Improvement": 1
    }
}
```

---

## 🧪 Debugging Practice

During this project, I practiced debugging the following errors:

|Error|Cause|Fix|
|---|---|---|
|`AttributeError`|Wrong attribute spelling like `attendence` instead of `attendance`|Use consistent attribute names|
|`FileNotFoundError`|Saving files before creating folders|Use `Path("data").mkdir(exist_ok=True)`|
|`NameError`|Missing imports like `csv` or `json`|Add required imports at the top|
|`TypeError`|Comparing string values with integers|Convert values using `int()` or `float()`|
|Logical Bug|Forgetting to call `clean_data()` before saving|Call methods in correct order|
|JSON Error|Using `json.load()` while saving|Use `json.dump()` for saving|

---

## 🧠 AI/ML Connection

This project is a foundation for real AI/ML pipelines.

Current project:

```text
StudentRecord → StudentPipeline → Clean CSV → JSON Report
```

Future ML project:

```text
DatasetRecord → DataPreprocessor → Clean Dataset → Model Training → Evaluation Report
```

Future GenAI/RAG project:

```text
DocumentRecord → RAGPipeline → Chunks → Embeddings → Vector Database → Answer Generation
```

---

## 📚 Skills Practiced

- Python OOP
    
- Data validation
    
- Rule-based prediction
    
- CSV export
    
- JSON report generation
    
- Path handling using `pathlib`
    
- Debugging runtime and logical errors
    
- Clean project structuring
    
- GitHub-ready documentation
    

---

## 🧾 Git Commands Used

```bash
git status
git add main.py data/clean_students.csv reports/summary_report.json README.md
git commit -m "Add Day 2 OOP student data pipeline"
git push
```

---

## 🧑‍💻 Interview Questions

1. What is a class?
    
2. What is an object?
    
3. What is an attribute?
    
4. What is a method?
    
5. What is `self` in Python?
    
6. What is `__init__()`?
    
7. What is the difference between a function and a method?
    
8. Why did we create `StudentRecord` and `StudentPipeline` separately?
    
9. What is separation of responsibility?
    
10. What does `to_dictionary()` do?
    
11. Why do we save clean data as CSV?
    
12. Why do we save summary reports as JSON?
    
13. What is `csv.DictWriter`?
    
14. What is `json.dump()`?
    
15. What is `json.load()`?
    
16. What is `Path("data").mkdir(exist_ok=True)` used for?
    
17. What causes `AttributeError`?
    
18. What causes `FileNotFoundError`?
    
19. Why is forgetting `clean_data()` a logical bug?
    
20. How can this project become a real ML pipeline?
    

---

## 🏁 Day 2 Learning Outcome

By completing this project, I learned how to convert a simple Python script into a reusable object-oriented pipeline. I practiced creating classes, managing object data, validating records, generating predictions, exporting structured files, debugging common OOP errors, and documenting the project professionally for GitHub.

---

## 📌 Resume Bullet

Built a reusable object-oriented Python data pipeline using custom classes to validate student records, generate rule-based performance predictions, export clean CSV datasets, and create JSON summary reports.

---

## 🔗 LinkedIn Project Description

Completed Day 2 of my AI/ML learning journey by building a reusable OOP-based Student Data Processing Pipeline in Python.

This project uses custom classes to represent student records and process multiple records through validation, prediction, CSV export, and JSON report generation. It helped me strengthen my understanding of Python OOP, clean project structure, file handling, and debugging practices.

Key skills practiced:

- Python OOP
    
- Classes and objects
    
- CSV and JSON handling
    
- Data validation
    
- Rule-based prediction
    
- Debugging
    
- GitHub documentation