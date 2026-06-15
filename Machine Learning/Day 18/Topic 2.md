# K-Nearest Neighbors Classification
## 1. Goal
```
1. Explain K-Nearest Neighbors
2. Understand instance-based learning
3. Calculate Euclidean distance
4. Explain the meaning of K
5. Understand majority voting
6. Explain why feature scaling is essential
7. Identify overfitting and underfitting in KNN
8. Train KNeighborsClassifier
9. Select a suitable K value
10. Use KNN for multiclass classification
11. Generate class probabilities
12. Debug common KNN errors
```
---
## 2. Why KNN Matters
KNN is a supervised learning algorithm that can solve:
```
Binary classification
Multiclass classification
Regression
```
Today, we focus on classification.
Typical applications include:
```
Flower classification
Handwritten-digit recognition
Basic recommendation systems
Customer-category prediction
Medical-pattern classification
Similarity-based document classification
```
Scikit-learn provides `KNeighborsClassifier`, which predicts classes using the votes of nearby training samples. Its major parameters include the number of neighbors, voting weights, distance metric and neighbor-search algorithm.

---
## 3. Beginner Intuition
Suppose a new student has:
```
CGPA = 8.0
DSA score = 75
```
We do not immediately calculate a regression equation.
Instead, KNN asks:
```
Which existing students are most similar to this student?
```
Assume the three nearest students are:

| Neighbor  | CGPA | DSA score | Placement  |
| --------- | ---- | --------- | ---------- |
| Student A | 8.1  | 78        | Placed     |
| Student B | 7.9  | 72        | Placed     |
| Student C | 8.2  | 74        | Not Placed |
Votes:
```
Placed: 2
Not Placed: 1
```
Prediction:
```
Placed
```
Because the majority of the three nearest neighbors are placed.

---
## 4. What Does “K” Mean?
`K` is the number of neighboring training examples used for prediction.
Examples:
```
K = 1 → use the closest neighbor
K = 3 → use the closest 3 neighbors
K = 5 → use the closest 5 neighbors
K = 11 → use the closest 11 neighbors
```
Scikit-learn exposes this through:
```
KNeighborsClassifier(n_neighbors=5)
```
The classifier’s `n_neighbors` parameter controls how many neighbors participate in each prediction.

---
## 5. How KNN Works
For each new sample:
```
Step 1: Receive the new feature values
Step 2: Calculate distance from every relevant training sample
Step 3: Sort training samples by distance
Step 4: Select the nearest K samples
Step 5: Count their class votes
Step 6: Return the majority class
```
Visual:
```
Training examples
	Class A: ● ● ● ●
	Class B: ▲ ▲ ▲ ▲

New sample: ★

Find the closest points to ★
↓
Take the nearest K points
↓
Use majority vote
```
---
## 6. KNN Is Instance-Based Learning
Algorithms such as Logistic Regression learn coefficients during training.
KNN does not learn an equation like:
```
z = w₁x₁ + w₂x₂ + b
```
It mainly retains the training examples and performs neighbor search when a prediction is requested.
This is why KNN is often called:
```
Instance-based learning
Memory-based learning
Lazy learning
```
Conceptually:
```
Logistic Regression:
Training performs more mathematical optimization
Prediction uses the learned equation

KNN:
Training mainly stores the examples
Prediction performs distance calculations and voting
```
---
## 7. Euclidean Distance
The most familiar KNN distance is Euclidean distance.
For two points with features:
```
Point A = (x₁, x₂, ..., xₙ)
Point B = (y₁, y₂, ..., yₙ)
```
Distance:
![[Pasted image 20260613150623.png]]
For two features:
```
distance = √[(x₁ − y₁)² + (x₂ − y₂)²]
```
With scikit-learn’s standard KNN settings, the Minkowski metric with `p=2` corresponds to Euclidean distance.

---
## 8. Manual Distance Example
New student:
```
CGPA = 8
DSA score = 70
```
Existing student:
```
CGPA = 7
DSA score = 74
```
Distance:
```
= √[(8 − 7)² + (70 − 74)²]
= √[1² + (−4)²]
= √[1 + 16]
= √17≈ 4.12
```
Smaller distance means:
```
The two students are more similar according to these features.
```
---
## 9. Why Feature Scaling Is Essential
Suppose the features are:
```
CGPA: 0–10
Annual income: 0–2,000,000
```
Consider two records:
```
CGPA difference = 2
Income difference = 500,000
```
Without scaling, the income difference dominates the distance calculation.
KNN may almost ignore CGPA—not because income is necessarily more important, but because its numerical values are much larger.
Correct workflow:
```
Train-test split
↓
Fit StandardScaler on X_train↓Scale X_train
↓
Scale X_test with the same scaler
↓
Train and evaluate KNN
```
`StandardScaler` standardizes each feature using training-set statistics by subtracting its mean and scaling to unit variance.

