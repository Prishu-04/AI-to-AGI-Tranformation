# Handling Nulls with `dropna()` and `fillna()`
In this slot, we focus only on **missing/null values**. In Pandas, missing values can appear as `NaN`, `None`, or `pd.NA`. Pandas provides tools such as `isna()`/`isnull()` to detect missing values, `dropna()` to remove rows or columns containing missing values, and `fillna()` to replace missing values with usable values.

---
## 1. What is a null value?
A null value means data is missing.
Example:
```
name = None
marks = NaN
attendance = blank
study_hours = missing
```
In ML, missing values are dangerous because many models cannot train directly on missing values.

---
## 2. Dataset for this slot.
```Python
data = {  
"student_id": [101, 102, 103, 104, 105, 106, 107],  
"name": ["Rahul", "Aman", None, "Sneha", "Karan", "Anjali", "Rohit"],  
"marks": [85, None, 45, 91, np.nan, 88, 35],  
"attendance": [90, 80, None, 95, 78, np.nan, 60],  
"study_hours": [5, 4, 3, None, 2, 5, np.nan],  
"subject": ["AI", "Data", "Web", "AI", None, "Data", "Web"]  
}
```
---
![[Pasted image 20260604093749.png]]

---
## 3. Check Null values
![[Pasted image 20260604093853.png]]
This returns `True` where data is missing
To get summary :
![[Pasted image 20260604093941.png]]

---
## 4. `dropna()` - remove missing data
`dropna()` removes missing values from a DataFrame. By default, it drops rows that contain any missing value.
![[Pasted image 20260604094134.png]]
Only Rahul remains because every other row has at least one null.
So `dropna()` is useful, but it can remove too much data.

---
## 5. Drop rows only when specific columns are missing.
Sometimes, some columns are very important. For example, we may decide:
```
name and marks are compulsory
```
Then:
![[Pasted image 20260604094342.png]]
This drops only rows where `name` or `marks` is missing.
Use this when certain columns are mandatory.

---
## 6. `fillna()` - fill missing values
`fillna()` replaces missing values with a chosen value. Pandas docs explain that `fillna()` can use a scalar value or a dictionary-like mapping for column-specific filling.
### Fill text columns
![[Pasted image 20260604094648.png]]
### Fill numeric columns
![[Pasted image 20260604094756.png]]

---
## 7. When to use `dropna()` vs `fillna()`
![[Pasted image 20260604094948.png]]

---
## 8. Common errors
### Error 1: Forgetting to save result
Wrong:
```Python
df["marks"].fillna(df["marks"].median())
```
Correct:
```Python
df["marks"] = df["marks"].fillna(df["marks"].median())
```
---
### Error 2: Filling text with mean
Wrong:
```Python
df["name"] = df["name"].fillna(df["name"].mean())
```
Correct:
```Python
df["name"] = df["name"].fillna("Unknown")
```
---
### Error 3: Dropping too many rows
```Python
df = df.dropna()
```
This may remove most of your dataset.
Better:
```Python
df["marks"] = df["marks"].fillna(df["marks"].median())
```
or:
```Python
df = df.dropna(subset=["name", "marks"])
```
---
## 9. Interview questions
1. What is a null value?
2. What is the difference between `None`, `NaN`, and `pd.NA`?
3. How do you check null values in Pandas?
4. What does `df.isnull().sum()` show?
5. What does `dropna()` do?
6. Why can `dropna()` be risky?
7. What does `fillna()` do?
8. When should you fill with mean?
9. When should you fill with median?
10. How do you fill missing text values?
11. What does `dropna(subset=["marks"])` do?
12. Why should missing values be handled before ML training?
---
