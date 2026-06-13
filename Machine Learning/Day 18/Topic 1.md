# Classification Foundations + Logistic Regression
## Goals
```
1. Explain what classification means
2. Differentiate classification from regression
3. Identify binary and multiclass problems
4. Explain why Logistic Regression is a classifier
5. Understand the sigmoid function
6. Understand probability and decision thresholds
7. Train LogisticRegression using scikit-learn
8. Use predict() and predict_proba()
9. Predict the class of a new student
10. Debug common Logistic Regression errors
```
---
## 2. Why Classification Matters
Classification is used when the output is a category or class rather than a continuous number.
Examples:
```
1. Explain what classification means
2. Differentiate classification from regression
3. Identify binary and multiclass problems
4. Explain why Logistic Regression is a classifier
5. Understand the sigmoid function
6. Understand probability and decision thresholds
7. Train LogisticRegression using scikit-learn
8. Use predict() and predict_proba()
9. Predict the class of a new student
10. Debug common Logistic Regression errors
```
Classification systems are used in areas such as :
![[Pasted image 20260613115349.png]]
The important engineering question is not merely:
```
Did the model predict correctly?
```
It is also:
```
What kind of wrong prediction did it make?What is the business cost of that mistake?
```
---
## 3. Classification vs Regression

| Point           | Classification                  | Regression           |
| --------------- | ------------------------------- | -------------------- |
| Output          | Class or category               | Continuous number    |
| Example         | Placed / Not Placed             | Final marks = 82     |
| Target examples | 0/1, Yes/No, class names        | Price, marks, salary |
| Basic model     | Logistic Regression             | Linear Regression    |
| Prediction      | Class and probability           | Numerical value      |
| Common metrics  | Accuracy, Precision, Recall, F1 | MAE, RMSE, R²        |
Simple rule:
```
Category output → Classification
Numerical output → Regression
```
Examples:
```
Predict final marks → Regression
Predict Pass/Fail → Classification
Predict salary amount → Regression
Predict Low/Medium/High salary group → Classification
Predict disease cost → Regression
Predict Disease/No Disease → Classification
```
---
## 4. What Is Classification?
Classification is a supervised learning task in which a model learns from labeled examples and predicts which class a new example belongs to.
General flow:
```
Features + Known Classes
          ↓     
    Train Classifier
          ↓ 
    New feature values
          ↓ 
    Class probability
          ↓ 
    Predicted class
```
Student placement example:
```
Features:CGPA
DSA score
Projects
Internship
Communication score
Label:Placed / Not Placed
```
The model learns patterns such as:
```
Higher DSA score
More projects
Relevant internship
Better communication        
↓
Higher estimated placement probability
```
These patterns are statistical associations, not guaranteed rules.

---
## 5. Binary Classification
Binary classification has exactly two possible classes.
Examples:
```
Placed / Not Placed
Spam / Not Spam
Fraud / Not Fraud
Approved / Rejected
Disease / No Disease
```
The classes are commonly represented as:
```
Positive class = 1Negative class = 0
```
For placement:
```
Placed     = 1
Not Placed = 0
```
The terms **positive** and **negative** do not mean morally good or bad. They simply identify which class is treated as the event of interest.

---
## 6. Multiclass Classification
Multiclass classification has three or more possible classes.
Examples:
```
Iris flower:
	Setosa / Versicolor / Virginica
Support ticket:
	Billing / Technical / Account / Refund
Risk category:
	Low / Medium / High
Digit recognition:
	0 / 1 / 2 / ... / 9
```
Binary:
```
Two mutually exclusive classes
```
Multiclass:
```
Three or more mutually exclusive classes
```
Scikit-learn’s `LogisticRegression` can also support multiclass classification with compatible solvers and a multinomial formulation; this slot’s implementation will remain binary so that you first understand probability and thresholds clearly.

---
## 7. What Is Logistic Regression?
Despite its name, **Logistic Regression is mainly a classification algorithm**.
It performs two main operations:
```
1. Calculate a linear score
2. Convert that score into a probability
```
The linear score is:
```
z = bias + weighted sum of features
```
For placement prediction:
```
z =bias
	+ w1 × cgpa
	+ w2 × dsa_score
	+ w3 × projects
	+ w4 × internship
	+ w5 × communication_score
```
The value `z` can be any real number:
```
-10
-2
.703
.512
```
But a probability must remain between:
```
0 and 1
```
Therefore, Logistic Regression passes `z` through the **sigmoid function**.

