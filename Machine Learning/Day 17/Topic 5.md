# Ridge and Lasso Regression + Regularization
## 1. Goal
```
1. Why overfitting happens
2. What regularization means
3. Ridge Regression
4. Lasso Regression
5. L1 vs L2 regularization
6. Alpha parameter
7. How regularization controls model complexity
8. How Ridge/Lasso help Polynomial Regression
9. Feature selection basics using Lasso
10. Common regularization mistakes
```
---
## 2. Why regularization Matters?
In Polynomial Regression, a high-degree model can become too flexible.
Example:
```
Degree 8 
Polynomial Regression
Train MAE = 0.1
Test MAE = 12.5
```
This means:
```
The model memorized training data.It failed on test data.
```
This is overfitting.
Regularization helps by controlling how large the model coefficients can become.
Simple idea:
```
Do not allow the model to become too extreme.
```
---
## 3. Beginner Explanation
Linear Regression tries to reduce prediction error.
Regularized Regression tries to reduce:
```
Prediction error + penalty for large coefficients
```
So the model is forced to stay simpler.
Without regularization:
```
Model can create very large weights.Large weights can make predictions unstable.
```
With regularization:
```
Model keeps weights controlled.
Predictions become more stable.
Overfitting risk reduces.
```
---
## 4. What are Coefficients Again?
In Multiple Linear Regression:
```
final_marks =w1 × study_hours
			+ w2 × attendance
			+ w3 × previous_score
			+ w4 × practice_questions
			+ bias
```
Here:
```
w1, w2, w3, w4 are coefficients/weights.
```
If coefficients become very large, model may become sensitive.
Example:
```
small input change → huge prediction change
```
Regularization controls this.

---
## 5. Ridge Regression
Ridge Regression is Linear Regression with **L2 regularization**.
It penalizes large squared coefficients.
Simple form:
```
Loss = prediction error + alpha × sum(coefficients²)
```
Meaning:
```
Ridge tries to keep coefficients small.
```
Ridge usually reduces coefficients close to zero, but not exactly zero.
Scikit-learn describes Ridge as solving a linear least-squares regression problem with L2 regularization.

---
## 6. Lasso Regression
Lasso Regression is Linear Regression with **L1 regularization**.
It penalizes absolute coefficient values.
Simple form:
```
Loss = prediction error + alpha × sum(|coefficients|)
```
Meaning:
```
Lasso can shrink some coefficients exactly to zero.
```
This means Lasso can perform basic feature selection.
Example:
```
favorite_color coefficient = 0
student_name_encoded coefficient = 0
```
The model is saying:
```
This feature is not useful.
```
Scikit-learn describes Lasso as a linear model that estimates sparse coefficients with L1 regularization.

---
## 7. Ridge vs Lasso

|Point|Ridge Regression|Lasso Regression|
|---|---|---|
|Regularization type|L2|L1|
|Penalty|Squared coefficients|Absolute coefficients|
|Coefficients|Shrinks near zero|Can become exactly zero|
|Feature selection|Not direct|Yes, basic feature selection|
|Good when|Many features are useful|Some features are useless|
|Risk|Keeps all features|May remove useful features if alpha too high|
Simple rule:
```
Use Ridge when many features contribute.
Use Lasso when you suspect some features are useless.
```
---
## 8. What is Alpha?
`alpha` controls regularization strength.
```
alpha = 0      → almost no regularization
alpha small    → weak regularization
alpha large    → strong regularization
```
Scikit-learn states that larger `alpha` values specify stronger regularization for both Ridge and Lasso.
Effect:
```
Low alpha:
Model more flexible
Overfitting risk higher

High alpha:
Model more restricted
Underfitting risk higher
```
Balance is important.

---
## 9. Dataset for This Slot
Use this dataset:
![[Pasted image 20260612141044.png]]
![[Pasted image 20260612141104.png]]
Features:
```
study_hours
attendance
previous_score
practice_questions
sleep_hours
mobile_usage_hours
```
Label:
```
final_marks
```
---
## 10. Basic Linear Regression Baseline
![[Pasted image 20260612142524.png]]
![[Pasted image 20260612142539.png]]Why use `StandardScaler`?
```
Ridge and Lasso are affected by feature scale.
Scaling makes regularization fair across features.
```
---
## 11. Ridge Regression Code
![[Pasted image 20260612143355.png]]
```
alpha=1.0
```
means moderate regularization.

---
## 12. Lasso Regression Code
![[Pasted image 20260612143849.png]]
Why `max_iter=10000`?
```
Lasso sometimes needs more iterations to converge.
```
---
## 13. Compare Models
![[Pasted image 20260612144052.png]]
How to choose?
```
Lower MAE is better.
Lower RMSE is better.
Higher R² is better.
But avoid overfitting and unstable coefficients.
```
---
## 14. Print Coefficients

