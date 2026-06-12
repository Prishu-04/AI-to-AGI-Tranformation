# Day 17: Regression Models

## Overview

Day 3 focuses on Regression Models, the first major supervised learning algorithm family in this ML journey.

Regression is used when the target output is a numerical value.  
This day covers Simple Linear Regression, Multiple Linear Regression, Polynomial Regression, Ridge Regression, Lasso Regression, regression metrics, overfitting, underfitting, regularization, and model comparison.

The final outcome is a complete Student Marks Prediction System.

---

## Topics Covered

- What is Regression?
    
- Regression vs Classification
    
- Simple Linear Regression
    
- Multiple Linear Regression
    
- Regression equation
    
- Coefficients and intercept
    
- MAE
    
- MSE
    
- RMSE
    
- R² Score
    
- Baseline model
    
- Polynomial Regression
    
- PolynomialFeatures
    
- Underfitting
    
- Overfitting
    
- Ridge Regression
    
- Lasso Regression
    
- Regularization
    
- Alpha parameter
    
- Model comparison
    
- Prediction range
    
- Regression mini project
    

---

## Slot-Wise Learning

|Slot|Topic|
|---|---|
|Slot 1|What is Regression + Simple Linear Regression|
|Slot 2|Multiple Linear Regression + Feature Impact|
|Slot 3|Regression Evaluation Metrics: MAE, MSE, RMSE, R²|
|Slot 4|Polynomial Regression + Overfitting/Underfitting|
|Slot 5|Ridge and Lasso Regression + Regularization|
|Slot 6|Regression Mini Project + Debugging + Interview Revision|

---

## Tools Used

- Python
    
- Pandas
    
- NumPy
    
- scikit-learn
    
- joblib
    

---

## What is Regression?

Regression is a supervised learning task where the model predicts a continuous numerical value.

Examples:

- Student marks prediction
    
- House price prediction
    
- Salary prediction
    
- Car price prediction
    
- Medical insurance cost prediction
    
- Delivery time prediction
    
- Sales forecasting
    

Simple rule:

```text
If output is a number → Regression
If output is a category → Classification
```

---

## Simple Linear Regression

Simple Linear Regression uses one input feature to predict one numerical output.

Example:

```text
study_hours → final_marks
```

Equation:

```text
y = mx + c
```

ML form:

```text
prediction = weight × feature + bias
```

Where:

- `m` = slope / weight
    
- `c` = intercept / bias
    

---

## Multiple Linear Regression

Multiple Linear Regression uses multiple input features to predict one numerical output.

Example:

```text
study_hours
attendance
previous_score
sleep_hours
practice_questions
        ↓
final_marks
```

Equation:

```text
final_marks =
w1 × study_hours
+ w2 × attendance
+ w3 × previous_score
+ w4 × sleep_hours
+ w5 × practice_questions
+ bias
```

---

## Coefficients and Intercept

### Coefficient

A coefficient shows the estimated effect of one feature on the target, assuming other features stay constant.

Example:

```text
study_hours coefficient = 4.5
```

Meaning:

```text
If study_hours increases by 1 hour, predicted marks increase by around 4.5 marks, assuming other features stay constant.
```

### Intercept

Intercept is the base prediction when all feature values are zero.

---

## Regression Metrics

### MAE — Mean Absolute Error

MAE measures the average absolute difference between actual and predicted values.

```text
MAE = average of |Actual - Predicted|
```

Example:

```text
MAE = 4
```

Meaning:

```text
The model is wrong by around 4 marks on average.
```

### MSE — Mean Squared Error

MSE measures average squared error.

```text
MSE = average of (Actual - Predicted)²
```

MSE punishes large errors more strongly.

### RMSE — Root Mean Squared Error

RMSE is the square root of MSE.

```text
RMSE = √MSE
```

RMSE is in the same unit as the target and punishes large errors more than MAE.

### R² Score

R² measures how much variance in the target is explained by the model.

```text
Best value = 1.0
```

Important:

```text
R² is not accuracy.
```

---

## Polynomial Regression

Polynomial Regression helps when a straight line is not enough.

Linear Regression:

```text
y = w1x + b
```

Polynomial Regression degree 2:

```text
y = w1x + w2x² + b
```

Important:

```text
Polynomial Regression usually creates polynomial features first, then trains Linear Regression on those transformed features.
```

---

## Underfitting and Overfitting

### Underfitting

Underfitting happens when the model is too simple.

Signs:

```text
High training error
High testing error
```

### Overfitting

Overfitting happens when the model memorizes training data and performs poorly on unseen data.

Signs:

