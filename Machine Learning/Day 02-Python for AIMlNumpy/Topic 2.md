# Functions, Loops, Conditions & List Comprehension
## 1. Conditions in Python
Conditions help your program make decisions.
![[Pasted image 20260529100933.png]]

---
## 2. AI/ML Use case of conditions
![[Pasted image 20260529101037.png]]

---
## 3. For Loops
A `for` loop is used when we want to repeat something over a sequence.
![[Pasted image 20260529101209.png]]

---
## 4. Using Loop to Calculate Average
![[Pasted image 20260529101306.png]]

---
## 5. While Loop
A `while` loop runs until a condition becomes false.
![[Pasted image 20260529101431.png]]

---
## 6. Functions
A function is a reusable block of code.
![[Pasted image 20260529101544.png]]

---
## 7. Function with Parameter
![[Pasted image 20260529101654.png]]

---
## 8. AI/ML Use Case of Function
In ML, functions are used for preprocessing, model evaluation, and prediction logic.
![[Pasted image 20260529101846.png]]

---
## 9. List Comprehension
List comprehension is a short way to create a list.
### Normal Method
![[Pasted image 20260529101957.png]]
### List Comprehension Method
![[Pasted image 20260529102052.png]]

---
## 10. List Comprehension with Condition
![[Pasted image 20260529102343.png]]

---
## 11. AI/ML Use Case of List Comprehension
Suppose we have raw data and want to normalize it.
![[Pasted image 20260529102450.png]]

---
## 12. Common Errors and Corrections
### Error 1: Indentation Error
![[Pasted image 20260529102640.png]]
Correct Code:
```Python
if True:
    print("Hello")
```
---
### Error 2: Function Called Before Defining
![[Pasted image 20260529102932.png]]
Correct Code:
```Python
def calculate_average(marks):
    return sum(marks) / len(marks)
result = calculate_average([10, 20, 30])
print(result)
```
---
### Error 3: Infinite While Loop
![[Pasted image 20260529103215.png]]

---
### Error 4: Division By Zero
![[Pasted image 20260529103426.png]]

---
## 13. Practice Tasks
### Task 1
Create a list of marks:
```
marks = [80, 45, 90, 32, 70]
```
Print whether each student has passed or failed.
Passing marks: `50`

---
### Task 2
Create a function:
```
calculate_average(marks)
```
It should return the average of marks.

---
### Task 3
Create a function:
```
check_grade(mark)
```
Rules:
```
90 and above = A
75 to 89 = B
50 to 74 = C
Below 50 = Fail
```
---
### Task 4
Use list comprehension to create a list of squared numbers from:
```
numbers = [1, 2, 3, 4, 5]
```
Expected output:
```
[1, 4, 9, 16, 25]
```
---
### Task 5
Use list comprehension to filter only passed marks from:
```
marks = [80, 45, 90, 32, 70]
```
Expected output:
```
[80, 90, 70]
```
---
## 14. Slot 2 Final Mini Code
```Python
marks = [80, 45, 90, 32, 70]

for mark in marks:
    if mark >= 50:
        print(mark, "Pass")
    else:
        print(mark, "Fail")


def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)


def check_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"


average = calculate_average(marks)

print("Average Marks:", average)

for mark in marks:
    grade = check_grade(mark)
    print("Mark:", mark, "Grade:", grade)


numbers = [1, 2, 3, 4, 5]

squares = [num * num for num in numbers]

print("Squares:", squares)


passed_marks = [mark for mark in marks if mark >= 50]

print("Passed Marks:", passed_marks)


accuracy = 0.87

def check_model_performance(accuracy):
    if accuracy >= 0.90:
        return "Excellent Model"
    elif accuracy >= 0.75:
        return "Good Model"
    else:
        return "Needs Improvement"


model_status = check_model_performance(accuracy)

print("Model Status:", model_status)
```
---
