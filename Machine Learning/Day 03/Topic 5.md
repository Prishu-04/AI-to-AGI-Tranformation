# Mini Project + GitHub Push
## Mini Project: Student Marks Analyzer
# 1. Project Problem Statement
Create a Python program that analyzes student marks using NumPy.
The program should:
```
1. Store student marks in a NumPy array
2. Calculate total marks of each student
3. Calculate average marks of each student
4. Decide pass/fail status
5. Assign grade
6. Find class topper
7. Save final report into a text file
```
---
## 2. Dataset
We will use this dataset:
```Python
students = ["Pratyaksh", "Rahul", "Sneha", "Aman", "Priya"]
marks = [
	[85, 90, 78],
    [70, 88, 92],
    [35, 40, 45],
    [95, 92, 88],
    [60, 75, 80]
]
```
Meaning:
```
Column 1 = Math
Column 2 = Science
Column 3 = English
```
---
## 3. Required Output
Your program should print:
```
Student Name
Marks
Total Marks
Average Marks
Grade
Result
```
Also, it should be saved as report in:
```
student_marks_report.txt
```
----
## 4. Grading Scale
```
Average >= 90     Grade A+
Average >= 75     Grade A
Average >= 60     Grade B
Average >= 50     Grade C
Average < 50      Fail
```
Pass condition:
```
Average >= 50
```
---
## Complete Code.
### Import library
```Python
import numpy as np
```

### Calculation of grade
```Python
def calculate_grade(average):  
if average >= 90:  
return "A+"  
elif average >= 75:  
return "A"  
elif average >= 60:  
return "B"  
elif average >= 50:  
return "C"  
else:  
return "Fail"
```

### Decide of Pass and Fail
```Python
def check_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"
```

### Main program
#### Dataset
```python
students = ["Pratyaksh", "Rahul", "Sneha", "Aman", "Priya"]
marks = np.array([
     [85, 90, 78],
    [70, 88, 92],
    [35, 40, 45],
    [95, 92, 88],
    [60, 75, 80]])
```


```Python
try:
    totals = np.sum(marks, axis=1)
    averages = np.mean(marks, axis=1)
    topper_index = np.argmax(totals)
    topper_name = students[topper_index]
    topper_marks = totals[topper_index]
    print("========== Student Marks Analyzer ==========\n")
    report = "========== Student Marks Analyzer ==========\n\n"
    for i in range(len(students)):
        grade = calculate_grade(averages[i])
        result = check_result(averages[i])
        print("Student Name:", students[i])
        print("Marks:", marks[i])
        print("Total Marks:", totals[i])
        print("Average Marks:", round(averages[i], 2))
        print("Grade:", grade)
        print("Result:", result)
        print("----------------------------------")
        report += "Student Name: " + students[i] + "\n"
        report += "Marks: " + str(marks[i]) + "\n"
        report += "Total Marks: " + str(totals[i]) + "\n"
        report += "Average Marks: " + str(round(averages[i], 2)) + "\n"
        report += "Grade: " + grade + "\n"
        report += "Result: " + result + "\n"
        report += "----------------------------------\n"
    print("\nClass Topper:", topper_name)
    print("Topper Total Marks:", topper_marks)
    report += "\nClass Topper: " + topper_name + "\n"
    report += "Topper Total Marks: " + str(topper_marks) + "\n"
    ### creation of text file
    with open("student_marks_report.txt", "w") as file:
        file.write(report)
    print("\nReport saved successfully as student_marks_report.txt")
except Exception as e:
    print("An error occurred:", e)
```
---
## 6. Important NumPy Concepts Used
### `np.sum()`
Used to calculate total marks.
```Python
totals = np.sum(marks, axis=1)
```
Meaning:
```
axis=1 means row-wise calculation
```
So it calculates total marks for each student.

---
### `np.mean()`
Used to calculate average marks.
```Python
averages = np.mean(marks, axis=1)
```
Meaning:
```
It calculates average of each row.
```
---
### `np.argmax()`
Used to find the topper.
```
topper_index = np.argmax(totals)
```
Meaning:
```
It returns the index of the highest total marks.
```
---