---
## 10. Standardization Formula
For one feature:
```
standardized value =(original value − training mean) / training standard deviation
```
After standardization, features become more comparable for distance calculation.
Example:
Before:

|Feature|Value|
|---|---|
|CGPA|8.2|
|Income|800,000|
After scaling:

| Feature | Scaled value |
| ------- | ------------ |
| CGPA    | 0.71         |
| Income  | 0.54         |
KNN can now calculate distance more fairly.

---
## 11. What Happens When K Is Too Small?
Suppose:
```
K = 1
```
The new sample receives the class of its single nearest neighbor.
Advantages:
```
Can capture very local patterns
Creates flexible decision boundaries
```
Risks:
```
Very sensitive to noise
One incorrect training label can change prediction
High overfitting risk
Unstable predictions
```
Pattern:
```
Very low training errorHigher test error
```
Therefore:
```
Very small K may overfit.
```
---
## 12. What Happens When K Is Too Large?
Suppose your training data contains 100 samples and you use:
```
K = 95
```
The prediction is influenced by almost the entire dataset.
Advantages:
```
Less sensitive to individual noisy samples
Creates smoother boundaries
```
Risks:
```
Local patterns disappear
Majority class may dominate
Model becomes too simple
Underfitting risk
```
Pattern:
```
High training error
High test error
```
Therefore:
```
Very large K may underfit.
```
---
## 13. Choosing a Good K
There is no single K value that is best for every dataset.
A common practical method:
```
1. Try several K values
2. Evaluate each on validation data
3. Select the K with the strongest validation performance
4. Evaluate the final choice once on untouched test data
```
For a learning exercise, we will try:
```
K = 1, 3, 5, 7, 9, 11, 13, 15
```
For binary classification, odd K values are often convenient because they reduce simple voting ties, although ties can still arise in weighted or multiclass settings.

---
## 14. Uniform vs Distance-Weighted Voting
### Uniform voting
Every neighbor gets one equal vote.
```
KNeighborsClassifier(
    n_neighbors=5,
    weights="uniform"
)
```
Example:
```
Neighbor 1: Placed
Neighbor 2: Placed
Neighbor 3: Not Placed
Neighbor 4: Not Placed
Neighbor 5: Placed
Prediction: Placed
```
### Distance-weighted voting
Closer neighbors receive greater influence.
```
KNeighborsClassifier(    
	n_neighbors=5,    
	weights="distance"
)
```
Scikit-learn supports both uniform and distance-based weighting. With distance weighting, closer neighbors have greater influence than farther neighbors.

---
## 15. Binary and Multiclass KNN
### Binary KNN
Possible classes:
```
Placed / Not Placed
Fraud / Not Fraud
Spam / Not Spam
```
### Multiclass KNN
Possible classes:
```
Setosa
Versicolor
Virginica
```
KNN naturally supports multiclass classification because it can count votes across any number of classes.

---
## 16. Dataset for This Slot: Iris
We will use the Iris flower dataset.
It contains:
```
150 total samples
4 numerical features
3 flower classes
50 samples per class
```
Features:
```
Sepal length
Sepal width
Petal length
Petal width
```
Classes:
```
Setosa
Versicolor
Virginica
```
Scikit-learn documents Iris as a classic multiclass classification dataset with 150 samples, four positive real-valued features and three classes.

---
## 17. Load and Inspect Iris
![[Pasted image 20260613151922.png]]
![[Pasted image 20260613152111.png]]
![[Pasted image 20260613152305.png]]
![[Pasted image 20260613152350.png]]
![[Pasted image 20260613152505.png]]
Expected class mapping:
```
0 → Setosa
1 → Versicolor
2 → Virginica
```
---
## 18. Train-Test Split
![[Pasted image 20260613153613.png]]
Why `stratify=y`?
```
It helps preserve class proportions in both subsets.
```
---
## 19. Build a Scaling + KNN Pipeline
![[Pasted image 20260613154220.png]]
The pipeline ensures:
```
Scaler fits only on X_train
X_train is scaled
KNN uses scaled training features
X_test receives the same scaling
```
---
## 20. Train the Classifier
![[Pasted image 20260613154323.png]]
For KNN, `fit()` mainly prepares and stores the training representation needed for neighbor search.
It does not learn a coefficient equation like Logistic Regression.

