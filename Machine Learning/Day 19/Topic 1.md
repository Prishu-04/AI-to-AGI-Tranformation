# SVM Foundations
## 1. Goal
```
- Explain what an SVM does without using memorized definitions.
- Understand hyperplanes, margins, and support vectors.
- Distinguish hard-margin and soft-margin SVM.
- Understand slack variables and hinge loss.
- Explain the basic purpose of `C`.
- Build a linear SVM with scikit-learn.
- Visualize its boundary, margins, and support vectors.
- Identify common scaling, data-shape, and overfitting errors.
```
----
## 2. Why SVM Matters ?
![[Pasted image 20260629093816.png]]
A Support Vector Machine tries to construct a decision boundary that separates classes while maintaining the **largest possible safety margin** between them.
SVMs support classification, regression, and outlier-detection tasks. They are especially relevant to small or medium-sized datasets and high-dimensional feature spaces, including text and information-retrieval problems.
### Industry applications
```
- Spam and phishing detection
- Document and sentiment classification
- Image-category classification
- Handwriting recognition
- Medical-risk classification
- Bioinformatics and gene-expression analysis
- Manufacturing defect detection
- One-class anomaly detection
```
---
## 3. Which companies and platforms work with SVMs?
Google Research hosts the original _Support-Vector Networks_ work by Corinna Cortes and Vladimir Vapnik. Microsoft Research has maintained dedicated SVM research, while Azure Machine Learning provides an SVM component for binary classification. This demonstrates SVM’s continuing importance as both a research method and a practical classical-ML algorithm.
### Interview relevance
SVM questions test whether you understand:
- Linear decision boundaries
- Geometry in machine learning
- Regularization
- Loss functions
- Feature scaling
- Overfitting
- Kernel methods
- Computational complexity
### Startup relevance
SVM is useful when a startup has:
- Limited labelled data
- Many engineered or text-derived features
- A need for a strong classical baseline
- Insufficient data or infrastructure for deep learning
- A prediction problem with a relatively stable feature space
Examples include a phishing detector, document-routing system, customer-complaint classifier, or industrial defect detector.

---
## 4. The Central Intuition
Imagine Imagine two groups of students standing on a playground:
- Red-shirt students belong to Class `-1`.
- Blue-shirt students belong to Class `+1`.
You need to draw a line separating them.
Many different lines may separate the groups:
```
Blue Blue Blue        Blue Blue Blue
      /                     |
-----/------          ------|------- 
Red Red Red           Red Red Red
```
Both lines may classify the existing students correctly.
But SVM asks:
> Which separating line leaves the widest possible empty corridor between the two groups?

That corridor is called the **margin**.
The boundary in the middle of the corridor is the **decision boundary** or **hyperplane**.
The nearest data points touching the corridor determine its position. These points are called **support vectors**.

---
## 5. Hyperplane
### Beginner explanation
In two dimensions, a hyperplane is a line.
In three dimensions, it is a plane.
In higher dimensions, we use the general word **hyperplane**.
The equation is:
![[Pasted image 20260619121051.png|543]]
The prediction rule:
![[Pasted image 20260619121123.png|221]]
The sign tells us which side of the hyperplane contains the point. Linear SVM implementations similarly classify a sample according to the sign of the weighted feature sum.
### Example
Suppose:
![[Pasted image 20260619121431.png|531]]
### Quick Check
![[Pasted image 20260619121550.png|523]]

---
## 6. What is the margins?
**The margin is the distance between the decision boundary and the closest training examples from each class.**
![[Pasted image 20260619121717.png|527]]
Therefore:
- Smaller ∥w∥ → larger margin
- Larger ∥w∥ → smaller margin
To maximize the margin, SVM minimizes:
	![[Pasted image 20260619121903.png|83]]
The original support-vector formulation is based on finding a separating surface with strong generalization through margin maximization.
### Why use ![[Pasted image 20260619122421.png|60]]
Because minimizing ∥w∥ and minimizing ∥w∥2 produce the same optimal direction, but the squared form is easier to differentiate:
![[Pasted image 20260619122515.png|161]]

