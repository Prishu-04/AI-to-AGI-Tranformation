# Classification Metrics
## 1. Goal
```
1. Build and interpret a confusion matrix
2. Explain TP, TN, FP and FN
3. Calculate Accuracy
4. Calculate Precision
5. Calculate Recall
6. Calculate F1-score
7. Read classification_report
8. Select metrics according to business risk
9. Evaluate binary classification
10. Evaluate multiclass classification
11. Explain macro, micro and weighted averaging
12. Identify when accuracy is misleading
13. Debug common classification-metric errors
```
---
# 2. Why Classification Metrics Matter

Suppose a disease-detection model makes 95 correct predictions out of 100.
You may say:
```
Accuracy = 95%The model is excellent.
```
But what if the five incorrect predictions were all patients who actually had the disease?
Then the model missed every important positive case.
Similarly, a fraud detector may achieve 99% accuracy by predicting every transaction as non-fraud when only 1% of transactions are fraudulent.
Therefore, classification evaluation asks:
```
How many predictions were correct?
Which class was predicted incorrectly?
Did the model miss positive cases?
Did it create false alarms?
What is the business cost of each mistake?
```
---
## 3. Confusion Matrix
A confusion matrix compares:
```
Actual classes vs Predicted classes
```
For binary classification:
![[Pasted image 20260615112207.png]]
Using class labels:
```
0 = Negative class
1 = Positive class
```
Scikit-learn normally displays:
```
Rows    = Actual classes
Columns = Predicted classes
```
So:
```
[[TN, FP], [FN, TP]]
```
---
## 4. True Positive
### Definition
The actual class is positive, and the model predicts positive.
```
Actual = 1Predicted = 1
```
Example in disease detection:
```
Patient has diseaseModel predicts disease
```
Example in fraud detection:
```
Transaction is fraudulentModel predicts fraud
```
This is a correct positive prediction.

---
## 5. True Negative
### Definition
The actual class is negative, and the model predicts negative.
```
Actual = 0Predicted = 0
```
Disease example:
```
Patient does not have diseaseModel predicts no disease
```
Fraud example:
```
Transaction is genuineModel predicts genuine
```
This is a correct negative prediction.

---
## 6. False Positive
### Definition
The actual class is negative, but the model predicts positive.
```
Actual = 0
Predicted = 1
```
It is also called:
```
Type I Error
False alarm
```
Examples:
```
A genuine email is classified as spam.
A genuine bank transaction is blocked as fraud.
A healthy patient is classified as diseased.
A loan-worthy customer is classified as risky.
```
False positives can cause:
```
Unnecessary investigation
Customer frustration
Lost business
Unnecessary medical testing
Valid emails being blocked
```
---
## 7. False Negative
### Definition
The actual class is positive, but the model predicts negative.
```
Actual = 1
Predicted = 0
```
It is also called:
```
Type II Error
Missed positive
```
Examples:
```
A fraudulent transaction is classified as genuine.
A sick patient is classified as healthy.
A spam message reaches the inbox.
An at-risk student is classified as safe.
```
False negatives can cause:
```
Missed disease
Financial loss
Security failure
Missed intervention
Dangerous false reassurance
```
---
## 8. Positive Class Must Be Defined
The positive class is the event you care about detecting.
For fraud detection:
```
Positive = FraudNegative = Genuine
```
For disease screening:
```
Positive = Disease
Negative = No Disease
```
For spam filtering:
```
Positive = SpamNegative = Not Spam
```
The word **positive** does not mean good. It means the class treated as the target event.
Metrics such as Precision and Recall depend on which class is selected as positive.

---
## 9. Confusion Matrix Example
Suppose a fraud model produces:
```
TN = 900
FP = 50
FN = 20
TP = 30
```
Confusion matrix:
![[Pasted image 20260615112607.png]]
Total predictions:
```
900 + 50 + 20 + 30 = 1000
```
Correct predictions:
```
TN + TP = 900 + 30 = 930
```
Incorrect predictions:
```
FP + FN = 50 + 20 = 70
```
---
## 10. Accuracy
Accuracy measures the proportion of all predictions that were correct.
![[Pasted image 20260615112929.png]]
Using the fraud example:
```
Accuracy = (30 + 900) / 1000
Accuracy = 0.93
Accuracy = 93%
```
Meaning:
```
The model correctly classified 93% of all transactions.
```
## When accuracy is useful
Accuracy is useful when:
```
Classes are reasonably balanced
False positives and false negatives have similar costs
Every class matters approximately equally
```
## When accuracy is misleading
Accuracy is risky when:
```
One class is much more commonThe cost of FP and FN differs greatlyThe minority class is the important class
```
---
## 11. Accuracy Trap
Dataset:
```
990 genuine transactions
10 fraudulent transactions
```
A useless model predicts:
```
Every transaction = Genuine
```
Results:
```
990 correct
10 wrong
```
Accuracy:
```
990 / 1000 = 99%
```
But:
```
Fraud detected = 0
Recall for fraud = 0%
```
So the classifier is useless despite 99% accuracy.

