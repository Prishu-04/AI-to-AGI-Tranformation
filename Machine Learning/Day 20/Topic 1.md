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