---
## 7. Support Vectors
Support vectors are the training points nearest to the decision boundary.
They are the most influential points in the model.
```
Class -1              Class +1
x  x  x        |        o  o  o
      X        |         O
---------------|----------------  
lower       decision      upper  
margin      boundary      margin
```
Here:
- `X` is a support vector from Class `-1`.
- `O` is a support vector from Class `+1`.
### Important intuition
A point far away from the boundary usually does not affect the final boundary much.
A point close to the boundary can significantly change:
- The margin
- The direction of the hyperplane
- The final prediction boundary
This is why the algorithm is called a **Support Vector Machine**: its boundary is supported or determined mainly by critical vectors close to the margin.
### Interview trap
**Question:** Does SVM use only support vectors during training?
**Correct explanation:** The optimization process considers the training data, but after fitting, the final decision function for a kernel SVM is determined through the support vectors. Do not loosely claim that all other data points are completely irrelevant during optimization.

---
## 8. Hard-margin SVM
Hard-margin SVM assumes:
- The classes are perfectly linearly separable.
- No training point is allowed inside the margin.
- No training point is allowed on the wrong side.
![[Pasted image 20260619123410.png|598]]
### Understanding the constraint## Problem with hard-margin SVM

Real data normally contains:

- Noise
- Outliers
- Incorrect labels
- Overlapping classes
- Measurement errors

One unusual point can make perfect separation impossible or produce an unreasonable boundary.
![[Pasted image 20260619123506.png|593]]
![[Pasted image 20260619123542.png|594]]
## Problem with hard-margin SVM
Real data normally contains:
- Noise
- Outliers
- Incorrect labels
- Overlapping classes
- Measurement errors
One unusual point can make perfect separation impossible or produce an unreasonable boundary.

---
## 9. Soft-Margin SVM
Soft-margin SVM allows some points to:
- Enter the margin
- Cross the margin
- Be misclassified
It introduces a slack variable:
	![[Pasted image 20260619160244.png|71]]
The constraint becomes:
	![[Pasted image 20260619160313.png|221]]
The optimization objective becomes:
		![[Pasted image 20260619160334.png|226]]
This objective balances:
1. **A wide margin**
		![[Pasted image 20260619160414.png|92]]
2. **Penalties for margin violations**
		![[Pasted image 20260619160441.png|76]]
Scikit-learn describes `C` as a regularization parameter that controls the trade-off between a simple, wide-margin decision surface and errors on individual training examples.

---
## 9. Understanding slack variables
Slack variables measure how severely individual observations violate the margin.
### Case 1: Correct and outside the margin
![[Pasted image 20260619160504.png|86]]
The point is correctly classified and safely located.
### Case 2: Correct but inside the margin
![[Pasted image 20260619160542.png|103]]
The point is correctly classified but too close to the decision boundary.
### Case 3: On the decision boundary
![[Pasted image 20260619160657.png|77]]
### Case 4: Misclassified
![[Pasted image 20260619160717.png|73]]
The point has crossed to the wrong side.

---
## 10. Understanding `C`
`C` controls how strongly SVM penalizes margin violations.
### Large `C`
The model strongly tries to classify every training point correctly.
Likely behavior:
- Narrower margin
- Greater sensitivity to unusual observations
- Lower training error
- Increased overfitting risk
### Small `C`
The model tolerates more margin violations.
Likely behavior:
- Wider margin
- Stronger regularization
- Simpler boundary
- Potential underfitting when too small
Think of `C` as the cost assigned to mistakes:
```
Large C:"Mistakes are extremely expensive.
"Small C:"A few mistakes are acceptable if the boundary is safer and simpler."
```
### Interview trap
**Wrong statement:** A larger `C` means stronger regularization.
**Correct statement:** In scikit-learn’s SVM formulation, a larger `C` penalizes training errors more strongly and therefore corresponds to **weaker effective regularization**. A smaller `C` allows more violations and imposes stronger regularization.

