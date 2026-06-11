import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = {
    "student_id": [101, 102, 103, 104, 105, 105, 106, 107, 108, 109],
    "cgpa": [8.5, 6.2, 15.0, 7.8, 5.9, 5.9, 9.1, -1.0, 8.0, np.nan],
    "attendance": [85, 45, 120, 78, 55, 55, 95, -10, 88, np.nan],
    "previous_score": [82, 45, 90, 76, np.nan, np.nan, 95, 35, 88, 70],
    "branch": ["CSE", "cse", "Cse ", "ECE", "ece", "ece", "ME", "me ", "CSE", np.nan],
    "internship": ["Yes", "yes", "Y", "No", "no", "no", "N", "YES ", "No", np.nan],
    "study_method": ["Online", "offline", "ONLINE ", "Offline", np.nan, np.nan, "Online", "offline", "Online", "Offline"],
    "skill_level": ["Advanced", "Beginner", "Intermediate", "Beginner", "Advanced", "Advanced", "Intermediate", "Beginner", "Advanced", np.nan],
    "final_marks": [85, 48, 90, 78, 52, 52, 96, 38, 88, 72]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nOriginal Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

df = df.drop_duplicates()

df["branch"] = df["branch"].str.strip().str.upper()

df["internship"] = df["internship"].str.strip().str.lower()
df["internship"] = df["internship"].replace({
    "yes": "Yes",
    "y": "Yes",
    "no": "No",
    "n": "No"
})

df["study_method"] = df["study_method"].str.strip().str.title()

df.loc[(df["cgpa"] < 0) | (df["cgpa"] > 10), "cgpa"] = np.nan
df.loc[(df["attendance"] < 0) | (df["attendance"] > 100), "attendance"] = np.nan
df.loc[(df["final_marks"] < 0) | (df["final_marks"] > 100), "final_marks"] = np.nan

print("\nAfter Basic Cleaning:")
print(df)

X = df.drop(["student_id", "final_marks"], axis=1)
y = df["final_marks"]

numerical_features = ["cgpa", "attendance", "previous_score"]
categorical_features = ["branch", "internship", "study_method", "skill_level"]

numerical_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(transformers=[
    ("num", numerical_pipeline, numerical_features),
    ("cat", categorical_pipeline, categorical_features)
])

model_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", LinearRegression())
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model_pipeline.fit(X_train, y_train)

y_pred = model_pipeline.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)

print("\nActual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(y_pred)

print("\nMAE:")
print(mae)