---
## 12. Precision
Precision answers:
```
Of everything predicted positive,how many were actually positive?
```
![[Pasted image 20260615113341.png]]
Using:
```
TP = 30
FP = 50
```
Then:
```
Precision = 30 / (30 + 50)
Precision = 0.375
Precision = 37.5%
```
Meaning:
```
Of all transactions flagged as fraud,only 37.5% were actually fraudulent.
```
Low Precision means:
```
Many false alarms
Many False Positives
```
---
## 13. When Precision Matters
Prioritize Precision when false positives are expensive.
Examples:

|Scenario|False-positive cost|
|---|---|
|Spam filter|Important email moved to spam|
|Fraud system|Genuine transaction blocked|
|Content moderation|Safe content removed|
|Hiring system|Qualified candidate rejected as unsuitable|
|Loan-risk system|Reliable borrower marked risky|
Strong intuition:
```
High Precision =When the model says positive,it is usually correct.
```
---
## 14. Recall
Recall answers:
```
Of all actual positive cases,how many did the model detect?
```
![[Pasted image 20260615113512.png]]
Using:
```
TP = 30
FN = 20
```
Then:
```
Recall = 30 / (30 + 20)
Recall = 0.60Recall = 60%
```
Meaning:
```
The model detected 60% of all fraudulent transactions.
```
Low Recall means:
```
Many positive cases were missedMany False Negatives
```
Recall is also called:
```
Sensitivity
True Positive Rate
```
---
## 15. When Recall Matters
Prioritize Recall when false negatives are expensive or dangerous.
Examples:

| Scenario               | False-negative cost                 |
| ---------------------- | ----------------------------------- |
| Disease screening      | Sick patient missed                 |
| Fraud detection        | Fraud remains undetected            |
| Cybersecurity          | Attack classified as safe           |
| Fire detection         | Real fire alarm not triggered       |
| Student-risk detection | At-risk student receives no support |
Strong intuition:
```
High Recall =The model finds most actual positive cases.
```
---
## 16. Precision vs Recall
Suppose a fraud model flags almost every transaction as fraud.
Then:
```
It finds most fraud cases
Recall becomes high
But it also creates many false alarms
Precision becomes low
```
Suppose the model flags fraud only when extremely confident.
Then:
```
Most flagged cases are genuine fraud
Precision becomes high
But many fraud cases are missed
Recall becomes low
```
This creates the **Precision–Recall trade-off**.

| Goal                 | Main concern           |
| -------------------- | ---------------------- |
| High Precision       | Reduce false positives |
| High Recall          | Reduce false negatives |
| Balanced performance | Use F1-score           |

---
## 17. F1-Score
F1-score balances Precision and Recall using their harmonic mean.
![[Pasted image 20260615114128.png]]
Using:
```
Precision = 0.375
Recall = 0.60
```
Then:
```
F1 ≈ 0.46
```
F1 becomes high only when both Precision and Recall are reasonably high.
Examples:

|Precision|Recall|F1 behaviour|
|---|---|---|
|High|High|High F1|
|High|Low|Reduced F1|
|Low|High|Reduced F1|
|Low|Low|Low F1|

---
## 18. When F1-Score Matters
Use F1-score when:
```
Classes are imbalanced
Both false positives and false negatives matter
You need one metric balancing Precision and Recall
```
Examples:
```
Fraud detection
Spam detection
Medical classification
Customer churnDefect detection
Cybersecurity alerts
```
Important:
```
F1 does not include True Negatives directly.
```
Therefore, do not use it blindly when correct negative detection is especially important.

---
## 19. Metric Summary

