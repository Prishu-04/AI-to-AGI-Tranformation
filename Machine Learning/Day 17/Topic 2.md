# Multiple Linear Regression + Feature Impact
## Goal
```
1. What Multiple Linear Regression is
2. Difference between Simple and Multiple Linear Regression
3. Multiple regression equation
4. Feature coefficients
5. Intercept/bias
6. How to interpret feature impact
7. How to train Multiple Linear Regression in scikit-learn
8. How to predict using multiple inputs
9. Common feature mismatch errors
10. Interview questions
```
---
## 2. What is Multiple Linear Regression?
Multiple Linear Regression means:
```
Multiple input features
One numerical output
Linear relationship
```
Example:
```
study_hours
attendance
previous_score
sleep_hours
practice_questions        
↓
final_marks
```
Instead of predicting marks using only study hours, we use more information.
Simple Linear Regression:
```
final_marks = weight × study_hours + bias
```
Multiple Linear Regression:
```
final_marks =    w1 × study_hours  
				+ w2 × attendance  
				+ w3 × previous_score  
				+ w4 × sleep_hours  
				+ w5 × practice_questions  
				+ bias
```
---
## 3. Why Multiple Features Are Better
In real life, marks do not depend only on study hours.
A student may study 8 hours but still score low because:
```
Poor revision quality
Low attendance
Weak previous basics
Less sleep
Fewer practice questions
High exam difficulty
```
So one feature is usually too weak.
Better model:
```
Multiple useful features → Better pattern learning
```
Example:
![[Pasted image 20260611161801.png]]
Both studied 8 hours, but their final marks are different because other features matter.

---
## 4. Simple vs Multiple Linear Regression

| Point              | Simple Linear Regression | Multiple Linear Regression              |
| ------------------ | ------------------------ | --------------------------------------- |
| Number of features | 1                        | 2 or more                               |
| Example input      | study_hours              | study_hours, attendance, previous_score |
| Equation           | `y = mx + c`             | `y = w1x1 + w2x2 + ... + b`             |
| Realism            | Basic                    | More realistic                          |
| Interpretation     | One slope                | One coefficient per feature             |
| Use case           | Simple relationship      | Real-world tabular ML                   |

---
## 5. Mathematical Intuition
Suppose model learns:
```
final_marks =    4.5 × study_hours  
				+ 0.25 × attendance  
				+ 0.40 × previous_score  
				+ 0.08 × practice_questions  
				+ 10
```
For a student:
```
study_hours = 6
attendance = 80
previous_score = 70
practice_questions = 100
```
Prediction:
```
final_marks =    4.5 × 6  
				+ 0.25 × 80  
				+ 0.40 × 70  
				+ 0.08 × 100
				+ 10
= 27 + 20 + 28 + 8 + 10= 93
```
So predicted marks = **93**.

---
## 6. What are Coefficients?
Each feature gets one coefficient.
```
study_hours coefficient = 4.5
attendance coefficient = 0.25
previous_score coefficient = 0.40
practice_questions coefficient = 0.08
```
Meaning:
```
When other features stay constant,
a 1-unit increase in that feature changes prediction by its coefficient.
```
Example:
```
study_hours coefficient = 4.5
```
Means:
```
If study_hours increases by 1 hour,
predicted marks increase by around 4.5 marks,
assuming other features stay the same.
```
Scikit-learn’s `LinearRegression` fits coefficients to minimize residual sum of squares between actual target values and predicted values.

---
## 7. Important Warning About Coefficients
Do not blindly say:
```
Bigger coefficient = more important feature
```
Why?
Because features may have different scales.
Example:
```
study_hours range: 1 to 10
attendance range: 0 to 100
practice_questions range: 0 to 300
```
A coefficient depends on feature scale.
Better interpretation requires:
```
domain understanding
feature scaling
correlation checking
model validation
```
For now, understand coefficients as **model-learned weights**, not final truth.

---
## 8. Dataset for This Slot
![[Pasted image 20260612091658.png]]
Features:
```
study_hours
attendance
previous_score
practice_questions
```
Label:
```
final_marks
```
Problem type:
```
Supervised Learning → Regression
```
---
## 9. Separate X and y
![[Pasted image 20260612091845.png]]
![[Pasted image 20260612091946.png]]
Here:
```
X = feature matrix
y = target vector
```
Shape check:
![[Pasted image 20260612092042.png]]
Meaning:
```
10 rows
4 input features
10 target values
```
---
## 10. Train-Test Split
![[Pasted image 20260612092303.png]]
`train_test_split` is the scikit-learn utility for splitting arrays or matrices into random train and test subsets.
Check:
![[Pasted image 20260612092539.png]]

