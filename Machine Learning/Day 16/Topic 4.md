# Feature Scaling: Standardization and Normalization
# Goal
```
1. What is feature scaling?
2. Why scaling is needed
3. Standardization
4. Normalization
5. StandardScaler
6. MinMaxScaler
7. When scaling is required
8. When scaling is not required
9. Scaling leakage
10. Common scaling errors
```
---
## 2. Why Scaling Matters
Suppose :
![[Pasted image 20260611104205.png]]
The value `800000` is much larger than `8.5`.
Some ML algorithms may give more importance to large-scale features, even if they are not actually more important.
Bad situation:
```
Salary Expectation dominates the model only because its number is large.
```
Scaling fixes this by bringing numerical features to a comparable range.

---
## 3. Beginner Explanation
Feature scaling means changing numerical values into a common scale without changing their meaning.
Example:
Original:
```
CGPA = 8.5
Attendance = 85
Previous Score = 78
```
After scaling:
```
CGPA = 0.85
Attendance = 0.85
Previous Score = 0.78
```
Now values are easier for many algorithms to compare.

---
## 4. Industry Applications
Scaling is important in:
```
Student marks prediction
Loan approval prediction
Customer segmentation
House price prediction
Medical risk prediction
Fraud detection
Recommendation systems
```
Especially algorithms based on distance, gradients, or numerical optimization need scaling.
Examples:
```
KNNK-Means
Logistic Regression
Linear Regression with regularization
SVM
Neural Networks
PCA
Gradient Descent-based models
```
Tree-based models usually need scaling less:
```
Decision Tree
Random Forest
Gradient Boosted Trees
```
---
## 5. Two Main Scaling Methods
```
Feature Scaling
│
├── Standardization
│   └── StandardScaler
│
└── Normalization
    └── MinMaxScaler
```
---
## 6. Standardization
Standardization transforms data so that:
```
Mean = 0
Standard Deviation = 1
```
Formula:
```
z = (x - mean) / standard deviation
```
Example:
If marks are:
```
40, 50, 60, 70, 80
```
Standardization converts them around zero:
```
-1.41, -0.71, 0, 0.71, 1.41
```
Use standardization when:
```
Data is roughly normally distributed
Algorithm is sensitive to feature scale
You are using Linear/Logistic Regression, SVM, PCA, KNN, K-Means
```
---
## 7. Normalization
Normalization usually means scaling values into a fixed range, commonly:
```
0 to 1
```
Formula:
```
x_scaled = (x - min) / (max - min)
```
Example:
Marks:
```
40, 50, 60, 70, 80
```
After Min-Max Normalization:
```
0.00, 0.25, 0.50, 0.75, 1.00
```
Use normalization when:
```
You want values between 0 and 1
Data does not follow normal distribution
You are using distance-based models
You are building neural networks later
```
---
## 8. Standardization vs Normalization

|Point|Standardization|Normalization|
|---|---|---|
|Output range|Not fixed|Usually 0 to 1|
|Formula|`(x - mean) / std`|`(x - min) / (max - min)`|
|Tool|`StandardScaler`|`MinMaxScaler`|
|Best for|Many ML algorithms|Fixed range requirement|
|Sensitive to outliers?|Less than MinMax|More sensitive|
|Common use|Regression, Logistic Regression, SVM, PCA|KNN, K-Means, Neural Networks|
Simple rule:
```
Use Standard
Scaler by default for many ML models.Use MinMaxScaler when you specifically need values between 0 and 1.
```
---
# 9. Dataset for This Slot
Run this:
![[Pasted image 20260611105358.png]]
Here:
```
Features:cgpa
		 attendance
		 previous_score
		 practice_questions
Label:final_marks
```
Problem type:
```
Supervised Learning → Regression
```
---
## 10. Separate X and y
![[Pasted image 20260611110108.png]]
Check scale:
![[Pasted image 20260611110248.png]]
You will notice:
```
cgpa ranges around 5 to 9
attendance ranges around 45 to 95
practice_questions ranges around 25 to 150
```
Different ranges mean scaling may help.

