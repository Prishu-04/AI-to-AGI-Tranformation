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