---
## 11. Train Multiple Linear Regression Model
![[Pasted image 20260612092757.png]]
This learns:
```
coefficient for study_hours
coefficient for attendance
coefficient for previous_score
coefficient for practice_questions
intercept/bias
```
---
## 12. Predict and Evaluate
![[Pasted image 20260612093034.png]]
Meaning:
```
Actual = real final marks
Predicted = model predicted marks
MAE = average absolute prediction error
```
---
## 13. Print Coefficients and Intercept
![[Pasted image 20260612093338.png]]
Better readable format:
![[Pasted image 20260612093927.png]]
This means each feature has its own learned effect.

---
## 14. Complete Code
```Python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "attendance": [40, 45, 50, 55, 60, 70, 75, 80, 90, 95],
    "previous_score": [35, 40, 45, 50, 55, 65, 70, 75, 85, 90],
    "practice_questions": [10, 20, 30, 40, 50, 65, 75, 85, 100, 120],
    "final_marks": [38, 42, 48, 52, 58, 68, 72, 78, 88, 94]
}

df = pd.DataFrame(data)

X = df[["study_hours", "attendance", "previous_score", "practice_questions"]]
y = df["final_marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)

coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print("Actual Marks:", y_test.values)
print("Predicted Marks:", y_pred)
print("MAE:", mae)

print("\nCoefficients:")
print(coefficients)

print("\nIntercept:")
print(model.intercept_)
```
---
## 15. Predict for a New Student
Now add:
![[Pasted image 20260612094450.png]]
Important:
```
The new input must have the same feature names and same feature order as training data.
```
Correct columns:
```
study_hours
attendance
previous_score
practice_questions
```
---
## 16. Feature Order Matters
During training:
```Python
X = df[["study_hours", "attendance", "previous_score", "practice_questions"]]
```
During prediction, use the same columns:
```Python
new_stu = pd.DataFrame({    
	"study_hours": [7],    
	"attendance": [85],    
	"previous_score": [75],    
	"practice_questions": [90]
})
```
Do not change to:
```Python
new_stu = pd.DataFrame({    
	"attendance": [85],    
	"study_hours": [7],    
	"practice_questions": [90],    
	"previous_score": [75]
})
```
Pandas/scikit-learn can often align or warn depending on version and estimator behavior, but for clean production practice, keep the **same columns, same names, same expected schema**.

---
## 17. Feature Impact Interpretation
Suppose coefficients are:

| Feature            | Coefficient |
| ------------------ | ----------- |
| study_hours        | 1.5         |
| attendance         | 0.2         |
| previous_score     | 0.6         |
| practice_questions | 0.04        |
Interpretation:
```
If study_hours increases by 1,
prediction increases by 1.5 marks,
assuming other features remain constant.

If attendance increases by 1 percentage point,
prediction increases by 0.2 marks,
assuming other features remain constant.

If previous_score increases by 1 mark,
prediction increases by 0.6 marks,
assuming other features remain constant.

If practice_questions increases by 1,
prediction increases by 0.04 marks,
assuming other features remain constant.
```
Strong interview phrase:
```
Coefficients show the estimated change in the target for one-unit change in a feature, holding other features constant.
```
---
## 18. Production Thinking
In production, never trust raw input directly.
Example bad inputs:
```
study_hours = 40
attendance = 150
previous_score = -10
practice_questions = "many"
```
Before prediction, validate:
```Python
def validate_student_input(study_hours, attendance, previous_score, practice_questions):
    if study_hours < 0 or study_hours > 24:
        raise ValueError("study_hours must be between 0 and 24")

    if attendance < 0 or attendance > 100:
        raise ValueError("attendance must be between 0 and 100")

    if previous_score < 0 or previous_score > 100:
        raise ValueError("previous_score must be between 0 and 100")

    if practice_questions < 0:
        raise ValueError("practice_questions cannot be negative")
```
Then predict only after validation.

---
## 19. Debugging Section
### Bug 1: Feature Mismatch Error
Training used:
```Python
X = df[["study_hours", "attendance", "previous_score", "practice_questions"]]
```
Prediction uses:
```Python
new_student = pd.DataFrame({    
	"study_hours": [7],    
	"attendance": [85],    
	"previous_score": [75]
})
model.predict(new_student)
```
Problem:
```
practice_questions is missing.
```
Possible error:
```
Feature names should match those that were passed during fit
```
Fix:
```Python
new_student = pd.DataFrame({
    "study_hours": [7],    
    "attendance": [85],    
    "previous_score": [75],    
    "practice_questions": [90]
})
```
---
### Bug 2: Target Column Included in X
Wrong:
```Python
X = df.drop("study_hours", axis=1)
y = df["final_marks"]
```
Problem:
```
final_marks may still be inside X.That causes data leakage.
```
Correct:
```Python
X = df.drop("final_marks", axis=1)
y = df["final_marks"]
```
Or explicit:
```Python
X = df[["study_hours", "attendance", "previous_score", "practice_questions"]]
y = df["final_marks"]
```
---
### Bug 3: Text Feature Not Encoded
Wrong:
```Python
X = df[["study_hours", "attendance", "branch"]]
model.fit(X_train, y_train)
```
Possible error:
```
could not convert string to float: 'CSE'
```
Why:
```
Linear Regression needs numerical input.
```
Fix:
```
Encode branch before model training.
```
You already learned this on Day 2.

