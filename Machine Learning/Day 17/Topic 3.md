# Regression Evaluation Metrics: MAE, MSE, RMSE, and R² Score
## 1. Goal
```
1. Why regression evaluation matters
2. Actual vs predicted values
3. Error / residual
4. MAE
5. MSE
6. RMSE
7. R² Score
8. Which metric to use
9. How to compare regression models
10. Common evaluation mistakes
```
---
## 2. Why Evaluation Matters
Training a model is not enough.
A beginner asks:
```
Did my model run?
```
A real ML engineer runs:
```
How wrong is my model?
Is the error acceptable?
Is the model better than a simple baseline?
Is the model overfitting?
Can this model be trusted in production?
```
For regression, we do not accuracy because the output is a continuous number.
Example:
```
Actual marks =80
Predicted marks=78.5
```
This is not "correct" or "wrong" like classification. Instead, we measure how far the prediction is from actual value.

---
## 3. Actual vs Predicted
Example:
![[Pasted image 20260612101104.png]]
The model is making numerical predeictions.
Now we ask:
```
How much error does the model make?
```
---
# 4. Error / Residual
Error means:
```
Error = Actual - Predicted
```
Example:
```
Actual = 80
Predicted = 78
Error = 80 - 78 = 2
```
Another example:
```
Actual = 65
Predicted = 70
Error = 65 - 70 = -5
```
Positive error:
```
Model predicted lower than actual.
```
Negative error:
```
Model predicted higher than actual.
```
In regression, error is also called:
```
Residual
```
---
## 5. Why We Need Metrics
If we simply add errors:
```
2 + (-5) + 5 + (-5) = -3
```
Positive and negative errors cancel each other.
That is why we use metrics like:
```
MAE
MSE
RMSE
R² Score
```
---
## 6. MAE — Mean Absolute Error
MAE means:
```
Average absolute error or Mean Absolute Error
```
Formula:
```
MAE = average of |Actual - Predicted|
```
Example:

| Actual | Predicted | Absolute Error |
| ------ | --------- | -------------- |
| 80     | 78        | 2              |
| 65     | 70        | 5              |
| 90     | 85        | 5              |
| 50     | 55        | 5              |
```
MAE = (2 + 5 + 5 + 5) / 4
MAE = 17 / 4
MAE = 4.25
```
Meaning:
```
On average, the model is wrong by 4.25 marks.
```
Scikit-learn defines `mean_absolute_error` as a non-negative regression loss where the best possible value is `0.0`.

---
## 7. When MAE is Useful
MAE is easy to explain.
For a marks prediction system:
```
MAE = 4
```
Means:
```
The model is wrong by around 4 marks on average.
```
This is business-friendly.
Good for:
```
Marks predictionPrice predictionSalary predictionDelivery time predictionMedical cost prediction
```
MAE is usually your first regression metric.

---
## 8. MSE — Mean Squared Error
MSE means:
```
Average squared error or Mean Squared Error
```
Formula:
```
MSE = average of (Actual - Predicted)²
```
Example:

|Actual|Predicted|Error|Squared Error|
|---|---|---|---|
|80|78|2|4|
|65|70|-5|25|
|90|85|5|25|
|50|55|-5|25|
```
MSE = (4 + 25 + 25 + 25) / 4
MSE = 79 / 4
MSE = 19.75
```
MSE punishes large errors more strongly because errors are squared. Scikit-learn provides `mean_squared_error` as a regression loss function.

---
## 9. Why MSE Punishes Big Errors
Compare two errors:
```
Error = 2
Squared error = 4
```

```
Error = 10
Squared error = 100
```
So one large mistake affects MSE a lot.
Use MSE when:
```
Large errors are very bad
You want to punish big mistakes strongly
```
Example:
```
Medical dosage prediction
Financial risk prediction
Demand forecasting
```
---
## 10. RMSE — Root Mean Squared Error
RMSE means:
```
Square root of MSE 
```
Formula:
```
RMSE = √MSE
```
From above:
```
MSE = 19.75
RMSE = √19.75
RMSE ≈ 4.44
```
RMSE is useful because it comes back to the original unit.
For marks:
```
RMSE = 4.44 marks
```
Meaning:
```
Model error is around 4.44 marks, with bigger mistakes punished more than MAE.
```
---
## 11. MAE vs RMSE

