import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import (
    DecisionTreeClassifier,
    plot_tree
)
from sklearn.ensemble import RandomForestClassifier
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

tree_model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    min_samples_split=4,
    min_samples_leaf=2,
    random_state=42
)

forest_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=5,
    min_samples_leaf=2,
    max_features="sqrt",
    bootstrap=True,
    random_state=42,
    n_jobs=-1
)

tree_model.fit(X_train, y_train)
forest_model.fit(X_train, y_train)

tree_train_pred = tree_model.predict(
    X_train
)

tree_test_pred = tree_model.predict(
    X_test
)

forest_train_pred = forest_model.predict(
    X_train
)

forest_test_pred = forest_model.predict(
    X_test
)

tree_train_accuracy = accuracy_score(
    y_train,
    tree_train_pred
)

tree_test_accuracy = accuracy_score(
    y_test,
    tree_test_pred
)

forest_train_accuracy = accuracy_score(
    y_train,
    forest_train_pred
)

forest_test_accuracy = accuracy_score(
    y_test,
    forest_test_pred
)

comparison = pd.DataFrame([
    {
        "Model": "Decision Tree",
        "Train Accuracy":
            tree_train_accuracy,
        "Test Accuracy":
            tree_test_accuracy,
        "Macro Precision":
            precision_score(
                y_test,
                tree_test_pred,
                average="macro",
                zero_division=0
            ),
        "Macro Recall":
            recall_score(
                y_test,
                tree_test_pred,
                average="macro",
                zero_division=0
            ),
        "Macro F1":
            f1_score(
                y_test,
                tree_test_pred,
                average="macro",
                zero_division=0
            )
    },
    {
        "Model": "Random Forest",
        "Train Accuracy":
            forest_train_accuracy,
        "Test Accuracy":
            forest_test_accuracy,
        "Macro Precision":
            precision_score(
                y_test,
                forest_test_pred,
                average="macro",
                zero_division=0
            ),
        "Macro Recall":
            recall_score(
                y_test,
                forest_test_pred,
                average="macro",
                zero_division=0
            ),
        "Macro F1":
            f1_score(
                y_test,
                forest_test_pred,
                average="macro",
                zero_division=0
            )
    }
])

comparison["Train-Test Gap"] = (
    comparison["Train Accuracy"]
    - comparison["Test Accuracy"]
)

print("Model Comparison:")
print(comparison)

print("\nDecision Tree Report:")
print(
    classification_report(
        y_test,
        tree_test_pred,
        target_names=iris.target_names,
        zero_division=0
    )
)

print("\nRandom Forest Report:")
print(
    classification_report(
        y_test,
        forest_test_pred,
        target_names=iris.target_names,
        zero_division=0
    )
)

forest_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance":
        forest_model.feature_importances_
}).sort_values(
    "Importance",
    ascending=False
)

print("\nRandom Forest Feature Importance:")
print(forest_importance)

new_flower = pd.DataFrame(
    [[5.9, 3.0, 5.1, 1.8]],
    columns=X.columns
)

tree_prediction = tree_model.predict(
    new_flower
)[0]

forest_prediction = forest_model.predict(
    new_flower
)[0]

print(
    "\nTree Prediction:",
    iris.target_names[tree_prediction]
)

print(
    "Forest Prediction:",
    iris.target_names[forest_prediction]
)

plt.figure(figsize=(16, 8))

plot_tree(
    tree_model,
    feature_names=X.columns,
    class_names=iris.target_names,
    filled=True,
    rounded=True,
    fontsize=9
)

plt.title("Controlled Decision Tree")
plt.tight_layout()
plt.show()