# Naive Bayes + ROC-AUC + Class Imbalance
## 1. Goal
```
1. Explain Bayes’ theorem intuitively  
2. Understand conditional probability  
3. Explain the naive independence assumption  
4. Select Gaussian, Multinomial or Bernoulli Naive Bayes  
5. Train Naive Bayes classifiers  
6. Use predict() and predict_proba()  
7. Explain the ROC curve  
8. Calculate TPR and FPR  
9. Calculate and interpret ROC-AUC  
10. Detect class imbalance  
11. Explain the majority-class accuracy trap  
12. Use class_weight="balanced"  
13. Understand oversampling and undersampling  
14. Compare multiple probability thresholds  
15. Select a threshold based on business costs
```
---
## 2. What is Naive Bayes?
Naive Bayes is a family of supervised classification algorithms based on:
```
Bayes’ theorem+A conditional-independence assumption
```
It predicts a class by asking:
```
Given the observed feature values,which class is most probable?
```
Examples:
```
Given the words in an email,
what is the probability that it is spam?

Given patient measurements,
what is the probability of disease?

Given document word counts,
which category is most probable?
```
Scikit-learn provides multiple Naive Bayes variants because each one assumes a different type of feature distribution.

---
## 3. Conditional Probability
Conditional probability asks:
```
What is the probability of event A
given that event B has occurred?
```
![[Pasted image 20260618123331.png]]
Example:
```
P(Spam | contains "free")
```
Read it as:
```
Probability that an email is spamgiven that it contains the word "free"
```
This is different from:
```
P(contains "free" | Spam)
```
which means:
```
Probability that the word "free" appears,given that the email is already known to be spam
```
The direction matters.

---
## 4. Bayes’ Theorem Intuition
Bayes’ theorem lets us update an existing belief after receiving new evidence.
![[Pasted image 20260618123421.png]]
The components are:
```
P(A)       → Prior probability
P(B|A)     → Likelihood
P(B)       → Evidence
P(A|B)     → Posterior probability
```
For spam detection:
```
A = Email is spam
B = Email contains "free"
```
Then:
```
Prior:How common are spam emails?

Likelihood:How commonly does "free" appear in spam?

Evidence:How commonly does "free" appear overall?

Posterior:After seeing "free", how likely is the email to be spam?
```
---
## 5. Bayes Example
Suppose:
```
20% of emails are spam.
70% of spam emails contain "free".
10% of non-spam emails contain "free".
```
First calculate the overall probability of `"free"`:
```
P(Free) = P(Free|Spam) × P(Spam) 
		+ P(Free|Not Spam) × P(Not Spam)
		= 0.70 × 0.20 \
		+ 0.10 × 0.80
		= 0.14 + 0.08
		= 0.22
```
Now:
```
P(Spam|Free) = (0.70 × 0.20) / 0.22
			≈ 0.636
```
Therefore:
```
An email containing "free"
has an estimated spam probability of about 63.6%.
```
This does not mean the word `"free"` guarantees spam. It updates the probability.

---
## 6. Why Is It Called “Naive”?
Suppose an email contains:
```
free
offer
money
winner
```
Naive Bayes makes the simplifying assumption that, after the class is known, each feature contributes independently.
Conceptually:
```
P(free, offer, money, winner | Spam)
≈
P(free | Spam) × P(offer | Spam) × P(money | Spam) × P(winner | Spam)
```
This is called **conditional independence**.
In reality, words are not fully independent:
```
"credit" and "card" are related"machine" and "learning" are related"limited" and "offer" are related
```
Even though the assumption is often unrealistic, Naive Bayes can still work effectively, especially for text and document classification, and it is computationally fast.

---
## 7. Naive Bayes Classification Rule
For every possible class, the model estimates:
```
Class prior × Likelihood of all observed features
```
Then it selects the class with the highest posterior score:
```
Predicted class = class with maximum posterior probability
```
For spam:
```
Score for Spam vs Score for Not Spam
```
For multiclass news classification:
```
Score for Sports
Score for Technology
Score for Politics
Score for Business
```
The class with the highest score is predicted.

