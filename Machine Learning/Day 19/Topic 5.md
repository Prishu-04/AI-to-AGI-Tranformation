## ElasticNet Regression
## 1. Why ElasticNet matters
ElasticNet is a **regularized linear regression model** that combines both **L1** and **L2** regularization. In scikit-learn’s formulation, the objective combines ordinary squared error with an L1 coefficient penalty and an L2 coefficient penalty.
Use ElasticNet when:
- You have many input features.
- Some features are irrelevant.
- Some features are strongly correlated.
- You want feature selection like Lasso.
- You also want coefficient stability like Ridge.
- You need an interpretable regression baseline.
Industry examples:
- House price prediction
- Insurance cost prediction
- Startup revenue forecasting
- Medical cost prediction
- Marketing spend optimization
- Demand forecasting
- Feature-selection-heavy regression tasks
---
## 2. Ridge vs Lasso limitations
### Ridge Regression
Ridge uses **L2 regularization**.
Scikit-learn defines Ridge as linear least squares with an L2-norm regularization penalty.
Ridge loss idea:
					![[Pasted image 20260629154736.png|183]]
### What Ridge does well
- Shrinks large coefficients.
- Reduces overfitting.
- Handles correlated features better than ordinary Linear Regression.
- Keeps model stable.
### Limitation of Ridge
Ridge usually **does not remove features completely**.
Example:
```
Before Ridge:
feature_1 = 25.0
feature_2 = 8.0
feature_3 = 0.5

After Ridge:
feature_1 = 10.2
feature_2 = 3.1
feature_3 = 0.08
```
It shrinks coefficients, but weak features often remain nonzero.

---
### Lasso Regression
Lasso uses **L1 regularization**.
Scikit-learn describes Lasso as a linear model that estimates sparse coefficients with L1 regularization, and its documentation notes that Lasso is equivalent to ElasticNet with `l1_ratio=1.0`.
Lasso loss idea:
					![[Pasted image 20260629154943.png|178]]
#### What Lasso does well
- Shrinks coefficients.
- Can set some coefficients exactly to zero.
- Performs automatic feature selection.
- Produces simpler models.
#### Limitation of Lasso
When features are highly correlated, Lasso may choose one feature and ignore other similar features.
Example:
```
area_sqft, bedrooms, bathrooms, rooms
```
These may all be correlated in a house-price dataset. Lasso may keep one and drop the others, even though the group together is meaningful.
A recent applied benchmark also found Lasso-style selection can become fragile under multicollinearity, while ElasticNet can be more stable in such settings.

---
## 3. ElasticNet Intuition
ElasticNet combines Ridge and Lasso.
```
ElasticNet = Lasso-style sparsity + Ridge-style stability
```
It uses:
- **L1 penalty** for feature selection
- **L2 penalty** for coefficient stability
ElasticNet is useful when you want:
```
Remove weak features,
but do not behave too aggressively when features are correlated.
```
Scikit-learn’s user guide states that `ElasticNetCV` can tune both `alpha` and `l1_ratio` using cross-validation.

---
## 4. ElasticNet Mathematics
![[Pasted image 20260629155237.png]]

---
## 5. Meaning of `alpha`
`alpha` controls the **overall regularization strength**.
### Small `alpha`
```
Less regularization
Coefficients shrink less
Model is more flexible
Higher overfitting risk
```
### Large `alpha`
```
More regularization
Coefficients shrink more
Model becomes simpler
Higher underfitting risk
```
Example:
```
ElasticNet(alpha=0.001)
ElasticNet(alpha=0.01)
ElasticNet(alpha=0.1)
ElasticNet(alpha=1)
ElasticNet(alpha=10)
```
Senior-engineer rule:
```
Do not guess alpha blindly.
Test values on a logarithmic scale and use cross-validation.
```
---
## 6. Meaning of `l1_ratio`
`l1_ratio` controls how much of the penalty is L1 versus L2.
![[Pasted image 20260629155445.png|275]]
In scikit-learn, `l1_ratio=1` corresponds to the Lasso penalty. The ElasticNet docs also warn that `l1_ratio <= 0.01` is not reliable unless you provide your own alpha sequence.
Practical values:
```Python
l1_ratio_values = [0.1, 0.3, 0.5, 0.7, 0.9]
```
----
## 7. Sparse coefficients
A sparse model has many coefficients equal to zero.
Example:
```
Total features: 20
Non-zero coefficients: 7
Zero coefficients: 13
```
This means the model effectively selected only 7 useful features.
Why sparse coefficients matter:
- Easier interpretation
- Smaller model
- Cleaner feature set
- Better interview explanation
- Better project README
- Useful resume story
Ridge usually shrinks coefficients but keeps them nonzero. Lasso and ElasticNet can create sparse coefficients because they include an L1 penalty.

