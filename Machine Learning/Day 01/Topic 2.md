# Python Basics — Variables, Data Types, Input/Output, Conditions
# 1. Variables
A *variable* is a name used to store data.
Example:
```Python
name = "Pratyaksh"
age =20
marks =85.5
print(name)
print(age)
print(marks)
```
Output:
![[Pasted image 20260528104236.png]]

---
### Rules of Variable
Correct:
```Python
student_name = "Rahul"
marks1 = 90
_total = 100
```
Wrong:
```Python
student name = "Rahul"
1marks = 90
total-marks = 100
```
WHy wrong:
Variable names cannot contain spaces.
Variable names cannot start with a number.
Hyphen is treated like minus operator.

---
# 2. Data types
A **data type** tells Python what kind of value is stored.
![[Pasted image 20260528104541.png]]
Python’s built-in function `bool()` returns either `True` or `False`, and Python’s built-in type system includes numeric, sequence, mapping, and exception types.

Example:
```Python
name = "Pratyaksh"
age = 20
cgpa = 8.5
is_learning = True

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_learning))
```
Output:
![[Pasted image 20260528104643.png|143]]

---
# 3. Input and Output

`print()` is used to show output.
![[Pasted image 20260528104903.png|318]]

`input()` is used to take user input
![[Pasted image 20260528105130.png|316]]

Python’s official input/output tutorial explains that programs can present output in human-readable form or write it to files for later use.

### Important Rule
`input()` gives data as string.
Wrong:
![[Pasted image 20260528105441.png|319]]
Correct:
![[Pasted image 20260528105555.png|319]]
Input : Enter your age: 45

---
# 4. Type Conversion
*Type conversion* means changing one data type into another.
![[Pasted image 20260528105726.png|318]]
Example:
![[Pasted image 20260528105843.png|431]]
### Common Mistake:
Wrong:
![[Pasted image 20260528105950.png]]
Correct:
![[Pasted image 20260528110024.png]]

---
# 5. If-Else Conditions
Conditions help your program make decisions
Example:
![[Pasted image 20260528110318.png]]
Input: `Enter your marks: 56`

---
### If-Elif-Else Grade System
![[Pasted image 20260528110458.png]]
Input : `Enter marks : 78`

##### Login FLow
```
marks = 82

Is marks >= 90? No
Is marks >= 75? Yes
Print Grade B
Stop checking further
```
---
# 6. Practice
### Ques 1 Problem Solve
Sample input:
```
Enter student name: Pratyaksh
Enter age: 20
Enter marks: 88
```
![[Pasted image 20260528110913.png]]

---
### Ques2 Debugging Lab
##### Error 1: Missing quote
Wrong:
![[Pasted image 20260528111152.png]]
Correct:
```Python
name = "Pratyaksh"
```
---
##### Error 2: Wrong Indentation
Wrong:
![[Pasted image 20260528111335.png]]
Correct:
```Python
marks = 80

if marks >= 40:
    print("Pass")
```
---
##### Error 3: Comparing string with integer
Wrong:
![[Pasted image 20260528111526.png]]
Correct:
```Python
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
```
---
##### Error 4: Single `=` in Condition
Wrong:
![[Pasted image 20260528111718.png]]
Correct:
```Python
marks = 80

if marks == 80:
    print("Good")
```
Remember:
```
=  means assignment
== means comparison
```
---
# Mini Assignment
### Student Grade Checker
Requirements:
```
1. Take student name.
2. Take roll number.
3. Take marks in 3 subjects.
4. Calculate total.
5. Calculate percentage.
6. Print grade.
7. If any subject mark is below 40, print "Fail".
```

![[Pasted image 20260528113007.png]]
Output:
![[Pasted image 20260528114023.png|311]]

---
