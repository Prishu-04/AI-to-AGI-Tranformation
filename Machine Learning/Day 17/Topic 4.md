# Polynomial Regression + Overfitting/Underfitting
## 1. Goal
```
1. Why straight-line models are not always enough
2. What non-linear relationships are
3. What Polynomial Regression is
4. What PolynomialFeatures does
5. Degree 1 vs Degree 2 vs Degree 3
6. Model complexity
7. Underfitting
8. Overfitting
9. Train error vs test error
10. How to detect overfitting in regression
```
---
## 2. Why Linear Regression May Fail
Linear Regression assumes the relationship is mostly straight-line.
Example:
```
More study hours → More marks
```
This may look at first.
But in real life is often not perfectly linear.
Example:
```
Study hours = 1 → low marks
Study hours = 4 → better marks
Study hours = 7 → high marks
Study hours = 12 → not always higher, because fatigue starts
```
So the relationship may be curved:
```
Marks increase with study hours,
but after some point, improvement slows down.
```
A straight line may not capture that curve properly.

---
## 3. Linear vs Non-Linear Relationship
### Linear Relationship
```
A straight-line pattern
```
Example:
```
study_hours increases → marks increase steadily
```
Visual:
```
Marks ↑
100 |                         * 
 90 |                     *
 80 |                 * 
 70 |             * 
 60 |         * 
 50 |     *    
    |____________________________→ Study Hours
```
---
### Non-Linear Relationship
```
A curved pattern
```
Example:
```
Marks improve fast at first,then slowly after a certain point.
```
Visual:
```
Marks ↑
100 |                    * * * 
 90 |              *  * 
 80 |          * 
 70 |      * 
 60 |   * 
 50 | *    
    |____________________________→ Study Hours
```
Here, a straight line may underfit.

---
## 4. What is Polynomial Regression?
Polynomial Regression is a regression method that allows a model to fit curved relationships by creating polynomial features.
Simple Linear Regression:
```
y = w1x + b
```
Polynomial Regression degree 2:
```
y = w1x + w2x² + b
```
Polynomial Regression degree 3:
```
y = w1x + w2x² + w3x³ + b
```
Important:
```
Polynomial Regression still uses LinearRegression.
The curve comes from transformed features like x² and x³.
```
Scikit-learn’s overfitting/underfitting example shows how polynomial features with linear regression can approximate non-linear functions, and how different polynomial degrees can underfit or overfit.

---
## 5. Degree Meaning

|Degree|Features Created|Complexity|
|---|---|---|
|1|`x`|Simple straight line|
|2|`x`, `x²`|Basic curve|
|3|`x`, `x²`, `x³`|More flexible curve|
|10|many high-power terms|Very complex, high overfitting risk|
Simple rule:
```
Low degree → simpler model
High degree → more complex model
```
---
## 6. Underfitting
Underfitting means the model is too simple to learn the real pattern.
Example:
```
Actual pattern is curved,
but model uses a straight line.
```
Symptoms:
```
High training error
High testing error
Poor predictions on both train and test data
```
Visual:
```
Actual data: curved
Model: straight line
Result: misses the pattern
```
In simple words:
```
Underfitting = model did not learn enough.
```
---
## 7. Overfitting
Overfitting means the model is too complex and learns noise instead of the real pattern.
Example:
```
Model fits every training point perfectly,but performs badly on new data.
```
Symptoms:
```
Very low training error
High testing error
Big gap between train and test performance
```
In simple words:
```
Overfitting = model memorized training data instead of learning general pattern.
```
---
## 8. Good Fit
A good model balances both.
```
Not too simple
Not too complex
Generalizes well on test data
```

| Case         | Train Error | Test Error | Meaning     |
| ------------ | ----------- | ---------- | ----------- |
| Underfitting | High        | High       | Too simple  |
| Good Fit     | Low/Medium  | Low/Medium | Balanced    |
| Overfitting  | Very Low    | High       | Too complex |