---
## 21. Predict Classes
![[Pasted image 20260613154650.png]]
Convert numeric classes to names:
![[Pasted image 20260613155001.png]]

---
## 22. Basic Accuracy
![[Pasted image 20260613155118.png]]
Accuracy is useful here as an introductory check because Iris is balanced, but you will study confusion matrix, precision, recall and F1-score properly in Slot 3.

---
## 23. Predict Class Probabilities
![[Pasted image 20260613155304.png]]
Example:

| setosa | versicolor | virginica |
| ------ | ---------- | --------- |
| 0.00   | 0.80       | 0.20      |
Prediction:
```
Versicolor
```
Because it received the greatest voting proportion.
For uniform KNN with `K=5`:
```
0.80 probability-like output≈ 4 of the 5 neighbors voted Versicolor
```
These outputs reflect neighbor voting; they should not automatically be treated as perfectly calibrated real-world probabilities.

---
## 24. Complete KNN Program

```Python
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

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

knn_pipeline = Pipeline(steps=[
    ("scaler", StandardScaler()),
    (
        "classifier",
        KNeighborsClassifier(
            n_neighbors=5,
            weights="uniform"
        )
    )
])

knn_pipeline.fit(X_train, y_train)

y_pred = knn_pipeline.predict(X_test)
y_probabilities = knn_pipeline.predict_proba(X_test)

accuracy = accuracy_score(y_test, y_pred)

results = X_test.copy()
results["Actual"] = iris.target_names[y_test.to_numpy()]
results["Predicted"] = iris.target_names[y_pred]

probability_df = pd.DataFrame(
    y_probabilities,
    columns=[
        f"Probability_{name}"
        for name in iris.target_names
    ],
    index=X_test.index
)

results = pd.concat([results, probability_df], axis=1)

print("Results:")
print(results)

print("\nAccuracy:")
print(accuracy)
```
---
## 25. Find the Best K
For correct model development, hyperparameter selection should ideally use cross-validation or a separate validation set rather than repeatedly choosing based on the final test set.
Use cross-validation:
![[Pasted image 20260615094913.png]]
![[Pasted image 20260615095001.png]]
Now train the selected K on all training data:
![[Pasted image 20260615095104.png]]

---
## 26. Compare Uniform and Distance Weights
![[Pasted image 20260615095253.png]]
Interpretation:
```
uniform:All selected neighbors vote equally
distance:Closer neighbors have greater voting influence
```
---
## 27. Inspect the Nearest Neighbors
You can inspect which samples influenced a prediction.
First access the trained scaler and classifier:
![[Pasted image 20260615095516.png]]
View the neighbor records:
![[Pasted image 20260615095652.png]]
This helps explain:
```
Which training examples were closest?
What were their classes?How far away were they?
```
---
## 28. Predict a New Flower
![[Pasted image 20260615101107.png]]
Important:
```
The new DataFrame must use the same feature namesas the training DataFrame.
```
---
## 29. KNN Decision-Boundary Intuition
KNN creates local decision regions.
With small K:
```
Boundary becomes irregular
Model follows individual samples closely
High variance
Possible overfitting
```
With larger K:
```
Boundary becomes smoother
Local detail decreases
Bias increases
Possible underfitting
```
Conceptually:
```
Small K:Flexible and sensitive
Large K:Stable but potentially too simple
```
This demonstrates the bias–variance trade-off.

---
## 30. Computational Considerations
KNN can become costly at prediction time because each new sample may need comparison with many stored training samples.
It can also require substantial memory because it retains training examples.
This matters when:
```
Dataset contains millions of rows
Feature dimension is high
Predictions must be extremely fast
Memory is limited
```
Scikit-learn supports multiple neighbor-search strategies, including brute force, KD-tree and Ball-tree approaches, selected through the `algorithm` parameter or automatically.

