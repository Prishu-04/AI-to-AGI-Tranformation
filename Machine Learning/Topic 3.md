# Type Conversion and Outlier Handling
There are two serious problems:
```
1. Wrong data types
2. Outlier/Invlaid extreme values
```
In Pandas, `pd.to_numeric(errors="coerce")` is used to convert values into numbers; invalid parsing becomes `NaN` when `errors="coerce"` is used. Pandas also provides `clip()` to limit values outside boundaries to fixed lower/upper limits.

---
## 1. What is type conversion?
Type conversion means changing data from one type to another.
Example:
```
"85"      → 85
"sixty"   → NaN
"4.5"     → 4.5
```
In datasets, numbers sometimes come as strings.
Example:
```Python
marks="85"
```
This looks like a number, but it is actually text.
If you try:
```Python
marks>=40
```
Python/Pandas may give an error because string and number comparison is not valid.

---
## 2. What is an outlier?
An outlier is a value that is extremely different from normal values.
Example:
```
marks = 500
attendance = -20
study_hours = 100
salary = 99999999
```
Some Outliners are real, but many are data-entry mistakes.
For student dataset:
```
marks should be 0–100
attendance should be 0–100
study_hours should be reasonable, maybe 0–12
```
---
## 3. Dataset for this slot
```Python
data = {  
	"student_id": [101, 102, 103, 104, 105, 106, 107, 108],  
	"name": ["Rahul", "Aman", "Priya", "Sneha", "Karan", "Anjali", "Rohit", "Neha"],  
	"marks": [85, "72", "sixty", 91, 120, 88, 35, -10],  
	"attendance": [90, "80", 70, 95, 85, 150, -20, 75],  
	"study_hours": [5, "4", 3, 6, 5, 50, 1, "two"],  
	"subject": ["AI", "Data", "ai", "AI", "Ai", "DATA", "Web", "web"]  
}
```
---
![[Pasted image 20260604102318.png]]
Problem inside the dataset:
![[Pasted image 20260604102347.png]]

---
## 4. Convert Columns to numeric
Use `pd.to_numeric()`:
![[Pasted image 20260604102659.png]]
Meaning:
```
"72"    → 72
"sixty" → NaN
"two"   → NaN
```
`errors="coerce"` converts invalid values into missing values instead of crashing.

---
## 5. Fill missing values after conversion
After conversion, invalid text becomes `Nan`.
![[Pasted image 20260604102854.png]]
Why median?
```
Median is safer when data has outliers.
```
---
## 6. Handle invalid range values
For marks:
```
valid marks = 0 to 100
```
For attendance:
```
valid attendance = 0 to 100
```
For study hours:
```
reasonable study hours = 0 to 12
```
There are two common ways.
### Method 1 : Remove Invalid rows:
![[Pasted image 20260604104053.png]]
### Method 2 : Clip Outliers
![[Pasted image 20260604104158.png]]
`clip()` trims values outside given boundaries to boundary values. FOr example, marks `120` becomes `100`, and attendance `-20` becomes `0`.
Use this when you do not want to delete rows.

---
## 7. Standardize text column
![[Pasted image 20260604104440.png]]
Now :
```
AI, ai, Ai → AI
DATA, Data → DATA
web, Web → WEB
```
---
## 8. Remove vs Clip - Which should you use?
![[Pasted image 20260604104537.png]]

---
## 9. IQR Method for outliers
For real analysis, one common method is the **IQR method**.
```
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
```
IQR is the difference between the 75th and 25th percentiles of the data.
Examples:
![[Pasted image 20260604104732.png]]

---
## 10. Common errors
### Error 1: Finding mean before conversion
Wrong:
```Python
df["marks"].mean()
```
If marks contain `"sixty"`, this may fail or behave incorrectly.
Correct:
```Python
df["marks"] = pd.to_numeric(df["marks"], errors="coerce")df["marks"] = df["marks"].fillna(df["marks"].median())
```
---
### Error 2: Using `and` instead of `&`
Wrong:
```python
df = df[(df["marks"] >= 0) and (df["marks"] <= 100)]
```
Correct:
```Python
df = df[(df["marks"] >= 0) & (df["marks"] <= 100)]
```
---
### Error 3: Forgetting parentheses
Wrong:
```Python
df = df[df["marks"] >= 0 & df["marks"] <= 100]
```
Correct:
```Python
df = df[(df["marks"] >= 0) & (df["marks"] <= 100)]
```
---
### Error 4: Not saving the changed column
Wrong:
```Python
pd.to_numeric(df["marks"], errors="coerce")
```
Correct:
```Python
df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
```
---
## 11. Interview Questions:
- What is type conversion?
- Why do numeric columns sometimes become object dtype?
- What does `pd.to_numeric()` do?
- What does `errors="coerce"` do?
- What is an outlier?
- Why are outliers dangerous in ML?
- What is the difference between invalid value and outlier?
- How do you remove invalid marks?
- What does `clip()` do?
- When should you remove rows instead of clipping?
- What is IQR?
- Why should text columns be standardized?
---
## 12. Assignment
Use your messy student dataset and do this:
```
1. Convert marks to numeric
2. Convert attendance to numeric
3. Convert study_hours to numeric
4. Fill new NaN values after conversion
5. Remove rows where marks < 0 or marks > 100
6. Remove rows where attendance < 0 or attendance > 100
7. Remove rows where study_hours < 0 or study_hours > 12
8. Convert subject to uppercase
9. Print dtypes before and after cleaning
10. Save as day5_type_outlier_student_cleaned.csv
```
---
