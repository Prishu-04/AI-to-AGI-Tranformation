# Error Handling + File Handling Basics
### 1. What is Error Handling?
Error handling means writing code in a way that your program does not crash when something goes wrong.
Example:  
If the user enters wrong input, file is missing, or division by zero happens, we handle it safely.

---
## 2. Basic Error Example 
![[Pasted image 20260529111649.png]]

---
## 3. `try-execept` Block
### Syntax
```Python
try:
    risky_code
except:
    error_handling_code
```
---
### Example
![[Pasted image 20260529112018.png]]

---
## 4. Multiple Error handling
![[Pasted image 20260529112231.png]]

---
## 5. try-except-else
`else` runs only when there is no error.
![[Pasted image 20260529112450.png]]

---
## 6.  `finally`
`finally` always runs, whether error occurs or not
![[Pasted image 20260529112618.png]]
 
---
## 7. AI/ML Use Case of Error Handling
In AI/ML, errors can happen when:
```
Dataset file is missingy
Wrong column name is used
Model input shape is incorrect
Data contains missing values
Wrong data type is passed
Internet/API request fails
```
Example:
![[Pasted image 20260529114510.png]]

---
## 8. File Handling
File handling means reading data from files or writing data into files.
In AI/ML, datasets are usually stored in files like:
```
.csv
.txt
.json
.xlsx
```
Today we start with `.txt` files.

---
## 9. Writing to a File
![[Pasted image 20260529114822.png]]
The content has written in the file.
![[Pasted image 20260529114857.png]]

---
## 10. Reading from a file
 ![[Pasted image 20260529115032.png]]

---
## 11. Better Method : `with open()`
This is the best method because it closes the file automatically.
![[Pasted image 20260529115313.png]]
The content get written in the file.
![[Pasted image 20260529115336.png]]
Reading :
![[Pasted image 20260529115455.png]]

---
## 12. File Modes
![[Pasted image 20260529115557.png]]

---
## 13. Append Data to file
![[Pasted image 20260529115709.png]]
In append, It doesnt overwrite the content it add up new content into existing file, but if file doesnt exist then it create the file and act as write.
![[Pasted image 20260529115818.png]]

---
## 14. Common Errors and Corrections
### Error 1 : File Not Found
![[Pasted image 20260529120010.png]]

Correct :
```Python
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file name.")
```
---
## 15. Practice Tasks
## Task 1
Create a program that divides two numbers.
Handle this error:
```
ZeroDivisionError
```
---
## Task 2
Create a list:
```
marks = [80, 90, 75]
```
Try to access index `5`.
Handle this error:
```
IndexError
```
---
## Task 3
Create a file:
```
day2_summary.txt
```
Write this inside it:
```
Day 2 Slot 3 Completed
Topic: Error Handling and File Handling
Status: Done
```
---
## Task 4
Read the same file and print its content.

---
## Task 5
Try to read a file named:
```
missing_file.txt
```
Handle the file-not-found error.

---
## 16. Slot 3 Final Mini Code
```Python
try:
    num1 = 20
    num2 = 0
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")


marks = [80, 90, 75]

try:
    print(marks[5])
except IndexError:
    print("Index does not exist")


try:
    age = int("twenty")
    print(age)
except ValueError:
    print("Invalid number format")


with open("day2_summary.txt", "w") as file:
    file.write("Day 2 Slot 3 Completed\n")
    file.write("Topic: Error Handling and File Handling\n")
    file.write("Status: Done\n")


with open("day2_summary.txt", "r") as file:
    content = file.read()
    print(content)


try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file name.")
finally:
    print("File handling practice completed")
```
---
