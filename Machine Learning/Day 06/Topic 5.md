# Matplotlib Core Plots 
## 1 Core Plots 
There are four Matplotlib plots:
```
1. Line plot
2. Bar chart
3. Scatter plot
4. Histogram
```
Each plot answers a different question. Matplotlib’s `plot()` draws lines and markers, `bar()` creates bar plots, `scatter()` displays relationships between two variables, and `hist()` divides numerical data into bins to show its distribution.
![[Pasted image 20260605113740.png]]

---
## 2. Dataset
```Python
import pandas as pd
import matplotlib.pyplot as plt


data = {
    "student_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "name": [
        "Rahul", "Aman", "Priya", "Sneha",
        "Karan", "Anjali", "Rohit", "Neha"
    ],
    "marks": [85, 72, 45, 91, 60, 88, 35, 67],
    "attendance": [90, 80, 70, 95, 78, 92, 60, 82],
    "study_hours": [5, 4, 3, 6, 2, 5, 1, 4],
    "subject": ["AI", "DATA", "AI", "AI", "DATA", "DATA", "WEB", "WEB"],
    "result": [
        "Excellent", "Good", "Needs Improvement", "Excellent",
        "Good", "Excellent", "Needs Improvement", "Good"
    ]
}

df1 = pd.DataFrame(data)

print(df1)
```
---
## 3. Line Plot
![[Pasted image 20260605114451.png]]
![[Pasted image 20260605114504.png]]

----
## 4. Bar Chart
A bar chart compares numerical values across categories. Matplotlib’s `bar()` positions bars using the x-category values and uses the supplied height values to determine each bar’s size.
![[Pasted image 20260605114621.png]]
### Why `plt.bar_label()` is useful
```Python
plt.bar_label(bars)
```
It displays the marks value above each bar, making comparison easier. Matplotlib provides `bar_label()` specifically for labeling bar-chart values.
### Observation
From this chart:
```
Highest marks: Sneha — 91
Lowest marks: Rohit — 35
```
---
## 5. Bar Charts for Categorical Counts
![[Pasted image 20260605114859.png]]
Now create the chart :
![[Pasted image 20260605114959.png]]
`plt.tight_layout()` a built-in function used to automatically adjust subplot parameters so that your plots fit cleanly within the figure are

---
## 6. Scatter Plot
A scatter plot displays individual points using one numeric column on the x-axis and another on the y-axis. Matplotlib defines `scatter()` as a plot of y versus x that can also vary marker size or color.
Use it to study the relationship between study hours and marks:
![[Pasted image 20260605115414.png]]
Interpretation:
Look at the direction of points:
```
Points moving upward from left to right:
Possible positive relationship

Points moving downward:
Possible negative relationship

Points spread randomly:
Weak or no visible relationship
```
In this dataset, students with more study hours generally have higher marks. However, a visual relationship alone does not prove that one feature causes the other.

---
## 7. Add Student names to scatter plot
![[Pasted image 20260605115619.png]]
![[Pasted image 20260605115629.png]]
Here:

```
df.iterrows() → visits every DataFrame row
plt.annotate() → writes the student name near its point
```
---
## 8. Histogram
A histogram shows how frequently numeric values fall into different ranges. Matplotlib’s `hist()` calculates bins, counts how many values fall inside each bin, and then draws the distribution.
![[Pasted image 20260605115912.png]]
What does `bins=5` mean?
```
The complete marks range is divided into five intervals.
Each bar shows how many students fall inside that interval.
```
Changing the number of bins can change how the distribution appears, so bins should be selected carefully.

---
## 9. Histogram for Attendance
![[Pasted image 20260605120104.png]]
Uss this to identify:
```
Common attendance range
Low-attendance students
Possible attendance outliers
```
---
## 10 Interview Questions:
1. What is the difference between a line plot and a bar chart?
2. When should you use a scatter plot?
3. What does a histogram show?
4. What does `bins` mean in a histogram?
5. What does `plt.bar()` do?
6. What does `plt.scatter()` do?
7. What does `plt.hist()` do?
8. What does `plt.bar_label()` do?
9. Why do we use `plt.xticks(rotation=45)`?
10. Why should `plt.savefig()` usually come before `plt.show()`?
11. Which chart would you use to compare departments?
12. Which chart would you use to examine the relationship between salary and experience?
---
## 11. Assignment
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
```
Task:
```
1. Bar chart: employee name vs salary
2. Bar chart: employee count by department
3. Scatter plot: experience vs salary
4. Scatter plot: rating vs salary
5. Histogram: salary distribution
6. Histogram: experience distribution
```