---
## 11. Train-Test Split First
Important rule:
```
Split first, then fit scaler only on training data.
```
Code:
![[Pasted image 20260611111839.png]]
Wrong workflow:
```
Scale full dataset
↓
Train-test split
```
Correct workflow:
```
Train-test split
↓
Fit scaler on X_train
↓
Transform X_train
↓
Transform X_test using same scaler
```
Why?
```
If scaler learns mean/min/max from full dataset,
test data information leaks into training.
```
This is called **scaling leakage**.

---
## 12. StandardScaler Code
![[Pasted image 20260611111946.png]]
Important:
```
scaler.fit_transform(X_train)
```
Means:
```
Learn mean and standard deviation from training data.Then transform training data.
```

```
scaler.transform(X_test)
```
Means:
```
Use training mean and standard deviation to transform test data.
```
Do not do this:
```
scaler.fit_transform(X_test)
```
Because that makes the test set use its own statistics.

---
## 13. MinMaxScaler Code
![[Pasted image 20260611113046.png]]
Output values usually fall between:
```
0 and 1
```
But if test data has values outside the training min/max range, transformed test values can go below 0 or above 1.
That is not always wrong. It simply means test data has values outside the training range.

---
## 14. Full Code: Scaling + Linear Regression

```Python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = {
    "cgpa": [8.5, 6.2, 7.8, 5.9, 9.1, 8.0],
    "attendance": [85, 45, 78, 55, 95, 88],
    "previous_score": [82, 45, 76, 50, 95, 88],
    "practice_questions": [120, 30, 90, 25, 150, 110],
    "final_marks": [85, 48, 78, 52, 96, 88]
}

df = pd.DataFrame(data)

X = df[["cgpa", "attendance", "previous_score", "practice_questions"]]
y = df["final_marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()

model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

mae = mean_absolute_error(y_test, y_pred)

print("Actual:", y_test.values)
print("Predicted:", y_pred)
print("MAE:", mae)
```
![[Pasted image 20260611113235.png]]

---
## 15. Very Important Note
For plain Linear Regression, scaling is not always mandatory.
But scaling becomes very important when you use:
```
Ridge Regression
Lasso Regression
Logistic Regression
KNN
K-Means
SVM
PCA
Neural Networks
Gradient Descent-based models
```
Since you will study Ridge, Lasso, KNN, K-Means, and PCA later, you must understand scaling now.