---
## 8. Main Naive Bayes Variants

|Variant|Expected features|Common use|
|---|---|---|
|`GaussianNB`|Continuous numerical data|Medical measurements, sensor values|
|`MultinomialNB`|Non-negative counts/frequencies|Word-count text classification|
|`BernoulliNB`|Binary 0/1 features|Word present/absent|
|`CategoricalNB`|Encoded categorical features|Discrete category data|
Today’s main focus:
```
GaussianNB 
MultinomialNB 
BernoulliNB
```
---
## 9. Gaussian Naive Bayes
`GaussianNB` assumes that each numerical feature follows an approximately Gaussian distribution within each class.
Examples:
```
Age
Blood pressure
Tumour radius
Exam score
Petal length
Sensor measurement
```
For every class and feature, it learns:
```
Mean
Variance
```
Then it evaluates how likely a new value is under each class distribution. Scikit-learn’s `GaussianNB` stores the class-specific means in `theta_` and variances in `var_`.

---
## 10. GaussianNB Example: Cancer Classification
We will define:
```
1 = Malignant
0 = Benign
```

```Python
import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

cancer = load_breast_cancer(as_frame=True)

X = cancer.data

# Original dataset:
# 0 = malignant
# 1 = benign
#
# Remap so the important disease class becomes positive:
# 1 = malignant
# 0 = benign
y = (cancer.target == 0).astype(int)

print("Feature Shape:", X.shape)

print("\nTarget Distribution:")
print(y.value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(
    classification_report(
        y_test,
        y_pred,
        target_names=[
            "Benign",
            "Malignant"
        ],
        zero_division=0
    )
)
```
![[Pasted image 20260618125017.png]]
Gaussian Naive Bayes does not require the features to be scaled merely to make numerical ranges comparable, because it estimates a mean and variance for every class-feature combination. Scaling may still be useful when the same preprocessing pipeline serves multiple algorithms.

---
## 11. GaussianNB Probabilities
![[Pasted image 20260618125159.png]]
![[Pasted image 20260618125219.png]]
Always check:
```
print(model.classes_)
```
Do not blindly assume that column 1 always represents your desired class without confirming the class order.

---
## 12. Important `predict_proba()` Warning
Naive Bayes can be a useful classifier, but its independence assumptions often make the probability outputs too extreme or poorly calibrated.
For example:
```
0.9999
```
does not automatically mean the real-world event has a reliable 99.99% probability.
Scikit-learn explicitly warns that Naive Bayes may classify well while providing poor probability estimates, so `predict_proba()` should be interpreted cautiously.
Use probabilities for:
```
Ranking
Threshold experiments
Model comparison
Initial decision support
```
But for high-stakes production use, check probability calibration separately.

---
## 13. Multinomial Naive Bayes
`MultinomialNB` is designed primarily for non-negative discrete feature values, such as:
```
Word occurrence counts
Token frequencies
Number of clicks
Number of events
Term-frequency features
```
It is especially common in text classification because a document can be represented as word-count features. Scikit-learn describes it as suitable for discrete features such as word counts; TF-IDF values may also work in practice.
Example representation:

| Document | free | offer | meeting | project |
| -------- | ---- | ----- | ------- | ------- |
| Email 1  | 2    | 1     | 0       | 0       |
| Email 2  | 0    | 0     | 2       | 1       |

---
## 14. MultinomialNB Spam Example
```Python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

messages = [
    "win free money now",
    "limited offer claim prize",
    "congratulations you are a winner",
    "free gift click this link",
    "urgent claim your reward",
    "exclusive money making offer",
    "project meeting at ten",
    "please review the report",
    "team standup tomorrow morning",
    "submit the assignment today",
    "your interview is scheduled",
    "let us discuss the project"
]

# 1 = spam
# 0 = not spam
labels = [
    1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0
]

multinomial_model = Pipeline(steps=[
    (
        "vectorizer",
        CountVectorizer()
    ),
    (
        "classifier",
        MultinomialNB(alpha=1.0)
    )
])

multinomial_model.fit(
    messages,
    labels
)

new_messages = [
    "claim your free prize",
    "project meeting tomorrow"
]

predictions = multinomial_model.predict(
    new_messages
)

probabilities = multinomial_model.predict_proba(
    new_messages
)

for message, prediction, probability in zip(
    new_messages,
    predictions,
    probabilities
):
    label = (
        "Spam"
        if prediction == 1
        else "Not Spam"
    )

    print("\nMessage:", message)
    print("Prediction:", label)
    print(
        "Spam probability:",
        probability[1]
    )
```
![[Pasted image 20260618130100.png]]

