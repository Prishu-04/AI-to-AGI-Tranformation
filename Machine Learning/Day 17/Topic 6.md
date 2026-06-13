# Tree-Based Regression Basics
#### DecisionTreeRegressor + RandomForestRegressor + Residual Analysis
## 1. Goal
 ```
 1. What tree-based regression is
2. How DecisionTreeRegressor works
3. How RandomForestRegressor works
4. Why decision trees can overfit
5. Why random forests usually perform better than a single tree
6. How to compare Linear, Ridge, Lasso, Decision Tree, and Random Forest
7. How to perform deeper residual analysis
8. Which datasets are good for regression practice
 ```
 ---
## 2. What is Tree-Based Regression? 
Tree-based regression predicts a **number** using decision rules.
Example:
```
If study_hours <= 4:    
	predict lower marks
If study_hours > 4 and attendance > 75:    
	predict higher marks
```
A decision tree works like a flowchart.
Example:
```
Is study_hours > 5?
│
├── Yes
│   └── Is attendance > 75?
│       ├── Yes → Predict 85 marks
│       └── No  → Predict 70 marks
│
└── No    
	└── Predict 50 marks
```
Unlike Linear Regression, a tree does not need a straight-line relationship.

---
## 3. DecisionTreeRegressor Basics
`DecisionTreeRegressor` is used for regression problems where the output is numerical.
It splits the data into groups based on feature values.
Example features:
```
study_hours
attendance
previous_score
practice_questions
sleep_hours
```
Target:
```
final_marks
```
A decision tree tries to split students into groups where students in the same group have similar final marks.
Scikit-learn’s decision tree regression example shows that if `max_depth` is too high, the tree can learn fine details and noise from the training data, which causes overfitting.

---
## 4. Decision Tree Important Parameters

| Parameter           | Meaning                         | Beginner Use         |
| ------------------- | ------------------------------- | -------------------- |
| `max_depth`         | Maximum depth of tree           | Controls overfitting |
| `min_samples_split` | Minimum samples needed to split | Prevents tiny splits |
| `min_samples_leaf`  | Minimum samples in leaf node    | Makes tree smoother  |
| `random_state`      | Reproducibility                 | Keep fixed           |
Most important for now:
```
max_depth
```
If `max_depth` is too high:
```
Tree becomes too complexTraining error becomes very lowTest error may become highOverfitting risk increases
```
If `max_depth` is too low:
```
Tree becomes too simpleTrain error highTest error highUnderfitting risk increases
```
---
## 5. RandomForestRegressor Basics
A Random Forest is a group of many decision trees.
Instead of trusting one tree, it trains many trees and averages their predictions.
Simple idea:
```
One decision tree = one opinion
Random forest = average opinion of many trees
```
Example:
```
Tree 1 predicts 78
Tree 2 predicts 82
Tree 3 predicts 80
Tree 4 predicts 79
Tree 5 predicts 81
Random Forest prediction = average = 80
```
This averaging usually makes predictions more stable.

---
## 6. Why Random Forest Often Beats One Tree
A single decision tree can overfit easily.
Random Forest reduces that risk because:
```
It trains many trees
Each tree sees slightly different data
Each tree may learn different patterns
Final prediction is averaged
Averaging reduces instability
```
Important parameters:

|Parameter|Meaning|
|---|---|
|`n_estimators`|Number of trees|
|`max_depth`|Maximum depth of each tree|
|`random_state`|Reproducibility|
|`min_samples_leaf`|Minimum samples per leaf|
Common beginner setting:
```
RandomForestRegressor(    
	n_estimators=100,    
	max_depth=5,    
	random_state=42
)
```
---
## 7. Dataset for This Bonus Slot
![[Pasted image 20260613093224.png]]
![[Pasted image 20260613093241.png]]

---
## 8. Train DecisionTreeRegressor
![[Pasted image 20260613094338.png]]
![[Pasted image 20260613094409.png]]

---
## 9. Train RandomForestRegressor
![[Pasted image 20260613095804.png]]
Important:
```
Tree-based models usually do not require feature scaling.
```
Why?
```
They split based on feature thresholds.
They do not depend on distance or gradient scale like KNN, SVM, Ridge, or Lasso.
```
---
## 10. Model Comparison with Tree Regressors
Now compare all regression models:
![[Pasted image 20260613102441.png]]
![[Pasted image 20260613103038.png]]
![[Pasted image 20260613103220.png]]
How to choose best model:
```
Lower MAE is better.
Lower RMSE is better.
Higher R² is better.
But also check overfitting, stability, and simplicity.
```
---
## 11. Train Error vs Test Error
To detect overfitting, compare train and test MAE.
![[Pasted image 20260613103503.png]]
How to read:
```
Low train MAE + high test MAE = overfitting
High train MAE + high test MAE = underfitting
Low train MAE + low test MAE = good fit
```
---
## 12. Residual Analysis Deeper
Residual means:
```
Residual = Actual - Predicted
```
Create a residual table for the best model.
![[Pasted image 20260613103717.png]]

