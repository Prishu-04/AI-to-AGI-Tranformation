# Support Vector Regression — SVR
## 1. Why SVR matters
So far, SVM was used for **classification** using `SVC`.
Now we use the same SVM idea for **regression** using `SVR`.
Scikit-learn defines `SVR` as **epsilon-Support Vector Regression**. Its important free parameters include `C` and `epsilon`, and it supports kernels such as `linear`, `poly`, `rbf`, `sigmoid`, and `precomputed`. The implementation is based on `libsvm`, and standard `SVR` can become expensive because fit-time complexity is more than quadratic in the number of samples. For larger datasets, scikit-learn suggests `LinearSVR` or `SGDRegressor` alternatives.
### Industry applications
SVR can be used for:
- House price prediction
- Stock or crypto price trend modelling
- Energy demand forecasting
- Medical cost prediction
- Weather-related numerical prediction
- Manufacturing defect severity prediction
- Sensor-value prediction
- Small/medium nonlinear regression problems
### Interview relevance
SVR tests your understanding of:
- Regression beyond Linear/Ridge/Lasso
- Margin-based regression
- Epsilon-insensitive loss
- Kernels in regression
- `C`, `epsilon`, and `gamma`
- Scaling
- Overfitting and underfitting
- Why SVR may be slow in production
### Startup relevance
SVR is useful when a startup has:
- Limited data
- Strong numerical features
- Nonlinear relationships
- Need for a strong classical ML baseline
- No need yet for deep learning
Example:

> A real-estate startup has 3,000 cleaned property records and wants a nonlinear house-price estimator. Before using XGBoost or neural networks, SVR can be tested as a strong baseline.

---
## 2. SVR vs SVC

| Concept             | SVC                                  | SVR                                         |
| ------------------- | ------------------------------------ | ------------------------------------------- |
| Task                | Classification                       | Regression                                  |
| Output              | Class label                          | Continuous number                           |
| Goal                | Separate classes with maximum margin | Fit a function with allowed error tolerance |
| Important parameter | `C`, `gamma`, kernel                 | `C`, `epsilon`, `gamma`, kernel             |
| Loss idea           | Hinge loss                           | Epsilon-insensitive loss                    |
Simple intuition:
```
SVC:Draw the best boundary between classes.
SVR:Draw the best prediction curve while ignoring small errors inside a tolerance tube.
```
---
## 3. Core intuition: epsilon tube
Linear Regression tries to minimize every error.
SVR says:
> “Small prediction errors are acceptable. I will only punish errors larger than a chosen tolerance.”

That tolerance is called:
						`ϵ`
Imagine a tube around the prediction line:
```
              points outside tube get penalty
                      x
                    /
      +ε tube  ------------------
prediction line ------------------
      -ε tube  ------------------
              x
        points inside tube are ignored
```
If a data point falls inside the tube, the error is treated as zero.
If it falls outside, only the amount beyond the tube is penalized.

---
## 4. SVR mathematics
![[Pasted image 20260629142446.png]]
Suppose:
						`ϵ=2`

| Actual | Predicted | Absolute Error | SVR Loss |
| ------ | --------- | -------------- | -------- |
| 100    | 101       | 1              | 0        |
| 100    | 102       | 2              | 0        |
| 100    | 105       | 5              | 3        |
Why loss is 3 in the last row:
5−2=3

---
## 5. Meaning of `epsilon`
`epsilon` controls the width of the no-penalty tube.
### Small `epsilon`
```
Narrow tube
More errors penalized
Model tries to fit points more tightly
Higher overfitting risk
```
### Large `epsilon`
```
Wide tube
More errors ignored
Simpler model
Higher underfitting risk
```
Practical intuition:
```
SVR(epsilon=0.01)  # tight tube
SVR(epsilon=0.1)   # common starting point
SVR(epsilon=1.0)   # wide tube
```
---
## 6. Meaning of `C` in SVR
`C` controls how strongly the model punishes errors outside the epsilon tube.
### Small `C`
- More tolerance for errors
- Smoother function
- More regularization
- Possible underfitting
### Large `C`
- Strong penalty for errors
- Model tries harder to fit training data
- More complex function
- Possible overfitting
Same trap as SVC:
> Larger `C` does **not** mean stronger regularization.  
> Larger `C` means the model penalizes errors more strongly, so effective regularization becomes weaker.

The official SVM guide explains that `C` controls the trade-off between decision-function simplicity and training errors, and RBF models also require careful attention to `gamma`.

