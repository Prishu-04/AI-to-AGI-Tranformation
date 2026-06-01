# Why do we need an Environment for ML
***
We need a Virtual Environment because In ML we use multiple packages so to keep them bound in a project. We require them.
# Creation of new Environment
***
### Steps to be followed
Please note one thing before doing this step your anaconda and vs code should be set up.
Step1 - Open VS code.
Step 2 - Create a Directory
Step 3 - Go the Terminal and Open command prompt.
Step 4 - Make sure that you are in the same file location.

##### Step 5 **General Syntax
```
conda create -p <virtual environment name> python==<version> 
```
Example
```cmd
conda create -p venv python==3.14
```
**Note**-There is no need to use always one version we can use any version but it should latest.

Step 6 After creating the environment. Create a file
```
requirement.txt

Write down all the libraries you want to import.
```

Step 7 Activate the Environment
```cmd
conda activate venv1/
```
After writing this, all the packages and libraries will be installed in this library.
To install now any package we do from requirement.txt file.
```cmd
pip install -r requirement.txt
```

After all this, We have Two types of file that we can create 
* .py file
```
Python.py

To run this file we write 
python <filename>.py
```
* .ipynb file 
```
Python.ipynb
```
 But, for running a Jupiter notebook file, There are two package to be installed:
 1. `pip install ipykernel`
 2.  

