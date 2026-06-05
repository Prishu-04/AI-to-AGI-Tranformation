# Seaborn Basics
## 1. Import Library
```Python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
Dataset:
```Python
data = {
    "employee_id": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110,
        111, 112, 113, 114, 115
    ],

    "name": [
        "Amit", "Riya", "Karan", "Neha", "Vikas",
        "Anjali", "Rohit", "Priya", "Rahul", "Sneha",
        "Arjun", "Meera", "Dev", "Pooja", "Varun"
    ],

    "salary": [
        28000, 45000, 80000, 120000, 36000,
        70000, 30000, 95000, 55000, 42000,
        65000, 105000, 50000, 75000, 33000
    ],

    "experience": [
        1, 3, 6, 9, 2,
        5, 1, 7, 4, 2,
        5, 8, 3, 6, 2
    ],

    "rating": [
        3, 4, 5, 5, 2,
        4, 3, 5, 4, 3,
        4, 5, 4, 4, 3
    ],

    "department": [
        "HR", "IT", "AI", "AI", "SALES",
        "DATA", "IT", "DATA", "WEB", "HR",
        "WEB", "AI", "DATA", "IT", "SALES"
    ],

    "level": [
        "Junior", "Mid-Level", "Senior", "Senior", "Junior",
        "Senior", "Junior", "Senior", "Mid-Level", "Mid-Level",
        "Mid-Level", "Senior", "Mid-Level", "Senior", "Junior"
    ]
}

df = pd.DataFrame(data)

print(df)
```
---
## 2. Count Plot
A count plot displays the number of observations in each categorical group using bars. Use it for columns such as department, level, result, or category.
### Employee Count by Department
![[Pasted image 20260605130520.png]]
### Count Plot Using `hue`
`hue` divides each category using another categorical column.
![[Pasted image 20260605130629.png]]
This helps answer:
```
Which departments contain Senior employees?
How are employee levels distributed across departments?
```
---
## 3. Histogram with `histplot()`
A histogram shows the distribution of numerical data by dividing values into intervals called bins. Seaborn’s `histplot()` can display univariate or bivariate distributions.
### Salary Distribution
![[Pasted image 20260605130841.png]]
### Histogram with KDE
![[Pasted image 20260605131116.png]]
`kde=True` adds a smooth estimated distribution curve. KDE represents observations using a continuous probability-density curve.

---
## 4. Box Plot
A box plot displays the distribution of quantitative values across categories. It helps compare the median, spread, quartiles, and possible outlier points.
### Salary Distribution by Department
![[Pasted image 20260605131311.png]]
### Salary Distribution by Employee Level
![[Pasted image 20260605131620.png]]

---
## 5. Scatter Plot
A scatter plot helps examine the relationship between two numeric columns. Seaborn’s `scatterplot()` can also separate observations using `hue`, `size`, and `style`.
![[Pasted image 20260605131801.png]]
### Using `hue` and `size`
![[Pasted image 20260605131854.png]]
Here:
```
x-axis     → experience
y-axis     → salary
hue        → employee level
point size → rating
```
---
## 6. Correlation Heatmap
A heatmap displays rectangular data as a color-encoded matrix. When a Pandas DataFrame is used, Seaborn uses its column and index information as labels.
First, select numeric columns and calculate correlation:
![[Pasted image 20260605132107.png]]
Create Heatmap:
![[Pasted image 20260605132054.png]]
`annot=True` writes the correlation values inside the heatmap cells.
Understanding Correlation
```
Close to +1 → strong positive relationship
Close to 0  → weak linear relationship
Close to -1 → strong negative relationship
```
---
## 7. Interview Questions:
- What is Seaborn?
- How is Seaborn related to Matplotlib?
- What does `countplot()` show?
- What does `histplot()` show?
- What does `kde=True` do?
- What information does a box plot provide?
- How does a box plot help identify possible outliers?
- What does `hue` do?
- What does `size` do in a scatter plot?
- What does a heatmap show?
- What does `annot=True` do?
- Why should correlation use numeric columns?
- What is the difference between correlation and causation?
- When should you use `countplot()` instead of `histplot()`?
---
## 8. Assignment
Using the employee dataset, create and save:
```
1. Count plot for employee levels
2. Department count plot using level as hue
3. Experience histogram with KDE
4. Salary box plot by employee level
5. Rating box plot by department
6. Experience vs salary scatter plot using department as hue
7. Correlation heatmap for salary, experience, and rating
```
---