---
## 7. Meaning of `gamma` in SVR
`gamma` matters for nonlinear kernels, especially:
- `rbf`
- `poly`
- `sigmoid`
For RBF SVR:
![[Pasted image 20260629142652.png|283]]
### Small `gamma`
- Each point has broad influence
- Smoother regression curve
- Possible underfitting
### Large `gamma`
- Each point has local influence
- Wiggly curve
- Possible overfitting
Dangerous setting:
```
SVR(kernel="rbf", C=1000, gamma=100, epsilon=0.01)
```
This can memorize noise.
Better starting point:
```
SVR(kernel="rbf", C=1.0, gamma="scale", epsilon=0.1)
```
---
## 8. Linear SVR, Polynomial SVR, RBF SVR
Scikit-learn’s official SVR example demonstrates Support Vector Regression with **linear, polynomial, and RBF kernels** on a toy regression problem.
### Linear SVR
Use when:
- Relationship is mostly linear
- Dataset is larger
- You need faster training
- Interpretability matters more
```
SVR(kernel="linear")
```
or for larger linear problems:
```
LinearSVR()
```
`LinearSVR` is implemented differently from kernel `SVR` and scales better for a large number of samples when a linear model is enough.
### Polynomial SVR
Use when:
- Relationship has polynomial curvature
- Feature interactions matter
- You want controlled nonlinear complexity
```
SVR(kernel="poly", degree=3)
```
Risk:
- High degree can overfit.
- Training can become slow.
### RBF SVR
Use when:
- Relationship is nonlinear
- You do not know the exact curve shape
- Dataset is small or medium-sized
- You want a strong nonlinear baseline
```
SVR(kernel="rbf")
```
Risk:
- Can overfit with high `C` and high `gamma`.
- Can be slow on large datasets.
---
## 9. Code Implementation
### Part A - Synthetic NonLinear Regression
```Python
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR, LinearSVR
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ---------------------------------------------------------
# 1. Create nonlinear regression data
# ---------------------------------------------------------
np.random.seed(42)

X = np.sort(6 * np.random.rand(300, 1), axis=0)
y = np.sin(X).ravel() + 0.15 * np.random.randn(300)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)


# ---------------------------------------------------------
# 2. Evaluation function
# ---------------------------------------------------------
def evaluate_regression_model(name, model, X_train, X_test, y_train, y_test):
    start_train = time.time()
    model.fit(X_train, y_train)
    train_time = time.time() - start_train

    start_pred = time.time()
    y_pred = model.predict(X_test)
    pred_time = time.time() - start_pred

    y_train_pred = model.predict(X_train)

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))

    return {
        "model": name,
        "train_rmse": train_rmse,
        "test_mae": mean_absolute_error(y_test, y_pred),
        "test_rmse": rmse,
        "test_r2": r2_score(y_test, y_pred),
        "generalization_gap_rmse": rmse - train_rmse,
        "training_time_sec": train_time,
        "prediction_time_sec": pred_time
    }


# ---------------------------------------------------------
# 3. Define models
# ---------------------------------------------------------
models = {
    "Linear Regression": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LinearRegression())
    ]),

    "Ridge": Pipeline([
        ("scaler", StandardScaler()),
        ("model", Ridge(alpha=1.0))
    ]),

    "Lasso": Pipeline([
        ("scaler", StandardScaler()),
        ("model", Lasso(alpha=0.001, max_iter=10000))
    ]),

    "ElasticNet": Pipeline([
        ("scaler", StandardScaler()),
        ("model", ElasticNet(alpha=0.001, l1_ratio=0.5, max_iter=10000))
    ]),

    "Linear SVR": Pipeline([
        ("scaler", StandardScaler()),
        ("model", SVR(kernel="linear", C=1.0, epsilon=0.1))
    ]),

    "LinearSVR": Pipeline([
        ("scaler", StandardScaler()),
        ("model", LinearSVR(C=1.0, epsilon=0.1, max_iter=10000, random_state=42))
    ]),

    "Polynomial SVR": Pipeline([
        ("scaler", StandardScaler()),
        ("model", SVR(kernel="poly", degree=3, C=10, epsilon=0.1, gamma="scale"))
    ]),

    "RBF SVR": Pipeline([
        ("scaler", StandardScaler()),
        ("model", SVR(kernel="rbf", C=10, epsilon=0.1, gamma="scale"))
    ])
}


# ---------------------------------------------------------
# 4. Train and compare
# ---------------------------------------------------------
results = []

for name, model in models.items():
    result = evaluate_regression_model(
        name,
        model,
        X_train,
        X_test,
        y_train,
        y_test
    )
    results.append(result)

results_df = pd.DataFrame(results).sort_values(by="test_rmse")
print(results_df)
```
![[Pasted image 20260629144117.png]]

