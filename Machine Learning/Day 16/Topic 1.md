# Data Preprocessing: Data Loading, Inspection, Missing Values, and Duplicates
## 1. Goal
1. Load data using Pandas
2. Inspect dataset structure
3. Understand missing values
4. Detect missing values
5. Handle missing values using basic methods
6. Detect duplicate rows
7. Remove duplicate rows
8. Understand beginner data-cleaning mistakes
9. Debug common Pandas preprocessing errors
---
## 2. Why this topic matter?
In real ML projects, your model is only as good as your data.
Bad data creates bad models.
```
Bad Data → Bad Features → Bad Model → Bad Prediction
```
A beginner thinks:
```
I need a better algorithm.
```
A real ML engineer first asks:
```
Is my data clean?
Are values missing?Are there duplicates?Are data types correct?Are target values valid?Are there leakage columns?
```
Before training any model, you must inspect and clean your data.

---
## 3. Industry Application
![[Pasted image 20260610142141.png]]
Example:
```
If a loan approval model has missing income values,
the model may make unreliable approval/rejection decisions.
```
So preprocessing is not optional.

---
## 4. Interview Relevance
Interviewers often ask:
```
How do you handle missing values?
When do you drop rows?
When do you fill missing values?
What is imputation?
How do you detect duplicates?
Why is preprocessing important?
Should missing values be filled before or after train-test split?
```
Strong answer:
```
I first inspect missingness patterns using df.isnull().sum() and percentages. Then I decide whether to drop, impute, or flag missing values based on column importance, missing percentage, business meaning, and leakage risk.
```
---
## 5. Startup/Product Relevance
Suppose you build:
```
AI Student Performance Predictor
```
User enters:
```
study_hours = missingattendance = 85previous_score = 70
```
Your product must decide:
```
Reject input?
Ask user to fill it?
Use default value?
Use trained imputer?
Show warning?
```
A production product cannot crash because one value is missing.

---
## 6. Beginner Explanation: What is Data Preprocessing?
Data preprocessing means preparing raw data before giving it to a machine learning model.
Raw data may contain:
```
Missing values
Duplicate rows
Wrong data types
Text categories
Outliers
Invalid values
Inconsistent formats
```
Clean data should be :
```
Complete enough
Consistent
Correctly typed
Leakage-free
Model-ready
```
Simple Pipeline:
```
Raw CSV
   ↓
Load with Pandas
   ↓
Inspect
   ↓
Clean missing values
   ↓
Remove duplicates
   ↓
Prepare for model
```
---
## 7. Today's Dataset
![[Pasted image 20260610144113.png]]
Problems  in the dataset:
```
Missing study_hours
Missing attendance
Missing previous_score
Missing study_method
Duplicate student_id = 105
Duplicate full row for student_id = 105
```
---
## Step 1: Load Data
In real projects, you usually load a csv file:
```Python
df = pd.read_csv("student_marks.csv")
```
For today, we created a DataFrame manually.
To see first rows:
![[Pasted image 20260610144306.png]]
To see last rows:
![[Pasted image 20260610144346.png]]
To see total rows and columns:
![[Pasted image 20260610144448.png]]

---
## 9. Step 2: Inspect Data
![[Pasted image 20260610144530.png]]
![[Pasted image 20260610144606.png]]
![[Pasted image 20260610144642.png]]

---
## 10. Step 3 : Detect missing values
![[Pasted image 20260610144747.png]]
![[Pasted image 20260610144811.png]]
Meaning:
```
study_hours has 1 missing value
attendance has 1 missing value
previous_score has 2 missing values
study_method has 2 missing values
```
TO calculate missing percentage:
![[Pasted image 20260610145034.png]]

---
## 11. What is Missing Values?
A missing value means data is absent.
In Pandas, missing values may appear as:
```
NaN
None
NA
blank cells in CSV
```
This means we do not know how many hours the student studied.

---
## 12. Why missing values are Dangerous?
Missing values can cause:
```
Model training errors
Wrong statistical summaries
Biased predictions
Reduced dataset size
Bad business decisions
```
Example:
If low-performing students often skip filling attendance, then missing attendance may carry meaning.
So blindly filling missing values can hide important patterns.
Senior engineer thinking:
```
Missingness itself can be information.
```
---
## 13. Methods to Handle Missing Values
Common methods:
```
1. Drop rows
2. Drop columns
3. Fill with mean
4. Fill with median
5. Fill with mode
6. Fill with constant value
7. Add missing indicator column
8. Use scikit-learn SimpleImputer
```
Scikit-learn’s `SimpleImputer` provides basic strategies for missing-value imputation, including filling with a constant, mean, median, or most frequent value.

---
## 14. Method 1: Drop Rows
![[Pasted image 20260610150255.png]]
use when :
```
Very few rows are missing
Dataset is large
Missing rows are not important
```
Avoid when :
```
Dataset is small
Missingness is meaningful
Too many rows will be removed
```
---
## 15. Method 2: Drop Column
![[Pasted image 20260610150457.png]]
Use when:
```
Column has too many missing values
Column is not important
Column is unreliable
```
Avoid when :
```
Column has too many missing values
Column is not important
Column is unreliable
```
---
## 16. Method 3: Fill Numerical Missing Values with mean
mean = average
![[Pasted image 20260610150839.png]]

---
## 17. Method 4: Fill Numerical Missing Values with Median
Median =middle values
![[Pasted image 20260610151036.png]]
Use median when:
```
Data has outliers
Distribution is skewed
Column is numerical
```
Example:
If income column has:
```
20000, 25000, 30000, 10000000
```
Mean becomes distorted, but median is safer.

---
## 18. Method 5: Fill Categorical Missing Values with Mode
Mode = most frequent value.
![[Pasted image 20260610151313.png]]

---
## 19. Method 6: Fill with Constant
Sometimes missing has meaning:
![[Pasted image 20260610151455.png]]

---
## 20. Method 7: Add Missing Indicator
![[Pasted image 20260610151731.png]]
Then fill:
![[Pasted image 20260610151844.png]]

---
## 21. Method 8 : SimpleImputer