---
## 9. Dataset for This Slot
We will create a slightly curved marks dataset.
![[Pasted image 20260612113339.png]]
Pattern:
```
Marks rise quickly at first,
then improvement slows down near high study hours.
```
That is a curved/non-linear pattern.

---
## 10. Linear Regression Baseline
First train normal Linear Regression.
```Python
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "final_marks": [30, 38, 50, 63, 74, 82, 88, 92, 94, 95]
}

df = pd.DataFrame(data)

X = df[["study_hours"]]
y = df["final_marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

linear_pred = linear_model.predict(X_test)

linear_mae = mean_absolute_error(y_test, linear_pred)
linear_mse = mean_squared_error(y_test, linear_pred)
linear_rmse = np.sqrt(linear_mse)
linear_r2 = r2_score(y_test, linear_pred)

print("Linear Regression Results")
print("Actual:", y_test.values)
print("Predicted:", linear_pred)
print("MAE:", linear_mae)
print("RMSE:", linear_rmse)
print("R2:", linear_r2)
```
![[Pasted image 20260612114441.png]]
This gives us a baseline.

---
## 11. Polynomial Regression Degree 2
![[Pasted image 20260612115058.png]]
What happened internally?
Original feature:
```
study_hours
```
After degree 2:
```
study_hours
study_hours²
```
Example:

| study_hours | study_hours² |
| ----------- | ------------ |
| 2           | 4            |
| 3           | 9            |
| 4           | 16           |
Now LinearRegression learns:
```
final_marks = w1×study_hours + w2×study_hours² + b
```
---
## 12. See Polynomial Features
![[Pasted image 20260612115316.png]]
This confirms that polynomial features were created.

---

# 13. Complete Comparison Code
```Python
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "final_marks": [30, 38, 50, 63, 74, 82, 88, 92, 94, 95]
}

df = pd.DataFrame(data)

X = df[["study_hours"]]
y = df["final_marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
linear_pred = linear_model.predict(X_test)

linear_mae = mean_absolute_error(y_test, linear_pred)
linear_rmse = np.sqrt(mean_squared_error(y_test, linear_pred))
linear_r2 = r2_score(y_test, linear_pred)

poly = PolynomialFeatures(degree=2, include_bias=False)

X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)
poly_pred = poly_model.predict(X_test_poly)

poly_mae = mean_absolute_error(y_test, poly_pred)
poly_rmse = np.sqrt(mean_squared_error(y_test, poly_pred))
poly_r2 = r2_score(y_test, poly_pred)

results = pd.DataFrame({
    "Model": ["Linear Regression", "Polynomial Regression Degree 2"],
    "MAE": [linear_mae, poly_mae],
    "RMSE": [linear_rmse, poly_rmse],
    "R2": [linear_r2, poly_r2]
})

print(results)

comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Linear_Prediction": linear_pred,
    "Polynomial_Prediction": poly_pred
})

print("\nActual vs Predicted:")
print(comparison)

print("\nPolynomial Feature Names:")
print(poly.get_feature_names_out(["study_hours"]))
```
![[Pasted image 20260612115616.png]]

---

# 14. Compare Different Degrees