---
## 15. What Does `alpha` Do?
Suppose a word never appeared in spam during training.
Without smoothing:
```
P(word | Spam) = 0
```
Because Naive Bayes multiplies probabilities, one zero can make the entire class score zero.
`alpha` adds smoothing:
```
MultinomialNB(alpha=1.0)
```
This prevents unseen feature-class combinations from receiving an exact zero probability. Scikit-learn exposes `alpha` as the additive Laplace/Lidstone smoothing parameter.
General intuition:
```
Larger alpha→ stronger smoothing
Smaller alpha→ feature counts affect probabilities more directly
```

---
## 16. Bernoulli Naive Bayes
`BernoulliNB` expects binary features:
```
0 = feature absent
1 = feature present
```
For text:
```
Does the document contain "free"?
Does the document contain "offer"?
Does the document contain "winner"?
```
It does not care how many times the word appears—only whether it appears.
Scikit-learn distinguishes BernoulliNB from MultinomialNB by noting that MultinomialNB uses occurrence counts, while BernoulliNB is designed for binary/Boolean features.

---
## 17. BernoulliNB Example
```Python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.pipeline import Pipeline

bernoulli_model = Pipeline(steps=[
    (
        "vectorizer",
        CountVectorizer(binary=True)
    ),
    (
        "classifier",
        BernoulliNB(alpha=1.0)
    )
])

bernoulli_model.fit(
    messages,
    labels
)

new_messages = [
    "free free free prize",
    "project review meeting"
]

predictions = bernoulli_model.predict(
    new_messages
)

probabilities = bernoulli_model.predict_proba(
    new_messages
)

for message, prediction, probability in zip(
    new_messages,
    predictions,
    probabilities
):
    print("\nMessage:", message)

    print(
        "Prediction:",
        "Spam" if prediction == 1
        else "Not Spam"
    )

    print(
        "Spam probability:",
        probability[1]
    )
```
![[Pasted image 20260618130353.png]]
Because `binary=True`, this:
```
free
```
and this:
```
free free free
```
both become:
```
free_present = 1
```
---
## 18. Which Naive Bayes Variant Should You Use?

| Data type                        | Recommended starting model |
| -------------------------------- | -------------------------- |
| Continuous measurements          | `GaussianNB`               |
| Word/token counts                | `MultinomialNB`            |
| Binary presence/absence features | `BernoulliNB`              |
| Encoded independent categories   | `CategoricalNB`            |
Examples:
```
Tumour measurements→ GaussianNBEmail word counts→ MultinomialNBWhether each keyword appears→ BernoulliNB
```
Choosing the wrong distribution assumption can reduce performance significantly.

---
## 19. Advantages of Naive Bayes
```
Very fast training
Fast prediction
Works with relatively small datasets
Effective baseline for text classification
Handles high-dimensional sparse features
Simple probabilistic interpretation
Supports multiclass classification naturally
```
Naive Bayes can be especially efficient because class-conditional feature distributions can be estimated separately.

---
## 20. Limitations of Naive Bayes
```
Independence assumption is often unrealistic
Correlated features may distort evidence
Probability estimates may be poorly calibrated
Wrong feature-distribution choice hurts results
Rare/unseen events require smoothing
Can be outperformed by stronger models on complex interactions
```
For example:
```
Tumour radius
Tumour area
Tumour perimeter
```
are strongly related. Treating them as conditionally independent may cause the same evidence to be counted multiple times.

