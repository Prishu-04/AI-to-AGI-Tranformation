import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 3.5, 6.5, 8.5],
    "attendance": [40, 45, 50, 55, 60, 70, 75, 80, 85, 90, 95, 98, 58, 72, 88],
    "previous_score": [35, 40, 45, 50, 55, 65, 70, 75, 82, 88, 92, 96, 48, 68, 84],
    "sleep_hours": [5, 5, 6, 6, 7, 7, 7, 8, 8, 8, 7, 7, 6, 7, 8],
    "practice_questions": [10, 20, 30, 40, 50, 65, 75, 85, 95, 110, 125, 140, 35, 70, 105],
    "final_marks": [38, 42, 48, 52, 58, 68, 72, 78, 84, 90, 94, 97, 51, 70, 87]
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

models = {
    "Linear Regression": Pipeline(steps=[
        ("scaler", StandardScaler()),
        ("model", LinearRegression())
    ]),

    "Ridge Regression": Pipeline(steps=[
        ("scaler", StandardScaler()),
        ("model", Ridge(alpha=1.0))
    ]),

    "Lasso Regression": Pipeline(steps=[
        ("scaler", StandardScaler()),
        ("model", Lasso(alpha=0.1, max_iter=10000))
    ]),

    "Polynomial Ridge": Pipeline(steps=[
        ("poly", PolynomialFeatures(degree=2, include_bias=False)),
        ("scaler", StandardScaler()),
        ("model", Ridge(alpha=1.0))
    ]),

    "Decision Tree": DecisionTreeRegressor(
        max_depth=3,
        random_state=42
    ),

    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        max_depth=5,
        random_state=42
    )
}

results = []
overfit_results = {}

for name, model in models.items():
    model.fit(X_train, y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    train_mae = mean_absolute_error(y_train, train_pred)
    test_mae = mean_absolute_error(y_test, test_pred)
    test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))
    test_r2 = r2_score(y_test, test_pred)

    results.append({
        "Model": name,
        "Train MAE": train_mae,
        "Test MAE": test_mae,
        "RMSE": test_rmse,
        "R2": test_r2,
        "Train-Test Gap": test_mae - train_mae
    })

results_df = pd.DataFrame(results).sort_values("Test MAE")

print("Model Comparison:")
print(results_df)

best_model_name = results_df.iloc[0]["Model"]
best_model = models[best_model_name]

best_pred = best_model.predict(X_test)

residual_df = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": best_pred
})

residual_df["Residual"] = residual_df["Actual"] - residual_df["Predicted"]
residual_df["Absolute_Error"] = abs(residual_df["Residual"])
residual_df["Squared_Error"] = residual_df["Residual"] ** 2

print("\nBest Model:", best_model_name)
print("\nResidual Analysis:")
print(residual_df)

print("\nResidual Summary:")
print("Residual Mean:", residual_df["Residual"].mean())
print("Average Absolute Error:", residual_df["Absolute_Error"].mean())
print("Maximum Absolute Error:", residual_df["Absolute_Error"].max())

forest_model = models["Random Forest"]
forest_model.fit(X_train, y_train)

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": forest_model.feature_importances_
}).sort_values("Importance", ascending=False)

print("\nRandom Forest Feature Importance:")
print(importance_df)

new_student = pd.DataFrame({
    "study_hours": [7],
    "attendance": [85],
    "previous_score": [75],
    "sleep_hours": [7],
    "practice_questions": [90]
})

prediction = best_model.predict(new_student)[0]
best_mae = results_df.iloc[0]["Test MAE"]

print("\nNew Student Prediction:")
print("Predicted Marks:", prediction)
print(f"Expected Marks Range: {prediction - best_mae:.0f} to {prediction + best_mae:.0f}")