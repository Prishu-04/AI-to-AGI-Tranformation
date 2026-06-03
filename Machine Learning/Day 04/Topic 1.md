# Introduction to Pandas + Series and DataFrame
## 1. What is Pandas?
**Pandas** is a Python library used for working with structured data.
Structured data means data stored in table format, like:
```
Rows and columns
CSV files
Excel files
Database tables
```
In AI/ML, Pandas is used before training a model because we first need to load, clean, analyze, and prepare data.

---
## 2. Why Pandas is Important in AI/ML?
Pandas is used for:
```
Reading datasets
Cleaning missing values
Filtering data
Selecting rows and columns
Analyzing data
Creating new columns
Saving cleaned datasets
Preparing data for ML models
```
Example:
```
Raw CSV Dataset → Pandas Cleaning → NumPy/Scikit-learn → ML Model
```
![[Pasted image 20260603095136.png]]

---
## 3. Installing Pandas
Run this in terminal:
```Bash
pip install pandas
```
check installation:
```Python
import pandas as pd
print(pd.__version__)
```
---
## 4. Importing Pandas:
```Python
import pandas as pd
```
---
## 5. Pandas Series
A **Series** is like a single column of data.
Example:
![[Pasted image 20260601092238.png]]
here:
```
0, 1, 2, 3 = index
85, 90, 78, 92 = values
```
---
## 6. Series with Custom Index:
![[Pasted image 20260601092427.png]]

---
### Accessing Series Values
![[Pasted image 20260601092718.png]]
Index :
![[Pasted image 20260601092945.png]]

---
## 7. AI/ML Use case of Series.
A Series can represent one feature column.
Example:
![[Pasted image 20260601093112.png]]
In ML, this can represent:
```
Study hours of students
Age column
Salary column
Marks column
Temperature column
```
---
## 8. Pandas Data Frame
A **Data Frame** is a table with rows and columns.
It is the most important Pandas object.
Example:
![[Pasted image 20260601093318.png]]

---
## 9. Understanding Data Frame
In this Table:
```
Rows = students
Columns = Name, Math, Science, English
```
Example:
```
Row 0 = Pratyaksh's data
Column Math = Math marks of all students
```
----
## 10. Checking Data Frame Columns:
![[Pasted image 20260601093529.png]]

---
## 11. Checking Data Frame Shape:
![[Pasted image 20260601093640.png]]
Meaning:
```
3 rows
4 columns
```
---
## 12. Checking First Rows using `head()`
![[Pasted image 20260601093824.png]]
By default: if no number is provided then it display 5 records or values.

---
## 13. Checking Last Rows using `tail()`
![[Pasted image 20260601094000.png]]
By default: if no number is provided then it display 5 records or values.

---
## 14. Selecting One Column
![[Pasted image 20260601094153.png]]

---
## 15. Selecting Multiple Columns
![[Pasted image 20260601094257.png]]

---
## 16. Creating New Column
You can create a new column using existing columns.
![[Pasted image 20260601094351.png]]

---
## 17. Creating Average Columns
![[Pasted image 20260601094540.png]]
To round off the averages:
![[Pasted image 20260601094705.png]]

---
## 18. Adding Result Column
![[Pasted image 20260601095010.png]]

---
## 19. AI/ML Meaning
In ML:
```
DataFrame = full dataset
Columns = features
Rows = samples
Target column = output/label
```
Example:
```
Math, Science, English = features
Result = target/label
```
So later, for ML:
```
X = Math, Science, English
y = Result
```
---
## 20. Common Errors and Corrections
### Error 1: Pandas Not installed
```Python
import pandas as pd
```
Error:
```
ModuleNotFoundError: No module named 'pandas'
```
Correction:
```Bash
pip install pandas
```
---
### Error 2: Forgetting `pd`
![[Pasted image 20260601095400.png]]
Correct :
```Python
df = pd.DataFrame(data)
```
---
### Error 3: Column Name Spelling Mistake
![[Pasted image 20260601095544.png]]
Because Actual column name is :
```
Math
```
Correct Code:
```Python
print(df["Math"])
```
---
### Error 4: Wrong Multiple Column Selection
![[Pasted image 20260601095722.png]]
Correct Code:
```Python
print(df[["Name", "Math"]])
```
---
### Error 5: Different Length Columns
![[Pasted image 20260601095846.png]]
Correct Code:
```python
data = {
    "Name": ["Pratyaksh", "Rahul", "Sneha"],
    "Math": [85, 70, 90]
}
df = pd.DataFrame(data)
```
---
## 21. Practice Tasks
## Task 1
Create a Pandas Series for marks:
```
[85, 90, 78, 92, 88]
```
Print the full Series.

---
## Task 2
Create a Series with custom index:
```
Math = 85
Science = 90
English = 78
Computer = 95
```
Print each subject mark separately.

---
## Task 3
Create a DataFrame with this data:
```
Name: Pratyaksh, Rahul, Sneha, Aman
Math: 85, 70, 90, 95
Science: 88, 75, 95, 92
English: 78, 80, 92, 88
```
Print the full DataFrame.

---
## Task 4
Print:
```
First 2 rows
Last 2 rows
Shape
Columns
Only Name column
Name and Math columns
```

---
## Task 5
Add these new columns:
```
Total
Average
Result
```
Pass condition:
```
Average >= 50
```
---
## 22. Slot 1 Final Mini Code
```Python
import pandas as pd

marks = pd.Series([85, 90, 78, 92, 88])

print("Marks Series:")
print(marks)

subject_marks = pd.Series(
    [85, 90, 78, 95],
    index=["Math", "Science", "English", "Computer"]
)

print("\nSubject Marks:")
print(subject_marks)

print("\nMath Marks:", subject_marks["Math"])
print("Science Marks:", subject_marks["Science"])
print("English Marks:", subject_marks["English"])
print("Computer Marks:", subject_marks["Computer"])

data = {
    "Name": ["Pratyaksh", "Rahul", "Sneha", "Aman"],
    "Math": [85, 70, 90, 95],
    "Science": [88, 75, 95, 92],
    "English": [78, 80, 92, 88]
}

df = pd.DataFrame(data)

print("\nStudent DataFrame:")
print(df)

print("\nFirst 2 Rows:")
print(df.head(2))

print("\nLast 2 Rows:")
print(df.tail(2))

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nName Column:")
print(df["Name"])

print("\nName and Math Columns:")
print(df[["Name", "Math"]])

df["Total"] = df["Math"] + df["Science"] + df["English"]

df["Average"] = df["Total"] / 3
df["Average"] = df["Average"].round(2)

df["Result"] = ["Pass" if avg >= 50 else "Fail" for avg in df["Average"]]

print("\nFinal DataFrame:")
print(df)
```
---
## 23 Interview Questions
1. What is Pandas?
2. Why is Pandas important in AI/ML?
3. What is a Series?
4. What is a DataFrame?
5. What is the difference between NumPy array and Pandas DataFrame?
6. What does `pd.read_csv()` do?
7. What does `df.head()` do?
8. What does `df.shape` return?
9. What does `df.dtypes` show?
10. What does `df.describe()` show?
11. How do you select one column?
12. How do you select multiple columns?
13. How do you create a new column?
14. Why do we use `index=False` in `to_csv()`?
15. What causes `KeyError` in Pandas?
---