---
## 21. ROC Curve
A classification model often generates a probability or decision score.
The predicted class depends on a threshold:
```
Probability >= threshold → Positive
Probability < threshold  → Negative
```
The ROC curve evaluates the classifier across many possible thresholds.
It plots:
```
X-axis → False Positive Rate
Y-axis → True Positive Rate
```
Scikit-learn’s `roc_curve` calculates FPR and TPR values across decreasing decision thresholds, while `roc_auc_score` summarizes the curve’s area.

---
# 22. True Positive Rate
True Positive Rate is the same as Recall:
![[Pasted image 20260618135235.png|168]]
It answers:
```
Of all actual positive cases,how many did the model detect?
```
Example:
```
TP = 80
FN = 20
TPR = 80 / 100
TPR = 0.80
```
Meaning:
```
The model detected 80% of actual positive cases.
```
---
## 23. False Positive Rate
![[Pasted image 20260618135331.png|161]]
It answers:
```
Of all actual negative cases,
how many were incorrectly classified as positive?
```
Example:
```
FP = 30
TN = 270
FPR = 30 / 300
FPR = 0.10
```
Meaning:
```
10% of actual negative cases generated false alarms.
```
---
## 24. Threshold Effect on ROC
Very high threshold:
```
Few positive predictions
Low TPR
Low FPR
```
Very low threshold:
```
Many positive predictionsHigh TPRHigh FPR
```
A useful model tries to achieve:
```
High TPR
Low FPR
```

This moves the curve toward the upper-left region.

---
## 25. ROC-AUC
ROC-AUC means:
```
Area Under the ROC Curve
```
Common interpretation:

| AUC     | Interpretation                    |
| ------- | --------------------------------- |
| `1.0`   | Perfect ranking on evaluated data |
| `0.9`   | Strong ranking ability            |
| `0.8`   | Useful ranking ability            |
| `0.7`   | Moderate ranking ability          |
| `0.5`   | Similar to random ranking         |
| `< 0.5` | Ranking is largely reversed       |
A deeper interpretation:
```
AUC estimates how often a randomly chosen positivereceives a higher score than a randomly chosen negative.
```
AUC is not accuracy, and it does not determine the production threshold automatically.

---
## 26. ROC-AUC Code
Continue from the GaussianNB cancer example:
![[Pasted image 20260618140137.png]]
![[Pasted image 20260618140242.png]]
Use probability or decision scores—not just hard class predictions—to construct a meaningful ROC curve.

---
## 27. Inspect ROC Thresholds
![[Pasted image 20260618140455.png]]
Every row represents a different classification threshold.
Example:

| Threshold | TPR  | FPR  |
| --------- | ---- | ---- |
| 0.90      | 0.55 | 0.02 |
| 0.70      | 0.74 | 0.05 |
| 0.50      | 0.84 | 0.10 |
| 0.30      | 0.93 | 0.20 |
Lowering the threshold usually:
```
Increases TPR/Recall
Increases FPR
```
---
## 28. ROC-AUC Limitations
A high AUC does not guarantee:
```
Good probability calibration
High Precision
Good minority-class performance at your chosen threshold
Fair performance across subgroups
Low business cost
```
In heavily imbalanced problems, Precision–Recall curves may provide additional insight because ROC performance can look strong even when many positive predictions are false alarms.
Use ROC-AUC as one evaluation view, not the only metric.

---
## 29. What Is Class Imbalance?
Class imbalance means one class has substantially more examples than another.
Example:
```
Genuine transactions = 9,900
Fraud transactions   = 100
```
Distribution:
```
99% genuine
1% fraud
```
The fraud class is the minority class.
Common imbalanced problems:
```
Fraud detection
Disease detection
Manufacturing defects
Cyberattacks
Customer churn
Loan default
Rare-event prediction
```
---
## 30. Majority-Class Accuracy Trap
Suppose:
```
99% of transactions are genuine
1% are fraudulent
```
A model always predicts:
```
Genuine
```
Its accuracy is:
```
99%
```
But:
```
Fraud Recall = 0%
Fraud detected = 0
```
Therefore, high accuracy does not imply that the model solves the actual business problem.
For imbalanced data, inspect:
```
Confusion matrix
Minority-class Precision
Minority-class Recall
Minority-class F1ROC-AUC
Precision–Recall performance
Business cost
```
---
## 31. Create an Imbalanced Dataset
![[Pasted image 20260618160216.png]]
![[Pasted image 20260618160241.png]]

