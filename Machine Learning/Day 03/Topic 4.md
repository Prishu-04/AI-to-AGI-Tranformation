# NumPy Introduction + Arrays
## What is NumPy?
NumPy stands for Numerical python.
It is a Python library used for working with numerical data, arrays, matrices and mathematical operations.
In AI/ML , NumPy is very important because datasets are usually handles as arrays.

---
## 2. Why NumPy is Important in AI/ML?
NumPy is used for :
```
Dataset storage
Matrix operations
Image data representation
Feature vectors
Mathematical calculations
Data preprocessing
Model input preparation
```
Example:
![[Pasted image 20260529141123.png]]
In ML, this is usually converted into a NumPy array:
![[Pasted image 20260529141147.png]]

---
## 3. Installation of NumPy
Run this in terminal :
```Bash
pip install numpy
```
To check installation:
![[Pasted image 20260529141411.png]]

---
## 4. Creating NumPy Array
![[Pasted image 20260529141518.png]]

---
## 5. Difference between NumPy Array and Python List
Python list repeats the values.  
![[Pasted image 20260529141733.png]]
NumPy array performs mathematical operation on each value.
![[Pasted image 20260529141810.png]]

---
## 6. Creating 2D Array
A **2D array** is like a table.
![[Pasted image 20260529142205.png]]
AI/ML Meaning
```
Each row = one student / one data sample
Each column = one feature
```
---
## 7. Creation of 3D Array
A **3D array** is commonly used for images.
![[Pasted image 20260529142440.png]]
Meaning :
```
Height = 2
Width = 2
Channels = 3
```
----
## 8. Checking Array Dimensions
![[Pasted image 20260529142645.png]]

---
## 9. Checking Shape
Shape tells the structure of the array.
![[Pasted image 20260529142758.png]]

---
## 10. Checking Size
Size tells the total number of elements.
![[Pasted image 20260529142925.png]]

---
## 11. Checking Data Type
![[Pasted image 20260529143055.png]]

---
## 12. Creating Special Arrays
### Array of Zeros
![[Pasted image 20260529143243.png]]

---
### Arrays of Ones
![[Pasted image 20260529143335.png]]

---
### 2D Zeros Array
![[Pasted image 20260529143452.png]]

----
### Range Array
![[Pasted image 20260529143557.png]]

---
### Range with Step
![[Pasted image 20260529143817.png]]

---
## 13. Basic Mathematical Operations
![[Pasted image 20260529144005.png]]

---
## 14. AI/ML Example: Normalize Marks
Normalization means converting values into a smaller range.
![[Pasted image 20260529144229.png]]

---
## 15. Common Errors and Corrections
### Errors 1: NumPy not Installed
```Python
import numpy as np
```
Error
```
ModuleNotFoundError: No module named 'numpy'
```
Correct:
Run:
```Bash
pip install numpy
```
---
### Error 2: Forgetting `np`
```Python
arr = array([1, 2, 3])
```
Error:
```
NameError: name 'array' is not defined
```
Correct :
```Python
arr=np.array([1,2,3])
```
---
### Error 3: Unequal Row Lengths
```Python
arr = np.array([  
[1, 2, 3],  
[4, 5]  
])    
print(arr)
```
Possible Error:
```
ValueError: setting an array element with a sequence
```
Correct Code:
```Python
arr = np.array([  
	[1, 2, 3],  
	[4, 5, 6]  
])  
print(arr)
```
---
### Error 4: Wrong Shape Format
```Python
arr=np.zeros(3,4)
```
Error:
```
Type Error
```
Correct Code:
```Python
arr=np.zeros((3,4))
```
Use double brackets because shape is passed as a tuple:

---
## 16. Practice Tasks
## Task 1
Create a NumPy array:
```
[10, 20, 30, 40, 50]
```
Print:
```
Array
Dimension
Shape
Size
Data type
```
---
## Task 2
Create a 2D NumPy array:
```
[    [85, 90, 78],    [70, 88, 92],    [60, 75, 80]]
```
Print:
```
Full dataset
Shape
Total elements
```
---
## Task 3
Create:
```
Array of 5 zeros
Array of 5 ones
Array from 1 to 10
Array of even numbers from 2 to 20
```
---
## Task 4
Create marks array:
```
marks = np.array([80, 90, 70, 60, 100])
```
Print normalized marks by dividing by `100`.

---
## Task 5
Create an array:
```
arr = np.array([5, 10, 15, 20])
```
Print:
```
arr + 5
arr - 5
arr * 2
arr / 5
```
---
## 17. Slot 4 Final Mini Code
```Python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Dimension:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)


dataset = np.array([
    [85, 90, 78],
    [70, 88, 92],
    [60, 75, 80]
])

print("Dataset:")
print(dataset)

print("Dataset Dimension:", dataset.ndim)
print("Dataset Shape:", dataset.shape)
print("Dataset Size:", dataset.size)
print("Dataset Data Type:", dataset.dtype)


zeros = np.zeros(5)
ones = np.ones(5)
range_array = np.arange(1, 11)
even_numbers = np.arange(2, 21, 2)

print("Zeros:", zeros)
print("Ones:", ones)
print("Range Array:", range_array)
print("Even Numbers:", even_numbers)


marks = np.array([80, 90, 70, 60, 100])
normalized_marks = marks / 100

print("Marks:", marks)
print("Normalized Marks:", normalized_marks)


numbers = np.array([5, 10, 15, 20])

print("Numbers + 5:", numbers + 5)
print("Numbers - 5:", numbers - 5)
print("Numbers * 2:", numbers * 2)
print("Numbers / 5:", numbers / 5)
```
