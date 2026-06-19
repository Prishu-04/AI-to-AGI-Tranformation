	# Train-Test Split + First scikit-learn Model
## 1. Goal.
```
1. Understand why train-test split is needed
2. Separate X and y
3. Split data into training and testing parts
4. Train your first scikit-learn model
5. Use fit()
6. Use predict()
7. Evaluate prediction error using MAE
8. Debug beginner scikit-learn errors
```
Today's first model will be:
```
Student Marks Prediction
```
Problem type:
```
Supervised Learning → Regression
```
----
## 2. Why Train-Test Split Matters
Suppose you study only the same 10 questions again and again.
Then in the exam, if the exact same 10 questions come, you may score high.
But if new questions come, your real understanding is tested.
ML works the same way.
```
Training data = practice questions
Testing data = exam questions
```
If you test the model on the same data it trained on, you do not know whether it learned real patterns or simply memorized.
That is why we split:
```
Training data → model learnsTesting data → model is evaluated on unseen data
```
---
## 3. Industry Relevance
Train-test split is used in almost every supervised ML project.
Examples:
![[Pasted image 20260609113107.png]]
In production, the real test is future data.
So the test set should behave like future unseen data.

---
## 4. Interview Relevance
Interviewers commonly ask:
```
Why do we split data into train and test?
What is generalization?
What happens if we test on training data?
What is random_state?
What is test_size?
What is data leakage?
```
Strong answer:
```
Train-test split helps estimate how well a model generalizes to unseen data. The model learns from training data and is evaluated on separate test data that was not used during fitting.
```
---
## 5. Startup Relevance.
Suppose you build:
```
AI Study Performance Predictor
```
You train the model on old student data.
But your actual users are new students.
If your model performs well only on old data but fails on new students, your startup product will lose trust.
So your model must generalize.
```
Good product = works on unseen users
Bad product = only works on training dataset
```
----
## 6. Core Concepts
### X and y
```
X = features/input columns
y = label/target/output column
```
### X_train
Features used to train the model.
### X_test
Features used to test the model.
### y_train
Correct answers for training data.
### y_test
Correct answers for test data.
### y_pred
Model predictions on X_test.

Full flow:
```
X, y
 ↓
train_test_split
 ↓
X_train, X_test, y_train, y_test
 ↓
model.fit(X_train, y_train)
 ↓
model.predict(X_test)
 ↓
compare y_pred with y_test
```
---
## 7. Visual Explanation
```
Full Dataset
│
├── X = study_hours, attendance, previous_score
│
└── y = final_marks


After split:

Training Set
├── X_train
└── y_train

Testing Set
├── X_test
└── y_test


Model learns:
X_train → y_train

Model predicts:
X_test → y_pred

Evaluation:
Compare y_pred with y_test
```
---
## 8. Model We Use Today: Linear Regression
Linear Regression is used for regression problems where the target is a continuous number.
Example:
```
Predict final marks
Predict house price
Predict salary
Predict delivery time
```
Scikit-learn describes linear models for regression as models where the predicted target is expected to be a linear combination of input features, written as predicted y = w0 + w1x1 + ... + wpxp.
For one feature:
```
marks = weight × study_hours + bias
```
For multiple features:
```
marks = w1 × study_hours + w2 × attendance + w3 × previous_score + bias
```
Do not worry about heavy math today. Just understand:
```
The model learns weights for each feature.
```
---
## 9. Metric We Use Today: MAE
MAE means:
```
Mean Absolute Error
```
It tells average prediction error.
Example:
```
Actual marks = 80
Predicted marks = 75
Error = 5
```
If MAE =4.5, it means:
```
On average, model prediction is wrong by 4.5 marks.
```
Scikit-learn defines `mean_absolute_error` as a non-negative regression loss where the best value is `0.0`.
Simple rule:
```
Lower MAE = better model
MAE = 0 = perfect prediction
```
---
## 10. First Complete ML Code.
![[Pasted image 20260609120352.png]]
![[Pasted image 20260609120424.png]]
![[Pasted image 20260609120449.png]]
![[Pasted image 20260609120517.png]]
![[Pasted image 20260609120532.png]]
![[Pasted image 20260609120840.png]]
![[Pasted image 20260609120907.png]]
![[Pasted image 20260609120940.png]]
![[Pasted image 20260609121003.png]]
![[Pasted image 20260609121057.png]]

---
## 11. Code Walkthrough
### Step 1: Import Libraries
```Python
import pandas as pd
```
Pandas is used to create and manage tabular data.
```Python
from sklearn.model_selection import train_test_split
```
Used to divide data into train and test sets.
```Python
from sklearn.linear_model import LinearRegression
```
Imports the Linear Regression model.
```Python
from sklearn.metrics import mean_absolute_error
```
Used to calculate average prediction error.