---
## 11. Hinge loss
SVM does not directly optimize ordinary classification accuracy.
![[Pasted image 20260619160906.png]]
Therefore, hinge loss penalizes both:
- Incorrect predictions
- Correct predictions that are not sufficiently far from the boundary
That is a major difference from simply optimizing accuracy.

---
## 12. SVM objective in loss form
A linear soft-margin SVM can be understood as minimizing:

![[Pasted image 20260619160936.png|344]]
The two parts are:

| Component       | Purpose                                    |
| --------------- | ------------------------------------------ |
| 1/2∥w∥2         | Keep the model regularized and margin wide |
| Hinge-loss term | Penalize unsafe or incorrect predictions   |
| CCC             | Control the importance of those penalties  |

---
## 13. Practical implementation
Install or update the required libraries:
```
pip install numpy matplotlib scikit-learn
```
### Complete linear SVM visualization
Run this in Jupyter Notebook or VS Code.
```
import numpy as npimport matplotlib.pyplot as pltfrom sklearn.datasets import make_blobsfrom sklearn.model_selection import train_test_splitfrom sklearn.pipeline import Pipelinefrom sklearn.preprocessing import StandardScalerfrom sklearn.svm import SVCfrom sklearn.metrics import (    accuracy_score,    classification_report,    confusion_matrix)# ---------------------------------------------------------# 1. Create a simple binary classification dataset# ---------------------------------------------------------X, y = make_blobs(    n_samples=200,    centers=2,    n_features=2,    cluster_std=1.35,    random_state=42)# ---------------------------------------------------------# 2. Split the data before fitting the scaler# ---------------------------------------------------------X_train, X_test, y_train, y_test = train_test_split(    X,    y,    test_size=0.25,    stratify=y,    random_state=42)# ---------------------------------------------------------# 3. Build a leakage-safe pipeline# ---------------------------------------------------------model = Pipeline(    steps=[        ("scaler", StandardScaler()),        (            "svm",            SVC(                kernel="linear",                C=1.0            )        )    ])# ---------------------------------------------------------# 4. Train and evaluate# ---------------------------------------------------------model.fit(X_train, y_train)y_train_pred = model.predict(X_train)y_test_pred = model.predict(X_test)print("Training accuracy:", accuracy_score(y_train, y_train_pred))print("Testing accuracy :", accuracy_score(y_test, y_test_pred))print("\nConfusion matrix:")print(confusion_matrix(y_test, y_test_pred))print("\nClassification report:")print(classification_report(y_test, y_test_pred))# ---------------------------------------------------------# 5. Extract the fitted scaler and SVM# ---------------------------------------------------------scaler = model.named_steps["scaler"]svm = model.named_steps["svm"]X_train_scaled = scaler.transform(X_train)print("\nWeight vector:", svm.coef_[0])print("Intercept:", svm.intercept_[0])print("Number of support vectors:", svm.n_support_)print("Total support vectors:", len(svm.support_vectors_))# ---------------------------------------------------------# 6. Generate a mesh in the ORIGINAL feature space# ---------------------------------------------------------x_min, x_max = X[:, 0].min() - 1.5, X[:, 0].max() + 1.5y_min, y_max = X[:, 1].min() - 1.5, X[:, 1].max() + 1.5xx, yy = np.meshgrid(    np.linspace(x_min, x_max, 500),    np.linspace(y_min, y_max, 500))grid_original = np.c_[xx.ravel(), yy.ravel()]# decision_function works through the entire pipelinedecision_scores = model.decision_function(grid_original)decision_scores = decision_scores.reshape(xx.shape)# ---------------------------------------------------------# 7. Convert support vectors to the original scale# ---------------------------------------------------------support_vectors_original = scaler.inverse_transform(    svm.support_vectors_)# ---------------------------------------------------------# 8. Plot data, boundary, margins, and support vectors# ---------------------------------------------------------plt.figure(figsize=(10, 7))plt.scatter(    X_train[:, 0],    X_train[:, 1],    c=y_train,    s=55,    label="Training data")plt.scatter(    X_test[:, 0],    X_test[:, 1],    c=y_test,    marker="x",    s=75,    label="Testing data")# Draw -1 margin, 0 boundary, and +1 marginplt.contour(    xx,    yy,    decision_scores,    levels=[-1, 0, 1],    linestyles=["--", "-", "--"])plt.scatter(    support_vectors_original[:, 0],    support_vectors_original[:, 1],    s=180,    facecolors="none",    edgecolors="black",    linewidths=1.5,    label="Support vectors")plt.title("Linear SVM: Decision Boundary, Margins and Support Vectors")plt.xlabel("Feature 1")plt.ylabel("Feature 2")plt.legend()plt.grid(alpha=0.25)plt.show()
```