----
## 10. Plot Prediction Curves
```Python
X_plot = np.linspace(0, 6, 500).reshape(-1, 1)  
  
for name, model in models.items():  
model.fit(X_train, y_train)  
y_plot = model.predict(X_plot)  
  
plt.figure(figsize=(9, 5))  
plt.scatter(X_train, y_train, s=25, label="Training data")  
plt.scatter(X_test, y_test, s=35, marker="x", label="Testing data")  
plt.plot(X_plot, y_plot, linewidth=2, label=name)  
  
plt.title(f"Prediction Curve — {name}")  
plt.xlabel("X")  
plt.ylabel("y")  
plt.legend()  
plt.grid(alpha=0.25)  
plt.show()
```
![[Pasted image 20260629144306.png]]

---
## 11. Experiment with `epsilon`
![[Pasted image 20260629144541.png]]
![[Pasted image 20260629144554.png]]

---
## 12. Experiment with `C`
![[Pasted image 20260629144711.png]]
### Interpretation

- Small `C`: smoother, more regularized, may underfit.
- Large `C`: tries harder to reduce errors, may overfit.

---
## 13. Experiment with `gamma`
![[Pasted image 20260629145806.png]]
Interpretation
- Low `gamma`: too smooth, may underfit.
- High `gamma`: too wiggly, may overfit.
- Balanced `gamma`: follows pattern without memorizing noise.
---
## 14. California Housing mini-comparison
![[Pasted image 20260629153201.png]]
Production note:

> On real datasets, do not blindly run RBF SVR on 100,000+ rows. First test LinearSVR, Ridge, ElasticNet, Random Forest, or gradient boosting baselines.

----
## 15. Debugging focus
### Error 1: Unscaled features
Bad:
```
model = SVR(kernel="rbf")
model.fit(X_train, y_train)
```
Problem:
SVR depends on distances and margins. Different feature scales can distort the model.
Correct:
```
model = Pipeline([    
("scaler", StandardScaler()),    
("svr", SVR(kernel="rbf"))])
```
---
### Error 2: `epsilon` too small
Symptoms:
```
Training RMSE low
Test RMSE high
Prediction curve very wiggly
```
Root cause:
The tube is too narrow, so the model reacts to small noise.
Fix:
```
SVR(epsilon=0.1)
SVR(epsilon=0.3)
```
Compare with cross-validation later.

---
### Error 3: `epsilon` too large
Symptoms:
```
Train RMSE high
Test RMSE high
Prediction curve too flat
```
Root cause:
The tube is too wide, so the model ignores too many errors.
Fix:
Reduce `epsilon`.

---
### Error 4: `C` too large
Symptoms:
```
Training performance excellent
Testing performance unstable
```
Root cause:
The model penalizes errors too aggressively and may overfit.
Fix:
Try smaller values:
```
C=[0.1, 1, 10]
```
---
### Error 5: `gamma` too large
Symptoms:
```
Prediction curve becomes highly wiggly
```
Root cause:
Each point has too local an influence.
Fix:
Try:
```
gamma=["scale", 0.01, 0.1, 1]
```
---
### Error 6: Training takes too long
Possible causes:
- Too many samples
- RBF or polynomial kernel
- Large grid search
- High-dimensional data
Fix:
- Use a subset first.
- Try `LinearSVR`.
- Try `SGDRegressor`.
- Use kernel approximation if needed.
- Reduce search space.
- Record training time.
This directly matches scikit-learn’s warning that standard `SVR` based on `libsvm` can be difficult to scale beyond a couple of tens of thousands of samples.

---
## 16. Common mistakes

| Mistake                    | Why it is bad                       | Fix                  |
| -------------------------- | ----------------------------------- | -------------------- |
| Not scaling features       | Distance geometry becomes distorted | Use `StandardScaler` |
| Using RBF SVR on huge data | Training can be very slow           | Try `LinearSVR`      |
| Setting huge `C`           | Overfitting risk                    | Tune with CV         |
| Setting tiny `epsilon`     | Noise-fitting risk                  | Increase epsilon     |
| Setting huge `gamma`       | Wiggly curve                        | Reduce gamma         |
| Comparing only R²          | Misses error magnitude              | Use MAE, RMSE, R²    |
| Tuning on test set         | Test leakage                        | Use validation/CV    |
| Ignoring training time     | Bad production choice               | Record fit time      |

