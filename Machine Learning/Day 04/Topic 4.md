# Build Pandas Student Data Analysis Project
## 1. Project goal
Create this file:
```
day4_pandas_student_analysis.py
```
Your project will:
```
1. Create a student DataFrame
2. Inspect the dataset
3. Add a result column
4. Filter Excellent, Good, and Needs Improvement students
5. Sort students by marks
6. Calculate basic analytics
7. Save final report as CSV
```
---
## 2. Dataset
```Python
import pandas as pd
data = {    
	"name": ["Rahul", "Aman", "Priya", "Sneha", "Karan", "Anjali", "Rohit"],    
	"marks": [85, 72, 45, 91, 60, 88, 35],
    "attendance": [90, 80, 70, 95, 78, 92, 60],
    "study_hours": [5, 4, 3, 6, 2, 5, 1],
   "department": ["AI", "Data", "Web", "AI", "Data", "AI", "Web"]
}
df = pd.DataFrame(data)
```
---
## 3. Add result Column
```Python
def get_result(row):
    if row["marks"] >= 80 and row["attendance"] >= 85 and row["study_hours"] >= 5:
        return "Excellent"
    elif row["marks"] >= 50 and row["attendance"] >= 75:
        return "Good"
    else:
        return "Needs Improvement"


df["result"] = df.apply(get_result, axis=1)
```
`DataFrame.apply()` applies a function along an axis of the DataFrame. Here, `axis=1` means the function is applied row by row.

---
## 4. Filter categories
```Python
excellent_students = df[df["result"] == "Excellent"]
good_students = df[df["result"] == "Good"]
needs_improvement_students = df[df["result"] == "Needs Improvement"]
```
---
## 5. Sort Students
```Python
sortdf=df.sort_values(by="marks",ascending=False)
```
`sort_values()` sorts a DataFrame by one or more columns, and `ascending=False` gives descending order.

---
## 6. Basic Analytics
```Python
average_marks = df["marks"].mean()
highest_marks = df["marks"].max()
lowest_marks = df["marks"].min()
average_attendance = df["attendance"].mean()
average_study_hours = df["study_hours"].mean()
result_counts = df["result"].value_counts()
department_counts = df["department"].value_counts()
```
---
## 7. Interview Questions
- What is EDA?
- Why do we add a new column in Pandas?
- What does `df.apply(..., axis=1)` do?
- How do you filter rows by category?
- How do you sort a DataFrame by marks?
- What does `value_counts()` do?
- What does `df["marks"].mean()` do?
- Why use `index=False` in `to_csv()`?
- Why should we inspect data before analysis?
- How can this project become an ML preprocessing project?
---
## 8. Assignment
Use the employee dataset from Slot 3 and build:
```
day4_employee_analysis.py
```
Tasks:
```
1. Create employee DataFrame
2. Add level column:
   Senior: experience >= 5 and salary >= 70000
   Mid-Level: experience >= 2 and salary >= 40000
   Junior: otherwise
3. Filter Senior, Mid-Level, and Junior employees
4. Sort employees by salary descending
5. Calculate average salary
6. Calculate highest salary
7. Calculate average experience
8. Count levels
9. Count departments
10. Save as day4_employee_analysis_report.csv
```