Pipeline stores the model inside the `"model"` step.
![[Pasted image 20260612144525.png]]
What to observe:
```
Ridge usually reduces coefficient size.y
Lasso may make some coefficients exactly 0.
```
If Lasso sets a coefficient to 0:
```
That feature is removed from the model mathematically.
```
---
## 15. Full Code: Linear vs Ridge vs Lasso
```Python
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "attendance": [40, 45, 50, 55, 60, 70, 75, 80, 85, 90, 95, 98],
    "previous_score": [35, 40, 45, 50, 55, 65, 70, 75, 82, 88, 92, 96],
    "practice_questions": [10, 20, 30, 40, 50, 65, 75, 85, 95, 110, 125, 140],
    "sleep_hours": [5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 7, 7],
    "mobile_usage_hours": [8, 7, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1],
    "final_marks": [38, 42, 48, 52, 58, 68, 72, 78, 84, 90, 94, 97]
}

df = pd.DataFrame(data)

X = df.drop("final_marks", axis=1)
y = df["final_marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

linear_pipeline = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

ridge_pipeline = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("model", Ridge(alpha=1.0))
])

lasso_pipeline = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("model", Lasso(alpha=0.1, max_iter=10000))
])

linear_pipeline.fit(X_train, y_train)
ridge_pipeline.fit(X_train, y_train)
lasso_pipeline.fit(X_train, y_train)

linear_pred = linear_pipeline.predict(X_test)
ridge_pred = ridge_pipeline.predict(X_test)
lasso_pred = lasso_pipeline.predict(X_test)

def evaluate_model(name, y_test, y_pred):
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    return {
        "Model": name,
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }

results = pd.DataFrame([
    evaluate_model("Linear Regression", y_test, linear_pred),
    evaluate_model("Ridge Regression", y_test, ridge_pred),
    evaluate_model("Lasso Regression", y_test, lasso_pred)
])

print("Model Comparison:")
print(results)

coef_df = pd.DataFrame({
    "Feature": X.columns,
    "Linear": linear_pipeline.named_steps["model"].coef_,
    "Ridge": ridge_pipeline.named_steps["model"].coef_,
    "Lasso": lasso_pipeline.named_steps["model"].coef_
})

print("\nCoefficient Comparison:")
print(coef_df)

print("\nActual:", y_test.values)
print("Linear Pred:", linear_pred)
print("Ridge Pred:", ridge_pred)
print("Lasso Pred:", lasso_pred)
```
---
## 16. Test Different Alpha Values
### For Ridge
![[Pasted image 20260612153756.png]]
![[Pasted image 20260612153852.png]]
![[Pasted image 20260612153929.png]]
### For Lasso :
![[Pasted image 20260612154917.png]]
![[Pasted image 20260612154938.png]]
![[Pasted image 20260612155023.png]]
Observe:
```
As alpha increases, regularization becomes stronger.
Lasso may push more coefficients to zero.
```
---
## 17. Ridge/Lasso with Polynomial Features
Ridge and Lasso are very useful when Polynomial Regression overfits.
Pipeline:
![[Pasted image 20260612160048.png]]
Meaning:
```
PolynomialFeatures creates complex features.
Ridge controls coefficient size.
Together, they reduce overfitting risk.
```
---
## 18. Production Thinking
For a real Student Marks Predictor, you should not pick a model only because it performs best once.
You should check:
```
Train MAE
Test MAE
Baseline MAE
Coefficient stability
Feature validity
Overfitting signs
Alpha tuning
Cross-validation
```
Best production mindset:
```
Choose the simplest model that gives stable test performance.
```
---
## 19. Debugging Section
### Bug 1: Forgetting Scaling with Ridge/Lasso
Bad:
```
model = Lasso(alpha=0.1)model.fit(X_train, y_train)
```
Why risky:
```
Features have different scales.Regularization may unfairly penalize large-scale/small-scale features.
```
Better:
```
Pipeline(steps=[    
	("scaler", StandardScaler()),    
	("model", Lasso(alpha=0.1, max_iter=10000))
])
```
---
### Bug 2: Alpha Too High
Bad:
```
Lasso(alpha=100)
```
Problem:
```
Regularization may be too strong.Model may underfit.Many coefficients may become zero.
```
Fix:
```
Try multiple alpha values and compare validation/test performance.
```
---
### Bug 3: Alpha Too Low
Bad mindset:
```
alpha = 0.000001 always best because it changes less.
```
Problem:
```
Too little regularization may not control overfitting.
```
Fix:
```
Tune alpha using validation or cross-validation.
```
---
### Bug 4: Lasso Convergence Warning
Possible warning:
```
ConvergenceWarning: Objective did not converge
```
Fix:
```
Lasso(alpha=0.1, max_iter=10000)
```
Also scaling helps.