---
## 17. Interview trap questions
#### 1. Is SVR a classifier?
No. SVR is used for regression and predicts continuous values.
#### 2. What does `epsilon` mean?
It is the width of the error-insensitive tube. Errors inside this tube are not penalized.
#### 3. Does a smaller `epsilon` always improve SVR?
No. A very small `epsilon` can make the model overfit noise.
#### 4. Does larger `C` mean stronger regularization?
No. Larger `C` penalizes errors more strongly and usually means weaker effective regularization.
#### 5. When would you prefer `LinearSVR` over SVR(kernel="rbf")`?
When the dataset is large and a linear relationship is acceptable.
#### 6. Why is scaling important for SVR?
Because SVR uses distance and margin-based geometry, especially with RBF and polynomial kernels.
#### 7. What happens when `gamma` is very high?
The model becomes highly local and can overfit.
#### 8. Can SVR use kernels?
Yes. `SVR` supports kernels such as linear, polynomial and RBF.

---
## 18. Mini project ideas
### Project 1: House Price SVR Lab
Build a house-price prediction system comparing:
- Linear Regression
- Ridge
- Lasso
- ElasticNet
- LinearSVR
- RBF SVR
- Random Forest
Advanced features:
- RMSE comparison
- Error distribution plot
- Training-time benchmark
- Prediction-time benchmark
- Saved best model pipeline
- Streamlit input form
Resume bullet:
> Built a house-price regression benchmark comparing Linear Regression, ElasticNet, LinearSVR, RBF SVR and Random Forest with standardized preprocessing, RMSE evaluation and training-latency analysis.

---
### Project 2: Energy Consumption Prediction
Predict daily energy demand using:
- Temperature
- Humidity
- Day of week
- Holiday flag
- Previous-day usage
- Industrial activity index
Models:
- Ridge
- ElasticNet
- LinearSVR
- RBF SVR
Advanced features:
- Time-based split
- Error by weekday
- Peak-demand error analysis
- API endpoint for forecast
- Monitoring for data drift
Resume bullet:
> Developed an SVR-based energy-demand forecasting pipeline with feature scaling, nonlinear kernel comparison, time-aware evaluation and production-latency benchmarking.

---
## 19. Practice task
Use the California Housing subset and complete this table:

|Model|MAE|RMSE|R²|Train Time|Prediction Time|
|---|---|---|---|---|---|
|Ridge||||||
|ElasticNet||||||
|LinearSVR||||||
|RBF SVR||||||
Then answer:
1. Which model gives the best RMSE?
2. Which model trains fastest?
3. Which model has the best production trade-off?
4. Does RBF SVR justify its extra cost?
5. Would you deploy SVR on the full dataset?
---
## 20. Debugging challenge
Find the problems in this code:
```Python
from sklearn.datasets import fetch_california_housing
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

data = fetch_california_housing(as_frame=True)

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = SVR(kernel="rbf", C=100000, gamma=1000, epsilon=0.00001)

model.fit(X_train, y_train)

print(model.score(X_test, y_test))
```
Expected issues:
1. No `random_state`
2. No scaling
3. RBF SVR on full dataset may be slow
4. `C` is extremely high
5. `gamma` is extremely high
6. `epsilon` is extremely small
7. Only R² is shown
8. No MAE or RMSE
9. No training-time measurement
10. No baseline model
11. No train-test gap
12. Test set may be misused for tuning
Corrected safer version:
```Python
from sklearn.datasets import fetch_california_housing
from sklearn.svm import SVR, LinearSVR
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

data = fetch_california_housing(as_frame=True)

X = data.data.sample(n=3000, random_state=42)
y = data.target.loc[X.index]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("svr", SVR(kernel="rbf", C=10, gamma="scale", epsilon=0.1))
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2:", r2_score(y_test, y_pred))
```
---
## 21. Revision summary
```
Support Vector Regression
│
├── Purpose
│   └── Predict continuous values
│
├── Key idea
│   └── Epsilon-insensitive tube
│
├── epsilon
│   ├── Small → tighter fit
│   └── Large → smoother fit
│
├── C
│   ├── Small → more regularization
│   └── Large → stronger error penalty
│
├── gamma
│   ├── Small → smooth curve
│   └── Large → wiggly curve
│
├── Kernels
│   ├── Linear
│   ├── Polynomial
│   └── RBF
│
├── Production choice
│   ├── SVR for small/medium nonlinear data
│   └── LinearSVR for larger linear data
│
└── Debugging
    ├── Always scale
    ├── Watch training time
    ├── Avoid huge C/gamma
    └── Do not tune on test set
```
---
### Assignment
Create:
```
day5_slot4_support_vector_regression.ipynb
```
Include:
1. SVR vs SVC explanation
2. Epsilon tube diagram
3. Linear, Polynomial and RBF SVR code
4. Linear Regression, Ridge, Lasso, ElasticNet comparison
5. MAE, RMSE and R² table
6. Training-time comparison
7. `epsilon`, `C`, and `gamma` experiments
8. California Housing subset experiment
9. Debugging challenge solution
10. 150-word conclusion: “When should I use SVR?”
---