---
### Bug 4: Wrong Shape for New Prediction
Wrong:
```Python
new_student = [7, 85, 75, 90]
model.predict(new_student)
```
Possible error:
```
Expected 2D array, got 1D array
```
Correct:
```Python
new_student = pd.DataFrame({    
	"study_hours": [7],    
	"attendance": [85],    
	"previous_score": [75],    
	"practice_questions": [90]
})
model.predict(new_student)
```
---
### Bug 5: Misreading Coefficients
Wrong interpretation:
```
previous_score coefficient is largest,
so previous_score is always most important.
```
Better:
```
Coefficient size depends on feature scale, correlation, and preprocessing.
Use coefficients carefully.
```
---
## 20. Common Beginner Mistakes
```
1. Thinking more features always improve the model.
2. Adding irrelevant features.
3. Including target column inside X.
4. Forgetting to encode categorical features.
5. Predicting with missing columns.
6. Using different feature order during prediction.
7. Blindly interpreting coefficient size as importance.
8. Not validating new user input.
9. Not checking MAE after adding features.
10. Thinking Linear Regression can capture every complex relationship.
```
---
## 21. Interview Questions
Prepare answers:
```
1. What is Multiple Linear Regression?
2. Difference between simple and multiple linear regression?
3. What is the equation of Multiple Linear Regression?
4. What are coefficients?
5. What is intercept?
6. How do you interpret a coefficient?
7. Why can coefficient interpretation be misleading?
8. Why should target column not be included in X?
9. What happens if prediction data has missing features?
10. Does adding more features always improve performance?
```
---
## 22. Interview Trap Questions
### Trap 1
Question:
```
Does adding more features always improve model performance?
```
Answer:
```
No. Irrelevant or noisy features can reduce performance and increase overfitting risk.
```
### Trap 2
Question:
```
Can coefficient values directly prove feature importance?
```
Answer:
```
Not always. Coefficients depend on feature scale, correlation between features, preprocessing, and model assumptions.
```
### Trap 3
Question:
```
What happens if final_marks is accidentally included in X?
```
Answer:
```
That creates data leakage because the model directly sees the answer during training, leading to unrealistic performance.
```
---
## 23. Mini Assignment Before Next Slot

Complete before saying **NEXT SLOT**:

```
Task 1:Run the Multiple Linear Regression code.

Task 2:Print:
	X.shape
	y.shape
	X_train.shape
	X_test.shape
	
Task 3:Print coefficients with feature names.

Task 4:Write the learned equation:
	final_marks =w1×study_hours 
		+ w2×attendance 
		+ w3×previous_score
		+ w4×practice_questions 
		+ intercept
		  
Task 5:Predict marks for:
	study_hours = 7
	attendance = 85
	previous_score = 75
	practice_questions = 90
	
Task 6:Show output as a range:
	prediction - 3 to prediction + 3

Task 7:Write 5 lines explaining why multiple features are better than only study_hours.

Task 8:Write 3 reasons why adding too many features can be bad.
```
---
## 24. Real-World Challenge
You are building:
```
AI Student Marks Predictor
```
You currently have these possible features:
```
study_hours
attendance
previous_score
sleep_hours
practice_questions
mobile_usage_hours
teacher_rating
revision_quality
exam_difficulty
favorite_color
student_name
```
Answer:
```
1. Which features are useful?
2. Which features are risky or irrelevant?
3. Which features may need encoding?
4. Which features need validation?
5. Which feature can cause privacy/product concerns?
6. Which features are available before prediction time?
```
Important ML engineer mindset:
```
Do not add features just because they exist.
Add features because they are useful, valid, ethical, and available at prediction time.
```
---
## 25. Cheat Sheet
```
Multiple Linear Regression:
Regression with multiple input features.

Equation:
y = w1x1 + w2x2 + ... + b

Coefficient:
Model-learned weight for each feature.

Intercept:
Base prediction when feature contribution is zero.

X:Feature matrix with multiple columns.

y:Target vector.

model.coef_:
Stores coefficients.

model.intercept_:
Stores intercept.

Feature mismatch:
Prediction input does not match training features.

Data leakage:
Target or future information accidentally included in X.
```
---
## 26. Mind Map
```
Multiple Linear Regression
│
├── Input
│   ├── study_hours
│   ├── attendance
│   ├── previous_score
│   └── practice_questions
│
├── Output
│   └── final_marks
│
├── Model Learns
│   ├── coefficient per feature
│   └── intercept
│
├── Workflow
│   ├── create dataset
│   ├── separate X and y
│   ├── train-test split
│   ├── fit model
│   ├── predict
│   ├── evaluate MAE
│   └── interpret coefficients
│
└── Risks    
	├── data leakage    
	├── irrelevant features    
	├── feature mismatch    
	├── unencoded text    
	└── overconfident interpretation
```
----