---
## 8. Sigmoid Function
![[Pasted image 20260613120605.png]]
The sigmoid converts any real number into a value between 0 and 1. Google’s ML material describes Logistic Regression as applying the sigmoid function to a linear output to obtain a probability.
Examples:

|Linear score `z`|Sigmoid output|
|---|---|
|Very negative|Close to 0|
|`0`|`0.5`|
|Very positive|Close to 1|
Interpretation:
```
Probability close to 0 → likely negative class
Probability close to 1 → likely positive class
```
For placement:
```
0.18 → 18% estimated probability of placement
0.52 → 52% estimated probability
0.91 → 91% estimated probability
```
---
## 9. Why Not Use Linear Regression for Classification?
Suppose Linear Regression predicts:
```
-0.40
.71
.8
```
These are unsuitable as probabilities because probability should remain within:
```
0 ≤ probability ≤ 1
```
The sigmoid solves this by bounding the output.
```
Linear score:
-∞ to +∞
Sigmoid probability:0 to 1
```
Logistic Regression therefore predicts a probability first and then converts it into a class.

---
## 10. Probability and Decision Threshold
Suppose the model predicts:
```
Placement probability = 0.78
```
Using a threshold of `0.50`:
```
Probability >= 0.50 → Placed
Probability < 0.50  → Not Placed
```
Examples:

|Probability|Threshold|Class|
|---|---|---|
|`0.82`|`0.50`|Placed|
|`0.63`|`0.50`|Placed|
|`0.49`|`0.50`|Not Placed|
|`0.12`|`0.50`|Not Placed|
The threshold does not always need to remain `0.50`.
For a high-risk system, it can be changed based on the cost of mistakes:
```
Lower threshold:
Find more positive cases
But create more false alarms
Higher threshold:Require stronger evidence for positive class
But miss more positive cases
```
You will study these trade-offs through **precision, recall and confusion matrices** in Slot 3.

---
## 11. `predict()` vs `predict_proba()`

### `predict()`
Returns the final class:
```
model.predict(X_test)
```
Example output:
```
[1, 0, 1, 1, 0]
```
### `predict_proba()`
Returns probability estimates for each class:
```
model.predict_proba(X_test)
```
Example:
```
[[0.20, 0.80], [0.75, 0.25], [0.10, 0.90]]
```
For every row:
```
First value  = probability of class 0
Second value = probability of class 1
```
For the first example:
```
Not Placed probability = 20%
Placed probability     = 80%
```
Scikit-learn’s probabilistic classifiers expose class probabilities through `predict_proba()`. Well-calibrated probabilities can be interpreted as meaningful confidence estimates, although probability calibration itself needs to be checked rather than assumed.

---
## 12. Logistic Regression Training Workflow
```
Dataset   
↓
Separate X and y   
↓
Train-test split   
↓
Scale numerical features   
↓
Train LogisticRegression   
↓
Predict classes   
↓
Predict probabilities   
↓
Evaluate
```
For this lesson, all features are numerical. We will use a `Pipeline` so scaling and model training remain together.

---
## 13. Complete Placement Dataset
```Python
data = {  
	"cgpa": [
			5.8, 6.1, 6.3, 6.5, 6.7, 6.8,  
			7.0, 7.1, 7.2, 7.4, 7.5, 7.6,  
			7.8, 7.9, 8.0, 8.2, 8.3, 8.4,
			8.5, 8.7, 8.8, 9.0, 9.1, 9.3  
			],  
	"dsa_score": [  
				30, 35, 38, 42, 45, 48,  
				50, 52, 55, 58, 60, 64,
				68, 70, 73, 76, 78, 80,
				83, 85, 88, 90, 92, 95  
				],  
	"projects": [  
				0, 1, 1, 1, 1, 2,  
				1, 2, 2, 2, 3, 2,  
				3, 3, 3, 4, 3, 4,  
				4, 4, 5, 5, 5, 6  
				],  
	"internship": [  
					0, 0, 0, 0, 0, 1,  
					0, 1, 0, 1, 1, 0,  
					1, 1, 1, 1, 1, 1,  
					1, 1, 1, 1, 1, 1  
					],  
	"communication_score": [  
							38, 42, 45, 48, 50, 52,  
							54, 56, 58, 60, 62, 64,  
							67, 69, 71, 74, 76, 78,  
							80, 83, 85, 88, 90, 94  
							],  
	"placed": [  
				0, 0, 0, 0, 0, 0,  
				0, 0, 0, 0, 0, 1,  
				0, 1, 1, 1, 1, 1,  
				1, 1, 1, 1, 1, 1  
				]  
}
```
![[Pasted image 20260613122919.png]]
![[Pasted image 20260613122947.png]]
Here:

```
Features:
cgpa
dsa_score
projects
internship
communication_score

Target:
placed
```
Encoding:
```
0 = Not Placed
1 = Placed
```
---
## 14. Separate Features and Target
![[Pasted image 20260613124200.png]]
Expected structure:
```
X → 2D feature matrix
y → 1D target vector
```
Never include `placed` inside `X`.
Wrong:
```
X = df
y = df["placed"]
```
That gives the model access to the correct answer and causes data leakage.

---
## 15. Train-Test Split
![[Pasted image 20260613124510.png]]
### Why `stratify=y`?
It tries to preserve the target class proportion in both train and test sets.
Example:
```
Full dataset:
50% class 0
50% class 1
With stratification:
Train and test stay close to the same proportion
```
This is especially useful for classification datasets.
Check it:
![[Pasted image 20260613124939.png]]

---
## 16. Build a Logistic Regression Pipeline
![[Pasted image 20260613125319.png]]
Why scale?
```
Features have different ranges:
CGPA                ≈ 5–10
DSA score           ≈ 0–100
Projects            ≈ 0–10
Communication score ≈ 0–100
```
Scaling gives the optimizer a better-conditioned problem and makes regularization act more fairly across features.
Scikit-learn ’s Logistic Regression estimator uses regularization by default. Its parameter `C` controls the inverse of regularization strength: smaller `C` means stronger regularization.

---
## 17. Train the Model
![[Pasted image 20260613125709.png]]
Internally, this performs:
```
1. StandardScaler learns mean and standard deviation from X_train
2. X_train is standardized
3. LogisticRegression learns coefficients
4. Training loss is optimized
```
The test set is not used to fit the scaler or model.

---
## 18. Predict Classes
![[Pasted image 20260613125914.png]]
Example interpretation:
```
Actual    = 1
Predicted = 1
Correct positive prediction
```
```
Actual    = 0
Predicted = 1
Incorrect positive prediction
```
You will name these cases formally as TP, TN, FP and FN in Slot 3.

---
## 19. Predict Probabilities
![[Pasted image 20260613130520.png]]
The most useful column is:
```
Probability_Placed
```
Example:
```
0.84 means the model estimated an 84% probability of class 1.
```
Do not describe this as a guaranteed 84% chance unless the classifier has been checked for probability calibration and evaluated on representative data.

---
## 20. Basic Accuracy Check
Metrics will be covered properly in Slot 3, but use accuracy here only as a quick check:
![[Pasted image 20260613130722.png]]
Interpretation:
```
Accuracy = correctly classified examples / total examples
```
Important:
```
Accuracy alone can be misleading,especially when one class is much more common than the other.
```
You will study that in Slot 5 under class imbalance.