---
## 31. Curse of Dimensionality Awareness
When the number of features becomes very large:
```
Distances between samples become less informative
Many samples appear similarly far apartMore data is required
Prediction can become slower
```
This is called the:
```
Curse of dimensionality
```
Before applying KNN to high-dimensional data, engineers may consider:
```
Feature selection
Dimensionality reduction
Removing noisy features
Using a model better suited to high dimensions
```
---
## 32. Production Failure Scenarios
### Scenario 1: Unscaled features
Training features:
```
Age: 18–70
Annual income: 100,000–10,000,000
```
Failure:
```
Income dominates distance.
```
Senior solution:
```
Use a saved preprocessing pipeline containing StandardScaler.
```
---
### Scenario 2: K larger than training size
Training samples:
```
20
```
Configured:
```
KNeighborsClassifier(n_neighbors=50)
```
Possible error:
```
Expected n_neighbors <= n_samples_fit
```
Senior solution:
```
Validate K against training-set size.Tune K through cross-validation.
```
---
### Scenario 3: Slow production prediction
Problem:
```
Millions of stored training examples
Many API predictions per second
```
Possible solutions:
```
Reduce dataset through representative sampling
Reduce dimensionality
Use approximate-neighbor systems
Use a faster classifier
Batch predictions
Profile latency and memory
```
---
### Scenario 4: New feature schema
Training uses four Iris features, but production sends only three.
Result:
```
Feature-count or feature-name mismatch
```
Solution:
```
Validate request schema.Preserve feature names and order.Save the full pipeline.
```
---
## 33. Debugging Section
### Error 1: K Is Too Large
Broken:
```
model = KNeighborsClassifier(n_neighbors=200)
model.fit(X_train, y_train)
model.predict(X_test)
```
Possible error:
```
ValueError: Expected n_neighbors <= n_samples_fit
```
Root cause:
```
The requested number of neighbors exceedsthe number of fitted training samples.
```
Fix:
```
k = min(5, len(X_train))
model = KNeighborsClassifier(n_neighbors=k)
```
Better prevention:
```
Tune K only within a valid range.
```
---
### Error 2: Predicting Before Fit
Broken:
```
model = KNeighborsClassifier(n_neighbors=5)
model.predict(X_test)
```
Error:
```
NotFittedError
```
Fix:
```
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```
---
### Error 3: Text Feature Not Encoded
Broken features:
```
branch = CSE / ECE / ME
```
Possible error:
```
ValueError: could not convert string to float
```
Fix:
```
Numerical features:SimpleImputer + StandardScaler
Categorical features:SimpleImputer + OneHotEncoder
Then:KNeighborsClassifier
```
Use `ColumnTransformer` and `Pipeline`.

---
### Error 4: Scaling the Full Dataset
Wrong:
```
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(    
	X_scaled,y
)
```
Problem:
```
The scaler learns test-set statistics.This causes preprocessing leakage.
```
Correct:
```
Split first
↓
Fit pipeline only on training data
↓
Predict on test data
```
---
### Error 5: Fitting Separate Scalers
Wrong:
```
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
```
Problem:
```
Train and test are transformed usingdifferent coordinate systems.
```
Correct:
```
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```
Or use Pipeline.

---
### Error 6: Wrong New-Sample Column Names
Broken:
```
new_flower = pd.DataFrame({    
	"sepal_length": [5.9],
    "sepal_width": [3.0],
    "petal_length": [5.1],
    "petal_width": [1.8]})
```
Training names were:
```
sepal length (cm)
sepal width (cm)
petal length (cm)
petal width (cm)
```
Possible error:
```
The feature names should match those
that were passed during fit.
```
Fix:
```
new_flower = pd.DataFrame(    
	[[5.9, 3.0, 5.1, 1.8]],
    columns=X.columns)
```
---
## 34. Common Beginner Mistakes
```
1. Using KNN without scaling
2. Assuming K=5 is always best
3. Choosing K using the test set repeatedly
4. Using K=1 without checking overfitting
5. Using a very large K and underfitting
6. Ignoring class imbalance
7. Treating voting fractions as guaranteed probabilities
8. Forgetting to encode categorical features
9. Ignoring prediction latency
10. Using irrelevant features in the distance calculation
11. Fitting separate scalers on train and test
12. Allowing K to exceed training sample count
13. Ignoring high-dimensional distance problems
14. Evaluating only training accuracy
15. Forgetting to preserve the preprocessing pipeline
```
---
## 35. Logistic Regression vs KNN

