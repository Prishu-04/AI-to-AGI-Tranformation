# Debugging Pandas Errors
## 1. Most common Pandas errors
![[Pasted image 20260603113314.png]]

---
## 2. Error 1 — `NameError: pd is not defined`
Wrong:
```Python
df = pd.DataFrame(data)
```
Error:
```
NameError: name 'pd' is not defined
```
Correct:
```Python
import pandas as pd
df = pd.DataFrame(data)
```
Root cause:
```
You used pd before importing Pandas.
```
---
## 3. Error 2 — `KeyError`
Dataset:
```Python
import pandas as pd
data = {    
	"name": ["Amit", "Riya", "Karan"],    
	"salary": [25000, 45000, 80000],    
	"experience": [1, 3, 6],    
	"rating": [3, 4, 5]}df = pd.DataFrame(data)
```
Wrong:
```Python
print(df["score"])
```
Error:
```
KeyError: 'score'
```
Root cause:
```
There is no column named score.
```
Correct:
```Python
print(df["salary"])
```
Debugging trick:
```Python
print(df.columns)
```
Use this whenever you get `KeyError`.

---
## 4. Error 3 — Wrong multiple-column selection
Wrong:
```Python
print(df["name", "salary"])
```
Possible error:
```
KeyError: ('name', 'salary')
```
Correct:
```Python
print(df[["name", "salary"]])
```
Remember:
```
One column  → df["salary"]
Many columns → df[["name", "salary"]]
```
---
## 5. Error 4 — Using `and` instead of `&`
Wrong:
```Python
senior = df[(df["salary"] >= 70000) and (df["experience"] >= 5)]
```
Possible error:
```
ValueError: The truth value of a Series is ambiguous
```
Correct:
```python
senior = df[(df["salary"] >= 70000) & (df["experience"] >= 5)]
```
Rule:
```
Use & for ANDUse | for ORUse ~ for NOTUse parentheses around every condition
```
Pandas `.loc` and boolean arrays are designed for boolean row selection, so this syntax becomes very important for filtering.

---
## 6. Error 5 — Missing parentheses in conditions
Wrong:
```Python
senior = df[df["salary"] >= 70000 & df["experience"] >= 5]
```
Correct:
```Python
senior = df[(df["salary"] >= 70000) & (df["experience"] >= 5)]
```
Always wrap every condition:
```
(df["salary"] >= 70000)(df["experience"] >= 5)
```
Then combine them using `&`.

---
## 7. Error 6 — `FileNotFoundError`
Wrong:
```Python
df = pd.read_csv("employee_data.csv")
```
Error:
```
FileNotFoundError: No such file or directory
```
Root cause:
```
The file is not in the current folder, or the file name/path is wrong.
```
Correct options:
```Python
df = pd.read_csv("employees.csv")
```
or:
```Python
df = pd.read_csv("data/employees.csv")
```
`pd.read_csv()` reads a CSV file into a DataFrame, so the file path must point to an actual existing file.
Debug:
```Python
import osprint(os.getcwd())print(os.listdir())
```
This tells you your current folder and files.

---
## 8. Error 7 — Wrong `axis` in `apply()`
Wrong:
```Python
def get_level(row):
   if row["experience"] >= 5 and row["salary"] >= 70000:
	   return "Senior" 
   elif row["experience"] >= 2 and row["salary"] >= 40000:
	   return "Mid-Level"
	else:
        return "Junior"df["level"] = df.apply(get_level)
```
Possible error:
```
KeyError: 'experience'
```
Correct:
```Python
df["level"] = df.apply(get_level, axis=1)
```
Why?
```
axis=1 applies the function row by row.
```
Pandas `DataFrame.apply()` applies a function along an axis of the DataFrame; 
the objects passed to the function depend on whether the axis is index-wise or column-wise.

---
## 9. Error 8 — Different column lengths
Wrong:
```Python
data = {
	"name": ["Amit", "Riya", "Karan"],
    "salary": [25000, 45000]}df = pd.DataFrame(data)
```
Error:
```
ValueError: All arrays must be of the same length
```
Correct:
```Python
data = {    "name": ["Amit", "Riya", "Karan"],    "salary": [25000, 45000, 80000]}df = pd.DataFrame(data)
```

Every column must have the same number of values.

---
## 10. Error 9 — Data type issue
Wrong:
```Python
df["salary"] = ["25000", "45000", "80000"]print(df["salary"].mean())
```
Problem:
```
Salary values are strings, not numbers.
```
Correct:
```Python
df["salary"] = df["salary"].astype(int)
print(df["salary"].mean())
```
Debug:
```Python
print(df.dtypes)
```
Use `df.dtypes` to check whether numeric columns are actually numeric.

---
## 11. Error 10 — Logical bug: filtering before creating column
Wrong:
```Python
senior = df[df["level"] == "Senior"]
df["level"] = df.apply(get_level, axis=1)
```
Problem:
```
You are filtering level before creating level.
```
Correct:
```Python
df["level"] = df.apply(get_level, axis=1)
senior = df[df["level"] == "Senior"]
```
This is a logical bug because the order of code matters.

---
## 12. Debugging checklist
Use this every time:
```
1. Print df.head()
2. Print df.columns
3. Print df.shape
4. Print df.dtypes
5. Print df.info()
6. Check spelling of column names
7. Check parentheses in filters
8. Use & instead of and
9. Check file path if using read_csv()
10. Check axis=1 when applying row-wise logic
```
---
## 13. Interview questions
1. What causes `KeyError` in Pandas?
2. How do you check all column names?
3. Why do we use `&` instead of `and`?
4. Why are parentheses required in multiple Pandas conditions?
5. What causes `FileNotFoundError`?
6. What does `df.dtypes` help debug?
7. Why is `axis=1` needed in `df.apply()`?
8. What is the correct syntax for selecting multiple columns?
9. What is a logical bug in Pandas?
10. What is your first debugging step when a Pandas filter fails?
---