---
## 13. How to Interpret Residuals
Look for these patterns:

|Residual Pattern|Meaning|
|---|---|
|Residuals close to 0|Good predictions|
|Large positive residual|Model underpredicted|
|Large negative residual|Model overpredicted|
|Errors bigger for high marks|Model struggles with top performers|
|Errors bigger for low marks|Model struggles with weak students|
|Random residuals|Better sign|
|Patterned residuals|Model missing some relationship|
Example:
```
Actual = 95
Predicted = 82
Residual = 13
```
Meaning:
```
Model underpredicted by 13 marks.
```
Example:
```
Actual = 50
Predicted = 65
Residual = -15
```
Meaning:
```
Model overpredicted by 15 marks.
```
---
## 14. Residual Analysis Summary Code
![[Pasted image 20260613103932.png]]
Interpretation:
```
Residual mean close to 0 is good.
High maximum absolute error means model has some large mistakes.
Average absolute error equals MAE.
```
---
## 15. Feature Importance in Tree Models
Tree-based models can show feature importance.
![[Pasted image 20260613104140.png]]
Meaning:
```
Higher importance means the feature was more useful for tree splits.
```
But be careful:
```
Feature importance is model-based, not absolute truth.
It can change with data, model settings, and correlated features.
```

---
## 16. Dataset Ideas for Regression Practice
### 1. House Price Prediction
Target:
```
house_price
```
Features:
```
area_sqft
bedrooms
bathrooms
location
house_age
parking
distance_from_city_center
```
Models to try:
```
Linear Regression
Ridge
Lasso
DecisionTreeRegressor
RandomForestRegressor
```
Good learning:
```
Feature encoding
Outlier handling
Price prediction
Residual analysis
```
---
### 2. Car Price Prediction
Target:
```
car_price
```
Features:
```
brandmodel
year
kilometers_driven
fuel_type
transmission
owner_type
engine_cc
mileage
```
Good learning:
```
Categorical encoding
Feature scaling
Tree models
Random forest comparison
```
---
## 3. Medical Insurance Cost Prediction
Target:
```
insurance_cost
```
Features:
```
age
bmi
children
smoker
region
medical_history_score
exercise_level
```
Good learning:
```
Ethical ML thinking
Outlier handling
High-cost prediction
MAE/RMSE interpretation
```
Important caution:
```
Medical predictions are high-risk.
Use such projects for learning, 
not real medical decisions.
```
---
## 17. Complete Bonus Slot Code
Use this full code if you want one final file:

```Python
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 3.5, 6.5, 8.5],
    "attendance": [40, 45, 50, 55, 60, 70, 75, 80, 85, 90, 95, 98, 58, 72, 88],
    "previous_score": [35, 40, 45, 50, 55, 65, 70, 75, 82, 88, 92, 96, 48, 68, 84],
    "sleep_hours": [5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 7, 7, 6, 7, 8],
    "practice_questions": [10, 20, 30, 40, 50, 65, 75, 85, 95, 110, 125, 140, 35, 70, 105],
    "final_marks": [38, 42, 48, 52, 58, 68, 72, 78, 84, 90, 94, 97, 51, 70, 87]
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

models = {
    "Linear Regression": Pipeline(steps=[
        ("scaler", StandardScaler()),
        ("model", LinearRegression())
    ]),

    "Ridge Regression": Pipeline(steps=[
        ("scaler", StandardScaler()),
        ("model", Ridge(alpha=1.0))
    ]),

    "Lasso Regression": Pipeline(steps=[
        ("scaler", StandardScaler()),
        ("model", Lasso(alpha=0.1, max_iter=10000))
    ]),

    "Polynomial Ridge": Pipeline(steps=[
        ("poly", PolynomialFeatures(degree=2, include_bias=False)),
        ("scaler", StandardScaler()),
        ("model", Ridge(alpha=1.0))
    ]),

    "Decision Tree": DecisionTreeRegressor(
        max_depth=3,
        random_state=42
    ),

    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        max_depth=5,
        random_state=42
    )
}

results = []
overfit_results = {}

for name, model in models.items():
    model.fit(X_train, y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    train_mae = mean_absolute_error(y_train, train_pred)
    test_mae = mean_absolute_error(y_test, test_pred)
    test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))
    test_r2 = r2_score(y_test, test_pred)

    results.append({
        "Model": name,
        "Train MAE": train_mae,
        "Test MAE": test_mae,
        "RMSE": test_rmse,
        "R2": test_r2,
        "Train-Test Gap": test_mae - train_mae
    })

results_df = pd.DataFrame(results).sort_values("Test MAE")

print("Model Comparison:")
print(results_df)

best_model_name = results_df.iloc[0]["Model"]
best_model = models[best_model_name]

best_pred = best_model.predict(X_test)

residual_df = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": best_pred
})

residual_df["Residual"] = residual_df["Actual"] - residual_df["Predicted"]
residual_df["Absolute_Error"] = abs(residual_df["Residual"])
residual_df["Squared_Error"] = residual_df["Residual"] ** 2

print("\nBest Model:", best_model_name)
print("\nResidual Analysis:")
print(residual_df)

print("\nResidual Summary:")
print("Residual Mean:", residual_df["Residual"].mean())
print("Average Absolute Error:", residual_df["Absolute_Error"].mean())
print("Maximum Absolute Error:", residual_df["Absolute_Error"].max())

forest_model = models["Random Forest"]
forest_model.fit(X_train, y_train)

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": forest_model.feature_importances_
}).sort_values("Importance", ascending=False)

print("\nRandom Forest Feature Importance:")
print(importance_df)

new_student = pd.DataFrame({
    "study_hours": [7],
    "attendance": [85],
    "previous_score": [75],
    "sleep_hours": [7],
    "practice_questions": [90]
})

prediction = best_model.predict(new_student)[0]
best_mae = results_df.iloc[0]["Test MAE"]

print("\nNew Student Prediction:")
print("Predicted Marks:", prediction)
print(f"Expected Marks Range: {prediction - best_mae:.0f} to {prediction + best_mae:.0f}")
```
---
## 18. Debugging Notes
### Error 1: RandomForestRegressor Not Imported
Wrong:
```
forest_model = RandomForestRegressor()
```
Error:
```
NameError: name 'RandomForestRegressor' is not defined
```
Fix:
```
from sklearn.ensemble import RandomForestRegressor
```
---
## Error 2: Decision Tree Overfitting
Bad:
```
DecisionTreeRegressor(random_state=42)
```
Problem:
```
Without max_depth, tree may grow too deep and overfit.
```
Better:
```
DecisionTreeRegressor(max_depth=3, random_state=42)
```
---
## Error 3: Wrong Target Column
Wrong:
```
X = df
y = df["final_marks"]
```
Problem:
```
final_marks is inside X.
This causes data leakage.
```
Correct:
```
X = df.drop("final_marks", axis=1)
y = df["final_marks"]
```
---
## Error 4: Feature Mismatch During Prediction
Wrong:
```
new_student = pd.DataFrame({    
	"study_hours": [7],    
	"attendance": [85],    
	"previous_score": [75]
})
```
Problem:
```
Training used 5 features, but prediction input has only 3.
```
Correct:
```
new_student = pd.DataFrame({    
	"study_hours": [7],    
	"attendance": [85],    
	"previous_score": [75],    
	"sleep_hours": [7],    
	"practice_questions": [90]
})
```
---
## 19. Interview Questions
Prepare these:
```
1. What is DecisionTreeRegressor?
2. How does a decision tree make regression predictions?
3. Why can decision trees overfit?
4. What does max_depth do?
5. What is RandomForestRegressor?
6. Why is Random Forest better than a single tree?
7. Do tree-based models require scaling?
8. What is residual analysis?
9. How do you identify underprediction and overprediction?
10. How do you compare regression models?
```
Strong answers:
```
DecisionTreeRegressor predicts numerical values by splitting data into regions based on feature thresholds.
```

```
RandomForestRegressor trains multiple decision trees and averages their predictions, which usually improves stability and reduces overfitting compared to a single tree.
```

```
Residual analysis means studying actual minus predicted values to understand where and how the model makes mistakes.
```
---
## 20. Mini Assignment
Complete:
```
Task 1:Create the student marks dataset.

Task 2:Train:
	Linear Regression
	Ridge
	Lasso
	Polynomial Ridge
	DecisionTreeRegressor
	RandomForestRegressor

Task 3:Calculate:
	Train MAE
	Test MAE
	RMSE
	R²
	Train-Test Gap
	
Task 4:Sort models by Test MAE.

Task 5:Select the best model.

Task 6:Create residual table:
	Actual
	Predicted
	Residual
	Absolute_Error
	Squared_Error

Task 7:Print residual summary.

Task 8:Print Random Forest feature importance.

Task 9:Predict marks for a new student.

Task 10:Show expected marks range using best model MAE.
```
---
