# Exploratory Data Analysis Basics
**Exploratory Data Analysis**. EDA means understanding a dataset before building models. In AI/ML, you should never directly train a model after loading data. First, inspect rows, columns, missing values, distributions, category counts, relationships, and possible patterns. Pandas provides important EDA tools like `head()`, `info()`, `describe()`, `value_counts()`, `groupby()`, and `corr()`. `describe()` summarizes central tendency, spread, and distribution shape; `corr()` computes pairwise correlation between numeric columns; and `groupby()` follows a split-apply-combine style for grouped analysis.

---
## 1. What is EDA?
EDA means:
```
Exploratory Data Analysis 
```
Simple meaning:
```
Before ML model → understand the data
```
EDA helps you answer:
```
1. How many rows and columns are there?
2. Which columns are numerical?
3. Which columns are categorical?
4. Are there missing values?
5. What is the average, maximum, and minimum?
6. Which category appears most?
7. Are columns related to each other?
8. Are there unusual values?
```
---
## 2. Dataset for Today
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
![[Pasted image 20260604122401.png]]

---
## 3. First Look of Data
![[Pasted image 20260604122434.png]]
`head()` returns the first `n` rows and is useful for quickly checking whether the object has the expected type of data. By default, it shows the first 5 rows.
Also check:
![[Pasted image 20260604122620.png]]
![[Pasted image 20260604122609.png]]
![[Pasted image 20260604122635.png]]

---
## 4. Dataset Info
![[Pasted image 20260604122740.png]]
`info()` prints DataFrame information, including index dtype, column names, non-null values, column dtypes, and memory usage.
Use it to check:
```
missing values
data types
number of rows
number of columns
```
---
## 5. Statistical Summary
![[Pasted image 20260604122919.png]]
`describe()` summarizes central tendency, dispersion, and distribution shape for the dataset’s numeric columns while excluding missing values.

---
## 6. Category Counts:
![[Pasted image 20260604123119.png]]
`Series.value_counts()` returns counts of unique values, sorted so the most frequent value appears first by default.

---
## 7. Basic Analysis
![[Pasted image 20260604123225.png]]

---
## 8. Group-Based Analysis 
Now check average marks by subject:
![[Pasted image 20260604123412.png]]
Check average attendance by result:
![[Pasted image 20260604123457.png]]

---
## 9. Correlation
Correlation tells whether numeric columns move together.
![[Pasted image 20260604123613.png]]
`DataFrame.corr()` computes pairwise correlation of numeric columns while excluding missing values.
Example interpretation:
```
marks and study_hours high positive correlation
→ students who study more may score higher
```
Remember: correlation does not always mean cause.

---
## 10 . Common Errors
### Error 1: Wrong column name
```Python
df["mark"].mean()
```
Correct:
```Python
df["marks"].mean()
```
Check:
```Python
print(df.columns)
```
---
## Error 2: Running correlation on text columns
Wrong:
```Python
df.corr()
```
If your DataFrame contains text columns, select numeric columns clearly:
```Python
df[["marks", "attendance", "study_hours"]].corr()
```
---
## Error 3: Grouping by wrong column
Wrong:
```Python
df.groupby("subjects")["marks"].mean()
```
Correct:
```Python
df.groupby("subject")["marks"].mean()
```
---
## Error 4: Forgetting brackets in method call
Wrong:
```Python
df.head
```
Correct:
```Python
df.head()
```
---
## 11. Interview Questions
1. What is EDA?
2. Why is EDA important before ML?
3. What does `df.head()` show?
4. What does `df.shape` show?
5. What does `df.info()` show?
6. What does `df.describe()` show?
7. What does `value_counts()` do?
8. What does `groupby()` do?
9. What is correlation?
10. Why should we select numeric columns before correlation?
11. What is the difference between numerical and categorical columns?
12. Why should we check missing values during EDA?
---
## 12. Assignment
Dataset:
```Python
data = {  
	"employee_id": [101, 102, 103, 104, 105, 106, 107, 108],
	"name": ["Amit", "Riya", "Karan", "Neha", "Vikas", "Anjali", "Rohit", "Priya"],  
	"salary": [25000, 45000, 80000, 120000, 35000, 70000, 30000, 95000],  
	"experience": [1, 3, 6, 8, 2, 5, 1, 7],  
	"rating": [3, 4, 5, 5, 2, 4, 3, 5],  
	"department": ["HR", "IT", "AI", "AI", "SALES", "DATA", "IT", "DATA"],  
	"level": ["Junior", "Mid-Level", "Senior", "Senior", "Junior", "Senior", "Junior", "Senior"]  
}
```
Do:
```
1. Print first 5 rows
2. Print shape
3. Print columns
4. Print dtypes
5. Print info
6. Print describe
7. Check missing values
8. Count departments
9. Count levels
10. Calculate average salary
11. Calculate highest salary
12. Calculate average salary by department
13. Calculate average rating by level
14. Print correlation between salary, experience, and rating
15. Save as day6_employee_eda_basics_report.csv
```
---