| Metric    | Main question                                       | Best when                                |
| --------- | --------------------------------------------------- | ---------------------------------------- |
| Accuracy  | How often was the model correct overall?            | Balanced classes and similar error costs |
| Precision | When it predicts positive, how often is it correct? | False positives are costly               |
| Recall    | How many actual positives did it find?              | False negatives are costly               |
| F1-score  | How balanced are Precision and Recall?              | Imbalanced data and both errors matter   |
## 20. Binary Classification Code
We will reuse the Student Placement dataset from Slot 1.
```Python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

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

X = df.drop("placed", axis=1)
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
```
---
## 21. Calculate Confusion Matrix
![[Pasted image 20260615115114.png]]
Extract values:
![[Pasted image 20260615115349.png]]
Important:
```
cm.ravel() gives TN, FP, FN, TP
only for a 2×2 matrix arranged as labels=[0, 1].
```
---
## 22. Calculate All Binary Metrics
![[Pasted image 20260615115946.png]]
![[Pasted image 20260615115959.png]]

---
## 23. Calculate Metrics Manually
![[Pasted image 20260615120120.png]]
The manual results should match scikit-learn.

---
## 24. Classification Report
`classification_report` summarizes:
```
Precision
Recall
F1-score
Support
```
Code:
![[Pasted image 20260615120253.png]]

---
## 25. What Is Support?
Support means:
```
Number of actual examples belonging to a class
```
Example:
```
Placed support = 20
```
Means:
```
There were 20 actual Placed examples in the evaluated data.
```
Support is not a model-quality metric. It tells you how many examples each class had.
Small support can make metrics unstable.

---
## 26. Reading a Classification Report
Suppose:
```
Placed:Precision = 0.80
Recall = 0.60
F1 = 0.69
Support = 50
```
Interpretation:
```
Precision 0.80:
80% of predicted Placed cases were actually Placed.

Recall 0.60:
The model found 60% of all students who were actually Placed.

F1 0.69:
Combined Precision–Recall performance was moderate.

Support 50:
There were 50 actual Placed examples.
```
---
## 27. Display the Confusion Matrix Visually
![[Pasted image 20260615120613.png]]
![[Pasted image 20260615120629.png]]
Remember:
```
Rows = actual
Columns = predicted
```
Always verify the axis labels instead of relying only on memory.

---
## 28. Actual vs Predicted Table
![[Pasted image 20260615122727.png]]
![[Pasted image 20260615122744.png]]
This allows you to inspect exactly which students were:
```
True Positives
True Negatives
False Positives
False Negatives
```
---
## 29. Complete Binary Metrics Program
```Python
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

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

X = df.drop("placed", axis=1)
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

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=[0, 1]
)

tn, fp, fn, tp = cm.ravel()

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)
recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)
f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)

print("Confusion Matrix:")
print(cm)

print("\nTN:", tn)
print("FP:", fp)
print("FN:", fn)
print("TP:", tp)

print("\nAccuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=[
            "Not Placed",
            "Placed"
        ],
        zero_division=0
    )
)

results = X_test.copy()
results["Actual"] = y_test
results["Predicted"] = y_pred
results["Probability_Placed"] = y_probability

print("\nDetailed Results:")
print(results)

ConfusionMatrixDisplay.from_predictions(
    y_test,
    y_pred,
    display_labels=[
        "Not Placed",
        "Placed"
    ],
    values_format="d"
)

plt.title("Student Placement Confusion Matrix")
plt.tight_layout()
plt.show()
```

---
## 30. Business Cost of False Positives and False Negatives
Metrics should be selected using business cost, not personal preference.
A simple cost model is:
![[Pasted image 20260615123458.png]]
Where:
```
C_FP = cost of one false positive
C_FN = cost of one false negative
```
Example:
```
FP = 50
Cost per FP = ₹100
FN = 20
Cost per FN = ₹1,000
```
Total cost:
```
50 × 100 + 20 × 1,000
= 5,000 + 20,000
= ₹25,000
```
Even though there are fewer false negatives, they create most of the cost.

---
## 31. Metric-Selection Scenarios
### Medical screening
Main danger:
```
Patient has disease
Model says no disease
```
This is a False Negative.
Priority:
```
High Recall
```
Precision still matters because too many false positives create unnecessary testing, but missing disease can be more dangerous.

---
### Spam filtering
Main danger:
```
Important emailModel sends it to spam
```
This is a False Positive when Spam is class 1.
Priority:
```
High Precision for the Spam class
```
---
### Fraud detection
Two costs:
```
False Negative:
Fraud goes undetected
False Positive:
Genuine customer transaction is blocked
```
Possible priority:
```
Recall + Precision
F1-score
Cost-sensitive threshold
```
---
### Fire alarm
Main danger:
```
Real fire
No alarm
```
This is a False Negative.
Priority:
```
Very high Recall
```
Some false alarms may be acceptable if missing a fire is catastrophic.

