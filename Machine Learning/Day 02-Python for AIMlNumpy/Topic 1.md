# Python Data Structures for AI/ML
### 1. List
A **list** stores multiple values in one variable.  
It is ordered, changeable, and allows duplicate values.
##### Syntax:
![[Pasted image 20260529091043.png]]
##### Accessing Elements:
![[Pasted image 20260529091228.png]]
##### Updating Of List
![[Pasted image 20260529091424.png]]
##### AIML Use Case
In AI/ML, lists can store:
![[Pasted image 20260529091540.png]]

---
### 2. Tuple
A **tuple** is like a list, but it cannot be changed after creation.
##### Syntax:
![[Pasted image 20260529091711.png]]
##### AI/ML Use Case
Tuples are commonly used for shapes:
![[Pasted image 20260529091822.png]]
##### Important Error
![[Pasted image 20260529091933.png]]
Correction:
If you want a sequence that can be mutable then use list instead of tuple.

---
### 3. Dictionary
A **dictionary** stores data in key-value pairs.
##### Syntax :
![[Pasted image 20260529092206.png]]
##### Accessing Values
![[Pasted image 20260529092345.png]]
##### AIML Use Case
Dictionaries are useful for storing model results:
![[Pasted image 20260529092454.png]]

---
### 4. Sets
A **set** stores unique values only.  
It removes duplicates automatically.
##### Syntax :
![[Pasted image 20260529092627.png]]
##### AIML Use Case
![[Pasted image 20260529093033.png]]
If there is an error :
```Python 
set is not callable
```
then :
First :
```Python
del set
```
then write down the code because it happens that there is a variable that is being named for this the set () doesnot work.

---
### 5. List of Lists
This is very important for AI/ML because datasets are usually stored in table-like form.
Example:
![[Pasted image 20260529093335.png]]
##### Accessing each row:
![[Pasted image 20260529093443.png]]
##### Accessing each value
![[Pasted image 20260529093725.png]]

---
### 6. Common Errors and Corrections
##### Error 1: Index out of Range
![[Pasted image 20260529093905.png]]
##### Error 2: Wrong Dictionary Key
![[Pasted image 20260529094030.png]]
##### Error 3 Modifying Tuple
![[Pasted image 20260529094142.png]]

----
### 7. Practice tasks
## Task 1
Create a list of 5 student marks and print:
1. Full list
2. First mark
3. Last mark
4. Average marks
---
## Task 2
Create a tuple for image shape:
```
(224, 224, 3)
```
Print height, width, and channel separately.

---
## Task 3
Create a dictionary for one ML model:
```
model name
accuracy
loss
dataset name
```
Print all values.

---
## Task 4
Create a list of labels:
```
["cat", "dog", "cat", "bird", "dog"]
```
Convert it into a set and print unique labels.

---
## Task 5
Create this dataset:
```
dataset = [    [10, 20, 30],    [40, 50, 60],    [70, 80, 90]]
```
Print:
```
First row
Second row
Value 50
Value 90
```
---
### 8. Mini Code
```Python
marks = [85, 90, 78, 92, 88]

print("Marks:", marks)
print("First Mark:", marks[0])
print("Last Mark:", marks[-1])

average = sum(marks) / len(marks)
print("Average:", average)

image_shape = (224, 224, 3)

print("Height:", image_shape[0])
print("Width:", image_shape[1])
print("Channels:", image_shape[2])

model = {
    "name": "Logistic Regression",
    "accuracy": 0.91,
    "loss": 0.21,
    "dataset": "Student Performance Dataset"
}

print("Model Name:", model["name"])
print("Accuracy:", model["accuracy"])
print("Loss:", model["loss"])
print("Dataset:", model["dataset"])

labels = ["cat", "dog", "cat", "bird", "dog"]
unique_labels = set(labels)

print("Unique Labels:", unique_labels)

dataset = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print("First Row:", dataset[0])
print("Second Row:", dataset[1])
print("Value 50:", dataset[1][1])
print("Value 90:", dataset[2][2])
```
---