|Point|MAE|RMSE|
|---|---|---|
|Meaning|Average absolute error|Root average squared error|
|Unit|Same as target|Same as target|
|Easy to explain|Very easy|Medium|
|Punishes big errors|Less|More|
|Best for|General interpretation|When large errors matter|
Simple rule:
```
Use MAE when you want easy business explanation.
Use RMSE when large errors should be punished more.
```
---
## 12. R² Score
R² Score tells how much variation in the target is explained by the model.
Best value:
```
1.0
```
Meaning:
```
Perfect prediction
```
Common interpretation:
```
R² = 0.85
```
Means:
```
Model explains around 85% of the variance in the target.
```
Scikit-learn describes `r2_score` as the coefficient of determination, with best possible score `1.0`; it can also be negative if the model is worse than a simple baseline.

---
## 13. R² Score Interpretation

| R² Score | Meaning                       |
| -------- | ----------------------------- |
| 1.0      | Perfect model                 |
| 0.8      | Strong model in many cases    |
| 0.5      | Moderate model                |
| 0.0      | Similar to predicting average |
| Negative | Worse than predicting average |
Important:
```
High R² does not always mean the model is production-ready.
```
You still need to check:
```
MAE/RMSE
Data leakage
Outliers
Business risk
Test performance
Residual patterns
```
---
## 14. Dataset for This Slot
![[Pasted image 20260612103913.png]]

---
## 15. Full Code: Train Model + Calculate Metrics

```Python
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

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
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("Actual:", y_test.values)
print("Predicted:", y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)
```
![[Pasted image 20260612104941.png]]

---
## 16. Create Actual vs Predicted Table
Add this:
![[Pasted image 20260612105004.png]]
This is very important for understanding metrics.

---
## 17. Manual Metric Calculation
You can calculate MAE manually:
![[Pasted image 20260612105149.png]]
MSE manually:
![[Pasted image 20260612105337.png]]
RMSE manually:
![[Pasted image 20260612105450.png]]
This helps you understand what scikit-learn is doing internally.

---
## 18. How to Judge the Metrics
For Student Marks Prediction:
```
MAE = 2 to 5 marks → good for beginner project
MAE = 5 to 10 marks → acceptable, needs improvement
MAE > 10 marks → weak model
```
But this depends on:
```
dataset size
data quality
feature quality
exam difficulty
target range
business use case
```
For final marks out of 100:
```
MAE = 3 
means average error of 3 marks.
```
That is easy to explain.

---
## 19. Model Comparison Example
Suppose you train two models:

| Model   | MAE | RMSE | R²   |
| ------- | --- | ---- | ---- |
| Model A | 6.5 | 8.2  | 0.72 |
| Model B | 3.8 | 5.1  | 0.89 |
Better model:
```
Model B
```

Why?
```
Lower MAE
Lower RMSE
Higher R²
```
But also check:
```
Is Model B overfitting?
Does it work on test data?
Is the dataset leakage-free?
Is it stable on new data?
```
---
## 20. Baseline Model
A baseline model is a simple model used for comparison.
For regression, a simple baseline is:
```
Always predict average final_marks
```
Code:

```
baseline_prediction = y_train.mean()baseline_preds = [baseline_prediction] * len(y_test)baseline_mae = mean_absolute_error(y_test, baseline_preds)print("Baseline Prediction:", baseline_prediction)print("Baseline MAE:", baseline_mae)
```
Your ML model should beat this baseline.
If it does not, your model is not useful yet.