---
## 21. Complete Working Program
```Python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = {
    "cgpa": [
        5.8, 6.1, 6.3, 6.5, 6.7, 6.8,
        7.0, 7.1, 7.2, 7.4, 7.5, 7.6,
        7.8, 7.9, 8.0, 8.2, 8.3, 8.4,
        8.5, 8.7, 8.8, 9.0, 9.1, 9.3
    ],
    "dsa_score": [
        30, 35, 38, 42, 45, 48,
        50, 52, 55, 58, 60, 64,
        68, 70, 73, 76, 78, 80,
        83, 85, 88, 90, 92, 95
    ],
    "projects": [
        0, 1, 1, 1, 1, 2,
        1, 2, 2, 2, 3, 2,
        3, 3, 3, 4, 3, 4,
        4, 4, 5, 5, 5, 6
    ],
    "internship": [
        0, 0, 0, 0, 0, 1,
        0, 1, 0, 1, 1, 0,
        1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1
    ],
    "communication_score": [
        38, 42, 45, 48, 50, 52,
        54, 56, 58, 60, 62, 64,
        67, 69, 71, 74, 76, 78,
        80, 83, 85, 88, 90, 94
    ],
    "placed": [
        0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 1,
        0, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1
    ]
}

df = pd.DataFrame(data)

X = df[
    [
        "cgpa",
        "dsa_score",
        "projects",
        "internship",
        "communication_score"
    ]
]

y = df["placed"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

model = Pipeline(steps=[
    ("scaler", StandardScaler()),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            random_state=42
        )
    )
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_probability = model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, y_pred)

results = X_test.copy()
results["Actual"] = y_test
results["Predicted"] = y_pred
results["Probability_Placed"] = y_probability

print("Classification Results:")
print(results.sort_values("Probability_Placed", ascending=False))

print("\nAccuracy:")
print(accuracy)
```
---
## 22. Predict a New Student
![[Pasted image 20260613131333.png]]
Possible output:
```
Predicted Class: Placed
Estimated Placement Probability: 79.24%
```
A safer product message:
```
print(f"Estimated placement-readiness probability: {placed_probability:.1%}")
print("This is a model estimate, not a guarantee of placement.")
```
---
## 23. Apply a Custom Threshold
Suppose you want a stricter threshold:
![[Pasted image 20260613131508.png]]
For example:
```
Probability = 0.65
At threshold 0.50 → Placed
At threshold 0.70 → Not Placed
```
This proves that a class prediction depends not only on the model but also on the chosen decision threshold.

---
## 24. Inspect Logistic Regression Coefficients
Retrieve the trained classifier:
![[Pasted image 20260613134617.png]]
Create a coefficient table:
![[Pasted image 20260613134906.png]]
Basic interpretation:
```
Positive coefficient:
Higher feature value tends to increase predicted class-1 log-odds.

Negative coefficient:
Higher feature value tends to reduce predicted class-1 log-odds.
```
Important caution:
```
Coefficient association is not causation.
Coefficient magnitude depends on scaling, correlation and regularization.
```
Because our pipeline standardizes features, comparing coefficient magnitudes is more meaningful than comparing coefficients from differently scaled raw features, but it is still not absolute proof of real-world importance.

---
## 25. Advanced Intuition: Log-Odds
The sigmoid probability can be transformed into odds:
```
Odds = p / (1 - p)
```
For:
```
p = 0.80
```
Odds are:
```
0.80 / 0.20 = 4
```
This means:
```
The modeled odds of class 1 are 4 to 1.
```
Logistic Regression assumes that the **logarithm of these odds** is a linear combination of the features. 
Google’s Logistic Regression explanation describes the linear score `z` as log-odds.
You do not need to derive log-odds fully today, but remember:
```
Features combine linearly in log-odds space.
Sigmoid converts log-odds into probability.
```

---
## 26. Regularization Awareness
Scikit-learn’s `LogisticRegression` is regularized by default. The parameter:
```
C
```
controls inverse regularization strength.
```
Small C → stronger regularization
Large C → weaker regularization
```
Example:
```
LogisticRegression(C=0.1)
```
Stronger regularization may:
```
Reduce extreme coefficients
Improve stability
Reduce overfitting
Increase underfitting if too strong
```
Example with weaker regularization:
```
LogisticRegression(C=10)
```
Do not tune `C` using the test set. Later, use validation or cross-validation.