---
### Step 2: Create Dataset
```Python
data = {    
	"study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	"attendance": [40, 45, 50, 55, 60, 70, 75, 80, 90, 95],
	"previous_score": [35, 40, 45, 50, 55, 65, 70, 75, 85, 90],
	"final_marks": [38, 42, 48, 52, 58, 68, 72, 78, 88, 94]}
```
Here:
```
study_hours, attendance, previous_score = featuresfinal_marks = label
```
---
### Step 3: Separate X and y
```Python
X = df[["study_hours", "attendance", "previous_score"]]y = df["final_marks"]
```
Meaning:
```
X contains input columns.y contains output column.
```
---
### Step 4: Train-Test Split
```Python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,    
    test_size=0.2,    
    random_state=42
)
```
Meaning:
```
test_size=0.2 → 20% data used for testing
random_state=42 → same split every time
```
For 10 rows:
```
8 rows → training
2 rows → testing
```
---
### Step 5: Create Model
```Python
model = LinearRegression()
```
This creates an empty model.
At this stage, it has not learned anything.

---
### Step 6: Train Model
```Python
model.fit(X_train, y_train)
```
This teaches the model:
```
study_hours + attendance + previous_score → final_marks
```
---
### Step 7: Predict
```Python
y_pred = model.predict(X_test)
```
The model predicts final marks for unseen test rows.

---
### Step 8: Evaluate
```Python
mae = mean_absolute_error(y_test, y_pred)
```
This compares:
```
Actual marks vs Predicted marks
```
---
## 12. Understanding random_state
Without `random_state`, every run may split the data differently.
Example:
```Python
train_test_split(X, y, test_size=0.2)
```
This may give different train/test rows each time.
With:
```Python
random_state=42
```
The split becomes reproducible.
Industry reason:
```
Reproducibility is important for debugging, experiments, and teamwork.
```
---
## 13. Understanding test_size
```Python
test_size=0.2
```
Means:
```
20% test data
80% train data
```
Common splits:
```
80/20
75/25
70/30
```
For small datasets, results can be unstable. In real projects, we use larger datasets and often cross-validation.

---
## 14. What Does model.fit() Actually Mean?
```Python
model.fit(X_train, y_train)
```
Means:
```
Learn internal parameters from training data.
```
For Linear Regression, the model learns:
```
weights for each featurebias/intercept
```
You can see them:
```Python
print(model.coef_)
print(model.intercept_)
```
Meaning:
```
coef_ = learned weights
intercept_ = learned bias
```
---
## 15 What does model.predict() Mean?
```
model.predict(X_test)
```
Means:
```
Use learned pattern to predict output for unseen examples.
```
Important:
```
predict() should be used after fit()
```
if you call `predict()` before `fit()`, you can get an error.

---
## 16. Debugging Section.
### Bug 1: NotFittedError
Broken code:
```Python
model = LinearRegression()
y_pred = model.predict(X_test)
```
Possible error:
```
NotFittedError: This LinearRegression instance is not fitted yet. Call 'fit' with appropriate arguments before using this estimator.
```
Why it happens:
```
You used predict() before fit().
```
Correct code:
```Python
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```
Senior engineer habit:
```
Always check training step executed before prediction.
```

---
### Bug 2: KeyError
Broken code:
```Python
X = df[["study_hour", "attendance", "previous_score"]]
```
Actual error:
```
KeyError: "['study_hour'] not in index"
```
Why it happens:
```
Column name is study_hours, not study_hour.
```
Debug:
```
print(df.columns)
```
Correct:
```Python
X = df[["study_hours", "attendance", "previous_score"]]
```
---
### Bug 3: Shape Mismatch
Broken code:
```Python
X = df[["study_hours", "attendance"]]
y = df["final_marks"].head(5)
model.fit(X, y)
```
Possible error:
```
ValueError: Found input variables with inconsistent numbers of samples
```
Why it happens:
```
X has 10 rows.y has 5 rows.
```
Debug:
```Python
print(X.shape)
print(y.shape)
```
Correct:
```Python
X = df[["study_hours", "attendance"]]
y = df["final_marks"]
```
---
### Bug 4: Wrong Target Column
Broken code:
```Python
y = df["marks"]
```
Actual error:
```
KeyError: 'marks'
```
Why:
```
The correct column name is final_marks.
```
Correct:
```Python
y = df["final_marks"]
```
---
### Bug 5: Text Data in Numeric Model
Suppose your dataset has:
```Python
data = {
    "study_hours": [1, 2, 3],
    "study_method": ["Online", "Offline", "Online"],
    "final_marks": [40, 50, 60]
}
```
Broken:
```Python
X = df[["study_hours", "study_method"]]
model.fit(X, y)
```
Possible error:
```
ValueError: could not convert string to float
```
Why:
```
LinearRegression expects numerical input.study_method is text.
```
Fix:
```Python
df["study_method"] = df["study_method"].map({    
	"Online": 1,    
	"Offline": 0
})
```
Proper encoding comes on day 2

