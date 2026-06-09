import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    2, 4, 6, 8, 10, 3, 5, 7, 9, 1],
    
    "attendance": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95,
                   58, 68, 78, 88, 96, 62, 72, 82, 92, 52],
    
    "previous_score": [40, 45, 50, 55, 60, 65, 70, 75, 80, 85,
                       48, 58, 68, 78, 88, 52, 62, 72, 82, 42],
    
    "final_marks": [42, 47, 53, 58, 64, 69, 75, 80, 86, 91,
                    50, 60, 70, 81, 92, 55, 65, 76, 87, 44]
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

print("Model trained successfully")
print(f"Mean Absolute Error:{mae:.2f}")
print()

study_hours=float(input("Enter study hours per day: "))
attendance=float(input("Enter attendance percentage: "))
prev_score=float(input("Enter previous score: "))

user_data = pd.DataFrame({
    "study_hours": [study_hours],
    "attendance": [attendance],
    "previous_score": [prev_score]
})
for i in range(0,user_data.size()):
     predicted_marks = model.predict(user_data)[i]
     lower_range = predicted_marks - mae
     upper_range = predicted_marks + mae

     lower_range = max(0, lower_range)
     upper_range = min(100, upper_range)

     print()
     print("Prediction Result")
     print("-----------------")
     print(f"Expected marks range: {lower_range:.0f} - {upper_range:.0f}")
     print()
     print("Note: This is only an estimated range, not a guaranteed final result.")
     print("Actual marks can change based on exam difficulty, revision, health, and performance on exam day.")