# Python Advanced + OOP Basics
## 1. Why OOP matters in AI/ML
In Day 1, we wrote code like this:
```Python
student = {
    "name": "Rahul",
    "marks": 85,
    "attendance": 90,
    "study_hours": 5.5
}
```
his is okay for small programs.
But in real AI/ML projects, we need cleaner structure:
```
Student
DataProcessor
ModelTrainer
PredictionService
ReportGenerator
```
Each of these can become a **class**.
Think of OOP like this:
```
Class = Blueprint
Object = Real thing created from blueprint  
Attribute = Data inside object  
Method = Function inside object
```
---
## 2. Real World analogy
Imagine a **car blueprint**.
The blueprint says:
```
Car has:- brand- color- speedCar can:- start- stop- accelerate
```
In Python:
```
Class = Car blueprint
Object = One actual car
Attributes = brand, color, speedMethods = start(), stop(), accelerate()
```
Same for AI/ML:
```
Class = Student blueprint
Object = Rahul / Priya / Aman
Attributes = marks, attendance, study_hours
Methods = predict_performance(), is_valid()
```
---
## 3. Basic Class Syntax:
![[Pasted image 20260601143930.png]]

---
## 4. Constructor: `__init__()`
`__init__()` runs automatically when an object is created. It is used to initialize object data.
![[Pasted image 20260601144205.png]]

---
## 5. What is `self`?
`self` means thus current object.
Example:
```python
student1 = Student("Rahul", 85, 90, 5.5)
student2 = Student("Priya", 72, 80, 4)
```
For `student1`
```Python
self.name = "Rahul"
self.marks = 85
```
So `self` helps each object store its own separate data.

---
# 6. Add a Method
A method is a function inside a class.
![[Pasted image 20260601144533.png]]

---
## 7. Add Validation method;
![[Pasted image 20260601144741.png]]

---
## 8. Add prediction Method
![[Pasted image 20260601145017.png]]

---
## 9. Batch Processing
![[Pasted image 20260601145421.png]]

![[Pasted image 20260601145433.png]]

---
## 10. Function-Based vs OOP-based code
![[Pasted image 20260601145555.png]]

---
## 11. Common Errors and Correction
### 1. Error 1: Forgetting `self`
![[Pasted image 20260601150531.png]]
Correct ;
```Python
class Student:
    def show_result(self):
        print("Hello")
```
### 2. Error 2: Wrong attribute name
![[Pasted image 20260601150734.png]]
Correct:
```Python
class Student:
    def __init__(self, marks):
        self.marks = marks
    def show_marks(self):
        print(self.marks)
```
---
### Error 3: Creating object with missing argument
![[Pasted image 20260601150835.png]]
Correct:
```Python
student = Student("Rahul", 85, 90, 5.5)
```
---
### Error 4: Using class name instead of object
![[Pasted image 20260601150931.png]]
Correct:
```Python
student1 = Student("Rahul", 85, 90, 5.5)
student1.show_result()
```
---
## 12. Interview Questions;
- What is a class?
- What is an object?
- What is the difference between a function and a method?
- What is `self`?
- What is `__init__()`?
- Why do we use OOP in AI/ML projects?
- What is an attribute?
- What is an instance?
- What causes `AttributeError`?
- Why is OOP better than writing everything in one large script?
---
## 13. Assignment
Create a class named:
```
Employee
```
It should have:
```
name
salary
experience
department
```
Add methods:
```
is_valid()
get_level()
show_info()
```
Rules:
```
Invalid:salary < 0 or experience < 0
Senior:experience >= 5 and salary >= 70000
Mid-Level:experience >= 2 and salary >= 40000
Junior:otherwise
```
Expected output:
```
Amit => Senior
Riya => Mid-Level
Karan => Junior
Invalid Employee
```
----
![[Pasted image 20260601152511.png]]

----
