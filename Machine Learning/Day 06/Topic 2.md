# Grouping with `groupby()`
## 1. What is `groupby()`?
`groupby()` means grouping rows based on a column value.
Example:
```
Group students by subject
AI students together
DATA students together
WEB students together
```
Then apply calculations:
```
Average marks by subject
Highest attendance by subject
Number of students by result
Average study hours by result
```
Simple formula:
```
groupby = split data → apply calculation → combine output
```
---
## 2. Dataset
```Python
data = {  
	"student_id": [101, 102, 103, 104, 105, 106, 107, 108],  
	"name": ["Rahul", "Aman", "Priya", "Sneha", "Karan", "Anjali", "Rohit", "Neha"],  
	"marks": [85, 72, 45, 91, 60, 88, 35, 67],  
	"attendance": [90, 80, 70, 95, 78, 92, 60, 82],  
	"study_hours": [5, 4, 3, 6, 2, 5, 1, 4],  
	"subject": ["AI", "DATA", "AI", "AI", "DATA", "DATA", "WEB", "WEB"],  
	"result": ["Excellent", "Good", "Needs Improvement", "Excellent", "Good", "Excellent", "Needs Improvement", "Good"]  
}
```
---
## 3. Group by one column
Find average marks by subject:
![[Pasted image 20260604130339.png]]
meaning:
```
AI students average marks = 73.66
DATA students average marks = 73.33
WEB students average marks = 51.00
```
---
## 4. Count records in each group 
use `count()`
![[Pasted image 20260604130526.png]]
Better way:
![[Pasted image 20260604130549.png]]
`value_counts()` returns counts of unique values in a Series, while `groupby()` is better when you want grouped calculations like mean, max, min, and multiple aggregations.

----
## 5. Multiple calculations using `agg()`
Use `agg()` when you want several calculations together.
![[Pasted image 20260604142015.png]]

---
## 6. Group multiple numeric columns
![[Pasted image 20260604142237.png]]

---
## 7. Group by multiple columns
![[Pasted image 20260604142401.png]]

---
## 8. Convert the groupby output into DataFrame.
![[Pasted image 20260604142535.png]]
Use `reset_index()` when you want to save or further process the grouped result.

---
## 9. Interview Questions
- What is `groupby()`?
- What does split-apply-combine mean?
- How do you calculate average marks by subject?
- How do you count students by subject?
- What does `agg()` do?
- Why do we use `reset_index()` after groupby?
- How do you group by multiple columns?
- What is the difference between `value_counts()` and `groupby()`?
- Why should grouped calculations usually use numeric columns?
- How is `groupby()` useful in EDA?
---
## 10. Asssignment
Use this Dataset:
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
1. Average salary by department
2. Highest salary by department
3. Lowest salary by department
4. Employee count by department
5. Average rating by level
6. Average experience by level
7. Salary summary by department using agg()
8. Group by department and level
9. Convert grouped output to DataFrame using reset_index()
10. Save summary as day6_employee_groupby_summary.csv
```
---
