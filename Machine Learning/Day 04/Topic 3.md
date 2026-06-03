# Selecting Rows, Columns & Filtering Data
## 1. What is Selection in Pandas?
Selection means choosing specific data from a DataFrame.
You can select:
```
Single column
Multiple columns
Single row
Multiple rows
Specific cell
Rows based on condition
```
In AI/ML, we use selection to separate useful columns, remove unwanted columns, and create features and labels.

---
## 2. Dataset for This Slot
same file :
```
student_performance.csv
```
---
## 3. Read CSV file
![[Pasted image 20260601114831.png]]

---
## 4. Selecting one Row
![[Pasted image 20260601114859.png]]

---
## 5. Selecting Multiple Columns
![[Pasted image 20260601115011.png]]

---
## 6. Selecting Rows using `iloc`
`iloc` is used for index-based selection.
Index starts from `0`.
![[Pasted image 20260601115127.png]]
### Selecting Multiple Rows
![[Pasted image 20260601115233.png]]

---
## 7. Selecting Specific Row and Column using `iloc`
![[Pasted image 20260601115345.png]]
Meaning:
```
Row index 0
Column index 1
```
![[Pasted image 20260601115431.png]]

---
## 8. Selecting Rows using `loc`
`loc` is used for label-based selection.
![[Pasted image 20260601115530.png]]
### Selecting Specific Column with `loc`
![[Pasted image 20260601115620.png]]
### Selecting Multiple Columns with `loc`
![[Pasted image 20260601115757.png]]

----
## 9. Difference between `loc`  and `ìloc`
![[Pasted image 20260601115851.png]]
Example:
![[Pasted image 20260601115947.png]]
Uses row number and column number.
![[Pasted image 20260601120026.png]]
Uses row label and column name.

---
## 10. Filtering Data
Filtering means selecting rows based on conditions.
Example: students who scored more than 80 in Math.
![[Pasted image 20260601120324.png]]

---
## 11. Filter Students with Attendance Above 90
![[Pasted image 20260601120428.png]]

---
## 12. Filter Students with Study Hours More Than 4
![[Pasted image 20260601120813.png]]

---
## 13. Multiple COnditions
Use:
```
& for AND| for OR
```
Important: each condition must be inside brackets.

---
### AND Condition
Students with Math marks above 80 and Attendance above 90:
![[Pasted image 20260601120954.png]]

---
### OR Condition
Students with Math marks above 90 or Science marks above 90:
![[Pasted image 20260601121041.png]]

---
## 14. Creating Total and Average Columns
![[Pasted image 20260601121202.png]]

---
## 15. Filter Passed Students
Pass condition:
```
Average >= 50
```

```Python
passed_students = df[df["Average"] >= 50]
print(passed_students)
```
---
## 16. Filter Failed Students
```Python
failed_students = df[df["Average"] < 50]
print(failed_students)
```
---
## 17. Add Result Column
![[Pasted image 20260601121618.png]]

---
## 18. Add Grade Column
![[Pasted image 20260601121724.png]]

---
## 19. AI/ML Use Case: Separating Features and Target
In machine learning:
```
X = input/featuresy = output/target/label
```
Example:
![[Pasted image 20260601121850.png]]

---
## 20. Practice Tasks
## Task 1
Read:
```
student_performance.csv
```
Print the full dataset.

---
## Task 2
Select and print:
```
Name column
Math column
Name and Attendance columns
Name, Math, Science, English columns
```
---
## Task 3
Using `iloc`, print:
```
First row
First 3 rows
Value at row 2, column 1
Value at row 3, column 2
```
---
## Task 4
Using filtering, print:
```
Students with Math > 80
Students with Attendance > 90
Students with Study_Hours > 4
Students with Math > 80 and Attendance > 90
Students with Math > 90 or Science > 90
```
---
## Task 5
Create:
```
Total column
Average column
Result column
Grade column
```
Then separate:
```
X = Math, Science, English, Attendance, Study_Hoursy = Result
y= result
```
---
# 22. Slot 3 Final Code
Create this file:
```Python
import pandas as pd

df = pd.read_csv("student_performance.csv")

print("========== Full Dataset ==========")
print(df)

print("\n========== Selecting One Column ==========")
print(df["Name"])

print("\n========== Selecting Math Column ==========")
print(df["Math"])

print("\n========== Selecting Multiple Columns ==========")
print(df[["Name", "Attendance"]])

print("\n========== Selecting Subject Columns ==========")
print(df[["Name", "Math", "Science", "English"]])

print("\n========== First Row using iloc ==========")
print(df.iloc[0])

print("\n========== First 3 Rows using iloc ==========")
print(df.iloc[0:3])

print("\n========== Specific Values using iloc ==========")
print("Row 2, Column 1:", df.iloc[2, 1])
print("Row 3, Column 2:", df.iloc[3, 2])

print("\n========== Specific Value using loc ==========")
print("Name at index 0:", df.loc[0, "Name"])
print("Math at index 3:", df.loc[3, "Math"])

print("\n========== Students with Math > 80 ==========")
students_math_above_80 = df[df["Math"] > 80]
print(students_math_above_80)

print("\n========== Students with Attendance > 90 ==========")
students_attendance_above_90 = df[df["Attendance"] > 90]
print(students_attendance_above_90)

print("\n========== Students with Study Hours > 4 ==========")
students_study_more_than_4 = df[df["Study_Hours"] > 4]
print(students_study_more_than_4)

print("\n========== Math > 80 AND Attendance > 90 ==========")
math_attendance_filter = df[(df["Math"] > 80) & (df["Attendance"] > 90)]
print(math_attendance_filter)

print("\n========== Math > 90 OR Science > 90 ==========")
math_or_science_filter = df[(df["Math"] > 90) | (df["Science"] > 90)]
print(math_or_science_filter)

df["Total"] = df["Math"] + df["Science"] + df["English"]

df["Average"] = df["Total"] / 3
df["Average"] = df["Average"].round(2)

df["Result"] = ["Pass" if avg >= 50 else "Fail" for avg in df["Average"]]


def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


df["Grade"] = df["Average"].apply(assign_grade)

print("\n========== Updated Dataset ==========")
print(df)

print("\n========== Passed Students ==========")
passed_students = df[df["Result"] == "Pass"]
print(passed_students)

print("\n========== Failed Students ==========")
failed_students = df[df["Result"] == "Fail"]
print(failed_students)

X = df[["Math", "Science", "English", "Attendance", "Study_Hours"]]
y = df["Result"]

print("\n========== Features X ==========")
print(X)

print("\n========== Target y ==========")
print(y)
```
----
