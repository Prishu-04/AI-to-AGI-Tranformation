# Features, Labels, Dataset Structure, X and y
## 1. Goal:
```
1. What is a dataset?
2. What are rows and columns?
3. What is a sample/example?
4. What are features?
5. What is a label/target?
6. What are X and y?
7. How to separate X and y using Pandas
8. Numerical vs categorical features
9. Basic data leakage from wrong feature selection
10. Common beginner errors in feature-label separation
```
---
## 2. Why this topic Matters
Machine Learning depends on this relationship:
```
Features → Model → Label Prediction
```
In code :
```Python
model.fit(x,y)
```
here:
```
x=input feature
y=output label/target
```
If you choose the wrong `x` and `y`, your model will learn the wrong thing.
A beginner thinks:
```
Dataset means Excel/CSV file.
```
An ML engineer thinks;
```
Dataset = examples + features + target + data types + quality + leakage risk.
```
---
## 3. Industry Applications
Every ML system needs correct features and labels:
![[Pasted image 20260608161838.png]]
Without correct features and labels, even the best algorithm fails.

---
## 4. Beginner Explanation: What is a dataset?
A dataset is a collection of data used for analysis or machine learning.
Example:
![[Pasted image 20260608162309.png]]
In ML:
```
Rows = examples/samples/records
Columns = variables/features/target
```
One row means one example.
One column means one type of information.

---
## 5. What is a Sample?
A sample is one data point or one row.
Example:
```
Student 1 = one sample
```

```
Study Hours = 8
Attendance = 90
Previous Marks = 85
Final Result = Pass
```
So this row is one example given to model.

---
## 6. What are Features?
Features are the input variables used by the model to make a prediction.
Example:
![[Pasted image 20260608162732.png]]
These are features because they help predict the result.
Scikit-learn’s feature extraction documentation explains that raw formats such as text and images often need to be transformed into numerical features usable by ML algorithms.

---
## 7. What is Label?
A label is the output or answer the model is trying to predict.
Example:
![[Pasted image 20260608162929.png]]
Google’s label guide describes direct labels as labels identical to the prediction your model is trying to make, such as a column that directly contains the value you want to predict.

---
## 8. Features and Label Together
For this Dataset:
![[Pasted image 20260608163358.png]]
We separate;
```
Features:
Study Hours
Attendance
Previous Marks

Label:
Final Result
```
In ML notation:
```
X = Features
y = Label
```
Visuals:
```
Study Hours
Attendance
Previous Marks
        ↓
      Model
        ↓
Final Result
```
---
## 9. Mathematical Intuition
In ML, we are trying to learn a function:
```
f(x)=y
```
Meaning:
```
Input features go into a function/model,
and the model predicts the label.
```
For student result prediction:
```
f(study_hours, attendance, previous_marks) = final_result
```
For house price prediction:
```
f(area, bedrooms, location) = price
```
For placement prediction:
```
f(CGPA, DSA_score, projects, internships) = placed_or_not
```
This is the base of supervised learning.

----
## 10. x and y in Machine learning
In most ML code:
```Python
X = input features
y = target/label
```
Example:
![[Pasted image 20260608164557.png]]
![[Pasted image 20260608164608.png]]
This means :
```
Remove final_result from input features.
Use final_result as output label.
```
The scikit-learn training pattern commonly uses `.fit(X, y)` for training, `.predict(X)` for prediction, and `.score(X, y)` for evaluation.

