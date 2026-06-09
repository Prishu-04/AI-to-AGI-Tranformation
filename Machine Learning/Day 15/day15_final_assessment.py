import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "attendance": [40, 45, 50, 55, 60, 70, 75, 80, 90, 95],
    "previous_score": [35, 40, 45, 50, 55, 65, 70, 75, 85, 90],
    "final_marks": [38, 42, 48, 52, 58, 68, 72, 78, 88, 94]
}

df = pd.DataFrame(data)

X = df[["study_hours", "attendance", "previous_score"]]
y = df["final_marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)

print("Actual:", y_test.values)
print("Predicted:", y_pred)
print("MAE:", mae)
print("Weights:", model.coef_)
print("Bias:", model.intercept_)