---

# 14. Code walkthrough

## Why use a pipeline?

```
Pipeline([    ("scaler", StandardScaler()),    ("svm", SVC(kernel="linear"))])
```

The scaler learns only from the training data when the pipeline is fitted.

This avoids the incorrect process:

```
scaler.fit(X)
```

before splitting the dataset.

SVM is sensitive to feature magnitudes because its geometry and distance calculations depend on the feature space. Microsoft’s Azure documentation similarly recommends normalizing the data before training its two-class SVM component.

## `svm.coef_`

For a linear kernel:

```
svm.coef_
```

contains the learned weight vector:

www

## `svm.intercept_`

```
svm.intercept_
```

contains:

bbb

## `svm.support_vectors_`

```
svm.support_vectors_
```

returns the observations that became support vectors.

Because the pipeline applies `StandardScaler`, these vectors are initially represented in the scaled feature space.

## `svm.n_support_`

```
svm.n_support_
```

shows the number of support vectors belonging to each class.

## `decision_function()`

```
model.decision_function(X)
```

returns signed distances or decision scores relative to the boundary:

- Negative score → one class
- Positive score → the other class
- Score near zero → close to the boundary

---

# 15. Manual hinge-loss implementation

```
import numpy as npdef hinge_loss(    X: np.ndarray,    y: np.ndarray,    weights: np.ndarray,    bias: float) -> float:    """    Calculate mean hinge loss.    Expected target labels:        -1 and +1    """    if set(np.unique(y)) - {-1, 1}:        raise ValueError("Hinge-loss labels must be encoded as -1 and +1.")    scores = X @ weights + bias    losses = np.maximum(0, 1 - y * scores)    return float(np.mean(losses))X_example = np.array([    [2.0, 1.0],    [1.0, 2.0],    [-1.0, -1.0],    [-2.0, -1.0]])y_example = np.array([1, 1, -1, -1])weights = np.array([0.8, 0.6])bias = 0.0loss = hinge_loss(    X=X_example,    y=y_example,    weights=weights,    bias=bias)print("Mean hinge loss:", loss)
```

### Coding question

Why would this produce an incorrect mathematical interpretation?

```
y_example = np.array([0, 0, 1, 1])
```

Because the hinge-loss expression:

1−yif(xi)1-y_if(x_i)1−yi​f(xi​)

assumes labels encoded as:

−1,+1-1,+1−1,+1

When yi=0y_i=0yi​=0, the multiplication no longer represents the side of the hyperplane correctly.

---

# 16. Compare different values of `C`

Modify the code and test:

```
for c_value in [0.01, 0.1, 1, 10, 100]:    model = Pipeline([        ("scaler", StandardScaler()),        ("svm", SVC(kernel="linear", C=c_value))    ])    model.fit(X_train, y_train)    train_score = model.score(X_train, y_train)    test_score = model.score(X_test, y_test)    support_count = len(        model.named_steps["svm"].support_vectors_    )    print(        f"C={c_value:<6} "        f"Train={train_score:.3f} "        f"Test={test_score:.3f} "        f"Support vectors={support_count}"    )
```

Do not automatically conclude that the value with the greatest training accuracy is best.

Look at:

- Test performance
- Generalization gap
- Number of support vectors
- Stability across multiple splits
- Cross-validation performance

