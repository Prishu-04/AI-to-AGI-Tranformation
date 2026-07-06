# Overfitting, Underfitting, Bias-Variance, and Learning Curves
## 1. Why this Topic Matters
In real ML projects, your model can fail in two main ways:
```
1. It is too simple.
2. It is too complex.
```
If it is too simple, it cannot learn the real pattern.
If it is too complex, it may memorize the training data and fail on new data.
Google’s ML Crash Course defines overfitting as creating a model that memorizes the training set so closely that it fails to make correct predictions on new examples.
### Industry applications
This concept matters in:
- Spam detection
- Loan approval
- Medical diagnosis support
- Fraud detection
- House price prediction
- Recommendation systems
- Resume screening
- Forecasting systems
- Computer vision
- NLP models
- Production AI APIs
### Interview relevance
Interviewers often ask:
- What is overfitting?
- What is underfitting?
- How do you detect overfitting?
- What is bias-variance trade-off?
- What does a learning curve tell you?
- How do you fix high variance?
- How do you fix high bias?
### Startup relevance
A startup does not need the most complex model first.
A startup needs:
```
A model that performs well on future unseen users.
```
A model with 99% training accuracy and 65% real-world accuracy is dangerous.

---
## 2. Training Error vs Test Error
### Training error
Training error measures performance on the data used to train the model.
```
Training error tells you:
"How well did the model learn the training data?"
```
### Test error
Test error measures performance on unseen data.
```
Test error tells you:
"How well does the model generalize?"
```
### The key gap
```
Generalization gap = Training performance - Test performance
```
For accuracy:
```
Train accuracy = 0.98
Test accuracy  = 0.78
Gap            = 0.20
```
This is a large gap.
Likely issue:
```
Overfitting
```
For RMSE:
```
Train RMSE = 12
Test RMSE  = 38
Gap        = 26
```
Again, large gap means the model performs much worse on unseen data.

---
## 3. Underfitting
Underfitting means:
```
The model is too simple to learn the pattern.
```
Example:
You try to fit a straight line to curved data.
```
Actual pattern: curved
Model: straight line
Result: poor performance everywhere
```
Scikit-learn’s official underfitting/overfitting example demonstrates this using polynomial regression: low-degree polynomial models can underfit nonlinear data, while overly high-degree models can overfit.
### Symptoms of underfitting

| Training score | Test score   | Meaning             |
| -------------- | ------------ | ------------------- |
| Low            | Low          | Model is too simple |
| High error     | High error   | Underfitting        |
| Small gap      | But both bad | High bias problem   |
Example:
```
Training accuracy: 0.62
Testing accuracy : 0.60
```
This is not overfitting.
This is underfitting.
### Causes
- Model too simple
- Not enough useful features
- Too much regularization
- Wrong algorithm
- Poor preprocessing
- Missing important variables
- Features not transformed properly
- Too few training epochs in neural networks
### Fixes
- Use a more complex model
- Add meaningful features
- Reduce regularization
- Add polynomial or interaction features
- Improve preprocessing
- Use nonlinear models
- Train longer, if the model is undertrained
---
## 4. Overfitting
Overfitting means:
```
The model memorized training data instead of learning the general pattern.
```
Example:
A student memorizes exact answers from a previous exam.
When the new exam changes slightly, the student fails.
### Symptoms of overfitting

| Training score  | Test score         | Meaning                       |
| --------------- | ------------------ | ----------------------------- |
| Very high       | Much lower         | Model memorized training data |
| Low train error | High test error    | High variance problem         |
| Large gap       | Bad generalization | Overfitting                   |
Example:
```
Training accuracy: 1.00
Testing accuracy : 0.72
```
This is classic overfitting.
### Causes
- Model too complex
- Too many features
- Too little data
- Noisy labels
- Data leakage
- Very deep decision tree
- Huge `C` in SVM
- Huge `gamma` in RBF SVM
- Too many polynomial features
- Weak validation strategy
### Fixes
- Use simpler model
- Add regularization
- Reduce model depth
- Reduce features
- Remove noisy features
- Get more data
- Use cross-validation
- Use early stopping
- Tune hyperparameters
- Prevent leakage
---
## 5. Bias and Variance
Important: here **bias** means mathematical/modeling bias, not social or ethical bias.
### Bias
Bias is error caused by wrong or overly simple assumptions.
High bias means:
```
The model is too simple.
```
Example:
```
Using Linear Regression for a strongly curved pattern.
```
High bias usually causes:
```
Underfitting
```
### Variance
Variance means the model changes too much when training data changes.
High variance means:
```
The model is too sensitive to training data.
```
Example:
```
A deep Decision Tree that changes drastically with small data changes.
```
High variance usually causes:
```
Overfitting
```
### Bias-variance trade-off
Classic intuition:
```
Simple model  → high bias, low variance
Complex model → low bias, high variance
```
Modern research adds nuance: over-parameterized models, especially in deep learning, can sometimes generalize well even after fitting training data closely, which is part of the modern “double descent” discussion. But for classical ML models in this roadmap, the standard bias-variance framework is still the practical debugging tool.