Now test degree 1, 2, 3, and 8.
```Python
degrees = [1, 2, 3, 8]  
results = []
predictions = []
for degree in degrees:
    # Create Polynomial Features
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    # Train Model
    model = LinearRegression()
    model.fit(X_train_poly, y_train)
    # Predictions
    train_pred = model.predict(X_train_poly)
    test_pred = model.predict(X_test_poly)
    # Metrics
    train_mae = mean_absolute_error(y_train, train_pred)
    test_mae = mean_absolute_error(y_test, test_pred)
    train_rmse = np.sqrt(mean_squared_error(y_train, train_pred))
    test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))
    train_r2 = r2_score(y_train, train_pred)
    test_r2 = r2_score(y_test, test_pred)
    # Store Results
    results.append({
        "Degree": degree,
        "Train MAE": train_mae,
        "Test MAE": test_mae,
        "Train RMSE": train_rmse,
        "Test RMSE": test_rmse,
        "Train R²": train_r2,
        "Test R²": test_r2
    })
    # Store Actual vs Predicted
    temp = pd.DataFrame({
        "Degree": degree,
        "Actual": y_test.values,
        "Predicted": test_pred
    })
    predictions.append(temp)
# Results Table
results_df = pd.DataFrame(results)
print("Model Comparison:")
print(results_df)
# Actual vs Predicted Table
comparison_df = pd.concat(predictions, ignore_index=True)
print("\nActual vs Predicted:")
print(comparison_df)
# Polynomial Feature Names
print("\nPolynomial Feature Names:")
for degree in degrees:
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    poly.fit(X)
    print(f"\nDegree {degree}:")
    print(poly.get_feature_names_out(["study_hours"]))
```
![[Pasted image 20260612121033.png]]
![[Pasted image 20260612121048.png]]
How to read output:
```
High train MAE + high test MAE → underfitting
Low train MAE + low test MAE → good fit
Very low train MAE + high test MAE → overfitting
```
---
## 15. Why High Degree Can Overfit
Degree 8 on only 10 data points is risky.
Why?
```
The model becomes too flexible.
It may bend too much to fit training points.
It may learn noise.
It may fail on new students.
```
In real projects:
```
Do not choose high degree just because training error becomes low.
```
Always check test error.

---
# 16. Production Thinking
For a Student Marks Predictor:
Bad thinking:
```
Degree 8 gives almost zero training error, so it is best.
```
Good thinking:
```
Does it perform well on test data?
Does it generalize to new students?
Is the model stable?
Is the model explainable enough?
```
Production goal:
```
Low test error + stable prediction + low leakage risk + reasonable complexity
```
---
## 17. Predict New Student Using Polynomial Model
Use degree 2:
![[Pasted image 20260612123300.png]]
Important:
```
You must transform new input using the same PolynomialFeatures object fitted on training data.
```
Wrong:
```
prediction = poly_model.predict(new_student)
```
Why wrong?
```
The polynomial model was trained on polynomial features,not raw study_hours only.
```
---
## 18. Better Way: Use Pipeline
Manual transformation can cause mistakes.
Use Pipeline:
![[Pasted image 20260612124801.png]]
Now prediction is easier:
![[Pasted image 20260612124944.png]]
This is cleaner and safer.

