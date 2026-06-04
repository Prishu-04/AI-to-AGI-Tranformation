# Aggregation and Summary Tables
## 1. What is Aggregation?
Aggregation means converting many rows into a smaller summary.
Example:
```
Many student rows → average marks by subject
Many employee rows → average salary by department
Many result rows → count of Excellent, Good, Needs Improvement
```
Common aggregation functions:
![[Pasted image 20260604145013.png]]

---
## 2. Dataset for this slot
```Python
import pandas as pd

data = {
    "student_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "name": ["Rahul", "Aman", "Priya", "Sneha", "Karan", "Anjali", "Rohit", "Neha"],
    "marks": [85, 72, 45, 91, 60, 88, 35, 67],
    "attendance": [90, 80, 70, 95, 78, 92, 60, 82],
    "study_hours": [5, 4, 3, 6, 2, 5, 1, 4],
    "subject": ["AI", "DATA", "AI", "AI", "DATA", "DATA", "WEB", "WEB"],
    "result": ["Excellent", "Good", "Needs Improvement", "Excellent", "Good", "Excellent", "Needs Improvement", "Good"]
}

df = pd.DataFrame(data)

print(df)
```
---
## 3. Simple Aggregation
Average Mean:
![[Pasted image 20260604145615.png]]
Highest Marks:
![[Pasted image 20260604145708.png]]
Lowest Marks:
![[Pasted image 20260604145741.png]]
Count Students:
![[Pasted image 20260604150033.png]]

----
## 4. Aggregation on multiple columns
![[Pasted image 20260604150221.png]]
`DataFrame.agg()` is an alias for `aggregate()` and can apply one or more operations across an axis.

---
## 5. Grouped aggregation with `agg()`
Summary table:
![[Pasted image 20260604150604.png]]
This creates a powerful EDA summary table:
Meaning:
```
For each subject:
- average/highest/lowest marks
- average/highest/lowest attendance
- average/highest/lowest study hours
- student count
```
---
## 6. Named Aggregation
The previous output has multi-level column names. For cleaner column names, use named aggregation:
![[Pasted image 20260604150912.png]]

---
## 7. Convert summary index into column
After `groupby()`, the group column usually becomes the index. Use:
![[Pasted image 20260604151047.png]]

---
## 8. Summary by Result
![[Pasted image 20260604151209.png]]

---
## 9. Group by two columns:
![[Pasted image 20260604151321.png]]

---
## 10. Sort summary table
![[Pasted image 20260604151450.png]]

---
## 11. Save summary Tables
![[Pasted image 20260604151541.png]]

----
## 12. Interview Questions:
- What is aggregation?
- What is the difference between simple aggregation and grouped aggregation?
- What does `agg()` do?
- Why do we use named aggregation?
- What does `reset_index()` do?
- How do you create average marks by subject?
- How do you create multiple summaries in one table?
- How do you group by two columns?
- Why should you avoid applying `mean()` to text columns?
- Why do we save summary tables as CSV?
---
## 13. Assignment
Employee dataset:
```Python
import pandas as pd

data = {
    "employee_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "name": ["Amit", "Riya", "Karan", "Neha", "Vikas", "Anjali", "Rohit", "Priya"],
    "salary": [25000, 45000, 80000, 120000, 35000, 70000, 30000, 95000],
    "experience": [1, 3, 6, 8, 2, 5, 1, 7],
    "rating": [3, 4, 5, 5, 2, 4, 3, 5],
    "department": ["HR", "IT", "AI", "AI", "SALES", "DATA", "IT", "DATA"],
    "level": ["Junior", "Mid-Level", "Senior", "Senior", "Junior", "Senior", "Junior", "Senior"]
}

df = pd.DataFrame(data)
```
Do:
```
1. Overall summary for salary, experience, and rating using agg()
2. Department summary:
   average_salary
   highest_salary
   lowest_salary
   average_experience
   average_rating
   employee_count
3. Level summary:
   average_salary
   average_experience
   average_rating
   employee_count
4. Department + level summary
5. Sort department summary by average_salary descending
6. Save:
   day6_department_summary_table.csv
   day6_level_summary_table.csv
   day6_department_level_summary_table.csv
```
---
