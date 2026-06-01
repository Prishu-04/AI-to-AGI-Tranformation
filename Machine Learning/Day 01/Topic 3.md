	# Loops + Functions Practice
By the end of this slot, you should be able to use:
```
for loop
while loop
range()
break
continue
functions
return
lists with loops
```

```
reading datasets
cleaning rows
calculating metrics
training models
checking predictions
debugging model outputs
```
---
### 1. For Loop
A `for` loop repeats code for a fixed number of times or over a sequence.
Example:
![[Pasted image 20260528115333.png|206]]
means:
```
Start from 1
Stop before 6
So output is 1 to 5
```
---
### Example: Print Table
![[Pasted image 20260528115511.png|395]]

---
### 2. Loop on List
A list stores multiple values.
![[Pasted image 20260528115640.png|276]]

---
##### Calculate Total Marks
![[Pasted image 20260528115732.png|271]]

---
##### Calculate Average
![[Pasted image 20260528115926.png|376]]

---
### 3. While Loop
A `while` loop repeats while a condition is true.
![[Pasted image 20260528121029.png|386]]

---
![[Pasted image 20260528121059.png]]

---
Example with validation:
![[Pasted image 20260528121220.png]]
Input : 
```
Enter marks between 0 and 100: 120
Invalid marks
Enter marks again: 90
```
---
# 4. Break and Continue
Python’s official tutorial says `break` exits the nearest enclosing loop, and `continue` skips the rest of the current loop iteration and moves to the next one.
### Break
![[Pasted image 20260528121355.png]]
Meaning:
```
When i becomes 6, loop stops.
```
---
### Continue
![[Pasted image 20260528121531.png]]
Meaning:
```
When i is 3, skip printing and continue next iteration.
```
---
# 5. Functions
A function is a reusable block of code.
Python functions are defined using the `def` keyword, followed by a function name and parameters.
Example:
![[Pasted image 20260528121749.png]]

---
### Function with Parameter
![[Pasted image 20260528121916.png]]

---
### Function with Return
![[Pasted image 20260528122048.png]]

---
### Practice
Input:
```
Enter number of subjects: 3
Enter marks: 90
Enter marks: 120
Invalid marks. Enter between 0 and 100.
Enter marks again: 85
Enter marks: 75
```
CODE:
```Python
def calculate_total(marks):
    total = 0

    for mark in marks:
        total += mark

    return total


def calculate_average(marks):
    total = calculate_total(marks)
    average = total / len(marks)
    return average


def find_highest(marks):
    highest = marks[0]

    for mark in marks:
        if mark > highest:
            highest = mark

    return highest


marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    mark = int(input("Enter marks: "))

    while mark < 0 or mark > 100:
        print("Invalid marks. Enter between 0 and 100.")
        mark = int(input("Enter marks again: "))

    marks.append(mark)

total = calculate_total(marks)
average = calculate_average(marks)
highest = find_highest(marks)

print("\n----- Marks Report -----")
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
```
Output:
![[Pasted image 20260528122316.png|258]]

---
# Debugging Lab
### Error 1: Infinite Loop
Wrong:
```Python
count = 1

while count <= 5:
    print(count)
```
Output:
```
count never increases, so loop never ends.
```
Correct:
```Python
count = 1

while count <= 5:
    print(count)
    count += 1
```
---
### Error 2: Function Called Before Definition
Wrong:
![[Pasted image 20260528122901.png]]
Correct:
```Python
def greet():
    print("Hello")

greet()
```
---
### Error 3: Missing return
Wrong:
![[Pasted image 20260528123147.png]]
Correct:
```Python
def add(a, b):
    result = a + b
    return result

answer = add(5, 3)
print(answer)
```
---
### Error 4: Empty List index
Wrong:
![[Pasted image 20260528123314.png]]
Correct:
```Python
marks = []

if len(marks) > 0:
    highest = marks[0]
    print(highest)
else:
    print("No marks available")
```
---
### Mini Assignment
##### Marks Utility program
Requirements:
```
1. Take n marks as input.
2. Validate every mark between 0 and 100.
3. Create functions:   
	- calculate_total()   
	- calculate_average()
	- find_highest()
	- find_lowest()
	- count_pass()
	- count_fail()
4. Print final report.
```
CODE:
```Python
def calculate_total(marks):
    total = 0
    for mark in marks:
        total += mark
    return total


def calculate_average(marks):
    return calculate_total(marks) / len(marks)


def find_highest(marks):
    highest = marks[0]
    for mark in marks:
        if mark > highest:
            highest = mark
    return highest


def find_lowest(marks):
    lowest = marks[0]
    for mark in marks:
        if mark < lowest:
            lowest = mark
    return lowest


def count_pass(marks):
    count = 0
    for mark in marks:
        if mark >= 40:
            count += 1
    return count


def count_fail(marks):
    count = 0
    for mark in marks:
        if mark < 40:
            count += 1
    return count


marks = []
n = int(input("Enter number of subjects: "))

for i in range(n):
    mark = int(input("Enter marks: "))

    while mark < 0 or mark > 100:
        print("Invalid marks.")
        mark = int(input("Enter marks again: "))

    marks.append(mark)

print("\n----- Final Report -----")
print("Marks:", marks)
print("Total:", calculate_total(marks))
print("Average:", calculate_average(marks))
print("Highest:", find_highest(marks))
print("Lowest:", find_lowest(marks))
print("Pass Count:", count_pass(marks))
print("Fail Count:", count_fail(marks))
```
Output:
![[Pasted image 20260528123802.png|343]]

---
# Interview Questions
Prepare these:
1. What is a loop?
2. Difference between `for` and `while` loop?
3. What is an infinite loop?
4. What does `break` do?
5. What does `continue` do?
6. What is a function?
7. What is the difference between `print()` and `return`?
8. Why do we use functions in AI/ML projects?