Cross-validation and formal tuning will be covered on Day 6.

---

# 17. Common coding mistakes

## Error 1: Predicting before fitting

```
model.predict(X_test)
```

Possible message:

```
NotFittedError: This Pipeline instance is not fitted yet.
```

### Cause

`fit()` was never called.

### Correction

```
model.fit(X_train, y_train)model.predict(X_test)
```

---

## Error 2: Inconsistent number of samples

Possible message:

```
ValueError: Found input variables with inconsistent numbers of samples
```

### Cause

`X` and `y` have different row counts.

### Debugging

```
print(X.shape)print(y.shape)
```

### Correction

Ensure:

```
X.shape[0] == y.shape[0]
```

---

## Error 3: Passing a one-dimensional feature array

Possible message:

```
ValueError: Expected 2D array, got 1D array instead
```

### Cause

```
model.predict([2.5, 3.1])
```

is interpreted as multiple samples with an invalid shape.

### Correction

```
model.predict([[2.5, 3.1]])
```

---

## Error 4: Strings remain in numeric features

Possible message:

```
ValueError: could not convert string to float
```

### Cause

Categorical columns were not encoded.

### Correction

Use a `ColumnTransformer` with:

- `StandardScaler`
- `OneHotEncoder(handle_unknown="ignore")`

---

## Error 5: Scaling before splitting

Broken workflow:

```
X_scaled = scaler.fit_transform(X)X_train, X_test = train_test_split(X_scaled)
```

### Root cause

The scaler learned the mean and standard deviation of test observations.

### Correction

Use a pipeline and fit it only on `X_train`.

---

## Error 6: Scaling training and test data independently

Broken code:

```
X_train = scaler.fit_transform(X_train)X_test = scaler.fit_transform(X_test)
```

### Root cause

The two datasets are mapped using different means and variances.

### Correction

```
X_train = scaler.fit_transform(X_train)X_test = scaler.transform(X_test)
```

Better:

```
Pipeline([    ("scaler", StandardScaler()),    ("svm", SVC(kernel="linear"))])
```

---

## Error 7: Incorrect feature count during inference

Possible message:

```
ValueError: X has 4 features, but SVC is expecting 5 features as input
```

### Cause

The production request is missing a feature or has an incorrect schema.

### Prevention

- Define an input schema.
- Validate feature names and order.
- Persist the preprocessing pipeline.
- Add inference tests.

---

## Error 8: Multiclass target used with `average="binary"`

Possible message:

```
ValueError: Target is multiclass but average='binary'
```

### Correction

Use an appropriate averaging method:

```
f1_score(y_test, y_pred, average="weighted")
```

or:

```
f1_score(y_test, y_pred, average="macro")
```

depending on the objective.

---

## Error 9: Training takes too long

Likely causes:

- Very large dataset
- Too many features
- Nonlinear SVC
- Broad hyperparameter search
- Duplicate records
- Poorly scaled data

Senior-engineer response:

- Establish a linear baseline.
- Try `LinearSVC`.
- Reduce unnecessary features.
- Remove duplicates.
- Profile training time.
- Restrict the tuning space.
- Consider approximate kernel methods.

Scikit-learn notes that standard `SVC` training scales at least quadratically with the number of samples and may become impractical for datasets with tens of thousands of observations; `LinearSVC` or `SGDClassifier` may be more appropriate for large linear problems.

---

## Error 10: Excellent training result, poor test result

Example:

```
Training accuracy: 1.00Testing accuracy: 0.69
```

Potential causes:

- `C` too large
- Noisy data
- Leakage
- Improper split
- Outliers
- Too many irrelevant features
- Dataset shift

Senior-engineer debugging order:

1. Confirm that no leakage exists.
2. Check duplicate records.
3. Compare class distributions.
4. Evaluate a simple baseline.
5. Reduce `C`.
6. Use cross-validation.
7. Inspect misclassified observations.
8. Review suspicious features.
9. Compare results across random seeds.
10. Check whether production data differs from training data.

