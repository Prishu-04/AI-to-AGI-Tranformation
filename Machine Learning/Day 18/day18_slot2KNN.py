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