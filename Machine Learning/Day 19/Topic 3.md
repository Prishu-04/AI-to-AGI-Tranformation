# SVM Implementation and Decision Boundaries
## 1. Why this slot matters
Accuracy alone can hide model behavior. A model may get good accuracy but create a very unstable, overfitted boundary.
Decision-boundary visualization helps you understand:
- Whether a model is underfitting
- Whether a model is overfitting
- Whether the dataset shape is linear or nonlinear
- Whether SVM kernel choice is correct
- Whether KNN or Random Forest is creating overly complex regions
- Whether `LinearSVC` is suitable instead of kernel-based `SVC`
Scikit-learn has official examples specifically comparing decision boundaries of different classifiers and also warns that toy-data intuition may not always transfer directly to real datasets.

---
## 2. Models we will compare
|Model|Boundary type|Strength|Risk|
|---|---|---|---|
|Logistic Regression|Linear|Simple, fast, interpretable|Underfits nonlinear data|
|Linear SVM|Linear|Strong margin-based classifier|Underfits curved data|
|`LinearSVC`|Linear|Better scaling for large linear problems|No kernel flexibility|
|Polynomial SVM|Curved|Captures polynomial interactions|Can overfit with high degree|
|RBF SVM|Flexible nonlinear|Strong on small/medium nonlinear data|Can overfit and become slow|
|KNN|Local nonlinear|Simple, flexible|Sensitive to scaling and noise|
|Random Forest|Piecewise nonlinear|Strong tabular baseline|Can become complex|
`SVC` supports kernel choices such as `linear`, `poly`, `rbf`, `sigmoid`, and `precomputed`; the official SVM guide also notes that standard `SVC` can become expensive for large datasets, while `LinearSVC` or `SGDClassifier` can be better for large linear problems