---

# 18. Production failure scenarios

## Scenario 1: Notebook works, API predictions fail

### Root cause

The notebook scaled data, but the deployed API loaded only the SVM estimator.

### Senior-engineer solution

Save and deploy the complete pipeline:

```
Pipeline([    ("preprocessing", preprocessing),    ("model", svm)])
```

Never separately reproduce training transformations using handwritten API code.

---

## Scenario 2: A new categorical value crashes prediction

Example:

```
ValueError: Found unknown categories ['new_department']
```

### Prevention

```
OneHotEncoder(handle_unknown="ignore")
```

Also monitor how frequently unseen categories appear.

---

## Scenario 3: Accuracy is high, minority-class recall is poor

Example:

```
Accuracy: 96%Fraud recall: 18%
```

### Root cause

The dataset is imbalanced, and accuracy hides the failure.

### Solution

Evaluate:

- Recall
- Precision
- F1-score
- Precision-recall curve
- Confusion matrix
- Business cost

Investigate class weighting and threshold behaviour.

---

## Scenario 4: Prediction latency increases after retraining

### Possible cause

The new SVM retained many more support vectors.

### Why it matters

Kernel-SVM inference depends on support vectors, so additional support vectors can increase prediction work.

### Senior-engineer response

- Log support-vector count per model version.
- Benchmark batch and single-request latency.
- Compare against `LinearSVC`.
- Add latency checks to deployment tests.

---

# 19. Two unique project ideas

## Project 1: AI Phishing Link Guardian

### Problem

Classify URLs as:

- Legitimate
- Suspicious
- Phishing

### Possible features

- URL length
- Number of dots
- Number of special characters
- Presence of an IP address
- HTTPS usage
- Domain age
- Suspicious keywords
- Character-level TF-IDF features

### Models

- Logistic Regression
- LinearSVC
- Random Forest

### API integrations

- Browser-extension API
- Domain reputation API
- FastAPI prediction endpoint
- Slack security-alert webhook

### Deployment

```
Browser Extension      ↓FastAPI      ↓Saved preprocessing + SVM pipeline      ↓Risk score and explanation
```

### Advanced features

- User feedback
- Drift monitoring
- Adversarial URL detection
- Real-time blacklist checks
- Human-review queue

---

## Project 2: Satellite Disaster-Response Classifier

### Problem

Use pretrained image embeddings and an SVM to classify locations as:

- Flooded
- Fire affected
- Damaged
- Normal

### Why SVM?

Instead of training a deep network from scratch:

1. Use a pretrained vision model to extract embeddings.
2. Train an SVM using a smaller labelled dataset.
3. Compare linear and RBF boundaries.

### Integrations

- Satellite imagery API
- Geographic information system
- Disaster-response dashboard
- SMS or email alert service

### Scaling strategy

- Extract embeddings offline.
- Store them in batches.
- Train a linear classifier first.
- Version the embedding model and SVM together.
- Retrain when new disaster images are verified.

---

# 20. Interactive checkpoints

Answer these without checking the notes.

### Question 1

Why does SVM select the maximum-margin boundary instead of any boundary that correctly separates the training data?

### Question 2

What is special about support vectors?

### Question 3

What happens when `C` becomes extremely large?

### Question 4

Can a correctly classified point still have nonzero hinge loss?

### Question 5

Why should numerical features generally be scaled before training an SVM?

---

# 21. Coding task

Using the Breast Cancer Wisconsin dataset:

```
from sklearn.datasets import load_breast_cancer
```

Build a pipeline containing:

- `StandardScaler`
- `SVC(kernel="linear")`

Requirements:

1. Use a stratified train-test split.
2. Print training and testing accuracy.
3. Print the confusion matrix.
4. Print precision, recall, and F1-score.
5. Print the total number of support vectors.
6. Compare `C = 0.01`, `1`, and `100`.
7. Explain which value generalizes best.

Do not select the model using test accuracy repeatedly. For this exercise, use the comparison only to understand behaviour; formal cross-validation comes on Day 6.