---
## 21. Production Thinking
In real product:
```
Do not only show prediction.
Also understand confidence/error range.
```
Example product output:
```
Predicted marks: 78
Expected error range: ±4 marks
Possible range: 74–82
```
If MAE is 4:
```
prediction = 78
mae = 4
print(f"Expected marks range: {prediction - mae:.0f} to {prediction + mae:.0f}")
```
This is much safer than:
```
Your marks will be exactly 78.
```
---
## 22. Debugging Section
### Bug 1: Using Accuracy for Regression
Wrong:
```Python
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
```
Why wrong:
```
Regression outputs continuous values.
Accuracy is for classification labels.
```
Correct:
```
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test, y_pred)
```
---
### Bug 2: Forgetting Predictions
Wrong:
```
mae = mean_absolute_error(y_test)
```
Error:
```
missing required argument y_pred
```
Correct:
```
mae = mean_absolute_error(y_test, y_pred)
```
---
### Bug 3: Shape Mismatch
Wrong:
```
mae = mean_absolute_error(y_train, y_pred)
```
Problem:
```
y_train has training rows.y_pred has test prediction rows.Lengths do not match.
```
Correct:
```
mae = mean_absolute_error(y_test, y_pred)
```
---
### Bug 4: RMSE Function Confusion
Some scikit-learn versions may not have a separate `root_mean_squared_error` import depending on version.
Safe method:
```
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
```
---
### Bug 5: Misinterpreting R²
Wrong:
```
R² = 0.90 means model is 90% accurate.
```
Correct:
```
R² = 0.90 means the model explains around 90% of the variance in the target, not classification accuracy.
```
---
## 23. Common Beginner Mistakes
```
1. Using accuracy for regression.
2. Looking only at R² and ignoring MAE.
3. Thinking low training error means good model.
4. Not comparing against baseline.
5. Not checking actual vs predicted values.
6. Confusing MSE and RMSE.
7. Saying R² is accuracy.
8. Using y_train with y_pred from X_test.
9. Not interpreting metric in business units.
10. Giving exact prediction without error range.
```
---
## 24. Interview Questions
Prepare answers:
```
1. Why do we need regression metrics?
2. What is MAE?
3. What is MSE?
4. What is RMSE?
5. What is R² Score?
6. Difference between MAE and RMSE?
7. Why does MSE punish large errors?
8. Can R² be negative?
9. Why is accuracy wrong for regression?
10. What is a baseline model?
```
---
## 25. Interview Trap Questions
### Trap 1
Question:
```
Is R² the same as accuracy?
```
Answer:
```
No. R² measures how much variance in the target is explained by the regression model. Accuracy is a classification metric.
```
### Trap 2
Question:
```
Can R² be negative?
```
Answer:
```
Yes. It can be negative when the model performs worse than a simple baseline that predicts the average target value.
```
### Trap 3
Question:
```
Which is easier to explain to business users: MAE or MSE?
```
Answer:
```
MAE is usually easier because it is in the same unit as the target and directly means average absolute error.
```
---
# 26. Mini Assignment Before Next Slot
Complete before saying **NEXT SLOT**:
```
Task 1:Run the full metric code.

Task 2: Print:
	ActualPredictedError
	Absolute_ErrorSquared_Error

Task 3: Calculate:
	MAE
	MSE
	RMSE
	R² Score

Task 4: Calculate MAE, MSE, RMSE manually from results DataFrame.

Task 5: Create baseline model that always predicts average y_train.

Task 6: Compare:
	Model MAE vs Baseline MAE
	
Task 7:Write what MAE means in marks.

Task 8:Write why R² is not accuracy.
```
---
## 27 Real-World Challenge
You built a Student Marks Predictor.
Your model results:
```
MAE = 4.2
RMSE = 6.8
R² = 0.86
Baseline MAE = 9.5
```
Answer:
```
1. Is your model better than baseline?
2. What does MAE = 4.2 mean?
3. Why is RMSE higher than MAE?
4. Is R² = 0.86 good?
5. What output range should you show if prediction = 78?
6. What should you check before deployment?
```
Expected product output:
```
Predicted marks: 78
Expected range: 74–82
```
---
## 28. Cheat Sheet
```
Error:
Actual - Predicted

MAE:
Average absolute error.
Lower is better.
Best = 0.

MSE:
Average squared error.
Lower is better.
Punishes large errors.

RMSE:
Square root of MSE.
Lower is better.
Same unit as target.

R² Score:
Variance explained by model.
Best = 1.
Can be negative.

Baseline:
Simple comparison model, often predicts mean target.

Regression metrics:
MAE, MSE, RMSE, R²

Classification metrics:
Accuracy, Precision, Recall, F1
```
---
## 29. Mind Map
```
Regression Evaluation
│
├── Actual vs Predicted
│
├── Error / Residual
│   └── Actual - Predicted
│
├── Metrics
│   ├── MAE
│   │   └── average absolute error
│   ├── MSE
│   │   └── average squared error
│   ├── RMSE
│   │   └── square root of MSE
│   └── R² Score
│       └── variance explained
│
├── Model Comparison
│   ├── lower MAE better
│   ├── lower RMSE better
│   └── higher R² better
│
├── Baseline
│   └── predict average target
│
└── Production
    ├── prediction range
    ├── error awareness
    └── no overconfident exact output
```
---