---
## 8. Correlated features
Suppose your dataset has:
```
house_area
number_of_rooms
number_of_bedrooms
number_of_bathrooms
parking_area
```
These may be correlated.
### Ridge behavior
Ridge tends to spread weight across correlated features.
### Lasso behavior
Lasso may select one feature and suppress others.
### ElasticNet behavior
ElasticNet can keep a more stable set of correlated features while still pushing weak coefficients toward zero.
Production takeaway:
```
If features are correlated and you still want feature selection,
ElasticNet is usually safer than pure Lasso.
```
---
## 9. ElasticNet vs Ridge vs Lasso
![[Pasted image 20260629155941.png]]
Practical model-selection rule:
```
Start with Ridge for stability.
Try Lasso for feature selection.
Try ElasticNet when Lasso becomes unstable or too aggressive.
Use ElasticNetCV for proper tuning.
```
---
## 10. ElasticNetCV
`ElasticNetCV` searches over regularization settings using cross-validation. It can test a list of `alphas` and a list of `l1_ratio` values, then select the best combination.
Example:
```
ElasticNetCV(    
	alphas=[0.001, 0.01, 0.1, 1, 10],    
	l1_ratio=[0.1, 0.3, 0.5, 0.7, 0.9],    
	cv=5)
```
Why this is better:
```
Manual guessing → weak engineering
Cross-validation tuning → professional engineering
```
---
## 11. Code Implementation
### Part A - Ridge, Lasso, ElasticNet comparison
![[Pasted image 20260630100047.png]]
![[Pasted image 20260630100115.png]]
![[Pasted image 20260630100502.png]]
![[Pasted image 20260630101028.png]]
![[Pasted image 20260630101011.png]]
![[Pasted image 20260630101159.png]]
### What to observe
- Ridge should usually keep most coefficients nonzero.
- Lasso may set some coefficients to zero.
- ElasticNet may create partial sparsity while staying less aggressive than Lasso.
----
![[Pasted image 20260630102540.png]]
![[Pasted image 20260630103059.png]]
![[Pasted image 20260630103116.png]]
![[Pasted image 20260630103201.png]]![[Pasted image 20260630141345.png]]
![[Pasted image 20260630141546.png]]
![[Pasted image 20260630141957.png]]
![[Pasted image 20260630142206.png]]

---
## 12. Convergence Warning Debugging
A `ConvergenceWarning` means the optimizer did not fully converge before stopping.
This usually happens because of:
- Too few iterations
- Bad scaling
- Too tiny `alpha`
- Too strict `tol`
- Difficult optimization problem
ElasticNet includes `max_iter` and `tol` parameters because its solver is iterative and may need enough iterations to converge.

----
![[Pasted image 20260630142359.png]]
![[Pasted image 20260630142449.png]]
### Why the warning happened
The broken model used:
```
alpha=0.000001
max_iter=5
tol=1e-8
```
Problem:

| Issue                | Why bad                             |
| -------------------- | ----------------------------------- |
| Tiny `alpha`         | Very weak regularization            |
| `max_iter=5`         | Optimizer gets almost no time       |
| `tol=1e-8`           | Very strict convergence requirement |
| No enough iterations | Optimization stops early            |
Fix:
```
ElasticNet(    
	alpha=0.01,
    l1_ratio=0.5,    
    max_iter=30000,    
    tol=1e-4)
```
---
## 13. Interpretation Guide
After running your notebook, interpret results like this:
### If Ridge performs best
Meaning:
```
Most features are useful.Feature removal is not helping much.L2 regularization is enough.
```
### If Lasso performs best
Meaning:
```
Some features are irrelevant.Sparse feature selection helped.
```
### If ElasticNet performs best
Meaning:
```
Some features are irrelevant,but correlated features still need stable regularization.
```
### If ElasticNetCV performs best
Meaning:
```
Manual alpha and l1_ratio were not optimal.Cross-validation found a better regularization balance.
```
---
## Part 14 — Interview Questions
1. What is regularization?
2. Why can Linear Regression overfit?
3. What is Ridge Regression?
4. What is Lasso Regression?
5. What is ElasticNet?
6. What does `alpha` control?
7. What does `l1_ratio` control?
8. Why does Lasso create sparse coefficients?
9. Why does Ridge usually not create exact zero coefficients?
10. Why can Lasso struggle with correlated features?
11. Why is ElasticNet useful with correlated features?
12. What is `ElasticNetCV`?
13. Why should we scale features before ElasticNet?
14. What causes `ConvergenceWarning`?
15. How do you fix `ConvergenceWarning`?
16. Why should we not tune using the test set?
17. Which metric is better for regression: MAE, RMSE, or R²?
18. When would you use ElasticNet over Random Forest?
19. When would you avoid ElasticNet?
20. How would you explain ElasticNet in a resume interview?
---
## 16 — Assignment
Create this notebook:
```
day5_slot5_elasticnet_regression.ipynb
```
It must include:
1. Ridge explanation
2. Lasso explanation
3. ElasticNet explanation
4. `alpha` explanation
5. `l1_ratio` explanation
6. Ridge/Lasso/ElasticNet comparison code
7. Coefficient comparison table
8. Zero-coefficient count
9. Coefficient bar plot
10. Coefficient shrinkage plot
11. ElasticNetCV tuning
12. Best `alpha` and `l1_ratio`
13. ConvergenceWarning experiment
14. Fixed convergence version
15. Debugging challenge solution
16. Final 150-word conclusion
---