---
## 11. Numerical vs Categorical Features
### Numerical Features
These are number based columns.
Examples:
```
Age
Salary
Study Hours
Attendance
CGPA
Loan Amount
House Area
```
Example:
```
CGPA = 8.5
Study Hours = 6
Salary = 1200000
```
### Categorical Features
These are categorical/text-based columns.
Examples:
```
Gender
City
Branch
Department
Product Category
Payment Method
```
Example:
```
City = Patna
Branch = CSE
Payment Method = UPI
```
Important:
Most ML models need categorical features to be converted into numbers later using:
```
Label Encoding
One-Hot Encoding
```
---
## 12. Direct Label vs Proxy Label
This is a powerful industry concept.
### Direct Label
A direct label is exactly what you want to predict.
Example:
You want to predict:
```
Will student get placed?
```
Dataset has:
```
Placed = Yes/No
```
This is a direct label.
### Proxy Label
A proxy label is an indirect approximation
Example:
You want to predict:
```
Student job-readiness
```
But you don not have a direct `job_ready` column.
SO you are:
```
Mock interview score
```
as an approximate label.
Google warns that proxy labels are compromises because they are imperfect approximations of the direct label.
Industry Thinking:
```
Bad label choice = bad product decision.
```
----
## 13. Dataset Example : Student Placement Prediction
Suppose we create this dataset:
![[Pasted image 20260609092519.png]]
Here:
```
Features:
CGPA
DSA Score
Projects
Internship
Communication Score

Label:
Placed
```
Problem type:
```
Supervised Learning
Classification
```
Why?
```
Because label is given.
Output is category: Yes/No.
```
---
## 14, Separate Features and Label
![[Pasted image 20260609092827.png]]
Shortcut method:
![[Pasted image 20260609092948.png]]
Meaning:
```
Drop placed from features.
Use placed as label.
```
---
## 15. Check Shape
Always check shape:
![[Pasted image 20260609093100.png]]
Meaning:
```
X has 4 rows and 5 feature columns.
y has 4 target values.
```
Important rule:
```
Number of rows in X must match number of rows in y.
```
---
## 16. Data Leakage Basics
Data leakage means the model gets information during training that it would not have in the real world.
Example of bad feature:
![[Pasted image 20260609093419.png]]
f your goal is to predict placement **before interview**, then `Final Interview Result` should not be a feature.
Why?
```
Because it directly reveals the answer.
```
This creates fake high accuracy.
Wrong:
```Python
X = df[["cgpa", "dsa_score", "final_interview_result"]]
y = df["placed"]
```
Correct;
```Python
X = df[["cgpa", "dsa_score"]]
y = df["placed"]
```
Senior Engineer thinking:
```
Only use features available at prediction time.
```
---
## 17. Common Feature-label Mistakes
### Mistake 1: Including Label Inside Features
Wrong:
```Python
X = df[["cgpa", "dsa_score", "placed"]]y = df["placed"]
```
Why wrong:
```
The model sees the answer during training.This causes leakage.
```
Correct:
```Python
X = df[["cgpa", "dsa_score"]]y = df["placed"]
```
---
### Mistake 2: Wrong Column Name
Wrong:
```
y = df["placement"]
```
Actual column:
```
placed
```
This causes:
```
KeyError
```
Correct:
```
y = df["placed"]
```
---
### Mistake 3: Mismatched Rows
Wrong:
```
X = df[["cgpa", "dsa_score"]].head(3)y = df["placed"]
```
Problem:
```
X has 3 rows.y has 4 rows.
```
This causes model training errors later.
Correct:
```
X = df[["cgpa", "dsa_score"]]y = df["placed"]
```
---
## 18. Production Thinking
In production, feature-label mistakes become serious
Example: Placement prediction product.
You train with:
```
CGPA
Projects
DSA Score
Interview Result
Placed
```
But in real usage, before placement season, interview result is not available.
So your deployed model fails because production input does not match training input.
Production rule:
```
Train-time features must match prediction-time available features.
```
Ask this before using any feature:
```
Will this information be available when the model makes prediction?
```
If answer is no, remove it.

---
## 19. Research Awareness
At research and industry level, feature quality is often more important than algorithm choice.
A weak feature set:
```
CGPA only
```
May perform poorly.
A stronger feature set:
```
CGPA
DSA Score
Projects
Internships
Communication Score
Mock Interview Score
Aptitude Score
```
May perform better.
But more features are not always better.
Bad features can cause:
```
NoiseBiasLeakageOverfittingUnfair decisions
```
---
## 20. Cheat Sheet

```
Dataset:
Collection of data used for ML.

Row:
One example/sample/record.

Column:
One variable.

Feature:
Input variable used for prediction.

Label:
Output/target the model predicts.

X:
Feature matrix.

y:
Target/label vector.

Numerical Feature:
Feature with numeric value.

Categorical Feature:
Feature with category/text value.

Data Leakage:
When model gets information it should not have during training.

Direct Label:
Exact target you want to predict.

Proxy Label:
Approximate substitute for the true target.
```
---
## 21. Mind Map
```
Dataset Structure
│
├── Rows
│   └── Samples / Examples
│
├── Columns
│   ├── Features
│   │   ├── Numerical
│   │   └── Categorical
│   │
│   └── Label / Target
│
├── X
│   └── Feature matrix
│
├── y
│   └── Target vector
│
└── Risks
    ├── Wrong column name
    ├── Shape mismatch
    ├── Text not encoded
    └── Data leakage
```
---
## 22 Practice Exercise
For each dataset, identify features and label.
### Dataset 1: House Price

|Area|Bedrooms|Location|Price|
|---|---|---|---|
Answer:
```
Features: Area, Bedrooms, Location
Label: Price
Problem Type: Regression
```
### Dataset 2: Loan Approval

|Income|Credit Score|Loan Amount|Approved|
|---|---|---|---|
Answer:
```
Features: Income, Credit Score, Loan Amount
Label: Approved
Problem Type: Classification
```
### Dataset 3: Customer Segmentation

| Age | Income | Monthly Spend |
| --- | ------ | ------------- |
Answer:
```
Features: Age, Income, Monthly Spend
Label: None
Problem Type: Unsupervised / Clustering
```
---
## 24. Mini Assignment
```
Task 1:
Create a Pandas DataFrame for Student Placement Prediction.

Task 2:
Separate X and y.

Task 3:
Print X.shape and y.shape.

Task 4:
Write which columns are numerical.

Task 5:
Write which columns are categorical.

Task 6:
Add one bad leakage column and explain why it should be removed.
```
---
## 25. # Interview Questions
Prepare answers for:
```
1. What is a feature?
2. What is a label?
3. What is X?
4. What is y?
5. What is a sample?
6. What is a categorical feature?
7. What is a numerical feature?
8. What is data leakage?
9. Why should the label not be inside features?
10. What is a proxy label?
```
---
