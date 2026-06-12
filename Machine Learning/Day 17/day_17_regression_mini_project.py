import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 3.5, 6.5, 8.5],
    "attendance": [40, 45, 50, 55, 60, 70, 75, 80, 85, 90, 95, 98, 58, 72, 88],
    "previous_score": [35, 40, 45, 50, 55, 65, 70, 75, 82, 88, 92, 96, 48, 68, 84],
    "sleep_hours": [5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 7, 7, 6, 7, 8],
    "practice_questions": [10, 20, 30, 40, 50, 65, 75, 85, 95, 110, 125, 140, 35, 70, 105],
    "final_marks": [38, 42, 48, 52, 58, 68, 72, 78, 84, 90, 94, 97, 51, 70, 87]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

X = df.drop("final_marks", axis=1)
y = df["final_marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

def evaluate_model(model_name, model, X_test, y_test):
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    return {
        "Model": model_name,
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }

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

poly_pipeline = Pipeline(steps=[
    ("poly", PolynomialFeatures(degree=2, include_bias=False)),
    ("scaler", StandardScaler()),
    ("model", Ridge(alpha=1.0))
])

models = {
    "Linear Regression": linear_pipeline,
    "Ridge Regression": ridge_pipeline,
    "Lasso Regression": lasso_pipeline,
    "Polynomial Ridge Degree 2": poly_pipeline
}

results = []

for model_name, model in models.items():
    model.fit(X_train, y_train)
    results.append(evaluate_model(model_name, model, X_test, y_test))

results_df = pd.DataFrame(results)

print("\nModel Comparison:")
print(results_df)

best_model_name = results_df.sort_values("MAE").iloc[0]["Model"]
best_model = models[best_model_name]

print("\nBest Model Based on MAE:")
print(best_model_name)

y_pred_best = best_model.predict(X_test)

comparison_df = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred_best,
    "Error": y_test.values - y_pred_best,
    "Absolute_Error": abs(y_test.values - y_pred_best)
})

print("\nActual vs Predicted:")
print(comparison_df)

new_student = pd.DataFrame({
    "study_hours": [7],
    "attendance": [85],
    "previous_score": [75],
    "sleep_hours": [7],
    "practice_questions": [90]
})

prediction = best_model.predict(new_student)[0]
best_mae = results_df.sort_values("MAE").iloc[0]["MAE"]

print("\nNew Student Prediction:")
print("Predicted Marks:", prediction)
print(f"Expected Marks Range: {prediction - best_mae:.0f} to {prediction + best_mae:.0f}")