---
## 32. Majority-Class Baseline
![[Pasted image 20260618160710.png]]
Expected pattern:
```
Accuracy → very high
Recall   → 0
F1       → 0
```
This proves why a baseline and per-class metrics are essential.

---
## 33. Logistic Regression Without Class Weights
![[Pasted image 20260618161007.png]]
The model may become biased toward the majority class because predicting it frequently reduces overall error.

---
## 34. `class_weight="balanced"`
![[Pasted image 20260618161202.png]]
In Logistic Regression, `"balanced"` automatically assigns weights inversely proportional to observed class frequencies.
Likely effect:
```
Minority Recall increases
False Negatives decrease
But:
False Positives may increase
Precision may decrease
Overall Accuracy may decrease
```

That is not automatically bad. The correct trade-off depends on business cost.

---

# 35. Compare Regular and Balanced Models

```Python
from sklearn.metrics import roc_auc_score

models = {
    "Regular Logistic Regression": regular_model,
    "Balanced Logistic Regression": balanced_model
}

comparison_rows = []

for name, fitted_model in models.items():
    predictions = fitted_model.predict(
        X_test_imb
    )

    scores = fitted_model.predict_proba(
        X_test_imb
    )[:, 1]

    comparison_rows.append({
        "Model": name,
        "Accuracy": accuracy_score(
            y_test_imb,
            predictions
        ),
        "Precision": precision_score(
            y_test_imb,
            predictions,
            zero_division=0
        ),
        "Recall": recall_score(
            y_test_imb,
            predictions,
            zero_division=0
        ),
        "F1": f1_score(
            y_test_imb,
            predictions,
            zero_division=0
        ),
        "ROC_AUC": roc_auc_score(
            y_test_imb,
            scores
        )
    })

comparison_df = pd.DataFrame(
    comparison_rows
)

print(comparison_df)
```
![[Pasted image 20260618164503.png]]
Do not select the winner from Accuracy alone.
Ask:
```
Which model finds more minority cases?
How many false alarms does it produce?
What is the cost of a missed positive?
What is the cost of an incorrect alert?
```
---
## 36. Oversampling
Oversampling increases the number of minority-class training examples.
### Random oversampling
Randomly duplicates minority-class examples.
Example:
```
Before:
950 majority
50 minority
After:
950 majority
950 minority
```
Advantages:
```
SimpleKeeps all majority examples
May improve minority learning
```
Risks:
```
Duplicates existing observations
Can increase overfitting
Increases training size
```
`RandomOverSampler` performs random minority sampling with replacement.

---
## 37. Synthetic Oversampling Awareness
Methods such as SMOTE generate synthetic minority examples between nearby minority observations.
Conceptually:
```
Minority sample AMinority sample B
↓
Create a synthetic point between them
```
Possible benefits:
```
Adds variation rather than exact duplicates
Can improve decision boundaries
```
Possible risks:
```
Can create unrealistic samples
Can overlap classesCan amplify noise
Requires careful preprocessing
```
Do not use SMOTE blindly for categorical, time-series or highly structured data.

---
## 38. Undersampling
Undersampling reduces majority-class training examples.
Example:
```
Before:
950 majority
50 minority
After:
50 majority
50 minority
```
Advantages:
```
Faster training
Simpler balanced dataset
Useful when majority data is extremely large
```
Risks:
```
Important majority information may be removed
Model may become unstableDataset becomes smaller
```
Random under-sampling removes selected majority observations; controlled methods can reduce majority classes to a chosen size.

---
## 39. Critical Resampling Rule
Never oversample or undersample the full dataset before train-test splitting.
Wrong:
```
Resample full dataset
↓
Train-test split
```
Why dangerous?
```
Duplicate or synthetic information can appearacross training and test sets.
Evaluation becomes overly optimistic.
```
Correct:
```
Train-test split
↓
Resample training data only
↓
Fit model
↓
Evaluate on untouched test data
```
The test set must represent the original real-world distribution.