---
## 3. What you should learn visually
### Underfitting
A model underfits when the boundary is too simple.
Example:
```
Moon-shaped data + straight line boundary= underfitting
```
Symptoms:
- Low training accuracy
- Low testing accuracy
- Boundary does not follow the data shape
### Overfitting
A model overfits when the boundary becomes too complex.
Symptoms:
- Very high training accuracy
- Lower testing accuracy
- Boundary becomes wiggly
- Model reacts to individual noisy points
### Good generalization
A good model:
- Has strong training performance
- Has strong testing performance
- Has a small train-test gap
- Creates a boundary that matches the true pattern without memorizing noise
---
## 4. Code Implementation
```Python
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# ---------------------------------------------------------
# 1. Create synthetic classification datasets
# ---------------------------------------------------------
datasets = {
    "Moons": make_moons(
        n_samples=500,
        noise=0.25,
        random_state=42
    ),
    "Circles": make_circles(
        n_samples=500,
        noise=0.12,
        factor=0.45,
        random_state=42
    ),
    "Linear-ish": make_classification(
        n_samples=500,
        n_features=2,
        n_redundant=0,
        n_informative=2,
        n_clusters_per_class=1,
        class_sep=1.4,
        random_state=42
    )
}


# ---------------------------------------------------------
# 2. Define models
# ---------------------------------------------------------
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Linear SVM": SVC(kernel="linear", C=1),
    "LinearSVC": LinearSVC(C=1, max_iter=10000),
    "Polynomial SVM": SVC(kernel="poly", degree=3, C=1, gamma="scale"),
    "RBF SVM": SVC(kernel="rbf", C=1, gamma="scale"),
    "KNN": KNeighborsClassifier(n_neighbors=7),
    "Random Forest": RandomForestClassifier(
        n_estimators=150,
        max_depth=5,
        random_state=42
    )
}


# ---------------------------------------------------------
# 3. Function to plot decision boundary
# ---------------------------------------------------------
def plot_decision_boundary(model, X, y, title):
    x_min, x_max = X[:, 0].min() - 0.7, X[:, 0].max() + 0.7
    y_min, y_max = X[:, 1].min() - 0.7, X[:, 1].max() + 0.7

    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 500),
        np.linspace(y_min, y_max, 500)
    )

    grid = np.c_[xx.ravel(), yy.ravel()]
    predictions = model.predict(grid)
    predictions = predictions.reshape(xx.shape)

    plt.figure(figsize=(8, 6))

    plt.contourf(xx, yy, predictions, alpha=0.25)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=35, edgecolors="k")

    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.grid(alpha=0.25)
    plt.show()


# ---------------------------------------------------------
# 4. Function to highlight support vectors for SVC models
# ---------------------------------------------------------
def plot_svm_support_vectors(pipe, X, y, title):
    scaler = pipe.named_steps["scaler"]
    svm_model = pipe.named_steps["model"]

    if not hasattr(svm_model, "support_vectors_"):
        print(f"{title}: This model does not expose support_vectors_.")
        return

    x_min, x_max = X[:, 0].min() - 0.7, X[:, 0].max() + 0.7
    y_min, y_max = X[:, 1].min() - 0.7, X[:, 1].max() + 0.7

    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 500),
        np.linspace(y_min, y_max, 500)
    )

    grid = np.c_[xx.ravel(), yy.ravel()]
    decision_scores = pipe.decision_function(grid)
    decision_scores = decision_scores.reshape(xx.shape)

    support_vectors_original = scaler.inverse_transform(
        svm_model.support_vectors_
    )

    plt.figure(figsize=(8, 6))

    plt.scatter(X[:, 0], X[:, 1], c=y, s=35, edgecolors="k")

    plt.contour(
        xx,
        yy,
        decision_scores,
        levels=[-1, 0, 1],
        linestyles=["--", "-", "--"]
    )

    plt.scatter(
        support_vectors_original[:, 0],
        support_vectors_original[:, 1],
        s=180,
        facecolors="none",
        edgecolors="black",
        linewidths=1.5,
        label="Support vectors"
    )

    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.grid(alpha=0.25)
    plt.show()


# ---------------------------------------------------------
# 5. Train, evaluate, time, and visualize all models
# ---------------------------------------------------------
all_results = []

for dataset_name, (X, y) in datasets.items():
    print("\n" + "#" * 80)
    print(f"DATASET: {dataset_name}")
    print("#" * 80)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        stratify=y,
        random_state=42
    )

    for model_name, model in models.items():
        pipe = Pipeline([
            ("scaler", StandardScaler()),
            ("model", model)
        ])

        start_time = time.time()
        pipe.fit(X_train, y_train)
        training_time = time.time() - start_time

        start_time = time.time()
        y_test_pred = pipe.predict(X_test)
        prediction_time = time.time() - start_time

        y_train_pred = pipe.predict(X_train)

        train_acc = accuracy_score(y_train, y_train_pred)
        test_acc = accuracy_score(y_test, y_test_pred)
        gap = train_acc - test_acc

        all_results.append({
            "dataset": dataset_name,
            "model": model_name,
            "train_accuracy": train_acc,
            "test_accuracy": test_acc,
            "generalization_gap": gap,
            "training_time_sec": training_time,
            "prediction_time_sec": prediction_time
        })

        print("\n" + "-" * 60)
        print(f"Model: {model_name}")
        print("-" * 60)
        print(f"Train accuracy       : {train_acc:.4f}")
        print(f"Test accuracy        : {test_acc:.4f}")
        print(f"Generalization gap   : {gap:.4f}")
        print(f"Training time        : {training_time:.6f} sec")
        print(f"Prediction time      : {prediction_time:.6f} sec")
        print("Confusion matrix:")
        print(confusion_matrix(y_test, y_test_pred))

        plot_decision_boundary(
            pipe,
            X,
            y,
            title=f"{dataset_name} — {model_name}"
        )

        if model_name in ["Linear SVM", "Polynomial SVM", "RBF SVM"]:
            plot_svm_support_vectors(
                pipe,
                X,
                y,
                title=f"{dataset_name} — {model_name} with Support Vectors"
            )


# ---------------------------------------------------------
# 6. Results DataFrame
# ---------------------------------------------------------
results_df = pd.DataFrame(all_results)

print("\nFinal comparison table:")
display(results_df.sort_values(
    by=["dataset", "test_accuracy"],
    ascending=[True, False]
))
```
---
## 5. What you observe after running the code .
### Dataset 1: Moons
Expected pattern:

| Model               | Expected behavior                    |
| ------------------- | ------------------------------------ |
| Logistic Regression | Underfits because boundary is linear |
| Linear SVM          | Underfits because boundary is linear |
| LinearSVC           | Similar to Linear SVM                |
| Polynomial SVM      | Can capture some curve               |
| RBF SVM             | Usually strong                       |
| KNN                 | Flexible, may perform well           |
| Random Forest       | Usually good but blocky boundary     |
### Dataset 2: Circles
Expected pattern:

| Model               | Expected behavior                         |
| ------------------- | ----------------------------------------- |
| Logistic Regression | Strong underfitting                       |
| Linear SVM          | Strong underfitting                       |
| RBF SVM             | Usually best among SVMs                   |
| KNN                 | Often strong                              |
| Random Forest       | Strong but rectangular/piecewise boundary |
### Dataset 3: Linear-ish
Expected pattern:

| Model               | Expected behavior              |
| ------------------- | ------------------------------ |
| Logistic Regression | Strong simple baseline         |
| Linear SVM          | Strong                         |
| LinearSVC           | Strong and scalable            |
| RBF SVM             | May also perform well          |
| KNN                 | May be okay                    |
| Random Forest       | May be good but less necessary |

