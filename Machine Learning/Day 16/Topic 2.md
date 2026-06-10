# Data Types, Invalid Values, Outliers Basics, and Category Cleaning
## 1. Goal
```
1. Identify numerical and categorical columns
2. Check column data types
3. Convert wrong data types
4. Clean messy text categories
5. Detect invalid values
6. Validate ranges
7. Understand basic outliers
8. Fix beginner Pandas cleaning errors
9. Prepare data for encoding and scaling
```
Today's Focus:
```
Raw Data
   ↓
Check Data Types
   ↓
Clean Invalid Values
   ↓
Clean Categories
   ↓
Detect Outliers
   ↓
Prepare for ML
```
---
## 2. Why This Topic Matters
A dataset can look clean but still be wrong.
Example:
```
CGPA = 15
Attendance = 140
Age = -5
Marks = "85%"
Internship = "yes", "YES", "Y", "Yes "
```
There may be no missing values, but the data is still not model-ready.
A beginner checks only:
```
df.isnull().sum()
```
A strong ML engineer checks:
```Python
df.info()
df.dtypes
df.describe()
df["column"].unique()
df["column"].value_counts()
```
---
## 3. Industry Applications
![[Pasted image 20260610161210.png]]

---
## 4. Beginner Explanation
### What is Data Type?
Data type means what kind of value a column stores.
Common Pandas data types:
```
int64     → whole numbers
float64   → decimal numbers
object    → text/mixed values
bool      → True/False
datetime  → date/time values
```
Example:
```
CGPA = float
Attendance = int/float
City = object/text
Internship = object/text or boolean
Placed = object/category
```
Check data types:
```
print(df.dtypes)
```
Or:
```
df.info()
```
---
## 5. Dataset for this slot
```Python
import pandas as pd
import numpy as np

data = {
    "student_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "cgpa": [8.5, 6.2, 15.0, 7.8, 5.9, 9.1, -1.0, 8.0],
    "attendance": [85, 45, 120, 78, 55, 95, -10, 88],
    "marks": ["82", "45", "90%", "76", "50", "95", "35", "88"],
    "branch": ["CSE", "cse", "Cse ", "ECE", "ece", "ME", "me ", "CSE"],
    "internship": ["Yes", "yes", "Y", "No", "no", "N", "YES ", "No"],
    "placed": ["Yes", "No", "Yes", "Yes", "No", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)

print(df)
```
This dataset has three problems:
```
cgpa has invalid values: 15.0, -1.0
attendance has invalid values: 120, -10
marks has "90%" stored as text
branch has inconsistent categories: CSE, cse, Cse 
internship has inconsistent categories: Yes, yes, Y, YES, No, no, N
```
---
## 6. Step 1: Check Data Types
```
print(df.dtypes)
```
Expected issue:
```
marks is object
```
But marks should be numerical.
Why is it object?
```
Because one value is "90%" as text.
```
Also check:
```
df.info()
```
This helps you catch hidden problems before model training.

---
## 7. Step 2: Check Unique Values
For categorical columns:
```
print(df["branch"].unique())
print(df["internship"].unique())
```
Output may look like:
```
['CSE' 'cse' 'Cse ' 'ECE' 'ece' 'ME' 'me ']['Yes' 'yes' 'Y' 'No' 'no' 'N' 'YES ']
```
Problem:
```
Same meaning, different spelling/case/space.
```
ML will treat them as different categories if not cleaned.

---
## 8. Step 3: Clean Text Categories
Pandas string methods through `.str` allow operations like lowercase conversion and whitespace stripping on Series values. `str.strip()` removes leading/trailing characters such as whitespace, which is useful for category cleanup.
### Clean Branch
```python
df["branch"] = df["branch"].str.strip().str.upper()
print(df["branch"].unique())
```
Now:
```
['CSE', 'ECE', 'ME']
```
### Clean Internship
```Python
df["internship"] = df["internship"].str.strip().str.lower()
df["internship"] = df["internship"].replace({    "yes": "Yes",    "y": "Yes",    "no": "No",    "n": "No"})
print(df["internship"].unique())
```
Now:
```
['Yes', 'No']
```
---
## 9. Step 4: Clean Numeric Columns Stored as Text
Problem:
```Python
print(df["marks"].dtype)
```
Output:
```
object
```
Why?
```
Because "90%" contains a percent sign.
```
Clean it:
```Python
df["marks"] = df["marks"].str.replace("%", "", regex=False)
df["marks"] = pd.to_numeric(df["marks"])
print(df["marks"])print(df["marks"].dtype)
```
Now marks becomes numeric.
Pandas `astype()` can convert columns to a specified dtype, but when a column has messy numeric text such as symbols, cleaning the symbols first and then converting is safer.

---
## 10. Step 5: Detect Invalid Values
Invalid values are values that do not make sense.
For CGPA:
```
Valid range = 0 to 10
```
Check invalid CGPA:
```Python
invalid_cgpa = df[(df["cgpa"] < 0) | (df["cgpa"] > 10)]
print(invalid_cgpa)
```
For attendance:
```
Valid range = 0 to 100
```
Check invalid attendance:
```Python
invalid_attendance = df[(df["attendance"] < 0) | (df["attendance"] > 100)]print(invalid_attendance)
```
---
## 11. Step 6: Fix Invalid Values
There are multiple strategies.
### Strategy 1: Replace invalid values with NaN
```Python
df.loc[(df["cgpa"] < 0) | (df["cgpa"] > 10), "cgpa"] = np.nandf.loc[(df["attendance"] < 0) | (df["attendance"] > 100), "attendance"] = np.nan
```
Then fill:
```Python
df["cgpa"] = df["cgpa"].fillna(df["cgpa"].median())
df["attendance"] = df["attendance"].fillna(df["attendance"].median())
```
### Strategy 2: Remove invalid rows
```Python
df = df[(df["cgpa"] >= 0) & (df["cgpa"] <= 10)]
df = df[(df["attendance"] >= 0) & (df["attendance"] <= 100)]
```
Use this only if the dataset is large and invalid rows are clearly wrong.
### Strategy 3: Clip values
```Python
df["cgpa"] = df["cgpa"].clip(0, 10)df["attendance"] = df["attendance"].clip(0, 100)
```
Be careful. Clipping can hide data-entry errors.

---
## 12. What are Outliers?
Outliers are unusual values compared to the rest of the data.
Example:
```
Study hours:2, 3, 4, 5, 6, 7, 100
```
Here:
```
100 is an outlier
```
Outliers may be:
```
Real extreme valuesData-entry mistakesFraud/anomalyMeasurement error
```
Do not automatically delete outliers.
Ask:
```
Is this value impossible or just rare?
```
Example:
```
Age = -5 → impossible → invalid
Income = 1 crore → rare but possible → outlier, not necessarily invalid
```
---
## 13. Basic Outlier Detection Using IQR
IQR means:
```
Interquartile Range
```
Formula:
```
IQR = Q3 - Q1
```
Outlier boundaries:
```
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```
Code:
```Python
Q1 = df["marks"].quantile(0.25)
Q3 = df["marks"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df["marks"] < lower_bound) | (df["marks"] > upper_bound)]
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Outliers:")
print(outliers)
```
Today you only need basic understanding. We will go deeper during model evaluation and feature engineering.

---
## 14. Debugging Section
