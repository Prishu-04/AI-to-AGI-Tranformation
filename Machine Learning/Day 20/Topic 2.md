# Validation Strategy and Data Leakage
## 1. Why Validation Strategy Matters
Validation strategy answers one question:
```
Will this model work on future unseen data?
```
A weak validation strategy gives fake confidence.
Example:
```
Notebook accuracy: 96%
Production accuracy: 71%
```
Possible reasons:
- Test data leaked into training
- Preprocessing was fitted before splitting
- Duplicate records existed across train and test
- Future information was used accidentally
- Same customer/patient/user appeared in both train and test
- Test set was repeatedly used for model selection
Google’s ML Crash Course says validation and test examples should represent new examples, and it specifically warns that duplicate examples across training and validation/test sets can distort evaluation.

---
## 2. Train, Validation, and Test Sets
## 1. Training set
Used to fit the model.
```
Model learns from this data.
```
## 2. Validation set
Used to compare models and tune hyperparameters.
```
Used for model selection.
```
## 3. Test set
Used only once at the end.
```
Used for final honest evaluation.
```
Correct workflow:
```
Raw Data
   ↓
Train / Validation / Test split
   ↓
Train model on training set
   ↓
Tune using validation set
   ↓
Final evaluation once on test set
```
Wrong workflow:
```
Try Model A → test score
Try Model B → test score
Try Model C → test score
Pick best test score
```
That is not a real test anymore. You have indirectly trained your decisions on the test set.

---
## 3. Simple Split Strategy
A common beginner split:
```
Train: 60%
Validation: 20%
Test: 20%
```
or:
```
Train: 70%
Validation: 15%
Test: 15%
```
For small datasets, cross-validation is usually better, but for this slot we focus on holdout validation and leakage prevention.
Scikit-learn’s `train_test_split` is the standard helper for creating random train/test subsets, and it supports important options like `test_size`, `random_state`, and `stratify`.

---
## 4. Stratified Splitting
For classification, random splitting can accidentally change class distribution.
Example:
```
Original dataset:
Class 0: 90%
Class 1: 10%

Bad test split:
Class 0: 98%
Class 1: 2%
```
That makes evaluation misleading.
Use:
```
stratify=y
```
This preserves class proportions in the split.
For cross-validation, `StratifiedKFold` preserves the percentage of samples for each class in binary or multiclass classification.

---
## 5. Reproducibility with `random_state`
Always set:
```
random_state=42
```
or another fixed number.
Why?
```
Same data split
Same experiment
Same result
Easier debugging
Easier GitHub reproducibility
```
Without `random_state`, your train-test split may change every run, and your metrics may shift.

---
## 6. What Is Data Leakage?
Data leakage happens when information that would not be available at prediction time is used during training or model selection.
Simple definition:
```
The model gets information it should not have.
```
Result:
```
Validation score becomes unrealistically high.
Production performance drops.
```
Scikit-learn defines leakage in practice as using information from test data during training, and warns that leakage causes overly optimistic performance estimates.

---
## 7. Types of Data Leakage
### 1. Preprocessing leakage
Wrong:
```Python
scaler.fit_transform(X)
train_test_split(X_scaled, y)
```
Problem:
```
Scaler learned mean and standard deviation from the full dataset,
including test data.
```
Correct:
```Python
X_train, X_test, y_train, y_test = train_test_split(X, y)
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```
Best:
```Python
Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])
```
Scikit-learn’s `Pipeline` fits transformers sequentially and then fits the final estimator, making it safer for cross-validation and model selection.

---
### 2. Target Leakage
Target leakage happens when a feature directly or indirectly contains the answer.
Example: loan approval prediction.
Bad feature:
If you are predicting whether a loan will default, this feature may contain future outcome information.
Other examples:

| Problem                | Leaky Feature                          |
| ---------------------- | -------------------------------------- |
| Diabetes prediction    | `doctor_diagnosis_result`              |
| Loan approval          | `approved_by_manager`                  |
| Churn prediction       | `retention_offer_accepted_after_churn` |
| Exam result prediction | `final_grade_status`                   |
| Fraud detection        | `chargeback_confirmed`                 |
Rule:
```
If the feature is created after the prediction moment, it is probably leakage.
```
---
### 3. Duplicate leakage
If the same or nearly same record appears in train and test, your model may appear stronger than it really is.
Example:
```
Train:  user_id=101, message="Win free iPhone now"
Test:   user_id=101, message="Win free iPhone now"
```
Google’s ML guidance specifically warns that duplicate examples in validation or test sets should be removed if they duplicate training examples, because the only fair test is against new examples.

---
### 4. Temporal leakage
Temporal leakage happens when future information helps predict the past.
Wrong for time series:
```
Random split
Train contains 2025 data
Test contains 2024 data
```
Correct:
```
Train: older data
Validation/Test: future data
```
Scikit-learn’s `TimeSeriesSplit` is designed for time-ordered data where ordinary cross-validation is inappropriate because it could train on future data and evaluate on past data.

---
### 5. Group leakage
Group leakage happens when related samples are split across train and test.
Examples:

| Dataset         | Group       |
| --------------- | ----------- |
| Medical records | Patient ID  |
| Customer churn  | Customer ID |
| Face images     | Person ID   |
| App malware     | App family  |
| Student marks   | Student ID  |
| Product reviews | Product ID  |
Wrong:
```
Same patient appears in train and test.
```
Correct:
```
A patient must be either fully in train or fully in test.
```
`GroupKFold` ensures each group appears exactly once in the test set across folds, preventing the same group from appearing across train and test folds.

---
### 6. feature-selection Leakage
Wrong:
```Python
Select best feature using full x and y
then split into train and test
```
Problem:
```
Feature selection already looked at the target values from the test set.
```
Correct:
```
Split first.
Fit feature selection only on training data.
```
Best:
```Python
Pipeline([
	("feature_selection",SelectKBest()),
	("model",LogisticRegression())
])
```
---
### 7. Encoding leakage
Target encoding or mean encoding can leak label information if done before splitting.
Example:
```
Category: city
Encoded value: average target for that city
```
If calculated using full data, test target values affect training features.
Correct;
```
Fit encoding only on tarining folds.
```
---
## 8. Senior Engineer Validation Workflow
Use this workflow in every serious ML project:
```
1. Define prediction moment.
2. Remove features unavailable at prediction time.
3. Remove duplicate or near-duplicate records.
4. Decide split type:
   - random split
   - stratified split
   - group split
   - time-based split
5. Keep test set untouched.
6. Fit preprocessing only on training data.
7. Tune only on validation/CV.
8. Evaluate once on test set.
9. Save metrics, random seed, data version, model version.
10. Write limitations clearly.
```
---
## 9. Complete Code
![[Pasted image 20260714123837.png]]
![[Pasted image 20260714123855.png]]
![[Pasted image 20260714123930.png]]![[Pasted image 20260714123946.png]]
![[Pasted image 20260714124000.png]]
![[Pasted image 20260714124027.png]]
![[Pasted image 20260714124037.png]]
This gives:
```
Train: 60%
Validation: 20%
Test: 20%
```
because:
```
0.25 of 80% = 20%
```
![[Pasted image 20260714124459.png]]
![[Pasted image 20260714124511.png]]
![[Pasted image 20260714124528.png]]