---
### Bug 5: Misunderstanding Zero Coefficients
Wrong:
```
Lasso coefficient is zero, so feature is permanently useless.
```
Better:
```
For this dataset, scaling, alpha, and model setup, Lasso did not use that feature.It does not prove the feature is always useless.
```
---
## 20. Common Beginner Mistakes
```
1. Not scaling before Ridge/Lasso.
2. Thinking Ridge removes features.
3. Thinking Lasso always selects the correct features.
4. Using one alpha value only.
5. Choosing alpha based only on training error.
6. Using very high alpha and causing underfitting.
7. Using very low alpha and not reducing overfitting.
8. Ignoring convergence warnings.
9. Comparing coefficients without scaling.
10. Thinking regularization fixes bad data.
```
---
## 21. Interview Questions
Prepare answers:
```
1. What is regularization?
2. Why do we need regularization?
3. What is Ridge Regression?
4. What is Lasso Regression?
5. Difference between L1 and L2 regularization?
6. What is alpha?
7. What happens when alpha increases?
8. Can Ridge make coefficients exactly zero?
9. Why can Lasso be used for feature selection?
10. Why should features be scaled before Ridge/Lasso?
```
---
## 22. Interview Trap Questions
### Trap 1
Question:
```
Does Ridge remove features?
```
Answer:
```
Usually no. Ridge shrinks coefficients toward zero but typically does not make them exactly zero.
```
### Trap 2
Question:
```
Can Lasso make coefficients exactly zero?
```
Answer:
```
Yes. Lasso uses L1 regularization and can shrink some coefficients exactly to zero, which can act like feature selection.
```
### Trap 3
Question:
```
If alpha is very large, is the model always better?
```
Answer:
```
No. Very large alpha can over-regularize the model and cause underfitting.
```
---
## 23. Mini Assignment Before Next Slot
Complete before saying **NEXT SLOT**:
```
Task 1:
Run Linear Regression, Ridge Regression, and Lasso Regression.

Task 2:
Use StandardScaler inside Pipeline for all three.

Task 3:
Print:
MAE
RMSE
R²

Task 4:
Print coefficient comparison table.

Task 5:
Try Ridge alpha:
0.001, 0.01, 0.1, 1, 10, 100

Task 6:
Try Lasso alpha:
0.001, 0.01, 0.1, 1, 10

Task 7:
Identify which alpha gives best MAE.

Task 8:
Check which Lasso coefficients become zero.

Task 9:
Write 5 lines explaining Ridge vs Lasso.

Task 10:
Write why scaling is important before regularization.
```
---
## 24. Real-World Challenge
You are building:
```
AI Student Marks Predictor
```
You compare models:
```
Linear Regression:
Train MAE = 1.2
Test MAE = 9.8

Ridge alpha=1:
Train MAE = 2.5
Test MAE = 4.3

Lasso alpha=0.1:
Train MAE = 3.0
Test MAE = 4.8
```
Answer:
```
1. Which model is overfitting?
2. Which model is best for test performance?
3. Why did Ridge increase train error but reduce test error?
4. Which model may remove weak features?
5. Which model would you choose and why?
6. What output range would you show if Ridge prediction = 78 and MAE = 4.3?
```

Expected thinking:

```
Linear Regression is overfitting.Ridge has best test MAE.Ridge improves generalization by controlling coefficient size.Output range: about 74–82.
```
---
## 25. Cheat Sheet
```
Regularization:
Technique to reduce overfitting by penalizing large coefficients.

Ridge Regression:
Linear Regression + L2 penalty.
Shrinks coefficients toward zero.

Lasso Regression:
Linear Regression + L1 penalty.
Can shrink coefficients exactly to zero.

Alpha:
Regularization strength.

Low alpha:
Weak regularization.

High alpha:
Strong regularization.

Too low alpha:
Overfitting risk.

Too high alpha:
Underfitting risk.

Ridge:
Good when many features are useful.

Lasso:
Good when some features may be useless.

Scaling:
Important before Ridge/Lasso.
```
---
## 26. Mind Map
```
Regularization
│
├── Problem
│   └── Overfitting
│
├── Idea
│   └── Penalize large coefficients
│
├── Ridge
│   ├── L2 regularization
│   ├── squared coefficient penalty
│   └── shrinks coefficients
│
├── Lasso
│   ├── L1 regularization
│   ├── absolute coefficient penalty
│   └── can set coefficients to zero
│
├── Alpha
│   ├── small → weak regularization
│   ├── large → strong regularization
│   └── too large → underfitting
│
├── Best Practice
│   ├── scale features
│   ├── compare train/test error
│   ├── tune alpha
│   └── use Pipeline
│
└── Production
    ├── stable model
    ├── lower test error
    └── no overconfident prediction
```
---
