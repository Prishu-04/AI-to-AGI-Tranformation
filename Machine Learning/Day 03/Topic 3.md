# Vectorized Operations and Broadcasting
## 1. Why Vectorization Matters?
Without NumPy:
![[Pasted image 20260602145739.png]]
With Numpy:
![[Pasted image 20260602145830.png]]

---
## 2. Element wise arithmetic
![[Pasted image 20260602145934.png]]

---
## 3. Vectorized operations on 2D dataset
Dataset:
![[Pasted image 20260602150149.png]]
Columns:
```
0 = marks  
1 = attendance  
2 = study_hours
```
Scale the full dataset:
![[Pasted image 20260602150233.png]]

---
## 5. Column-wise Scaling
![[Pasted image 20260602150459.png]]
AI/Ml meaning;
```
marks and attendance are percentages, so divide by 100
study_hours may be around 0–10, so divide by 10
```
---
## 6. Broadcasting basics
Broadcasting means NumPy automatically applies a smaller value or array across a bigger array.
Example:
![[Pasted image 20260602150715.png]]
Here, `5` is broadcast to every element.
Conceptually:
```
[85, 72, 45, 91, 60] + 5
becomes
[85, 72, 45, 91, 60] + [5, 5, 5, 5, 5]
```
NumPy’s beginner guide explains broadcasting as a mechanism that lets NumPy perform operations on arrays with different shapes when the dimensions are compatible.

---
## Broadcasting with 2D array with 1D array
Suppose:
![[Pasted image 20260602150914.png]]
Shape check:
![[Pasted image 20260602151057.png]]
Meaning:
```
students has 5 rows and 3 columns
scale_values has 3 values
NumPy applies those 3 values to each row
```
---
## 7. Add weights to features.
In ML, every feature can have different importance:
![[Pasted image 20260602151303.png]]
Each column got multiplied by its own weight:
```
marks × 0.5
attendance × 0.3
study_hours × 0.2
```

---
## 8. Calculate final score
![[Pasted image 20260602151445.png]]
Meaning:
```
axis=1 means row-wise sum
one final score for each student
```
![[Pasted image 20260602151528.png]]

---
## 9. Common Errors
### Error 1: Shape Mismatch
![[Pasted image 20260602151932.png]]
Reason:
```
students shape = (2, 3)
scale_values shape = (2,)
```
Fix:
```Python
scale_values = np.array([100, 100, 10])
```
---
### Error 2: Wrong Axis
```Python
np.sum(weighted_scores, axis=0)
```
This gives column-wise sum.
```Python
np.sum(weighted_scores, axis=1)
```
This gives row-wise sum.
For our final student scores, we need:
```Python
final_scores = np.sum(weighted_scores, axis=1)
```
---
### Error 3: Using List instead of NumPy array
![[Pasted image 20260602152419.png]]
Fix:
```python
marks = np.array([85, 72, 45])  
print(marks / 100)
```
---
## 10. Interview Questions
- What is vectorization?
- What is broadcasting?
- Why is NumPy faster than manual Python loops?
- What is element-wise operation?
- What does `students / scale_values` do?
- What does `axis=1` mean?
- What does `axis=0` mean?
- Why do we scale features?
- Why do different columns need different scale values?
- What causes a broadcasting `ValueError`?
---
## 11. Assignment
Use this employee dataset:
```python
import numpy as np
employees = np.array([    
	[25000, 1, 3],
    [45000, 3, 4],
    [80000, 6, 5],
    [120000, 8, 5],
    [35000, 2, 2]
])
```
Columns:
```
salary, experience, rating
```
Tasks:
```
1. Scale salary by 100000
2. Scale experience by 10
3. Scale rating by 5
4. Use weights: salary = 0.4, experience = 0.3, rating = 0.3
5. Calculate final employee score
6. Print top performers where final score >= 0.75
7. Print average employee score
```
---
