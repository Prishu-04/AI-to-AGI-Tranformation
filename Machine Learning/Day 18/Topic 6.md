# Classification Project + Model Comparison + Debugging Assessment

## 1. Goal
```
1. Frame a binary classification problem  
2. Build a mixed-data preprocessing pipeline  
3. Handle numerical and categorical features  
4. Compare five classification algorithms  
5. Evaluate models on validation data  
6. Analyze class imbalance  
7. Select a decision threshold  
8. Evaluate once on untouched test data  
9. Save and reload the full model pipeline  
10. Validate production input  
11. Debug classification-project failures  
12. Explain the project in an interview
```
---
## 2. Project Overview
```
Loan Approval Prediction System
```
### Problem Statement
Predict whether loan application should be approved or not
### ML type
```
Supervised Learning
```
### Problem type
```
Binary Classification
```
### Target mapping
```
0 = Rejected
1 = Approved
```
### Numerical features
```
applicant_income
loan_amount
credit_score
existing_debt
employment_years
loan_term
```
### Categorical features
```
employment_type
education
property_area
self_employed
```
---
## 3. Important Ethical Warning
A real lending system is a **high-impact decision system**.
This project is for learning. A real deployment would require:
```
Legal and regulatory review
Fairness testing
Bias analysis
Human review
Explainability
Security
Data-governance controls
Appeal mechanisms
Continuous monitoring
```
The model must not become the sole authority for approving or rejecting a real applicant.

---
## 4. Production-Style Workflow

```
Raw application data        
		↓
Input validation
        ↓
Train/Validation/Test split
        ↓
Numerical preprocessing        
		├── Missing-value imputation        
		└── StandardScaler        
		↓
Categorical preprocessing        
		├── Missing-value imputation        
		└── One-Hot Encoding        
		↓
Model training        
		↓
Validation comparison        
		↓
Best-model selection        
		↓
Threshold selection        
		↓
Final test evaluation        
		↓
Save pipeline + threshold        
		↓
Production prediction
```
`ColumnTransformer` applies separate transformations to selected columns, while `Pipeline` chains preprocessing and prediction into one reusable estimator. This ensures the transformations learned during training are also used during validation and prediction.

---
## 5. Why We Need Three Data Splits
We will create:
```
60% Training data
20% Validation data
20% Test data
```
### Training set
Used to fit:
```
Imputers
Scalers
Encoders
Model parameters
```
### Validation set
Used to:
```
Compare models
Select the best model
Select the classification threshold
```
### Test set
Used only once for final evaluation.
```
Training → Learn
Validation → Choose
Testing → Final unbiased check
```
`train_test_split` supports random train/test partitioning, and `stratify=y` helps retain class proportions during classification splits.

---
## 6. Create the Project File
Create:
```
day4_classification_project.py
```
We will use a synthetic dataset so the entire project runs without downloading an external CSV.

---
## 7. How to Compare the Models
### Logistic Regression
Strengths:
```
Interpretable coefficients
Fast prediction
Strong baseline
Probability output
```
Limitation:
```
Primarily learns a linear decision boundary
```
### KNN
Strengths:
```
Simple intuition
Can learn non-linear local boundaries
```
Limitations:
```
Slow prediction on large data
Sensitive to scaling and irrelevant features
```
### Decision Tree
Strengths:
```
Easy-to-read decision rules
Non-linear patterns
No normal scaling requirement
```
Limitation:
```
Can overfit easily
```
### Random Forest
Strengths:
```
Stable tree ensemble
Captures interactions
Usually less variance than one tree
```
Limitations:
```
Less interpretable
Larger model
Slower than a single tree
```
### Gaussian Naive Bayes
Strengths:
```
Very fast
Works well as a baseline
Probabilistic model
```
Limitations:
```
Strong conditional-independenceand Gaussian assumptions
```
---
## 8. Which Metric Should Select the Model?
There is no universal answer.
For loan approval:
### False Positive
```
Model predicts Approved
Actual result should be Rejected
```
Possible consequence:
```
A risky loan is approved
Financial loss increases
```
### False Negative
```
Model predicts Rejected
Actual result should be Approved
```
Possible consequence:
```
A suitable applicant is rejected
Lost business
Possible unfair customer impact
```
Therefore, you must decide the relative cost of:
```
FP vs FN
```
---
## 9. Threshold Selection
Assume:
```
False Positive cost = 5 units
False Negative cost = 2 units
```
Why is FP more costly here?
```
Approving an unsuitable loan may produce
greater financial loss than reject
ingone potentially suitable application.
```
These numbers are educational assumptions, not real banking costs.

---
