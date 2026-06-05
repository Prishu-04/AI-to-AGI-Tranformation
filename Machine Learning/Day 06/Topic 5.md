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
