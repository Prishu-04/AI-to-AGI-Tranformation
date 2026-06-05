# Matplotlib Basics
## 1. What is Matplotlib?
Matplotlib is a Python visualization library used to create static, animated, and interactive plots, and `pyplot` is commonly used for simple plotting tasks like creating figures, plotting lines, and adding titles/labels.

---
## 2. Import Libraries
![[Pasted image 20260605110901.png]]

---
## 3. Dataset
![[Pasted image 20260605111013.png]]
![[Pasted image 20260605110958.png]]

---
## 4. Matplotlib Plot - Marks by Student
![[Pasted image 20260605111343.png]]
Menaing:
```
plt.figure()      → creates figure size
plt.plot()        → creates line plot
plt.title()       → adds chart title
plt.xlabel()      → adds x-axis label
plt.ylabel()      → adds y-axis label
plt.grid(True)    → adds grid lines
plt.show()        → displays chart
```
---
## 5. Improve the Plot with markers
![[Pasted image 20260605111628.png]]

---
## 6. Add Attendance Line
![[Pasted image 20260605111925.png]]
Meaning :
```
label="Marks"        → name of first line
label="Attendance"   → name of second line
plt.legend()         → shows label box
```
---
## 7. Save Plot as image 
![[Pasted image 20260605112348.png]]

---
## 8. Interview Questions
1. What is visual EDA?
2. Why do we use charts before ML?
3. What is Matplotlib?
4. Why do we import `matplotlib.pyplot as plt`?
5. What does `plt.figure(figsize=(8, 5))` do?
6. What does `plt.plot()` do?
7. What does `plt.title()` do?
8. What does `plt.xlabel()` and `plt.ylabel()` do?
9. What does `plt.grid(True)` do?
10. What does `plt.legend()` do?
11. What does `plt.savefig()` do?
12. Why should we check missing values before plotting?
---
## 9. Assignment
Tasks:
```
1. Use student names on x-axis
2. Plot marks
3. Plot study_hours
4. Add title
5. Add x-axis label
6. Add y-axis label
7. Add legend
8. Add grid
9. Save as day6_study_hours_marks_plot.png
```
---