|Point|Logistic Regression|KNN|
|---|---|---|
|Learning style|Learns coefficients|Stores examples and searches neighbors|
|Boundary|Primarily linear|Can be highly non-linear|
|Scaling|Strongly recommended|Essential in most distance-based settings|
|Prediction speed|Usually fast|Can be slow on large datasets|
|Interpretability|Coefficients available|Neighbor examples can be inspected|
|Memory use|Relatively low|Stores training examples|
|Main hyperparameter|`C`|`n_neighbors`|
|High dimensions|Can work well|Distances may become less useful|

---
## 36. Interview Questions
Prepare answers for:
```
1. What is KNN?
2. What does K represent?
3. How does KNN make a classification?
4. What is Euclidean distance?
5. Why is scaling important for KNN?
6. What happens when K is too small?
7. What happens when K is too large?
8. How do you select K?
9. What is distance-weighted voting?
10. Can KNN solve multiclass problems?
11. Why is KNN called a lazy learner?
12. Does KNN require model training?
13. What is the curse of dimensionality?
14. Why can KNN prediction be slow?
15. Difference between Logistic Regression and KNN?
```
---
## 37. Interview Trap Questions
### Trap 1
**Does KNN always need StandardScaler?**
Strong answer:
```
KNN needs comparable feature scales because it relies on distance. StandardScaler is a common choice, although another suitable transformation may be selected based on the feature distribution and domain.
```
### Trap 2
**Is K=1 the most accurate because it uses the closest sample?**
Strong answer:
```
Not necessarily. K=1 can be highly sensitive to noise and often has high variance, so validation performance must be checked.
```
### Trap 3
**Should K be selected using the final test set?**
Strong answer:
```
No. K should be selected using validation data or cross-validation. The test set should be reserved for final evaluation.
```
### Trap 4
**Does KNN learn coefficients?**
Strong answer:
```
No. It predicts through distance-based neighbor lookup and class voting rather than a learned linear coefficient equation.
```
### Trap 5
**Do tree-based models and KNN have the same scaling requirement?**
Strong answer:
```
No. KNN is distance-based and usually requires scaling. Decision trees split using thresholds and generally do not require feature scaling.
```
---
## 39. Coding Assignment
Complete before moving to Slot 3:
```
Task 1:
Load Iris using load_iris(as_frame=True).

Task 2:
Print:
Feature names
Class names
Dataset shape
Class distribution

Task 3:
Split using:
test_size=0.20
random_state=42
stratify=y

Task 4:
Build:
StandardScaler → KNeighborsClassifier

Task 5:
Use K=5 and calculate test accuracy.

Task 6:
Create an actual-vs-predicted table.

Task 7:
Print class-voting probabilities.

Task 8:
Try K values from 1 to 20 using cross-validation.

Task 9:
Compare uniform and distance weighting.

Task 10:
Inspect the nearest neighbors of one test sample.

Task 11:
Predict the class of one new flower.

Task 12:
Explain whether the final K appears underfit, balanced or overfit.
```
---
## 40. Real-World Challenge
You are building a student-placement classifier.
Cross-validation results:

| K   | Training Accuracy | Validation Accuracy |
| --- | ----------------- | ------------------- |
| 1   | 100%              | 79%                 |
| 3   | 96%               | 87%                 |
| 5   | 93%               | 91%                 |
| 9   | 89%               | 88%                 |
| 25  | 72%               | 70%                 |
Answer:
```
1. Which K is most likely overfitting?
2. Which K appears best balanced?
3. Which K is underfitting?
4. Why is training accuracy not enough?
5. Would you choose K=5 immediately?
6. What else should you examine?
```
Expected reasoning:
```
K=1 is likely overfitting.
K=5 appears best balanced.
K=25 is likely underfitting.
K should be confirmed through repeated or stratified cross-validation.
Final performance should be checked once on untouched test data.
```
---
## 41. Quick Revision Sheet
```
KNN:
Predicts using nearby training examples.

K:
Number of neighbors used.

Distance:
Measures similarity between samples.

Euclidean Distance:
Straight-line distance in feature space.

Small K:
Flexible, sensitive, overfitting risk.

Large K:
Smooth, underfitting risk.

Uniform Weights:
All neighbors vote equally.

Distance Weights:
Closer neighbors influence more.

StandardScaler:
Makes feature scales comparable.

fit():
Stores/prepares training examples.

predict():
Finds neighbors and returns majority class.

predict_proba():
Returns neighbor-vote proportions.

Cross-validation:
Used to select K without tuning on test data.

Main limitation:
Prediction can become slow and memory-intensive.
```
---