---

# 22. Debugging challenge

The following code contains several engineering problems:

```
from sklearn.datasets import load_breast_cancerfrom sklearn.model_selection import train_test_splitfrom sklearn.preprocessing import StandardScalerfrom sklearn.svm import SVCdata = load_breast_cancer()X = data.datay = data.targetscaler = StandardScaler()X = scaler.fit_transform(X)X_train, X_test, y_train, y_test = train_test_split(    X,    y,    test_size=0.30)model = SVC(    kernel="linear",    C=100000)model.fit(X_train, y_train)X_test = scaler.fit_transform(X_test)print(model.score(X_test, y_test))
```

Find at least **five problems or risks**.

Hints:

- Leakage
- Reproducibility
- Stratification
- Scaling consistency
- Regularization
- Pipeline design

Do not fix it by changing only one line. Refactor it into a proper pipeline.

---

# 23. MCQs

## 1. Which points primarily determine an SVM boundary?

A. Every point equally  
B. Support vectors  
C. Only class centroids  
D. Random test samples

## 2. Increasing `C` generally means:

A. More tolerance for margin violations  
B. Stronger effective regularization  
C. Greater penalty for training violations  
D. Features are automatically scaled

## 3. Which point can have positive hinge loss?

A. Only a misclassified point  
B. Only a support vector  
C. A misclassified point or a correctly classified point inside the margin  
D. No correctly classified point

## 4. Why is scaling important?

A. It changes classification into regression  
B. Large-magnitude features can dominate the geometry  
C. It automatically removes outliers  
D. It balances the target classes

## 5. A hard-margin SVM works best when:

A. Classes strongly overlap  
B. Data contains many outliers  
C. Data is perfectly linearly separable  
D. All features are categorical strings

### Answers

1. **B**
2. **C**
3. **C**
4. **B**
5. **C**

---

# 24. Interview questions

1. What is a hyperplane?
2. What is the geometric margin?
3. Why does maximizing the margin support generalization?
4. What are support vectors?
5. Explain hard-margin and soft-margin SVM.
6. What is a slack variable?
7. What does `C` control?
8. Why does a large `C` risk overfitting?
9. Explain hinge loss.
10. Can a correctly classified point have positive hinge loss?
11. Why is feature scaling important for SVM?
12. What happens if an outlier appears near the margin?
13. Why can SVC become slow on large datasets?
14. When would you select `LinearSVC` over `SVC`?
15. How would you debug an SVM with 100% training accuracy and poor validation accuracy?

---

# 25. Assignment

Create a notebook named:

```
day5_slot1_svm_foundations.ipynb
```

It must contain:

1. Hyperplane explanation
2. Margin explanation
3. Support-vector explanation
4. Hard-margin versus soft-margin comparison
5. Hinge-loss implementation
6. Linear SVM visualization
7. `C` comparison
8. Breast Cancer dataset exercise
9. Five debugging findings
10. A 150-word conclusion explaining when you would use SVM

---

# 26. Real-world challenge

You are building a medical screening model with:

- 2,000 observations
- 120 numerical features
- Some overlapping classes
- Different feature scales
- A high cost for false negatives

Write a short engineering decision covering:

- Whether SVM is a reasonable baseline
- Why scaling is necessary
- Why hard-margin SVM is inappropriate
- How you would start selecting `C`
- Which evaluation metrics matter most
- What safety disclaimer the product requires

---

# 27. Revision summary

```
SVM│├── Hyperplane│   └── wᵀx + b = 0│├── Prediction│   └── sign(wᵀx + b)│├── Margin│   ├── Width = 2 / ||w||│   └── Larger margin → smaller ||w||│├── Support vectors│   └── Critical points closest to the boundary│├── Hard margin│   └── No violations allowed│├── Soft margin│   ├── Slack variables│   └── Some violations allowed│├── C│   ├── Large C → stronger error penalty│   └── Small C → more regularization│└── Hinge loss    └── max(0, 1 − y f(x))
```