---
## 16. Debugging Section
### Bug 1: Scaling y by Mistake
Wrong:
```
scaler = StandardScaler()y_scaled = scaler.fit_transform(y)
```
Possible error:
```
ValueError: Expected 2D array, got 1D array instead
```
Why:
```
Scaler expects 2D feature matrix.y is usually 1D.
```
Also, for beginner regression workflows, do not scale y unless you understand target transformation.
Correct:
```Python
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```
---
### Bug 2: Fitting Scaler on Test Data
Wrong:
```Python
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
```
Why wrong:
```
You are fitting scaler separately on test data.This breaks consistency and can cause leakage-like evaluation issues.
```
Correct:
```
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```
---
### Bug 3: Scaling Before Train-Test Split
Wrong:
```Python
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(    
	X_scaled,
    y,
    test_size=0.2,
    random_state=42
)
```
Why dangerous:
```
Scaler learned mean and standard deviation from full dataset,including test data.
```
Correct:
```Python
X_train, X_test, y_train, y_test = train_test_split(    
	X,
    y,    
    test_size=0.2,    
    random_state=42)
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```
---
### Bug 4: Column Name Error After Scaling
After scaling, output becomes NumPy array:
```Python
X_train_scaled = scaler.fit_transform(X_train)
print(X_train_scaled["cgpa"])
```
Possible error:
```
IndexError or TypeError
```
Why:
```
Scaled output is NumPy array, not DataFrame.It does not have column names.
```
Fix:
```Python
X_train_scaled_df = pd.DataFrame(    
	X_train_scaled,    
	columns=X_train.columns
)
print(X_train_scaled_df["cgpa"])
```
---
### Bug 5: Text Column in Scaler
Wrong:
```Python
X = df[["cgpa", "branch", "attendance"]]
X_scaled = scaler.fit_transform(X)
```
Possible error:
```
ValueError: could not convert string to float
```
Why:
```
branch is categorical text.Scaling works on numerical columns only.
```
Correct workflow:
```
Numerical columns → scaling
Categorical columns → encoding
```
---
## 17. Common Beginner Mistakes
```
1. Scaling before train-test split.
2. Fitting scaler on test data.
3. Scaling categorical text columns.
4. Thinking all models require scaling.
5. Forgetting to transform test data.
6. Using different scalers for train and test.
7. Not saving scaler for production.
8. Assuming MinMaxScaler always keeps test data between 0 and 1.
9. Scaling target y without understanding why.
10. Losing column names after scaling and getting confused.
```
---
## 18. Production Thinking
In production, the scaler is part of the model pipeline.
Training:
```
Fit scaler on training data
Train model on scaled training data
Save scaler + model
```
Prediction:
```
User input
↓
Apply saved scaler
↓
Apply saved model
↓
Return prediction
```
Wrong production behavior:
```
Fit a new scaler on each user input
```
Why wrong?
```
A single user input cannot define proper mean/std.Production input must use training-time scaler.
```
Senior solution:
```
Save preprocessing pipeline with the model.
Use sklearn Pipeline or ColumnTransformer.
```
---
## 19. Mini Assignment Before Next Slot
Complete:
```
Task 1:Create the dataset from this slot.
Task 2:Separate X and y.
Task 3:Apply train-test split.
Task 4:Use StandardScaler correctly:
	fit_transform on X_train
	transform on X_test
Task 5:Use MinMaxScaler correctly:
	fit_transform on X_train
	transform on X_test
Task 6:Train LinearRegression using StandardScaler data.
Task 7:Calculate MAE.
Task 8:Convert scaled array back into DataFrame with column names.
Task 9:Write 5 lines explaining why scaling before splitting is dangerous.
Task 10:Write which algorithms need scaling.
```
---
## 20. Interview Questions
Prepare answers:
```
1. What is feature scaling?
2. Why is scaling needed?
3. What is standardization?
4. What is normalization?
5. Difference between StandardScaler and MinMaxScaler?
6. Which algorithms need scaling?
7. Which algorithms usually do not need scaling?
8. Why should scaling be fitted only on training data?
9. What is scaling leakage?
10. Why should we save scaler in production?
```
---
## 21. Interview Trap Questions
### Trap 1
Question:
```
Should we scale before train-test split?
```
Answer:
```
No. Split first, fit scaler only on training data, then transform both train and test using the same scaler.
```
### Trap 2
Question:
```
Do decision trees always need feature scaling?
```
Answer:
```
Usually no. Tree-based models split based on feature thresholds, so scaling is generally not required.
```
### Trap 3
Question:
```
Can MinMaxScaler output values greater than 1 for test data?
```
Answer:
```
Yes. If test values are outside the training min-max range, transformed values can go below 0 or above 1.
```
---
## 22. Cheat Sheet
```
Feature Scaling:
Converting numerical features into comparable scale.

Standardization:
Mean = 0, 
standard deviation = 1.

StandardScaler:
Used for standardization.

Normalization:
Usually scales values between 0 and 1.

MinMaxScaler:
Used for min-max normalization.

fit():
Learn scaling parameters.

transform():
Apply learned scaling parameters.

fit_transform():Fit and transform together.

Scaling leakage:
When scaler learns from test data.

Correct workflow:
Split → fit scaler on train → transform train/test.
```
---
## 23. Mind Map
```
Feature Scaling
│
├── Why?
│   ├── Different feature ranges
│   ├── Better optimization
│   └── Fair distance calculation
│
├── Methods
│   ├── Standardization
│   │   └── StandardScaler
│   └── Normalization
│       └── MinMaxScaler
│
├── Needed For
│   ├── KNN
│   ├── K-Means
│   ├── SVM
│   ├── Logistic Regression
│   ├── Ridge/Lasso
│   └── PCA
│
├── Less Needed For
│   ├── Decision Tree
│   └── Random Forest
│
└── Production Rule    
	├── fit on train only    
	├── transform test    
	└── save scaler
```
---