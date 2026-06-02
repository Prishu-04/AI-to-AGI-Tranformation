# Classes, Objects, and Methods Deeper
## 1. Instance Attribute
Instance attributes are values that belong to a specific object.
![[Pasted image 20260602091535.png]]

---
## 2. What `__init__()` Really does
`__init__()` is called automatically when you create an object.
Python internally does:
```
Create empty Student object
Call __init__()
Store name and marks inside object
Return the object
```
![[Pasted image 20260602091759.png]]

---
## 3. What does `self` really means
`self` means **the current object**.
![[Pasted image 20260602091930.png]]
So `self` receives `student1`.
That is why every normal method inside a class must have `self`.

---
## 4. Methods
A method is a function inside a class.
![[Pasted image 20260602092055.png]]

----
## 5. Method Types You Need Now
![[Pasted image 20260602092128.png]]
Example:
![[Pasted image 20260602092238.png]]
![[Pasted image 20260602092255.png]]

---
## 6. Class Variable vs Instance variable
Class variables are shared by all instances, while instance variables are generally unique to each instance.
### Instance variable
![[Pasted image 20260602092531.png]]
Each student has different name.

### Class Variable
![[Pasted image 20260602092706.png]]

---
## 7. AI/ML Example: Dataset Record Class
In AI/ML, every row of data can be treated like an object.
![[Screenshot 2026-06-02 092909.png]]
![[Pasted image 20260602092937.png]]

---
## 8. Why `to_dictionary()` is important
In real AI/ML projects, objects are useful for internal logic, but CSV,JSON, APIs and Pandas usually works with dictionary-like data.
So this:
```
<object name>.to_dictionary()
```
![[Pasted image 20260602093410.png]]
Flow :
```
OOP object → dictionary → CSV / JSON / Pandas DataFrame / API response
```
---
## 9. Batch processing with OOP
![[Pasted image 20260602093734.png]]

---
## 10. Common Errors
### Error 1: Missing `self`
Wrong:
```Python
class Student:
    def show_info():
        print("Hello")
```
Error:
```
TypeError: show_info() takes 0 positional arguments but 1 was given
```
Correct:
```Python
class Student:
    def show_info(self):
        print("Hello")
```
---
## Error 2: Attribute spelling mistake
Wrong:
```Python
class Student:
    def __init__(self, marks):
        self.marks = marks
    def show_marks(self):
        print(self.mark)
```
Error:
```
AttributeError: 'Student' object has no attribute 'mark'
```
Correct:
```Python
class Student:
    def __init__(self, marks):
        self.marks = marks
    def show_marks(self):
        print(self.marks)
```
---
### Error 3: Confusing class variable and instance variable
```Python
class Student:
    school_name = "ABC School"
    def __init__(self, name):
        self.name = name
```
Correct usage:
```Python
student =Student("Rahul")
print(student.name)
print(Student.school_name)
```
Avoid changing shared class variables accidentally unless you really mean it.

---
## Error 4: Calling method without brackets
Wrong:
```Python
student.show_info
```
This only refers to the method. It does not execute it.
Correct:
```Python
student.show_info()
```
---
## 11. Interview Questions
- What is the difference between class and object?
- What is an instance?
- What is an instance variable?
- What is a class variable?
- What is the role of `__init__()`?
- Why do methods need `self`?
- What is the difference between a function and a method?
- What does `to_dictionary()` do?
- Why is OOP useful in ML pipelines?
- What causes `AttributeError`?
---
## 12. Assignment
Create a class:
```
Product
```
Attributes:
```
name
price
rating
stock
```
Methods:
```
is_valid()
get_category()
to_dictionary()
show_info()
```
Rules:
```
Invalid:
price < 0 or rating < 0 or rating > 5 or stock < 0

Premium:
price >= 50000 and rating >= 4.5

Standard:
price >= 10000 and rating >= 3.5

Budget:
otherwise
```
Expected style:
```
Laptop => Premium
Phone => Standard
Keyboard => Budget
Fake Item => Invalid Product
```
---
