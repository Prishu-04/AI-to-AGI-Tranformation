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
![[Pasted image 20260610154917.png]]
For Categorical :
![[Pasted image 20260610154940.png]]

---
## 22. Step 4 : Detect Duplicates
![[Pasted image 20260610155056.png]]
Better:
![[Pasted image 20260610155132.png]]
To view duplicates:
![[Pasted image 20260610155301.png]]

---
## 23. Remove Duplicates
![[Pasted image 20260610155351.png]]

---
## 24. Debugging Error
### Bug 1: KeyError
Broken code:
```
df["study_hour"].mean()
```
Error:
```
KeyError: 'study_hour'
```
Why:
```
Correct column name is study_hours.
```
Debug:
```
print(df.columns)
```
Correct:
```
df["study_hours"].mean()
```
---
### Bug 2: NameError
Broken code:
```
df = pd.DataFrame(data)
```
Error:
```
NameError: name 'pd' is not defined
```
Why:
```
You did not import pandas.
```
Correct:
```
import pandas as pd
```
---
### Bug 3: np Not Defined
Broken code:
```
"study_hours": [5, 2, np.nan]
```
Error:
```
NameError: name 'np' is not defined
```
Why:
```
You used np.nan but did not import NumPy.
```
Correct:
```
import numpy as np
```
---
### Bug 4: Mode Index Error
Broken code:
```
mode_value = df["study_method"].mode()[0]
```
Possible error:
```
KeyError: 0
```
or issue if all values are missing.
Safer check:
```
mode_series = df["study_method"].mode()
if not mode_series.empty:    
	mode_value = mode_series[0]
else:    
	mode_value = "Unknown"
```
---
### Bug 5: Chained Assignment Warning
Risky code:
```
df[df["study_hours"].isnull()]["study_hours"] = 5
```
Possible warning:
```
SettingWithCopyWarning
```
Why:
```
You may be modifying a copy instead of the original DataFrame.
```
Better:
```
df.loc[df["study_hours"].isnull(), "study_hours"] = 5
```
---
## 25. Production Failure Scenarios
### Scenario 1: Missing Input in App
User leaves attendance blank.
Problem:
```
Model API receives missing value and crashes.
```
Senior solution:
```
Validate input before prediction.Return helpful error message.Use trained imputer if appropriate.
```
---
### Scenario 2: Duplicate Data in Training
Same high-scoring student appears 50 times by mistake.
Problem:
```
Model becomes biased toward that pattern.
```
Senior solution:
```
Check duplicates before training.Use unique identifiers.Audit suspicious repeated records.
```
---
### Scenario 3: Wrong Missing Value Strategy
You fill missing salary with mean in a dataset where salary has extreme outliers.
Problem:
```
Mean becomes distorted.Model learns unrealistic values.
```
Senior solution:
```
Use median or domain-based imputation.Check distribution first.
```
---
## 26. Interview Questions
Prepare answers:
```
1. What is data preprocessing?
2. Why is preprocessing important?
3. How do you detect missing values?
4. How do you handle missing numerical values?
5. When do you use mean imputation?
6. When do you use median imputation?
7. How do you handle missing categorical values?
8. What are duplicate rows?
9. Should duplicates always be removed?
10. Why should imputation be fitted only on training data?
```
---
## 27. Interview Trap Questions
### Trap 1
```
Should we always drop rows with missing values?
```
Answer:
```
No. It depends on dataset size, missing percentage, column importance, and whether missingness has meaning.
```
### Trap 2
```
Can we fill all missing values with 0?
```
Answer:
```
No. Zero may be a valid value and may distort the data. Use mean, median, mode, constant, or domain-based strategy depending on context.
```
### Trap 3
```
Should we remove all duplicate rows always?
```
Answer:
```
No. Some repeated rows may represent real repeated events. We must understand business context first.
```
---