---
### Loan default prediction
Suppose:
```
Positive = Will Default
```
False Negative:
```
Risky borrower predicted safePossible financial loss
```
False Positive:
```
Safe borrower predicted riskyLost customer and unfair rejection
```
Metric selection must account for:
```
Financial cost
Fairness
Regulation
Customer impact
```
---
### Student intervention system
Suppose:
```
Positive = Student needs support
```
False Negative:
```
At-risk student receives no intervention
```
False Positive:
```
Student unnecessarily receives additional support
```
Recall may be prioritized because offering extra support is usually less harmful than missing a struggling student.

---
## 32. Binary Metric Averaging
For binary classification, scikit-learn commonly uses:
```
average="binary"
```
Example:
```
precision_score(    
	y_test,    
	y_pred,    
	average="binary",    
	pos_label=1)
```
This calculates the metric only for the selected positive class.
To evaluate class 0 instead:
```
precision_score(    
	y_test,    
	y_pred,    
	average="binary",    
	pos_label=0)
```
The result may change because the positive class changed.

---
## 33. Multiclass Evaluation
For Iris:
```
Class 0 = Setosa
Class 1 = Versicolor
Class 2 = Virginica
```
There is no single natural positive class.
Metrics are first calculated for each class using a one-vs-rest interpretation.
Then they can be averaged using:
```
Macro average
Weighted average
Micro average
```
---
## 34. Macro Average
Macro average:
```
Calculate metric separately for every class
Then take the simple average
```
Formula idea:
```
Macro F1 =(F1 class 0 + F1 class 1 + F1 class 2) / 3
```
Every class receives equal importance, regardless of class size.
Use macro average when:
```
All classes matter equally
You want poor minority-class performance to remain visible
The dataset may be imbalanced
```
---
## 35. Weighted Average
Weighted average:
```
Calculate metric per class
Weight each class according to its support
```
A class with more examples contributes more to the final score.
Use weighted average when:
```
You want an overall summary accounting for class frequency
Class sizes differ
```
Risk:
```
A large majority class can hide weak minority-class performance.
```
Always inspect per-class metrics too.

---
## 36. Micro Average
Micro average:
```
Aggregate TP, FP and FN across all classes
Then calculate the metric
```
Each individual prediction receives equal weight.
For ordinary single-label multiclass classification:
```
Micro Precision
Micro Recall
Micro F1
```
are generally equal to overall Accuracy.
Use micro averaging when:
```
You want overall instance-level performance
Large classes should naturally contribute more
```
---
## 37. Macro vs Weighted vs Micro

|Average|Gives equal weight to|Best use|
|---|---|---|
|Macro|Every class|All classes equally important|
|Weighted|Classes according to support|Overall result accounting for imbalance|
|Micro|Every prediction|Global instance-level performance|

Example class supports:
```
Class A = 900 samples
Class B = 90 samples
Class C = 10 samples
```
Macro:
```
A, B and C each contribute one-third.
```
Weighted:
```
Class A dominates because it has 900 samples.
```
Micro:
```
Counts all individual decisions together.
```
---
## 38. Multiclass Metrics with Iris and KNN

```Python
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

iris = load_iris(as_frame=True)

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model = Pipeline(steps=[
    ("scaler", StandardScaler()),
    (
        "classifier",
        KNeighborsClassifier(
            n_neighbors=5
        )
    )
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

macro_precision = precision_score(
    y_test,
    y_pred,
    average="macro",
    zero_division=0
)

macro_recall = recall_score(
    y_test,
    y_pred,
    average="macro",
    zero_division=0
)

macro_f1 = f1_score(
    y_test,
    y_pred,
    average="macro",
    zero_division=0
)

weighted_f1 = f1_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

micro_f1 = f1_score(
    y_test,
    y_pred,
    average="micro",
    zero_division=0
)

print("Accuracy:", accuracy)
print("Macro Precision:", macro_precision)
print("Macro Recall:", macro_recall)
print("Macro F1:", macro_f1)
print("Weighted F1:", weighted_f1)
print("Micro F1:", micro_f1)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names,
        zero_division=0
    )
)
```
![[Pasted image 20260615125252.png]]

---
## 39. Per-Class Metrics Without Averaging
Use:
![[Pasted image 20260615140400.png]]
![[Pasted image 20260615140425.png]]
This is often more useful than using only one overall number.