---
## 6. Model Complexity
Model complexity means how flexible the model is.
### Low complexity
Examples:
- Linear Regression
- Logistic Regression
- Shallow Decision Tree
- Ridge with high regularization
- SVM with very small `C`
Risk:
```
Underfitting
```
### High complexity
Examples:
- Deep Decision Tree
- High-degree Polynomial Regression
- KNN with `k=1`
- RBF SVM with high `C` and high `gamma`
- Random Forest with very deep trees
Risk:
```
Overfitting
```
---
## 7. Learning Curves
A learning curve shows model performance as training size increases.
Usually, it plots:
```
Training score vs number of training examples
Validation score vs number of training examples
```
Scikit-learn’s learning-curve documentation says a learning curve shows validation and training scores for varying numbers of training samples.
### Learning curve patterns
#### Pattern 1 — Underfitting
```
Training score: low
Validation score: low
Gap: small
```
Meaning:
```
Adding more data may not help much.
Use a better model or better features.
```
#### Pattern 2 — Overfitting
```
Training score: high
Validation score: low
Gap: large
```
Meaning:
```
Model memorizes training data.
More data or stronger regularization may help.
```
#### Pattern 3 — Good fit
```
Training score: good
Validation score: good
Gap: small
```
Meaning:
```
Model generalizes well.
```
---
## 8. Complete Code.
![[Pasted image 20260703152501.png]]
![[Pasted image 20260703152631.png]]
![[Pasted image 20260703152700.png]]
![[Pasted image 20260703152719.png]]
![[Pasted image 20260703152740.png]]
![[Pasted image 20260703152757.png]]
![[Pasted image 20260703152853.png]]
![[Pasted image 20260703152920.png]]
![[Pasted image 20260703152943.png]]
![[Pasted image 20260703153009.png]]
![[Pasted image 20260703153035.png]]
![[Pasted image 20260703153100.png]]
## 10. Decision Tree Complexity
![[Pasted image 20260706102934.png]]
![[Pasted image 20260706103102.png]]
![[Pasted image 20260706103048.png]]
![[Pasted image 20260706103008.png]]
![[Pasted image 20260706103246.png]]
![[Pasted image 20260706103423.png]]
![[Pasted image 20260706103957.png]]
### Interpretation

| Pattern                          | Diagnosis    |
| -------------------------------- | ------------ |
| Train low, test low              | Underfitting |
| Train high, test much lower      | Overfitting  |
| Train good, test good, gap small | Good fit     |

---
## 12. Learning curve Code
```Python
def plot_learning_curve(model, X, y, title, scoring="accuracy"):
    train_sizes, train_scores, validation_scores = learning_curve(
        estimator=model,
        X=X,
        y=y,
        train_sizes=np.linspace(0.1, 1.0, 5),
        cv=5,
        scoring=scoring,
        n_jobs=-1
    )

    train_mean = train_scores.mean(axis=1)
    train_std = train_scores.std(axis=1)

    validation_mean = validation_scores.mean(axis=1)
    validation_std = validation_scores.std(axis=1)

    plt.figure(figsize=(8, 5))

    plt.plot(
        train_sizes,
        train_mean,
        marker="o",
        label="Training score"
    )

    plt.plot(
        train_sizes,
        validation_mean,
        marker="o",
        label="Validation score"
    )

    plt.fill_between(
        train_sizes,
        train_mean - train_std,
        train_mean + train_std,
        alpha=0.15
    )

    plt.fill_between(
        train_sizes,
        validation_mean - validation_std,
        validation_mean + validation_std,
        alpha=0.15
    )

    plt.title(title)
    plt.xlabel("Training examples")
    plt.ylabel(scoring)
    plt.legend()
    plt.grid(alpha=0.25)
    plt.show()
```
![[Pasted image 20260706104425.png]]
![[Pasted image 20260706105410.png]]
![[Pasted image 20260706105439.png]]
Expected pattern:
```
Training score high
Validation score high
Gap smaller than deep tree
```
Diagnosis:
```
Better generalization
```
---
## 13. Validation Curve Awareness
A learning curve changes the **amount of training data**.
A validation curve changes **one hyperparameter**.
Example:
```
Decision Tree max_depth = 1, 2, 3, 5, 10, None
```
Scikit-learn’s validation-curve documentation explains that plotting training and validation scores against a hyperparameter helps identify whether an estimator is overfitting or underfitting for certain hyperparameter values.
We will use this more deeply in **GridSearchCV and hyperparameter tuning**.

