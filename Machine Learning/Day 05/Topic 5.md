# Debugging Data-Cleaning Errors
## 1. Most common data-cleaning errors
![[Pasted image 20260604115140.png]]

---
## 2. Error 1 — Wrong column name
Broken code
```Python
df["mark"] = pd.to_numeric(df["mark"], errors="coerce")
```
Error
```
KeyError: 'mark'
```
Root cause
Your actual column is:
```
marks
```
not:
```
mark
```
Fix
```Python
print(df.columns)
df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
```
Always check column names before cleaning.

---
## 3. Error 2 — Finding median before type conversion
Broken code
```Python
df["marks"] = df["marks"].fillna(df["marks"].median())
```
If the column contains:
```
85, "72", "sixty", 91
```
then Pandas may fail because `"sixty"` is text.
Fix
```Python
df["marks"] = pd.to_numeric(df["marks"], errors="coerce")df["marks"] = df["marks"].fillna(df["marks"].median())
```
`pd.to_numeric(errors="coerce")` converts invalid parsing into `NaN`, so values like `"sixty"` become missing values instead of crashing.

---
## 4. Error 3 — Forgetting to save the cleaned result
Broken code
```Python
df.drop_duplicates()
```
This displays or returns a cleaned DataFrame, but your original `df` may remain unchanged.
Fix
```Python
df = df.drop_duplicates()
```
or:
```Python
df.drop_duplicates(inplace=True)
```
`drop_duplicates()` returns a DataFrame with duplicate rows removed.

---
## 5. Error 4 — Using `and` instead of `&`
Broken code
```Python
df = df[(df["marks"] >= 0) and (df["marks"] <= 100)]
```
Error
```
ValueError: The truth value of a Series is ambiguous
```
Fix
```Python
df = df[(df["marks"] >= 0) & (df["marks"] <= 100)]
```
Rule:
```
Use & for ANDUse | for ORUse ~ for NOTUse parentheses around every condition
```
---
## 6. Error 5 — Missing parentheses in conditions
Broken code
```Python
df = df[df["marks"] >= 0 & df["marks"] <= 100]
```
Fix
```Python
df = df[(df["marks"] >= 0) & (df["marks"] <= 100)]
```
Each condition must be inside parentheses.
Correct structure:
```
(condition_1) & (condition_2)
```
---
## 7. Error 6 — Dropping too many rows with `dropna()`
Risky code
```
df = df.dropna()
```
If every row has at least one missing value, this can remove almost the full dataset. Pandas `dropna()` removes missing values, and by default it drops rows containing missing values.
Better approach
```Python
df["name"] = df["name"].fillna("Unknown")
df["subject"] = df["subject"].fillna("Unknown")
df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
df["marks"] = df["marks"].fillna(df["marks"].median())
```
Use `fillna()` when the row is still useful. `fillna()` fills missing values using a value or column-specific mapping.

---
## 8. Error 7 — Clipping before numeric conversion
Broken code
```Python
df["marks"] = df["marks"].clip(lower=0, upper=100)
```
If `marks` contains `"sixty"`, clipping may fail or behave wrongly.
Fix
```Python
df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
df["marks"] =df["marks"].fillna(df["marks"].median())
df["marks"] = df["marks"].clip(lower=0, upper=100)
```
`clip()` trims values outside boundaries to the boundary values, such as `120 → 100` or `-10 → 0`.

---
## 9. Error 8 — Filling text column with mean
Broken code
```Python
df["name"] = df["name"].fillna(df["name"].mean())
```
Error / problem
`name` is a text column, so mean does not make sense.
Fix
```Python
df["name"] = df["name"].fillna("Unknown")
```
For text columns, use a label like:
```Python
UnknownMissingNot Provided
```
---
## 10. Error 9 — Wrong order of cleaning
Bad order
```Python
df["marks"] = df["marks"].fillna(df["marks"].median())
df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
df["marks"] = df["marks"].clip(0, 100)
```
Better order
```Python
df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
df["marks"] = df["marks"].fillna(df["marks"].median())
df["marks"] = df["marks"].clip(lower=0, upper=100)
```
Correct order:
```
Convert type → fill nulls → handle outliers
```
---
## 11. Debugging checklist
Use this every time your cleaning code fails:
```
1. Print df.head()
2. Print df.columns
3. Print df.dtypes
4. Print df.isnull().sum()
5. Print df.duplicated().sum()
6. Convert numeric columns first
7. Fill nulls after conversion
8. Use parentheses in filters
9. Use & instead of and
10. Print cleaned output again
```
Useful debug commands:
```Python
print(df.head())
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())
print(df.duplicated().sum())
```
---
## 12. Interview questions
1. What is the first thing you check when cleaning code fails?
2. What causes `KeyError`?
3. Why should we print `df.columns`?
4. Why should we print `df.dtypes`?
5. Why does `"sixty"` break median calculation?
6. What does `errors="coerce"` do?
7. Why should type conversion happen before `fillna()`?
8. Why should type conversion happen before `clip()`?
9. Why should we assign `df = df.drop_duplicates()`?
10. Why is `df.dropna()` risky?
11. Why do we use `.str.upper()` instead of `.upper()`?
12. Why do we use `&` instead of `and`?
---