---
## 17. Production Thinking
Your notebook model is not yet production-ready.
A production ML system must handle:
```
Missing inputs
Wrong input types
Out-of-range values
Schema mismatch
Model versioning
Prediction logging
Monitoring
Retraining
```
Example:
User enters:
```
study_hours = "eight"
```
But model expects:
```
study_hours = 8
```
Your API should validate this before prediction.
Production validation example:
```python
def validate_input(study_hours, attendance, previous_score):
    if not isinstance(study_hours, (int, float)):
        raise ValueError("study_hours must be numeric")

    if study_hours < 0 or study_hours > 24:
        raise ValueError("study_hours must be between 0 and 24")

    if attendance < 0 or attendance > 100:
        raise ValueError("attendance must be between 0 and 100")

    if previous_score < 0 or previous_score > 100:
        raise ValueError("previous_score must be between 0 and 100")
```
---
## 18. Mini Prediction Function
After training, you can create a prediction function:
![[Pasted image 20260609130926.png]]
This simulates real product behaviour:
```
User input → Model prediction → Output
```
---
## 19. Important Warning
This dataset is very small.
So this model is only for learning workflow.
In real ML:
```
10 rows is not enough.
```
You need:
```
More data
Better features
Validation
Cross-validation
Error analysis
Production testing
```
Today’s goal is not to build the best marks predictor.
Today’s goal is to understand the first complete supervised ML workflow.

---
## 20. Beginner-to-Industry Mental Upgarde.
Beginner says:
```
I trained Linear Regression.
```
ML engineer says:
```
I separated features and target, split data into train and test sets, trained a regression model using LinearRegression, generated predictions on unseen test data, and evaluated average prediction error using MAE.
```
Resume-style wording later:
```
Built a supervised regression workflow using Pandas and scikit-learn, including fe
```
---
## 21. Complete Notebook Structure
Your Notebook should have these sections:
```
1. Problem Statement
2. Import Libraries
3. Create / Load Dataset
4. Explore Dataset
5. Separate Features and Target
6. Train-Test Split
7. Model Training
8. Prediction
9. Evaluation
10. Debugging Notes
11. Conclusion
```
---
## 22 Practice Exercise
```Python
new_rows = {
    "study_hours": [11, 12, 3.5, 6.5, 8.5],
    "attendance": [96, 98, 58, 73, 88],
    "previous_score": [92, 95, 48, 67, 82],
    "final_marks": [96, 98, 50, 70, 85]
}
```
Then:
```
1. Retrain the model
2. Predict again
3. Compare MAE
4. Check if error increased or decreased
```
---
## 23. Interview Questions
1. Why do we split data into train and test?
2. What is X_train?
3. What is X_test?
4. What is y_train?
5. What is y_test?
6. What does fit() do?
7. What does predict() do?
8. What is MAE?
9. Why is testing on training data wrong?
10. What is random_state?
---
## 24. Interview Trap Questions
### Trap 1
Question:
```
Can I evaluate my model on X_train?
```
Answer:
```
You can check training performance, but final evaluation should be on unseen test data. Training performance alone does not show generalization.
```
### Trap 2
Question:
```
If MAE is low, is the model production-ready?
```
Answer:
```
Not necessarily. You must check data leakage, feature quality, dataset size, validation, edge cases, deployment input schema, and monitoring.
```
### Trap 3
Question:
```
Why use random_state?
```
Answer:
```
To make the split reproducible so experiments can be debugged and compared consistently.
```
---
## 25. Mini Assignment
```
Task 1:
Run the full code.

Task 2:
Print model.coef_ and model.intercept_.

Task 3:
Create the predict_marks() function.

Task 4:
Predict marks for:
study_hours = 7
attendance = 85
previous_score = 80

Task 5:
Add 5 new rows and retrain.

Task 6:
Write 3 errors you faced or could face.

Task 7:
Write your explanation of train-test split in your own words.
```
---
## 26. Real-World Challenge
You are building:
```
AI Student Performance Predictor
```
Answer:
```
1. What features will you collect?
2. What is the label?
3. Is this classification or regression?
4. What model will you try first?
5. What metric will you use?
6. What can go wrong in production?
7. How will you validate user input?
```
Think like a founder:
```
Would students trust marks prediction?
Could wrong prediction demotivate students?
Should you show exact marks or performance range?
Should you explain why the prediction came?
```
---
## 27. Cheat Sheet
```
X:
Input features.

y:
Target/label.

X_train:
Features used for training.

X_test:
Features used for testing.

y_train:
Correct answers for training.

y_test:
Correct answers for testing.

fit():
Train the model.

predict():
Generate predictions.

MAE:
Average absolute prediction error.

random_state:
Makes split reproducible.

test_size:
Controls test set percentage.

Generalization:
Model performance on unseen data.
```
---
## 28. Mind Map
```
First ML Model
│
├── Dataset
│   ├── Features: X
│   └── Label: y
│
├── Split
│   ├── X_train
│   ├── X_test
│   ├── y_train
│   └── y_test
│
├── Model
│   ├── LinearRegression()
│   ├── fit()
│   └── predict()
│
├── Evaluation
│   └── MAE
│
└── Debugging
    ├── NotFittedError
    ├── KeyError
    ├── Shape mismatch
    └── Text-to-float error
```
---