---
## 14. Senior Engineer Debugging Framework
When a model performs badly, do not randomly change algorithms.
Use this checklist.
### Case 1 — Training and test both bad
```
Train score: low
Test score : low
```
Diagnosis:
```
Underfitting
```
Fix:
- Use stronger model
- Add better features
- Reduce regularization
- Improve preprocessing
- Try nonlinear model
- Check if target is noisy
---
### Case 2 — Training excellent, test bad
```
Train score: very high
Test score : much lower
```
Diagnosis:
```
Overfitting
```
Fix:
- Reduce complexity
- Add regularization
- Get more data
- Use cross-validation
- Prune trees
- Lower polynomial degree
- Lower SVM `C` or `gamma`
- Remove leakage
- Check noisy labels
---
### Case 3 — Training good, test good
```
Train score: good
Test score : goodGap         : small
```
Diagnosis:
```
Good generalization
```
Next:
- Tune carefully
- Validate with cross-validation
- Check error slices
- Prepare for deployment
---
## 15. Top 10 Common Errors
### 1. Confusing overfitting with high accuracy
High training accuracy alone is not good.
You need validation/test performance.

---
### 2. Calling every bad model “overfitting”
If train score is also low, it is not overfitting.
It is underfitting.

---
### 3. Tuning repeatedly on test set
Bad workflow:
```
Try model A → test score
Try model B → test score
Try model C → test score
Pick best test score
```
This leaks the test set into model selection.
Correct workflow:
```
Train set → validation/CV tuning
Test set → final evaluation once
```
---
### 4. Ignoring data leakage
A model can look good because it accidentally saw future or target-related information.
Always check features carefully.

---
### 5. Thinking more data always fixes underfitting
If the model is too simple, more data may not fix it.
You may need better features or a better model.

---
### 6. Thinking complex models are always better
A complex model can memorize noise.
Choose the simplest model that meets the business goal.

---
### 7. Ignoring train-test gap
Always compare training and testing scores.

---
### 8. Not plotting learning curves
Numbers alone may not show whether more data would help.

---
### 9. Using accuracy for imbalanced data
Accuracy can hide failure on minority class.
Use precision, recall, F1, ROC-AUC, and confusion matrix.

---
### 10. Not saving experiment results
Senior engineers track:
- Model name
- Hyperparameters
- Train score
- Validation score
- Test score
- Dataset version
- Random seed
- Code version

---
## 16. Production Failure Scenarios
### Scenario 1 — Model performs well in notebook but fails in production
Possible causes:
- Train-production distribution shift
- Data leakage in notebook
- Different preprocessing in API
- Different feature order
- Missing values in production
- New categories
- Poor monitoring
Senior engineer response:
```
Compare training data and production data distributions.
Log inputs.
Validate schema.
Replay production examples locally.
Check preprocessing pipeline.
```
---
### Scenario 2 — Fraud model has 98% accuracy but misses fraud cases
Problem:
Class imbalance.
Fix:
- Check recall
- Check confusion matrix
- Use class weighting
- Tune threshold
- Review false negatives
---
### Scenario 3 — Decision tree has 100% training accuracy
Likely issue:
Overfitting.
Fix:
- Set `max_depth`
- Set `min_samples_leaf`
- Use cross-validation
- Compare Random Forest
- Inspect test performance
---
## 17. Debugging Challenge
You are given this result:

| Model                          | Train Accuracy | Test Accuracy |
| ------------------------------ | -------------- | ------------- |
| Decision Tree `max_depth=None` | 1.00           | 0.71          |
| Decision Tree `max_depth=1`    | 0.62           | 0.60          |
| Decision Tree `max_depth=5`    | 0.88           | 0.84          |
Answer:
1. Which model is overfitting?
2. Which model is underfitting?
3. Which model generalizes best?
4. What should you try next?
### Expected reasoning
```
max_depth=None → overfitting
max_depth=1    → underfitting
max_depth=5    → best generalization among these
```
Next steps:
- Try `max_depth=3,4,5,6,7`
- Use cross-validation
- Tune `min_samples_leaf`
- Compare Random Forest
- Check confusion matrix
---
## 18. Interview Questions
1. What is overfitting?
2. What is underfitting?
3. What is generalization?
4. What is training error?
5. What is test error?
6. What is generalization gap?
7. What is bias?
8. What is variance?
9. Explain bias-variance trade-off.
10. How do you detect overfitting?
11. How do you detect underfitting?
12. How can learning curves help?
13. How do you fix high bias?
14. How do you fix high variance?
15. Why should we not tune on the test set?
16. Why can a deep Decision Tree overfit?
17. Why can high-degree Polynomial Regression overfit?
18. Does more data always help?
19. How do you debug 100% training accuracy and poor test accuracy?
20. What does it mean if training and validation curves converge at a low score?
---