---
## 40. Random Oversampling Code
Install when required:
```
pip install imbalanced-learn
```
Use the imbalanced-learn pipeline:
![[Pasted image 20260618165927.png]]
Use `imblearn.pipeline.Pipeline`, not the standard scikit-learn pipeline, when samplers are included.

---
## 41. Random Undersampling Code
![[Pasted image 20260618171247.png]]```

---
## 42. Threshold Selection
The default binary threshold is commonly:
```
0.50
```
But different thresholds produce different business outcomes.
Suppose the positive probability is:
```
0.42
```
At threshold `0.50`:
```
Prediction = Negative
```
At threshold `0.30`:
```
Prediction = Positive
```
Threshold selection controls the Precision–Recall trade-off.

---
## 43. Compare Thresholds
![[Pasted image 20260618171808.png]]
![[Pasted image 20260618171826.png]]

---
## 44. Threshold Trade-Off
Lower threshold:
```
More positive predictions
Recall usually increases
False Negatives usually decrease
False Positives usually increase
Precision may decrease
```
Higher threshold:
```
Fewer positive predictions
Precision may increase
False Positives usually decrease
False Negatives usually increase
Recall usually decreases
```
Examples:
```
Disease screening→ lower threshold may be appropriate
Automatically blocking bank transactions
→ higher threshold may reduce customer disruption
```
---
## 45. Cost-Based Threshold Selection
Suppose:
```
Cost of False Negative = ₹10,000
Cost of False Positive = ₹500
```
For each threshold:
```
Total Cost=FN × 10,000+FP × 500
```
Code:
![[Pasted image 20260618172022.png]]
The threshold with the highest Accuracy may not have the lowest business cost.

---
## 46. Important Threshold Rule
Do not select a threshold using the final test set repeatedly.
Correct workflow:
```
Training data
→ Fit model
Validation data or cross-validation predictions
→ Select threshold
Untouched test data
→ Final unbiased evaluation
```
Otherwise, threshold selection begins to overfit the test set.

---
## 47. Complete Model-Comparison Function
```Python
from sklearn.metrics import classification_report
def evaluate_classifier(
    name,
    fitted_model,
    X_test,
    y_test,
    threshold=0.50
):
    probabilities = fitted_model.predict_proba(
        X_test
    )[:, 1]
    predictions = (
        probabilities >= threshold
    ).astype(int)
    tn, fp, fn, tp = confusion_matrix(
        y_test,
        predictions,
        labels=[0, 1]
    ).ravel()
    metrics = {
        "Model": name,
        "Threshold": threshold,
        "Accuracy": accuracy_score(
            y_test,
            predictions
        ),
        "Precision": precision_score(
            y_test,
            predictions,
            zero_division=0
        ),
        "Recall": recall_score(
            y_test,
            predictions,
            zero_division=0
        ),
        "F1": f1_score(
            y_test,
            predictions,
            zero_division=0
        ),
        "ROC_AUC": roc_auc_score(
            y_test,
            probabilities
        ),
        "TN": tn,
        "FP": fp,
        "FN": fn,
        "TP": tp
    }
   print("\n", name)
    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )
    return metrics