---
## 27. Production-Level Thinking
A student placement model should not directly declare:
```
You will not get placed.
```
That can be harmful and overconfident.
A better output is:
```
Estimated placement-readiness probability: 64%
Current strengths:
• Strong CGPA
• Good project count

Potential improvement areas:
• DSA assessment score
• Communication assessment score
This estimate is based on historical patterns and is not a guarantee.
```
Production checks should include:
```
Input validation
Missing-value handling
Feature-schema validation
Probability monitoring
Class-distribution monitoring
Fairness analysis
Threshold review
Model retraining
Human review for high-impact decisions
```
---
## 28. Production Failure Scenarios
### Scenario 1: Wrong Input Range
Input:
```
CGPA = 85
```
Expected:
```
CGPA between 0 and 10
```
Solution:
```Python
def validate_student_input(
    cgpa,
    dsa_score,
    projects,
    internship,
    communication_score
):
    if not 0 <= cgpa <= 10:
        raise ValueError("cgpa must be between 0 and 10")

    if not 0 <= dsa_score <= 100:
        raise ValueError("dsa_score must be between 0 and 100")

    if projects < 0:
        raise ValueError("projects cannot be negative")

    if internship not in (0, 1):
        raise ValueError("internship must be 0 or 1")

    if not 0 <= communication_score <= 100:
        raise ValueError(
            "communication_score must be between 0 and 100"
        )
```
---
### Scenario 2: Changed Feature Schema
Training:
```
cgpa
dsa_score
projects
internship
communication_score
```
Production input:
```
cgpa
dsa_score
projects
communication_score
```
Missing:
```
internship
```
The model can fail because prediction features do not match training features.
Senior solution:
```
Define and validate an explicit input schema.
Use a DataFrame with the exact training column names.
Save preprocessing and classifier together.
```
---
### Scenario 3: Historical Bias
Suppose past placement outcomes were affected by biased hiring or unequal opportunity.
The model can learn those historical patterns.
Senior-engineer response:
```
Audit data collectionReview sensitive and proxy variables
Evaluate metrics across relevant subgroups
Use the model as decision support, not unquestioned authority
Document known limitations
```
---
## 29. Common Beginner Mistakes
```
1. Thinking Logistic Regression predicts continuous values
2. Calling Logistic Regression a regression model
3. Using predict() when probability is required
4. Treating probability as a guarantee
5. Including target column inside X
6. Forgetting train-test split
7. Fitting scaler before train-test split
8. Forgetting to encode text features
9. Using mismatched columns during prediction
10. Ignoring class distribution
11. Treating 0.50 as the only possible threshold
12. Looking only at accuracy
13. Confusing positive class with a morally positive outcome
14. Interpreting coefficients as causation
15. Ignoring probability calibration
```
---
## 30. Debugging Section
### Error 1: Continuous Target Used for Classification
Broken:
```
y = df["final_marks"]
model.fit(X_train, y_train)
```
Possible error:
```
ValueError: Unknown label type: continuous
```
Why:
```
LogisticRegression requires categorical class labels.final_marks contains continuous numerical values.
```
Fix:
```
y = df["placed"]
```
---
### Error 2: Raw Text Feature
Broken dataset:
```
internship = Yes / No
```
Possible error:
```
ValueError: could not convert string to float: 'Yes'
```
Fix:
```
df["internship"] = df["internship"].map({    "No": 0,    "Yes": 1})
```
For nominal features with more than two categories, use `OneHotEncoder` inside a `ColumnTransformer`.

---
### Error 3: Predict Before Training
Broken:
```
model.predict(X_test)
```
before:
```
model.fit(X_train, y_train)
```
Error:
```
NotFittedError: This Pipeline instance is not fitted yet
```
Fix:
```
model.fit(X_train, y_train)y_pred = model.predict(X_test)
```
---
### Error 4: Feature Name Mismatch
Training features:
```
cgpa
dsa_score
projects
internship
communication_score
```
Prediction input accidentally uses:
```
communication
```
Possible error:
```
ValueError: The feature names should match those that were passed during fit.
```
Fix:
```
new_student = pd.DataFrame({    "cgpa": [8.1],    "dsa_score": [76],    "projects": [3],    "internship": [1],    "communication_score": [74]})
```
---
### Error 5: Convergence Warning
Possible warning:
```
ConvergenceWarning: lbfgs failed to converge
```
Possible causes:
```
Features are not scaledmax_iter is too smallData is difficult to optimizeSolver choice is unsuitable
```
Initial fixes:
```
Pipeline(steps=[    ("scaler", StandardScaler()),    (        "classifier",        LogisticRegression(max_iter=1000)    )])
```
Do not blindly increase iterations without first checking scaling and data quality.

