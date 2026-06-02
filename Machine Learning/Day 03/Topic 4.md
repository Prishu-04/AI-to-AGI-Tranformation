# Build NumPy-Based Student Analytics
## 1. Project Goal
We will build:
```
day3_numpy_student_analytics.py
```
It will analyze student data using NumPy.
Dataset columns:
```
marks, attendance, study_hours
```
The program will calculate:
```
1. Average marks
2. Highest marks
3. Lowest marks
4. Average attendance
5. Average study hours
6. Scaled feature values
7. Weighted performance score
8. Student categories
9. Category counts
```
---
## 2. Dataset
```Python
import numpy as np
students = np.array([    
	[85, 90, 5],
    [72, 80, 4],
    [45, 70, 3],
    [91, 95, 6],
    [60, 78, 2],
    [88, 92, 5],
    [35, 60, 1]
])
```
Meaning:
![[Pasted image 20260602160006.png]]

---
## Complete Code
```Python
import numpy as np


students = np.array([
    [85, 90, 5],
    [72, 80, 4],
    [45, 70, 3],
    [91, 95, 6],
    [60, 78, 2],
    [88, 92, 5],
    [35, 60, 1]
])

marks = students[:, 0]
attendance = students[:, 1]
study_hours = students[:, 2]

print("Student Dataset:")
print(students)

print("-" * 40)

print("Basic Analytics")
print("Average marks:", np.mean(marks))
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Average attendance:", np.mean(attendance))
print("Average study hours:", np.mean(study_hours))

print("-" * 40)

scale_values = np.array([100, 100, 10])
scaled_students = students / scale_values

print("Scaled Dataset:")
print(scaled_students)

print("-" * 40)

weights = np.array([0.5, 0.3, 0.2])
weighted_scores = scaled_students * weights
final_scores = np.sum(weighted_scores, axis=1)

print("Final Performance Scores:")
print(final_scores)

print("-" * 40)

excellent_mask = final_scores >= 0.75
good_mask = (final_scores >= 0.55) & (final_scores < 0.75)
needs_improvement_mask = final_scores < 0.55

excellent_students = students[excellent_mask]
good_students = students[good_mask]
needs_improvement_students = students[needs_improvement_mask]

print("Excellent Students:")
print(excellent_students)

print("Good Students:")
print(good_students)

print("Needs Improvement Students:")
print(needs_improvement_students)

print("-" * 40)

print("Category Counts")
print("Excellent:", len(excellent_students))
print("Good:", len(good_students))
print("Needs Improvement:", len(needs_improvement_students))
```
---
## 2. Interview Questions:
- Why do we extract columns before analytics?
- What does `np.mean()` do?
- What does `axis=1` mean?
- Why do we scale features?
- Why are weights used?
- What is a final performance score?
- What is a boolean mask?
- How do we count filtered rows?
- Why should we use NumPy instead of loops?
- What does `np.savetxt()` do?
---
