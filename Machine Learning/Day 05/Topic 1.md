# Data Cleaning Basics
Today we start **data cleaning**, one of the most important steps before ML model training. Real datasets often contain **missing values, duplicate rows, wrong data types, invalid values, spelling inconsistencies, and outliers**. Pandas provides built-in methods like `isnull()`, `fillna()`, `dropna()`, and `drop_duplicates()` for handling these problems. Pandas docs describe missing data handling as a core workflow, and `fillna()` is specifically used to replace missing values with non-missing values.

---
## 1. Why data cleaning matters in AI/ML
Bad data gives bad results:
Example:
```
salary = -50000
marks = 120
attendance = None
experience = "five"
department = "Ai", "AI", "ai"
duplicate employee rows
```
If you train a model on this, the model learns wrong patterns.
Data cleaning means:
```
Raw messy data → clean usable data → analysis / ML model
```
---
## 2. Create messy employee dataset
![[Pasted image 20260603122559.png]]
This dataset has :
```
1. Missing name
2. Missing salary
3. Missing rating
4. Duplicate employee row
5. Negative salary
6. Wrong data type in experience
7. Department spelling inconsistency
```
---
## 3. Check missing values
![[Pasted image 20260603122721.png]]
Meaning:
```
name has 1 missing value
salary has 1 missing value
rating has 1 missing value
```
---
## 4. Check duplicate rows
![[Pasted image 20260603122844.png]]
if duplicate rows exist, remove them:
![[Pasted image 20260603123050.png]]
`drop_duplicates()` returns a DataFrame with duplicate rows removed, and Pandas allows checking certain columns optionally.

---
## 5. Handle missing Values
There are two common ways:
```
drop missing values
fill missing values
```
### Option 1: Drop rows with missing values
![[Pasted image 20260603123401.png]]
`dropna()` removes missing values from a DataFrame.
But be careful. If you drop too many rows, you may lose useful data.

---
### Option 2: Fill missing values
Better for this project:
![[Pasted image 20260603123618.png]]
Meaning:
```
missing name → Unknown
missing salary → average salary
missing rating → average rating
```
`fillna()` can fill missing values using a single value or column-specific values.

---
## 6. Fix Invalid values
Negative salary is invalid.
![[Pasted image 20260603123830.png]]
This removes rows where salary is less than 0.

---
## 7. Fix Wrong datatype
In the dataset:
```
experience = "four"
```
This is a string, but experience should be numeric.
Use:
![[Pasted image 20260603124105.png]]
This converts invalid values to `NaN`.
Then Fill missing experience:
![[Pasted image 20260603124343.png]]

---
## 8. Fix text inconsistency
Department:
```
AI
ai
DATA
Data
```
Make them consistent:
![[Pasted image 20260603124608.png]]

---
## 9. Common Commands
![[Pasted image 20260603124716.png]]

---
## 10. Interview questions
1. What is data cleaning?
2. Why is data cleaning important before ML?
3. What are missing values?
4. How do you check missing values in Pandas?
5. What does `fillna()` do?
6. What does `dropna()` do?
7. What does `drop_duplicates()` do?
8. Why are duplicate rows harmful?
9. Why is negative salary invalid?
10. What does `pd.to_numeric(errors="coerce")` do?
11. Why do we standardize text columns?
12. Why should we check data after cleaning?
---
## 11. Assignment
Create a messy student dataset with these problems:
```
1. one missing name
2. one missing marks
3. one duplicate row
4. one invalid marks value above 100
5. one invalid attendance below 0
6. one subject written as "AI", "ai", "Ai"
```
Clean it using Pandas and save:
```
day5_cleaned_student_data.csv
```
dataset:
```Python
data = {  
	"student_id": [101, 102, 103, 104, 105, 106, 106, 108, 109, 110],  
	"name": ["Rahul", "Aman", "Priya", "Sneha", None, "Anjali", "Anjali", "Rohit", "Karan", "Neha"],  
	"marks": [85, 72, None, 91, 120, 88, 88, 35, "sixty", 45],  
	"attendance": [90, 80, 70, 95, 85, 92, 92, -10, 78, None],  
	"study_hours": [5, 4, 3, 6, 5, 5, 5, 1, 2, None],  
	"subject": ["AI", "Data", "ai", "AI", "Ai", "DATA", "DATA", "Web", "web", "Data"]  
}
```
---