---
### Error 6: Target Leakage
Wrong:
```
X = df[    [        "cgpa",        "dsa_score",        "projects",        "internship",        "communication_score",        "placed"    ]]y = df["placed"]
```
The model sees the answer inside the features.
Fix:
```
X = df.drop("placed", axis=1)y = df["placed"]
```
---
## 31. Interview Questions
Prepare these answers in your own words:
```
1. What is classification?
2. Classification vs regression?
3. What is binary classification?
4. What is multiclass classification?
5. What is Logistic Regression?
6. Why is Logistic Regression a classifier?
7. What does the sigmoid function do?
8. What is a decision threshold?
9. Difference between predict() and predict_proba()?
10. Why do we use stratify=y?
11. Why is feature scaling useful?
12. What does a positive coefficient mean?
13. Can the threshold be changed from 0.50?
14. What is regularization in Logistic Regression?
15. Why should probabilities not automatically be treated as calibrated confidence?
```
---
## 32. Interview Trap Questions
### Trap 1
**Is Logistic Regression a regression model?**
Strong answer:
```
Despite its name, Logistic Regression is primarily used for classification. It models class probability by applying the sigmoid function to a linear score.
```
### Trap 2
**Does `predict_proba()` return one probability?**
Strong answer:
```
For binary classification it returns one probability per class. The second column normally corresponds to the probability of classes_[1], so class order should be checked using model.classes_ or the classifier step.
```
For the pipeline:
```
print(model.named_steps["classifier"].classes_)
```
### Trap 3
**Is 0.50 always the best threshold?**
Strong answer:
```
No. The threshold should reflect business costs and the trade-off between different classification errors.
```
### Trap 4
**Does 90% probability mean the prediction is guaranteed?**
Strong answer:
```
No. It is a model estimate. Its reliability depends on data quality, calibration, distribution shift and evaluation on representative data.
```
### Trap 5
**Does a positive coefficient prove causation?**
Strong answer:
```
No. It represents an association learned by the model while holding other modeled features constant, not proof that changing the feature causes the outcome.
```
------
## 34. Practice Exercise

Classify each problem as binary, multiclass or regression:

```
1. Predict whether a transaction is fraudulent.
2. Predict a student's final score.
3. Predict flower species among three classes.
4. Predict loan approved/rejected.
5. Predict support ticket category.
6. Predict customer lifetime value.
7. Predict positive/neutral/negative sentiment.
8. Predict whether a user will cancel a subscription.
```
Answers:
```
1. Binary classification
2. Regression
3. Multiclass classification
4. Binary classification
5. Multiclass classification
6. Regression
7. Multiclass classification
8. Binary classification
```
---
## 35. Coding Assignment
Complete before moving to Slot 2:
```
Task 1:
Run the full Logistic Regression program.

Task 2:
Print:
X_train.shape
X_test.shape
y_train.value_counts()
y_test.value_counts()

Task 3:
Print predicted classes.

Task 4:
Print probability of both classes.

Task 5:
Create a results DataFrame with:
Actual
Predicted
Probability_Not_Placed
Probability_Placed

Task 6:
Predict placement for three new students.

Task 7:
Apply thresholds:
0.40
0.50
0.70

Task 8:
Print Logistic Regression coefficients.

Task 9:
Explain one positive and one negative coefficient.

Task 10:
Create and test the input-validation function.
```
---
## 36. Real-World Challenge
You are designing a placement-readiness system.
The model predicts:
```
Student A → 0.82Student B → 0.56Student C → 0.31
```
Answer:
```
1. What are their classes at threshold 0.50?
2. What are their classes at threshold 0.70?
3. Which student is most uncertain?
4. Should Student B be declared "not placement-ready"?
5. What safer message should the product show?
6. What happens if the training data is biased?
7. Which features must be available at prediction time?
```
Recommended product message for Student B:
```
Estimated placement-readiness probability: 56%.The result is uncertain and should be combined with skill assessments, project review and interview feedback.
```
---
## 37. Quick Revision Sheet
```
Classification:
Predicts a category.

Binary Classification:
Two possible classes.

Multiclass Classification:
Three or more classes.

Logistic Regression:
Linear score + sigmoid probability.

Sigmoid:
Maps any real value to 0–1.

predict():
Returns final class.

predict_proba():
Returns class probabilities.

Threshold:
Converts probability into class.

Default learning threshold:
Commonly 0.50 for binary classification.

stratify=y:
Preserves class proportions during splitting.

Positive coefficient:
Increases class-1 log-odds as the feature increases.

Negative coefficient:
Decreases class-1 log-odds as the feature increases.

C:
Inverse regularization strength.

Pipeline:
Keeps scaling and classifier together.
```
---
