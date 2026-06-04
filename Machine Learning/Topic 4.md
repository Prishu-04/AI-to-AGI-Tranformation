# Build Data-Cleaning Project.
## 1. Project Goal
Your Project will:
```
1. Create a messy student dataset
2. Inspect missing values and duplicates
3. Remove duplicate rows
4. Fill missing text values
5. Convert numeric columns properly
6. Fill numeric null values
7. Handle invalid/outlier values
8. Standardize text columns
9. Add result column
10. Save cleaned dataset as CSV
```
---
## 2. Messy Dataset.
```Python
data = {  
	"student_id": [101, 102, 103, 104, 105, 106, 106, 108, 109, 110],  
	"name": ["Rahul", "Aman", "Priya", "Sneha", None, "Anjali", "Anjali", "Rohit", "Karan", "Neha"],  
	"marks": [85, "72", "sixty", 91, 120, 88, 88, 35, -10, None],  
	"attendance": [90, "80", 70, 95, 85, 92, 92, -20, 78, None],  
	"study_hours": [5, "4", 3, 6, 5, 5, 5, 1, "two", None],  
	"subject": ["AI", "Data", "ai", "AI", "Ai", "DATA", "DATA", "Web", "web", None]  
}
```
Problems:
![[Pasted image 20260604112554.png]]

---
## 3. Cleaning Strategy
![[Pasted image 20260604112616.png]]

---
## 4. Complete Project Code
```Python
import pandas as pd
import numpy as np


data = {
    "student_id": [101, 102, 103, 104, 105, 106, 106, 108, 109, 110],
    "name": ["Rahul", "Aman", "Priya", "Sneha", None, "Anjali", "Anjali", "Rohit", "Karan", "Neha"],
    "marks": [85, "72", "sixty", 91, 120, 88, 88, 35, -10, None],
    "attendance": [90, "80", 70, 95, 85, 92, 92, -20, 78, None],
    "study_hours": [5, "4", 3, 6, 5, 5, 5, 1, "two", None],
    "subject": ["AI", "Data", "ai", "AI", "Ai", "DATA", "DATA", "Web", "web", None]
}

df = pd.DataFrame(data)

print("Original Messy Data:")
print(df)

print("-" * 40)

print("Data Types Before Cleaning:")
print(df.dtypes)

print("-" * 40)

print("Missing Values Before Cleaning:")
print(df.isnull().sum())

print("-" * 40)

print("Duplicate Rows Before Cleaning:")
print(df.duplicated().sum())

print("-" * 40)

df = df.drop_duplicates()

df["name"] = df["name"].fillna("Unknown")
df["subject"] = df["subject"].fillna("Unknown")

df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
df["attendance"] = pd.to_numeric(df["attendance"], errors="coerce")
df["study_hours"] = pd.to_numeric(df["study_hours"], errors="coerce")

df["marks"] = df["marks"].fillna(df["marks"].median())
df["attendance"] = df["attendance"].fillna(df["attendance"].mean())
df["study_hours"] = df["study_hours"].fillna(df["study_hours"].median())

df["marks"] = df["marks"].clip(lower=0, upper=100)
df["attendance"] = df["attendance"].clip(lower=0, upper=100)
df["study_hours"] = df["study_hours"].clip(lower=0, upper=12)

df["subject"] = df["subject"].str.upper()


def get_result(row):
    if row["marks"] >= 80 and row["attendance"] >= 85 and row["study_hours"] >= 5:
        return "Excellent"
    elif row["marks"] >= 50 and row["attendance"] >= 75:
        return "Good"
    else:
        return "Needs Improvement"


df["result"] = df.apply(get_result, axis=1)

print("Cleaned Data:")
print(df)

print("-" * 40)

print("Data Types After Cleaning:")
print(df.dtypes)

print("-" * 40)

print("Missing Values After Cleaning:")
print(df.isnull().sum())

print("-" * 40)

print("Duplicate Rows After Cleaning:")
print(df.duplicated().sum())

print("-" * 40)

print("Result Counts:")
print(df["result"].value_counts())

print("-" * 40)

print("Subject Counts:")
print(df["subject"].value_counts())

df.to_csv("day5_cleaned_student_dataset.csv", index=False)

print("-" * 40)
print("Cleaned dataset saved as day5_cleaned_student_dataset.csv")
```
---
## 5. Interview Questions:
1. What is data cleaning?
2. Why do we remove duplicates?
3. What does `fillna()` do?
4. What does `drop_duplicates()` do?
5. Why do we use `pd.to_numeric(errors="coerce")`?
6. What does `clip()` do?
7. Why should marks be between 0 and 100?
8. Why do we standardize text columns?
9. Why do we use median for marks?
10. Why do we use `axis=1` in `apply()`?
11. What does `to_csv(index=False)` do?
12. Why is data cleaning important before ML?
---