```
---
## 48. Common Beginner Mistakes
```
1. Confusing P(A|B) with P(B|A)
2. Thinking the naive independence assumption is always true
3. Using GaussianNB for word-count data
4. Using MultinomialNB with negative feature values
5. Using BernoulliNB when feature frequency matters
6. Treating Naive Bayes probabilities as perfectly calibrated
7. Assuming predict_proba() columns have a fixed class order
8. Calculating ROC using only hard class labels
9. Treating ROC-AUC as Accuracy
10. Looking only at Accuracy on imbalanced data
11. Applying resampling before train-test split
12. Resampling the test dataset
13. Assuming class_weight always improves every metric
14. Selecting threshold on the final test set
15. Assuming 0.50 is universally optimal
16. Using oversampling without checking overfitting
17. Undersampling away valuable majority information
18. Ignoring business cost
```

---
## 49. Debugging Section
### Error 1: Negative Values with MultinomialNB
Broken workflow:
```
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import MultinomialNB
# StandardScaler may create negative values
X_scaled = StandardScaler().fit_transform(X)
model = MultinomialNB()
model.fit(X_scaled, y)
```
Possible error:
```
ValueError:Negative values in data passed to MultinomialNB
```
Why:
```
MultinomialNB expects non-negative count/frequency features.
```
Fix:
```
Use CountVectorizer or non-negative frequency features.Do not standardize counts into negative values.
```
---
### Error 2: Incorrect `predict_proba()` Column
Wrong:
```
positive_probability = (    model.predict_proba(X_test)[:, 1])
```
without checking class order.
Better:
```
print(model.classes_)positive_index = list(    model.classes_).index(1)positive_probability = (    model.predict_proba(X_test)[        :,        positive_index    ])
```
---
### Error 3: ROC Curve with Hard Predictions
Weak approach:
```
roc_curve(    y_test,    y_pred)
```
This uses only two score values and produces an uninformative curve.
Better:
```
positive_scores = model.predict_proba(    X_test)[:, 1]roc_curve(    y_test,    positive_scores)
```
---
### Error 4: Resampling Before Splitting
Wrong:
```
X_resampled, y_resampled = sampler.fit_resample(    X,    y)X_train, X_test, y_train, y_test = (    train_test_split(        X_resampled,        y_resampled    ))
```
Problem:
```
Information from duplicated or synthetic examplescan leak into the test set.
```
Fix:
```
Split first.Resample training data only.
```
---
### Error 5: Standard Pipeline with a Sampler
Broken:
```
from sklearn.pipeline import PipelinePipeline(steps=[    ("sampler", RandomOverSampler()),    ("model", LogisticRegression())])
```
Problem:
```
A sampler uses fit_resample(),not the usual transform interface.
```
Fix:
```
from imblearn.pipeline import Pipeline
```
---
### Error 6: Assuming Every Model Supports `class_weight`
Broken:
```
GaussianNB(    class_weight="balanced")
```
Possible error:
```
TypeError:Unexpected keyword argument 'class_weight'
```
`class_weight` support is estimator-specific. `LogisticRegression` and `RandomForestClassifier` support it, but GaussianNB does not expose the same constructor parameter. GaussianNB can accept `sample_weight` during fitting.

---
## 50. Production Failure Scenarios
### Scenario 1: Probability overconfidence
The model returns:
```
Fraud probability = 99.9%
```
But actual outcomes at that score are fraudulent only 75% of the time.
Problem:
```
Poor probability calibration
```
Senior response:
```
Create calibration plotsEvaluate Brier scoreUse probability calibration when necessaryDo not present raw probability as certainty
```
---
### Scenario 2: Class distribution changes
Training:
```
Fraud = 1%
```
Production after an attack:
```
Fraud = 8%
```
Possible effects:
```
More alertsChanged PrecisionChanged business costsProbability reliability decreases
```
Senior response:
```
Monitor class prevalenceMonitor score distributionMonitor Precision and Recall when labels arriveReview thresholdRetrain when necessary
```
---
### Scenario 3: Oversampling amplifies noisy labels
A mislabeled minority observation gets duplicated many times.
Result:
```
Model strongly learns incorrect information
```
Senior response:
```
Audit minority-class labelsInspect duplicates and outliersCompare class weighting with resamplingUse cross-validation
```
---
### Scenario 4: Threshold chosen only for Accuracy
Threshold `0.85` achieves:
```
Accuracy = 97%Minority Recall = 10%
```
The model misses 90% of the important class.
Senior response:
```
Select threshold from business cost,Recall requirements and Precision constraints.
```
---
## 51. Interview Questions
Prepare answers for:
```
1. What is conditional probability?
2. Explain Bayes’ theorem intuitively.
3. What is prior probability?
4. What is posterior probability?
5. Why is Naive Bayes called naive?
6. What is Gaussian Naive Bayes?
7. When should MultinomialNB be used?
8. When should BernoulliNB be used?
9. What does alpha do?
10. Why can Naive Bayes probability estimates be unreliable?
11. What is a ROC curve?
12. What are TPR and FPR?
13. What is ROC-AUC?
14. Is ROC-AUC the same as Accuracy?
15. What is class imbalance?
16. Why can Accuracy be misleading?
17. What does class_weight="balanced" do?
18. What is oversampling?
19. What is undersampling?
20. Why must resampling happen only on training data?
21. How does threshold affect Precision and Recall?
22. How would you select a production threshold?
```

---
## 52. Interview Trap Questions
### Trap 1
**Are Naive Bayes features really independent?**
Strong answer:
```
Usually not. Naive Bayes assumes conditional independence to simplify probability estimation. It can still perform well even when the assumption is imperfect.
```
### Trap 2
**Can MultinomialNB use standardized negative values?**
Strong answer:
```
No. It expects non-negative count or frequency-like features. Standardization can create negative values and violate that assumption.
```
### Trap 3
**Does higher ROC-AUC mean the default threshold is good?**
Strong answer:
```
No. ROC-AUC evaluates ranking across thresholds. Production threshold quality must be assessed separately using Precision, Recall, business cost and constraints.
```
### Trap 4
**Does class weighting balance the number of samples?**
Strong answer:
```
No. It changes the loss contribution assigned to each class. The original number of observations remains unchanged.
```
### Trap 5
**Should the test set be oversampled?**
Strong answer:
```
No. The test set should remain untouched and preserve the real-world class distribution.
```
---
## 54. Coding Assignment
Complete before Slot 6:
```
Task 1:
Train GaussianNB on the breast-cancer dataset.

