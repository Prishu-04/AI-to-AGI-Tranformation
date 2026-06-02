# Debugging OOP and File Errors
## 1. Debugging mindset
When your code fails, do not panic. Follow this flow:
```
Read error → Find line number → Check variable → Check type → Check path/key/attribute → Fix root cause → Run again
```
In AI/ML, this habit saves hours because later your errors will come from:
```
CSV columns
Pandas DataFrames
model inputs
API requests
file paths
JSON configs
Docker folders
```
---
## 2. Most common errors in our OOP pipeline
![[Pasted image 20260602111954.png]]

---
### 3. Error 1 — `AttributeError`
#### Broken code
```Python
class StudentRecord:
    def __init__(self, name, marks, attendance,study_hours):
	    self.name = name
        self.marks = marks
        self.attendence = attendance
        self.study_hours = study_hours
    def is_valid(self):    
	    if self.attendance < 0 or self.attendance >100:
		    return False
        return True
```
#### Error
```
AttributeError: 'StudentRecord' object has no attribute 'attendance'
```
#### Root cause
Inside `__init__()` you created:
```
self.attendence
```
But inside `is_valid()` you used:
```
self.attendance
```
Python sees them as two different names.
#### Correct code
```Python
class StudentRecord:
	def __init__(self, name, marks, attendance,study_hours):
		self.name = name
        self.marks = marks
        self.attendance = attendance
        self.study_hours = study_hours
```
#### Debugging trick
Before the failing line, print:
```
print(student.__dict__)
```
This shows all attributes inside the object.

---
### 4. Error 2 — `FileNotFoundError`
#### Broken code
```Python
pipeline.save_clean_data("data/clean_students.csv")
```
But you forgot:
```Python
Path("data").mkdir(exist_ok=True)
```
#### Possible error
```
FileNotFoundError: [Errno 2] No such file or directory: 'data/clean_students.csv'
```
#### Root cause
You are trying to save a file inside a folder that does not exist.
#### Correct code
```Python
from pathlib import Path
data_folder =Path("data")
data_folder.mkdir(exist_ok=True)
pipeline.save_clean_data(data_folder / "clean_students.csv")
```
`pathlib` provides object-oriented filesystem paths, and `Path.mkdir()` is the clean way to create directories before saving files.

---
### 5. Error 3 — `NameError`
#### Broken code
```Python
def save_clean_data(self, filename):
    writer = csv.DictWriter(file, fieldnames=fieldnames)
```
#### Error
```
NameError: name 'csv' is not defined
```
#### Root cause
You forgot to import the `csv` module.
#### Correct code
```Python
import csv
```
Place it at the top of your file.
Same for JSON:
```Python
import json
```
The `csv` module is Python’s standard tool for reading and writing tabular CSV data, while `json` is used for encoding and decoding JSON data.

---
### 6. Error 4 — Wrong method call order
#### Broken code
```Python
pipeline = StudentPipeline(students)
pipeline.save_clean_data(data_folder / "clean_students.csv")
pipeline.save_report(reports_folder / "summary_report.json")
pipeline.show_summary()
```
#### Output problem
```
Student Pipeline Summary
Total students: 8
Valid students: 0
Invalid students: 0
Prediction counts: {'Excellent': 0, 'Good': 0, 'Needs Improvement': 0}
```
#### Root cause
You never called:
```Python
pipeline.clean_data()
```
So `clean_students` and `invalid_students` stayed empty.
#### Correct order
```Python
pipeline = StudentPipeline(students)
pipeline.clean_data()
pipeline.save_clean_data(data_folder / "clean_students.csv")
pipeline.save_report(reports_folder / "summary_report.json")
pipeline.show_summary()
```
This is a **logical bug**. The code runs, but the output is wrong.

---
### 7. Error 5 — `TypeError` from wrong data type
#### Broken code
```
student = StudentRecord("Rahul", "85", 90, 5.5)if student.marks >= 80:    print("Excellent")
```
#### Error
```
TypeError: '>=' not supported between instances of 'str' and 'int'
```
#### Root cause
`"85"` is a string, not an integer.
#### Correct code
```
student = StudentRecord("Rahul", int("85"), 90, 5.5)
```
Or better: convert while reading input/CSV.
```
marks = int(row["marks"])attendance = int(row["attendance"])study_hours = float(row["study_hours"])
```
This is very common because CSV values are usually read as strings.

---
### 8. Error 6 — Writing object directly into CSV
#### Broken code
```
writer.writerow(student)
```
#### Problem
`student` is an object. `csv.DictWriter` expects a dictionary with keys matching your column names.
#### Correct code
```
writer.writerow(student.to_dictionary())
```
The reason we created `to_dictionary()` is exactly this:
```
StudentRecord object → dictionary row → CSV file
```
---
### 9. Error 7 — Wrong JSON function
#### Broken code
```
with open(filename, "w") as file:    json.load(file)
```
#### Error / problem
You are opening the file for writing but trying to read JSON from it.
#### Correct code for saving
```
with open(filename, "w") as file:    json.dump(report, file, indent=4)
```
#### Correct code for reading
```
with open(filename, "r") as file:    data = json.load(file)
```
Remember:

| Function      | Use                                   |
| ------------- | ------------------------------------- |
| `json.dump()` | Save Python dictionary into JSON file |
| `json.load()` | Read JSON file into Python dictionary |

---
# 10. Debugging with `breakpoint()`
Add `breakpoint()` inside `clean_data()`:
```Python
def clean_data(self):
    for student in self.students:  
          breakpoint()  
	    if student.is_valid():
	          self.clean_students.append(student)
	    else: 
		    self.invalid_students.append(student)
```
When debugger opens, try:
```
student.name
student.marks
student.attendance
student.study_hours
student.is_valid()
n
c
q
```
Meaning:

|Command|Meaning|
|---|---|
|`n`|Go to next line|
|`c`|Continue program|
|`q`|Quit debugger|
|variable name|Inspect value|
Python’s `pdb` debugger supports breakpoints, stepping, stack inspection, and evaluating Python code in the current stack frame.

---
# 11. Debugging version of your pipeline
Use this version to inspect what is happening:
```Python
def clean_data(self):
    for student in self.students:
        print("Checking:", student.name)
        print("Marks:", student.marks)
        print("Attendance:", student.attendance)
        print("Study Hours:", student.study_hours)
        print("Is Valid:", student.is_valid())
        if student.is_valid():
	        self.clean_students.append(student)
	        print("Added to clean students")
        else:
            self.invalid_students.append(student)
            print("Added to invalid students")
            print("-" * 30)
```
This is called **print debugging**. It is simple, but very useful for beginners.

---
## 12. Interview questions
1. What is `AttributeError`?
2. What is `FileNotFoundError`?
3. What is `NameError`?
4. What is the difference between runtime error and logical bug?
5. Why is forgetting `clean_data()` a logical bug?
6. Why does CSV data often need type conversion?
7. Why do we use `student.to_dictionary()` before writing CSV?
8. What is the difference between `json.dump()` and `json.load()`?
9. Why do we create folders before saving files?
10. How does `breakpoint()` help during debugging?
---