---
## 40. Threshold Effects on Metrics
For binary classifiers, changing the probability threshold changes the confusion matrix.
![[Pasted image 20260615140612.png]]
Typical effect of increasing threshold:
```
Fewer positive predictions
False Positives may decrease
Precision may increase
False Negatives may increase
Recall may decrease
```
Typical effect of decreasing threshold:
```
More positive predictions
False Negatives may decrease
Recall may increase
False Positives may increase
Precision may decrease
```
There is no universally best threshold.
It depends on business cost.

---
## 41. Compare Thresholds
For the binary placement model:
```Python
threshold_results = []
probabilities = model.predict_proba(X_test)[:, 1]
for threshold in [0.30, 0.50, 0.70]:
    custom_pred = (
        probabilities >= threshold
    ).astype(int)
    threshold_results.append({
        "Threshold": threshold,
        "Accuracy": accuracy_score(
            y_test,
           custom_pred
        ),
        "Precision": precision_score(
            y_test,
            custom_pred,
            average="macro",
            zero_division=0
        ),
        "Recall": recall_score(
            y_test,
            custom_pred,
            average="macro",
            zero_division=0
        ),
        "F1": f1_score(
            y_test,
            custom_pred,
            average="macro",
            zero_division=0
        )
    })
print(pd.DataFrame(threshold_results))
```
![[Pasted image 20260615142450.png]]
Do not tune the threshold repeatedly on the final test set. Use validation data or cross-validation predictions during real model development.

---
## 42. Debugging Section
### Error 1: Swapping Actual and Predicted
Wrong:
```
confusion_matrix(    
	y_pred,    
	y_test
)
```
Correct:
```
confusion_matrix(    
	y_test,    
	y_pred
)
```
Why?
```
Most metric functions expect:first actual labelsthen predicted labels
```
Swapping them can change Precision and Recall interpretation.

---
### Error 2: Confusing Matrix Orientation
Wrong assumption:
```
Rows = predicted
Columns = actual
```
Scikit-learn default:
```
Rows = actual
Columns = predicted
```
Prevention:
```
Always label the axes.
Use ConfusionMatrixDisplay.
```
---
### Error 3: Binary Average on Multiclass Data
Broken:
```
precision_score(    y_test,    y_pred)
```
on a multiclass target.
Possible error:
```
ValueError:Target is multiclass but average='binary'
```
Fix:
```
precision_score(    y_test,    y_pred,    average="macro")
```
Other options:
```
average="micro"
average="weighted"
average=None
```
---
### Error 4: No Predicted Positive Cases
Suppose a model predicts every example as class 0.
Then:
```
TP + FP = 0
```
Precision becomes mathematically undefined.
Possible warning:
```
UndefinedMetricWarning:
Precision is ill-defined and being set to 0.0
due to no predicted samples
```
Temporary reporting fix:
```
precision_score(    y_test,    y_pred,    zero_division=0)
```
But the real engineering response is:
```
Investigate class imbalance
Check threshold
Check features
Check model settings
Check data quality
```
Do not hide a bad model using `zero_division=0`.

---
### Error 5: Probabilities Passed Directly to Confusion Matrix
Wrong:
```
probabilities = model.predict_proba(    X_test)[:, 1]
confusion_matrix(    y_test,    probabilities)
```
Possible error:
```
ValueError:Classification metrics can't handle a mixof binary and continuous targets
```
Fix:
```
custom_pred = (    
	probabilities >= 0.50).astype(int)
confusion_matrix(    
	y_test,    
	custom_pred)
```
---
### Error 6: Wrong Positive Label
Suppose:
```
0 = Disease
1 = Healthy
```
Using default:
```
recall_score(y_test, y_pred)
```
calculates Recall for class 1, which is Healthy.
To calculate disease Recall:
```
recall_score(    
	y_test,    
	y_pred,    
	pos_label=0)
```
Always document the class mapping.

---
### Error 7: Accuracy on Imbalanced Data
Problem:
```
Accuracy = 98%
Minority-class Recall = 0%
```
Fix:
```
Inspect class distribution
Inspect confusion matrix
Inspect per-class Precision/Recall/F1
Use stratified splitting
Consider class weighting or resampling
```
Class imbalance will be covered more deeply in Slot 5.

