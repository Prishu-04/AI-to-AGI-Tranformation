import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "attendance": [40, 45, 50, 55, 60, 70, 75, 80, 85, 90, 95, 98],
    "previous_score": [35, 40, 45, 50, 55, 65, 70, 75, 82, 88, 92, 96],
    "practice_questions": [10, 20, 30, 40, 50, 65, 75, 85, 95, 110, 125, 140],
    "sleep_hours": [5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 7, 7],
    "mobile_usage_hours": [8, 7, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1],
    "final_marks": [38, 42, 48, 52, 58, 68, 72, 78, 84, 90, 94, 97]
}

df = pd.DataFrame(data)

X = df.drop("final_marks", axis=1)
y = df["final_marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

linear_pipeline = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

ridge_pipeline = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("model", Ridge(alpha=1.0))
])

lasso_pipeline = Pipeline(steps=[
    ("scaler", StandardScaler()),
    ("model", Lasso(alpha=0.1, max_iter=10000))
])

linear_pipeline.fit(X_train, y_train)
ridge_pipeline.fit(X_train, y_train)
lasso_pipeline.fit(X_train, y_train)

linear_pred = linear_pipeline.predict(X_test)
ridge_pred = ridge_pipeline.predict(X_test)
lasso_pred = lasso_pipeline.predict(X_test)

def evaluate_model(name, y_test, y_pred):
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    return {
        "Model": name,
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }

results = pd.DataFrame([
    evaluate_model("Linear Regression", y_test, linear_pred),
    evaluate_model("Ridge Regression", y_test, ridge_pred),
    evaluate_model("Lasso Regression", y_test, lasso_pred)
])

print("Model Comparison:")
print(results)

coef_df = pd.DataFrame({
    "Feature": X.columns,
    "Linear": linear_pipeline.named_steps["model"].coef_,
    "Ridge": ridge_pipeline.named_steps["model"].coef_,
    "Lasso": lasso_pipeline.named_steps["model"].coef_
})

print("\nCoefficient Comparison:")
print(coef_df)

print("\nActual:", y_test.values)
print("Linear Pred:", linear_pred)
print("Ridge Pred:", ridge_pred)
print("Lasso Pred:", lasso_pred)