# 1. How to Read a Python Error
How to Read a Python Error
```
1. File name
2. Line number
3. Error type
4. Error message
```
Example:
![[Pasted image 20260528155118.png]]

![[Pasted image 20260528155147.png]]
Correct Code:
```Python
marks = int(input("Enter marks: "))
total = marks + 10
print(total)
```
---
# 2. Top Python Errors You Must Know
![[Pasted image 20260528155358.png]]

----
# 3. Debug Your Student Marks Analyzer
### Bug1 : Syntax Error
![[Pasted image 20260528155623.png]]
Correct :
```Python
marks = 80

if marks >= 40:
    print("Pass")
```
---
### Bug2: Indentation Error
![[Pasted image 20260528155802.png]]
Correct :
```Python
marks = 80

if marks >= 40:
    print("Pass")
```
---
### Bug3 : Type Error
![[Pasted image 20260528155954.png]]
Correct :
```Python
marks = int(input("Enter marks: "))
bonus = 5
final_marks = marks + bonus
print(final_marks)
```
---
### Bug 4 : Value Error
![[Pasted image 20260528160138.png]]
Correct :
```Python
try:
    marks = int(input("Enter marks: "))
    print(marks)
except ValueError:
    print("Please enter numeric marks only.")
```
---
### Bug 5 : Index Error
![[Pasted image 20260528160449.png]]
Correct
```Python
students = []
if len(students) > 0:
    topper = students[0]
    print(topper)
else:
    print("No student data available.")
```
---
### Bug 6 : Key Error
![[Pasted image 20260528160632.png]]
Correct :
```Python
student = {
    "name": "Rahul",
    "marks": 85
}
if "grade" in student:
    print(student["grade"])
else:
    print("Grade not found.")
```
Better fix :
```Python
student = {
    "name": "Rahul",
    "marks": 85,
    "grade": "B"
}

print(student["grade"])
```
---
### Bug 7: Zero Divisor Error
![[Pasted image 20260528160857.png]]
Correct :
```Python
students = []
if len(students) > 0:
    average = 100 / len(students)
    print(average)
else:
    print("Cannot calculate average without students.")
```
---
# 5. Logging
Use logging when you want to track:
```
program started
data loaded
invalid input happened
model training started
model accuracy calculated
file saved
error happened
```
Example:
```Python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")

try:
    marks = int(input("Enter marks: "))
    logging.info("Marks entered successfully")
except ValueError:
    logging.error("Invalid marks entered")
    print("Please enter numeric marks only.")
```
This creates:
```
app.log
```
Example log:
```
2026-05-28 15:45:10 - INFO - Program started2026-05-28 15:45:16 - ERROR - Invalid marks entered
```
---
## 6. Mini Debugging Assessment
Fix this code yourself:
```Python
students = []
n = input("Enter number of students: ")
for i in range(n):
	name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    student = {        
	    "name": name        
	    "marks": marks
	    }    
	    students.append(student)average = sum(students)/len(students)
	    print("Average:", average)
```
Find at least **4 bugs**.
Hints:
```
Bug 1: n data type
Bug 2: dictionary comma
Bug 3: sum(students) is wrong
Bug 4: empty list risk
```
Correct version:
```Python
students = []
try:    
	n = int(input("Enter number of students: "))
    if n <= 0:
        print("Number of students must be greater than 0.")          exit()
    except ValueError:    
	    print("Please enter a valid number.")
	    exit()
	    
	for i in range(n):
	    name = input("Enter name: ")
	    while True:
	        try:
				marks = int(input("Enter marks: "))
				if marks < 0 or marks > 100:
					print("Marks must be between 0 and 100.")
				else:
					break
			except ValueError:
				print("Please enter numeric marks only.")
		student = {
			"name": name,
			"marks": marks
		}
		students.append(student)
		total = 0
		for student in students:
		    total += student["marks"]
		    average = total / len(students)
		    print("Average:", average)
```
---
# Senior Engineer Debugging Method
Use this every time:
```
1. Read the last line of error first.
2. Identify error type.
3. Go to the line number.
4. Check variable values.
5. Check data types.
6. Reproduce the bug with small input.
7. Fix minimum necessary code.
8. Run again.
9. Add prevention.
10. Document error in errors_and_fixes.md
```
---