```text
Very low training error
High testing error
```

### Good Fit

A good fit has reasonable training error and testing error.

---

## Ridge Regression

Ridge Regression is Linear Regression with L2 regularization.

It penalizes large squared coefficients.

```text
Loss = prediction error + alpha × sum(coefficients²)
```

Ridge usually shrinks coefficients toward zero but does not usually make them exactly zero.

---

## Lasso Regression

Lasso Regression is Linear Regression with L1 regularization.

It penalizes absolute coefficient values.

```text
Loss = prediction error + alpha × sum(|coefficients|)
```

Lasso can shrink some coefficients exactly to zero, which can act like feature selection.

---

## Alpha Parameter

Alpha controls regularization strength.

```text
alpha small  → weak regularization
alpha large  → strong regularization
```

If alpha is too low:

```text
Overfitting risk remains.
```

If alpha is too high:

```text
Model may underfit.
```

---

## Mini Project

# Student Marks Prediction System

## Problem Statement

Predict a student's final marks using study hours, attendance, previous score, sleep hours, and practice questions.

## ML Type

Supervised Learning

## Problem Type

Regression

## Features

- study_hours
    
- attendance
    
- previous_score
    
- sleep_hours
    
- practice_questions
    

## Label

- final_marks
    

## Models Used

- Linear Regression
    
- Ridge Regression
    
- Lasso Regression
    
- Polynomial Ridge Regression
    

## Metrics Used

- MAE
    
- RMSE
    
- R² Score
    

## Product Rule

Do not show overconfident exact output.

Bad output:

```text
Your marks will be exactly 78.342
```

Better output:

```text
Expected marks range: 74–82
```

---

## Files in This Folder

```text
day-03-regression-models/
│
├── README.md
├── notes.md
├── day3_slot1_simple_linear_regression.py
├── day3_slot2_multiple_linear_regression.py
├── day3_slot3_regression_metrics.py
├── day3_slot4_polynomial_regression.py
├── day3_slot5_ridge_lasso.py
├── day3_regression_mini_project.py
├── debugging_notes.md
└── student_marks_regression_model.pkl
```

---

## Important Code Pattern

### Model Comparison

```python
models = {
    "Linear Regression": linear_pipeline,
    "Ridge Regression": ridge_pipeline,
    "Lasso Regression": lasso_pipeline,
    "Polynomial Ridge Degree 2": poly_pipeline
}
```

### Evaluation Function

```python
def evaluate_model(model_name, model, X_test, y_test):
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    return {
        "Model": model_name,
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }
```

### Prediction Range

```python
prediction = best_model.predict(new_student)[0]
best_mae = results_df.sort_values("MAE").iloc[0]["MAE"]

print(f"Expected Marks Range: {prediction - best_mae:.0f} to {prediction + best_mae:.0f}")
```

---

## Debugging Notes

Common errors learned:

- `NotFittedError` from predicting before fitting
    
- `ValueError` from wrong input shape
    
- Feature mismatch during prediction
    
- Target column included in X
    
- Using accuracy for regression
    
- R² treated as accuracy
    
- Polynomial model predicting on raw input
    
- Scaling full data before train-test split
    
- Very high polynomial degree causing overfitting
    
- Alpha too high causing underfitting
    
- Lasso convergence warning
    

---

## Interview Questions Covered

- What is regression?
    
- Regression vs classification?
    
- What is Simple Linear Regression?
    
- What is Multiple Linear Regression?
    
- What is a coefficient?
    
- What is intercept?
    
- What is MAE?
    
- What is RMSE?
    
- What is R² Score?
    
- Why is R² not accuracy?
    
- What is Polynomial Regression?
    
- What is underfitting?
    
- What is overfitting?
    
- What is regularization?
    
- What is Ridge Regression?
    
- What is Lasso Regression?
    
- Difference between Ridge and Lasso?
    
- What is alpha?
    
- Why can Lasso perform feature selection?
    

---

## Final Learning Outcome

After completing Day 3, I can build, evaluate, compare, debug, and explain regression models using scikit-learn. I can train Linear Regression, Polynomial Regression, Ridge, and Lasso models, evaluate them using MAE, RMSE, and R², detect overfitting and underfitting, and convert predictions into safer product-style output ranges.

---

## Resume Bullet

Built a Student Marks Prediction regression system using Python, Pandas, NumPy, and scikit-learn, comparing Linear Regression, Polynomial Regression, Ridge, and Lasso models with MAE, RMSE, and R² evaluation, while applying Pipeline-based preprocessing, overfitting analysis, and prediction-range output for safer product behavior.