---
## 6. How to diagnose model behavior
### Case 1: Underfitting
Example result:
```
Train accuracy: 0.72
Test accuracy : 0.70
```
Meaning:
- Model is too simple.
- Boundary does not match data shape.
- Try RBF SVM, polynomial SVM, KNN, or Random Forest.
### Case 2: Overfitting
Example result:
```
Train accuracy: 1.00
Test accuracy : 0.76
```
Meaning:
- Model memorized training patterns.
- Boundary is probably too complex.
- Reduce `C`, reduce `gamma`, reduce tree depth, or increase K in KNN.
### Case 3: Good generalization
Example result:
```
Train accuracy: 0.93
Test accuracy : 0.91
Gap           : 0.02
```
Meaning:
- Model learned useful structure.
- Train-test gap is controlled.
- Boundary is not too simple or too wiggly.
---
## 7. Production comparison
### `SVC`
Use when:
- Dataset is small or medium-sized
- Nonlinear boundary may exist
- Accuracy matters more than training speed
- You want kernel flexibility
Avoid as first choice when:
- Dataset has tens or hundreds of thousands of rows
- Inference latency is strict
- You do not need nonlinear kernels
### `LinearSVC`
Use when:
- Dataset is large
- Boundary is mostly linear
- Features are sparse or high-dimensional
- You need faster training than kernel `SVC`
`LinearSVC` is implemented differently from `SVC(kernel="linear")` and supports dense and sparse inputs; official docs describe multiclass handling with one-vs-rest.
### Logistic Regression
Use when:
- You need interpretability
- You need a fast baseline
- You want probability estimates
- You are working with linear decision boundaries
Scikit-learn’s `LogisticRegression` applies regularization by default and supports dense and sparse inputs.
### KNN
Use when:
- Dataset is small
- Boundary is local/nonlinear
- You want an intuitive baseline
Avoid when:
- Dataset is large
- Inference speed matters
- Features are noisy or badly scaled
KNN classification is based on neighbors and distances, so scaling and inference cost matter.
### Random Forest
Use when:
- You need a strong tabular baseline
- Data has nonlinear feature interactions
- You want less preprocessing than distance-based models
- You want feature-importance awareness
A `RandomForestClassifier` fits many decision trees on subsamples and averages their predictions to improve performance and control overfitting.

---
## 8. Important debugging cases
## Error 1: Plot looks wrong because scaler was not inside the pipeline

Bad:

```
X_scaled = scaler.fit_transform(X)
```

before splitting.

Better:

```
Pipeline([    ("scaler", StandardScaler()),    ("model", SVC())])
```

## Error 2: `LinearSVC` does not show support vectors

This fails:

```
model.named_steps["model"].support_vectors_
```

Reason:

`LinearSVC` does not expose `support_vectors_` like `SVC`.

Use support-vector highlighting only for:

```
SVC(kernel="linear")SVC(kernel="poly")SVC(kernel="rbf")
```

## Error 3: RBF SVM overfits

Symptoms:

```
Train accuracy: 1.00Test accuracy : 0.75
```

Fix:

```
SVC(kernel="rbf", C=1, gamma="scale")
```

or reduce:

```
Cgamma
```

## Error 4: KNN looks too noisy

Cause:

```
KNeighborsClassifier(n_neighbors=1)
```

Fix:

Try:

```
KNeighborsClassifier(n_neighbors=5)KNeighborsClassifier(n_neighbors=7)KNeighborsClassifier(n_neighbors=11)
```

## Error 5: Random Forest boundary too complex

Cause:

```
RandomForestClassifier(max_depth=None)
```

Fix:

```
RandomForestClassifier(max_depth=4)
```

or tune:

```
max_depthmin_samples_leafn_estimators
```

---

# 9. Practice tasks

After running the code, answer these:

1. Which model underfits the **Moons** dataset most clearly?
2. Which model gives the smoothest nonlinear boundary?
3. Which model gives the most block-like decision boundary?
4. Which model has the highest train-test gap?
5. Which model trains fastest?
6. Which model predicts fastest?
7. Which SVM kernel performs best on **Circles**?
8. Does `LinearSVC` behave closer to Logistic Regression or RBF SVM?
9. Which model would you deploy for a small nonlinear dataset?
10. Which model would you deploy for a large high-dimensional sparse text dataset?

---

# 10. Interview questions

1. Why do we visualize decision boundaries?
2. Why can accuracy alone be misleading?
3. Why does Linear SVM fail on moon-shaped data?
4. How does RBF SVM create a nonlinear boundary?
5. Why does KNN create local decision boundaries?
6. Why does Random Forest create piecewise boundaries?
7. Why is `LinearSVC` more production-friendly for large linear datasets?
8. Why does `SVC(kernel="rbf")` become slow on large datasets?
9. How do you detect underfitting from train-test scores?
10. How do you detect overfitting from decision-boundary plots?

---

# 11. Assignment

In your notebook, write a final observation table:

|Dataset|Best model|Worst model|Underfitting model|Overfitting model|Production choice|
|---|---|---|---|---|---|

Then write a **150-word engineering summary**:

> “Based on decision-boundary complexity, train-test gap, and training time, I would choose ___ for ___ dataset because ___.”

----
