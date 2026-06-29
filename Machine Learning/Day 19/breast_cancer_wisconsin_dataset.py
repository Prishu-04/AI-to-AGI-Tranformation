import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import (
     accuracy_score,
     confusion_matrix,
     classification_report,precision_score,
     recall_score,
     f1_score
)

## Load dataset
cancer=load_breast_cancer()
## feature and label
x=cancer.data
y=cancer.target

print("Dataset shape:", x.shape)
print("Classes:", cancer.target_names)

## Split the data before train 
X_train, X_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.25,
    stratify=y,
    random_state=42
)

## Model train
results = []

for c_value in [0.01, 1, 100]:

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("svm", SVC(
            kernel="linear",
            C=c_value,
            random_state=42
        ))
    ])

    model.fit(X_train, y_train)

    # Predictions
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # Metrics
    train_acc = accuracy_score(y_train, y_train_pred)
    test_acc = accuracy_score(y_test, y_test_pred)

    precision = precision_score(y_test, y_test_pred)
    recall = recall_score(y_test, y_test_pred)
    f1 = f1_score(y_test, y_test_pred)

    cm = confusion_matrix(y_test, y_test_pred)

    support_vectors = len(
        model.named_steps["svm"].support_vectors_
    )

    print("=" * 60)
    print(f"C = {c_value}")

    print(f"Training Accuracy : {train_acc:.4f}")
    print(f"Testing Accuracy  : {test_acc:.4f}")

    print("\nConfusion Matrix")
    print(cm)

    print("\nClassification Report")
    print(classification_report(y_test, y_test_pred))

    print(f"Total Support Vectors: {support_vectors}")

    results.append({
        "C": c_value,
        "Train Accuracy": train_acc,
        "Test Accuracy": test_acc,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
        "Support Vectors": support_vectors
    })

## Summary dataframe
results_df = pd.DataFrame(results)
print("\nSummary")
print(results_df.round(4))

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

plt.plot(
    results_df["C"],
    results_df["Train Accuracy"],
    marker="o",
    linewidth=2,
    label="Training Accuracy"
)

plt.plot(
    results_df["C"],
    results_df["Test Accuracy"],
    marker="s",
    linewidth=2,
    label="Testing Accuracy"
)

plt.xscale("log")  # because C changes exponentially

plt.xlabel("C value (log scale)")
plt.ylabel("Accuracy")
plt.title("Linear SVM Performance for Different C Values")
plt.xticks([0.01, 1, 100], ["0.01", "1", "100"])
plt.grid(alpha=0.3)
plt.legend()

plt.show()

plt.figure(figsize=(8, 5))

plt.plot(
    results_df["C"],
    results_df["Support Vectors"],
    marker="o",
    linewidth=2
)

plt.xscale("log")
plt.xlabel("C value (log scale)")
plt.ylabel("Number of Support Vectors")
plt.title("Support Vectors vs C")
plt.xticks([0.01, 1, 100], ["0.01", "1", "100"])
plt.grid(alpha=0.3)

plt.show()