---
## 43. Common Beginner Mistakes
```
1. Looking only at Accuracy
2. Confusing Precision with Recall
3. Confusing FP with FN
4. Not defining the positive class
5. Reading confusion-matrix axes incorrectly
6. Treating F1 as universal best metric
7. Ignoring per-class support
8. Using average="binary" for multiclass data
9. Looking only at weighted averages
10. Ignoring minority-class performance
11. Passing probabilities instead of class labels
12. Selecting thresholds on the final test set
13. Assuming 0.50 is always best
14. Using zero_division=0 to hide model failure
15. Ignoring business cost
```
---
## 44. Interview Questions
Prepare these:
```
1. What is a confusion matrix?
2. What is a True Positive?
3. What is a True Negative?
4. What is a False Positive?
5. What is a False Negative?
6. What is Accuracy?
7. What is Precision?
8. What is Recall?
9. What is F1-score?
10. Precision vs Recall?
11. When should Recall be prioritized?
12. When should Precision be prioritized?
13. Why is Accuracy misleading for imbalanced data?
14. What is support in classification_report?
15. What is macro averaging?
16. What is weighted averaging?
17. What is micro averaging?
18. Why must the positive class be defined?
19. How does threshold affect Precision and Recall?
20. How would you select a metric for a medical classifier?
```
---
## 45. Interview Trap Questions
### Trap 1
**A model has 99% Accuracy. Is it excellent?**
Strong answer:
```
Not necessarily. I would inspect class distribution, confusion matrix and per-class Precision, Recall and F1. With severe class imbalance, 99% Accuracy can still mean the minority class is never detected.
```
### Trap 2
**Which is always better: Precision or Recall?**
Strong answer:
```
Neither is universally better. The choice depends on whether false positives or false negatives are more costly.
```
### Trap 3
**Is F1-score always the best classification metric?**
Strong answer:
```
No. F1 balances Precision and Recall but ignores True Negatives directly. The correct metric depends on class balance, error costs and product goals.
```
### Trap 4
**Is macro F1 better than weighted F1?**
Strong answer:
```
Not universally. Macro F1 treats every class equally, while weighted F1 reflects class frequency. I would inspect both along with per-class metrics.
```
### Trap 5
**Why can micro F1 equal Accuracy?**
Strong answer:
```
In standard single-label multiclass classification, micro averaging aggregates all class decisions globally, so micro Precision, Recall and F1 generally equal overall Accuracy.
```
---
## 47. Coding Assignment
Complete before moving to Slot 4:
```
Task 1:
Train the Logistic Regression placement model.

Task 2:
Print the confusion matrix.

Task 3:
Extract TN, FP, FN and TP.

Task 4:
Calculate manually:
Accuracy
Precision
Recall
F1

Task 5:
Verify using scikit-learn.

Task 6:
Print classification_report.

Task 7:
Build an Actual/Predicted/Probability table.

Task 8:
Label every prediction as TP, TN, FP or FN.

Task 9:
Compare thresholds:
0.30
0.50
0.70

Task 10:
Explain which threshold gives:
highest Precision
highest Recall
best F1

Task 11:
Evaluate Iris using:
macro
micro
weighted
per-class metrics

Task 12:
Write five business scenarios and select the most important metric.
```
---
## 48. Real-World Challenge
A disease classifier produces:
```
TN = 920
FP = 50
FN = 20
TP = 10
```
Answer:
```
1. Calculate Accuracy.
2. Calculate Precision.
3. Calculate Recall.
4. Calculate F1-score.
5. Is the model useful for disease screening?
6. Which error is most dangerous?
7. Which metric should be prioritized?
8. What threshold change might improve Recall?
```
Key observation:
```
Accuracy is high because most patients are healthy.

But disease Recall is:
10 / (10 + 20) = 33.3%

The model misses two-thirds of diseased patients.
```
Therefore, the model is unsafe for screening despite high Accuracy.

---
## 49. Quick Revision Sheet
```
Confusion Matrix:
Actual classes vs predicted classes.

TP:
Actual positive, predicted positive.

TN:
Actual negative, predicted negative.

FP:
Actual negative, predicted positive.

FN:
Actual positive, predicted negative.

Accuracy:
Overall percentage correct.

Precision:
Of predicted positives, how many were correct?

Recall:
Of actual positives, how many were detected?

F1:
Balance of Precision and Recall.

High Precision:
Few false positives.

High Recall:
Few false negatives.

Macro:
Equal weight to every class.

Weighted:
Weight classes by support.

Micro:
Aggregate all decisions globally.

Metric selection:
Based on class balance and business cost.
```
---