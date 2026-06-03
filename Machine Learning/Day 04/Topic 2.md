# Reading CSV Files + Dataset Exploration
## 1. What is a CSV File?
CSV means **Comma Separated Values**.
It stores data in table format.
Example:
```
Name,Math,Science,English
Pratyaksh,85,88,78
Rahul,70,75,80
Sneha,90,95,92
```
In AI/ML, most beginner datasets are available in CSV format.
Examples:
```
student_performance.csv
titanic.csv
iris.csv
house_price.csv
sales_data.csv
```
---
## 2. Why CSV Files are important in AI/ML?
In AI/ML, CSV files are used to store:
```
Training data
Testing data
Student records
Sales data
Medical data
Customer data
Model output data
```
Basic Flow:
```
CSV File → Pandas DataFrame → Data Cleaning → ML Model
```
---
## 3. Create a CSV File.
create this file :
```
student_performance.csv
```
Data:
```csv
Student_ID,Name,Math,Science,English,Attendance,Study_Hours
1,Pratyaksh,85,88,78,92,5
2,Rahul,70,75,80,85,3
3,Sneha,90,95,92,96,6
4,Aman,95,92,88,90,7
5,Priya,60,75,80,80,4
6,Rohit,45,55,50,70,2
7,Neha,88,84,90,94,5
8,Karan,35,40,45,60,1
```
---
## 4. Reading CSV File using Pandas
![[Pasted image 20260601104741.png]]

---
## 5. `read_csv()`
`read_csv()` is used to load CSV data into a Pandas DataFrame.
```Python
df = pd.read_csv("student_performance.csv")
```
Here:
```
student_performance.csv = file name
df = DataFrame variable
```
---
## 6. Dataset Exploration
Dataset exploration means checking the dataset before using it.
Before applying AI/ML, always check:
```
How many rows and columns are there?
What are the column names?
What are the first few records?
What are the last few records?
What are the data types?
Are there missing values?
What is the basic statistical summary?
```
---
## 7. Display First Rows using `head()`
![[Pasted image 20260601105036.png]]

---
## 8. Display Last Rows using `tail()`
![[Pasted image 20260601105134.png]]

---
## 9. Checking Shape
![[Pasted image 20260601105405.png]]

---
## 10. Checking Columns
![[Pasted image 20260601105700.png]]
To print clean columns:
![[Pasted image 20260601105753.png]]

---
## 11. Checking Dataset Information using `ìnfo()`
![[Pasted image 20260601105929.png]]

---
## 12. Checking Statistical Summary using `describe()`
![[Pasted image 20260601110057.png]]

---
## 13. Checking Data types:
![[Pasted image 20260601110217.png]]

---
## 14. Checking Missing Values
Missing values mean some cells are empty.
![[Pasted image 20260601110358.png]]

![[Pasted image 20260601110426.png]]

---
## 15. Creating Total and Average Columns
![[Pasted image 20260601110659.png]] 

---
## 16. Save updated DataFrame to CSV
![[Pasted image 20260601110808.png]]

![[Pasted image 20260601110912.png]]

---
## 17. Common Errors and Corrections:
### Error 1: File Not Found
![[Pasted image 20260601111326.png]]
Correct code:
```Python
df = pd.read_csv("student_performance.csv")
```
---
### Error 2: Pandas Not Imported
```Python
df = pd.read_csv("student_performance.csv")
```
Error :
```
NameError: name 'pd' is not defined
```
Correct:
```Python
import pandas as pd
df = pd.read_csv("student_performance.csv")
```
---
### Error 3: Wrong Column name
![[Pasted image 20260601111606.png]]
Correct :
Column name are case sensitive.
```Python
df["Math"]
```
---
### Error 4: Saving Index By Mistake
Code
```Python
df.to_csv("updated.csv")
```
This saves an extra index column.
Better Code
```Python
df.to_csv("updated.csv", index=False)
```
---
### Error 5: CSV File Has Extra Spaces in Column Names
Sometimes CSV columns may look like:
```
 Name Math Science
```
Correct:
```Python
df.columns = df.columns.str.strip()
```
This removes extra spaces from column names.

---
## 18. Practice tasks
## Task 1
Create a CSV file named:
```
student_performance.csv
```
Add the dataset given above.

---
## Task 2
Read the CSV file using Pandas and print the full DataFrame.

---
## Task 3
	Print:
```
First 5 rows
First 3 rows
Last 5 rows
Last 3 rows
Shape
Columns
Data types
```

---
## Task 4
Use:
```
df.info()
df.describe()
df.isnull().sum()
```

---
## Task 5
Create new columns:
```
Total
Average
```
Then save the updated dataset as:
```
student_performance_updated.csv
```
---
## 19. Slot 2 Final Code
```Python
import pandas as pd

df = pd.read_csv("student_performance.csv")

print("========== Full Dataset ==========")
print(df)

print("\n========== First 5 Rows ==========")
print(df.head())

print("\n========== First 3 Rows ==========")
print(df.head(3))

print("\n========== Last 5 Rows ==========")
print(df.tail())

print("\n========== Last 3 Rows ==========")
print(df.tail(3))

print("\n========== Dataset Shape ==========")
print(df.shape)

print("\n========== Columns ==========")
print(list(df.columns))

print("\n========== Data Types ==========")
print(df.dtypes)

print("\n========== Dataset Info ==========")
print(df.info())

print("\n========== Statistical Summary ==========")
print(df.describe())

print("\n========== Missing Values ==========")
print(df.isnull().sum())

df["Total"] = df["Math"] + df["Science"] + df["English"]

df["Average"] = df["Total"] / 3
df["Average"] = df["Average"].round(2)

print("\n========== Updated Dataset ==========")
print(df)

df.to_csv("student_performance_updated.csv", index=False)

print("\nUpdated dataset saved as student_performance_updated.csv")
```
---