---
## 19. Debugging Section
### Bug 1: Predicting Raw X on Polynomial Model
Wrong:
```
poly_model.predict(X_test)
```
Error/problem:
```
Model expected polynomial features but received raw features.
```
Fix:
```
X_test_poly = poly.transform(X_test)poly_model.predict(X_test_poly)
```
Or use Pipeline:
```
poly_pipeline.predict(X_test)
```
---
### Bug 2: Fitting PolynomialFeatures on Test Data
Wrong:
```
X_train_poly = poly.fit_transform(X_train)X_test_poly = poly.fit_transform(X_test)
```
Why wrong:
```
You fitted transformation separately on test data.
```
Correct:
```
X_train_poly = poly.fit_transform(X_train)X_test_poly = poly.transform(X_test)
```
Same Day 2 rule:
```
Fit only on train.Transform train/test using training-fitted transformer.
```
---
### Bug 3: Using Very High Degree on Tiny Dataset
Wrong mindset:
```
Degree 15 gives lowest training error, so it is best.
```
Problem:
```
Likely overfitting.
```
Correct mindset:
```
Choose degree based on test error or cross-validation, not training error only.
```
---
### Bug 4: 1D Input Error
Wrong:
```
X = df["study_hours"]
```
Possible error:
```
Expected 2D array, got 1D array
```
Correct:
```
X = df[["study_hours"]]
```
---
### Bug 5: Reusing Wrong Polynomial Object
Problem:
```
You trained poly_model with degree=2,but transform new data using a new degree=3 transformer.
```
Fix:
```
Use the same fitted transformer, or use Pipeline to avoid this mistake.
```
---
## 20. Common Beginner Mistakes
```
1. Thinking Linear Regression cannot create curves.
2. Forgetting that Polynomial Regression still uses LinearRegression.
3. Using high degree without checking test error.
4. Predicting raw data with polynomial-trained model.
5. Fitting PolynomialFeatures separately on test data.
6. Choosing model only by training error.
7. Not comparing degree 1, 2, 3.
8. Ignoring overfitting.
9. Ignoring underfitting.
10. Not using Pipeline for polynomial transformations.
```
---
## 21. Interview Questions
Prepare answers:
```
1. What is Polynomial Regression?
2. Why do we use Polynomial Regression?
3. Is Polynomial Regression still a linear model?
4. What does PolynomialFeatures do?
5. What is degree in Polynomial Regression?
6. What is underfitting?
7. What is overfitting?
8. How do you detect overfitting?
9. Why is high-degree polynomial risky?
10. Why is test error more important than training error?
```
---
## 22. Interview Trap Questions
### Trap 1
Question:
```
Is Polynomial Regression completely different from Linear Regression?
```
Answer:
```
No. Polynomial Regression usually creates polynomial features first, then trains a Linear Regression model on those transformed features.
```
### Trap 2
Question:
```
If training error is zero, is the model perfect?
```
Answer:
```
No. It may be overfitting. We must check test error or validation performance.
```
### Trap 3
Question:
```
Can a simple straight line underfit data?
```
Answer:
```
Yes. If the real relationship is curved or complex, a straight line may be too simple and underfit.
```
---
## 23. Mini Assignment Before Next Slot
Complete before saying **NEXT SLOT**:
```
Task 1:Run Linear Regression on the curved study_hours dataset.

Task 2:Run Polynomial Regression with degree 2.

Task 3:Print:
	MAE
	RMSE
	R²
	
Task 4:Compare degree 1, 2, 3, and 8 using train MAE and test MAE.

Task 5:Identify:
	Which degree underfits?
	Which degree seems balanced?
	Which degree may overfit?

Task 6:Predict marks for study_hours = 7.5 using degree 2.

Task 7:Rewrite polynomial model using Pipeline.

Task 8:Write 5 lines explaining why high degree can be dangerous.
```
---
## 24. Real-World Challenge
You are building:
```
AI Student Marks Predictor
```
You compare models:
```
Degree 1:
	Train MAE = 7.8
	Test MAE = 8.5
Degree 2:
	Train MAE = 2.7
	Test MAE = 3.4
Degree 8:
	Train MAE = 0.1
	Test MAE = 12.5
```
Answer:
```
1. Which model is underfitting?
2. Which model is balanced?
3. Which model is overfitting?
4. Which model should you choose?
5. Why should you not choose degree 8?
6. What would you show as prediction range if degree 2 MAE = 3.4?
```
Expected thinking:
```
Degree 1 underfits.Degree 2 is balanced.Degree 8 overfits.Choose degree 2.
```
---
## 25. Cheat Sheet
```
Polynomial Regression:
Regression using polynomial features like x², x³.

PolynomialFeatures:
Creates polynomial feature columns.

Degree 1:
Straight line.

Degree 2:
Basic curve.

Degree 3:
More flexible curve.

High degree:
More complex, higher overfitting risk.

Underfitting:
Train error high, test error high.

Overfitting:
Train error very low, test error high.

Good fit:
Train error and test error both reasonably low.

Best practice:
Compare train and test error.

Use Pipeline.
Avoid choosing model only by training error.
```
---
## 26. Mind Map
```
Polynomial Regression
│
├── Why?
│   └── Straight line may not capture curved patterns
│
├── How?
│   ├── Create polynomial features
│   ├── x
│   ├── x²
│   └── x³
│
├── Model
│   └── LinearRegression on transformed features
│
├── Degree
│   ├── Low degree → simple
│   ├── Medium degree → balanced
│   └── High degree → complex
│
├── Errors
│   ├── Underfitting
│   │   └── high train + high test error
│   ├── Good fit
│   │   └── low train + low test error
│   └── Overfitting
│       └── very low train + high test error
│
└── Production Rule    
	├── use test error    
	├── avoid high degree blindly    
	└── use Pipeline
```
---
