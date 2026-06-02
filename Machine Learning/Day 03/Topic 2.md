# NumPy Indexing, Slicing, Shape & Reshape and Filtering
## 1. What is Indexing?
Indexing means accessing a specific element from an array.
![[Pasted image 20260529151316.png]]

---
## 2. Negative Indexing
Negative indexing starts from the end.
![[Pasted image 20260529151249.png]]

---
## 3. Slicing in NumPy
Slicing means taking a part of an array.
### Syntax:
```Python
array[start:end]
```
Note :
```
start is included
end is excluded
```
Example:
![[Pasted image 20260529151610.png]]
Because index `1` to `3` is printed.

---
## 4. Common Slicing Examples
![[Pasted image 20260529151751.png]]
Meaning:
```
arr[:3]  = from start to index 2
arr[2:]  = from index 2 to end
arr[:]   = full array
arr[::2] = every second element
```
---
## 5. Indexing in 2D Array
A 2D array has rows and columns.
![[Pasted image 20260529151959.png]]
Structures:
```
[
  [85, 90, 78],   row 0
  [70, 88, 92],   row 1
  [60, 75, 80]    row 2
]
```
### Accessing the value:
![[Pasted image 20260529152121.png]]
Better Way
```Python
print(dataset[0, 1])
print(dataset[1, 2])
print(dataset[2, 0])
```
---
## 6. Slicing Rows in 2D Array
![[Pasted image 20260529152330.png]]

---
## 7. Slicing Columns in 2D Array
![[Pasted image 20260529152703.png]]
Meaning
```
dataset[:, 0] = all rows, column 0
dataset[:, 1] = all rows, column 1
dataset[:, 2] = all rows, column 2
```
---
## 8. Slicing Multiple Rows and Columns
![[Pasted image 20260529153217.png]]

---
## 9. AI/ML Use Case: features and Labels
In ML Datasets:
```
X = features/input
y = label/output
```
Example:
![[Pasted image 20260529153434.png]]

---
## 10. Shape
Shape tells the structure of the array.
Example:
![[Pasted image 20260529153602.png]]
Meaning:
```
2 rows
3 columns
```
---
## 11. Reshape
Reshape means changing the structure of an array.
Example:
![[Pasted image 20260529153835.png]]
Meaning :
```
Original: 1D array with 6 elements
New shape: 2 rows and 3 columns
```
---
## 12. More Reshape Examples
![[Pasted image 20260529154010.png]]

---
## 13. Flattening Array
![[Pasted image 20260529154136.png]]

---
## 14. AI/ML Use Case of Reshape
Images are often stored as arrays.
Example:
```
28 x 28 image = 784 pixels
```
In ML, Sometimes we convert:
```
28 x 28 → 784
```
![[Pasted image 20260529154444.png]]
For model input, we may flatten it:
![[Pasted image 20260529154519.png]]

---
## 15. Common Errors and Corrections
### Error 1: Index out of Range
![[Pasted image 20260529154753.png]]
Correct:
```Python
arr = np.array([10, 20, 30])  
print(arr[2])
```
---
### Error 2: Wrong 2D Index
![[Pasted image 20260529154959.png]]
Correct:
```Python
dataset = np.array([  
[85, 90, 78],  
[70, 88, 92]  
])  
print(dataset[1, 1])
```
---
### Error 3: Invalid Reshape
![[Pasted image 20260529155123.png]]
Why?
```
Original elements = 6
New shape needs = 4 × 2 = 8 elements
```
Correct:
```Python
arr = np.array([1, 2, 3, 4, 5, 6])  
new_arr = arr.reshape(2, 3)  
print(new_arr)
```
---
## 16. Practice Tasks
## Task 1
Create this array:
```
arr = np.array([10, 20, 30, 40, 50, 60])
```
Print:
```
First element.
Last element
Elements from index 1 to 4
Every second element
```
---
## Task 2
Create this 2D dataset:
```
dataset = np.array([    
	[85, 90, 78],
    [70, 88, 92],
    [60, 75, 80]
])
```
Print:
```
First row
Second row
Value 88
Value 80
First column
Second column
```
---
## Task 3
Create this ML dataset:
```
data = np.array([    
	[85, 90, 78, 1],
    [70, 88, 92, 1],
    [35, 40, 45, 0],
    [95, 92, 88, 1]
])
```
Separate:
```
X = first 3 columns
y = last column
```
Print both.

---
## Task 4
Create array from 1 to 12.
Convert it into:
```
3 rows and 4 columns
2 rows and 6 columns
```
---
## Task 5
Create a 2D array and flatten it into 1D.

---
## 17. Slot 5 Final Mini Code
```Python
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

print("First Element:", arr[0])
print("Last Element:", arr[-1])
print("Index 1 to 4:", arr[1:5])
print("Every Second Element:", arr[::2])


dataset = np.array([
    [85, 90, 78],
    [70, 88, 92],
    [60, 75, 80]
])

print("First Row:", dataset[0])
print("Second Row:", dataset[1])
print("Value 88:", dataset[1, 1])
print("Value 80:", dataset[2, 2])
print("First Column:", dataset[:, 0])
print("Second Column:", dataset[:, 1])


data = np.array([
    [85, 90, 78, 1],
    [70, 88, 92, 1],
    [35, 40, 45, 0],
    [95, 92, 88, 1]
])

X = data[:, 0:3]
y = data[:, 3]

print("Features X:")
print(X)

print("Labels y:")
print(y)


numbers = np.arange(1, 13)

reshape_3_4 = numbers.reshape(3, 4)
reshape_2_6 = numbers.reshape(2, 6)

print("Original Numbers:", numbers)
print("Reshape 3x4:")
print(reshape_3_4)

print("Reshape 2x6:")
print(reshape_2_6)


flat_array = reshape_3_4.flatten()

print("Flattened Array:", flat_array)
```
---
## 17. Boolean Filtering
Boolean filtering means selecting data based on a conditions.
Example: find students with marks greater than or equal to 80.
![[Pasted image 20260602143251.png]]

---
## 18. Filtering Multiple Conditions
Find students with:
```
marks >= 80
attendance >= 85
```
![[Pasted image 20260602143438.png]]
Remember : when there are multiple conditons then use brackets for that.

---
## 19. Interview Questions
1. What is indexing in NumPy?
2. What is slicing?
3. What does `students[0]` return?
4. What does `students[0, 1]` return?
5. What does `students[:, 0]` mean?
6. What does `students[0:3]` mean?
7. What is boolean filtering?
8. What is a mask?
9. Why do we use `&` instead of `and` in NumPy?
10. Why do we use parentheses around NumPy conditions?

---