Task 2:
Remap:
1 = Malignant
0 = Benign

Task 3:
Print:
Confusion Matrix
Precision
Recall
F1
Classification Report

Task 4:
Print predict_proba() results and model.classes_.

Task 5:
Calculate and plot ROC-AUC.

Task 6:
Create a ROC threshold table.

Task 7:
Build a MultinomialNB spam classifier.

Task 8:
Build a BernoulliNB spam classifier.

Task 9:
Explain the difference between count and binary features.

Task 10:
Create a 95/5 imbalanced synthetic dataset.

Task 11:
Compare:
DummyClassifier
Regular Logistic Regression
Balanced Logistic Regression

Task 12:
Compare thresholds from 0.20 to 0.70.

Task 13:
Calculate FP/FN business costs.

Task 14:
Try RandomOverSampler and RandomUnderSampler.

Task 15:
Explain why the test data must remain untouched.
```
---
## 55. Real-World Challenge
A fraud model gives these threshold results:

|Threshold|Precision|Recall|FP|FN|
|---|---|---|---|---|
|0.20|0.25|0.95|300|5|
|0.40|0.48|0.82|120|18|
|0.60|0.72|0.61|45|39|
|0.80|0.91|0.28|8|72|
Business costs:
```
One False Positive = ₹500
One False Negative = ₹10,000
```
Answer:
```
1. Which threshold has the highest Recall?
2. Which threshold has the highest Precision?
3. Calculate business cost for every threshold.
4. Which threshold gives the lowest cost?
5. Why might Accuracy choose a different threshold?
6. Should the threshold be selected using final test data?
```
Key thinking:
```
False Negatives are far more expensive.
A lower threshold may create more alerts,but can still reduce total business loss.
```
---
## 56. Quick Revision Sheet

```
Bayes’ theorem:
Updates probability using evidence.

Prior:
Probability before new evidence.

Likelihood:
Probability of evidence given a class.

Posterior:
Updated class probability.

Naive assumption:
Features are conditionally independent given the class.

GaussianNB:
Continuous numerical data.

MultinomialNB:
Non-negative counts/frequencies.

BernoulliNB:
Binary feature presence/absence.

ROC:
TPR versus FPR across thresholds.

TPR:
TP / (TP + FN)

FPR:
FP / (FP + TN)

ROC-AUC:
Threshold-independent ranking measure.

Class imbalance:
One class is much rarer than another.

class_weight="balanced":
Weights classes inversely to frequency.

Oversampling:
Increase minority training observations.

Undersampling:
Reduce majority training observations.

Threshold selection:
Choose using validation data and business cost.
```