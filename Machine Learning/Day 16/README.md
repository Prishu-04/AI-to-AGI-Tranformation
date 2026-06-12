# Day 16: Data Preprocessing

## Overview

Day 2 focuses on Data Preprocessing, one of the most important parts of Machine Learning.  
The goal of this day is to learn how to clean raw messy data and prepare it for ML models.

A model cannot perform well if the data is dirty, inconsistent, missing, duplicated, wrongly typed, unencoded, or incorrectly scaled.

This day covers Pandas-based data cleaning and scikit-learn-based production-style preprocessing using Pipeline and ColumnTransformer.

---

## Topics Covered

- Data loading and inspection
    
- Missing values
    
- Duplicate rows
    
- Data types
    
- Invalid values
    
- Category cleaning
    
- Outlier basics
    
- Label Encoding
    
- One-Hot Encoding
    
- Feature scaling
    
- Standardization
    
- Normalization
    
- StandardScaler
    
- MinMaxScaler
    
- Pipeline
    
- ColumnTransformer
    
- Leakage-safe preprocessing
    
- Preprocessing mini project
    
- Debugging and interview revision
    

---

## Slot-Wise Learning

|Slot|Topic|
|---|---|
|Slot 1|Data Loading, Inspection, Missing Values, and Duplicates|
|Slot 2|Data Types, Invalid Values, Outliers Basics, and Category Cleaning|
|Slot 3|Encoding Categorical Variables|
|Slot 4|Feature Scaling: Standardization and Normalization|
|Slot 5|Scikit-learn Pipeline and ColumnTransformer Basics|
|Slot 6|Revision + Preprocessing Mini Project + Debugging Assessment|

---

## Tools Used

- Python
    
- Pandas
    
- NumPy
    
- scikit-learn
    

---

## Key Concepts

### Data Preprocessing

Data preprocessing means cleaning, transforming, encoding, scaling, and preparing raw data so it becomes suitable for machine learning models.

Raw data may contain:

- Missing values
    
- Duplicate rows
    
- Wrong data types
    
- Invalid values
    
- Inconsistent categories
    
- Outliers
    
- Unencoded text
    
- Features with different scales
    

---

## Data Inspection

Important Pandas commands:

```python
df.head()
df.tail()
df.shape
df.info()
df.describe()
df.columns
df.dtypes
```

---

## Missing Values

Check missing values:

```python
df.isnull().sum()
```

Common strategies:

|Column Type|Strategy|
|---|---|
|Numerical|Mean, median, constant, missing indicator|
|Categorical|Mode, "Unknown", domain value|
|Too many missing values|Drop column after analysis|
|Few missing rows|Drop rows if safe|

Example:

```python
df["study_hours"] = df["study_hours"].fillna(df["study_hours"].mean())
df["attendance"] = df["attendance"].fillna(df["attendance"].median())
df["study_method"] = df["study_method"].fillna("Unknown")
```

---

## Duplicate Rows

Check duplicates:

```python
df.duplicated().sum()
```

Remove duplicates:

```python
df = df.drop_duplicates()
```

Important note:

Do not remove duplicates blindly. Some repeated rows may represent real repeated events.

---

## Invalid Values

Examples of invalid values:

```text
CGPA = 15
Attendance = 130
Age = -5
Marks = -10
```

Fix invalid values:

```python
df.loc[(df["cgpa"] < 0) | (df["cgpa"] > 10), "cgpa"] = np.nan
df.loc[(df["attendance"] < 0) | (df["attendance"] > 100), "attendance"] = np.nan
```

Then impute:

```python
df["cgpa"] = df["cgpa"].fillna(df["cgpa"].median())
df["attendance"] = df["attendance"].fillna(df["attendance"].median())
```

---

## Category Cleaning

Messy categories:

```text
CSE, cse, Cse 
yes, YES, Y, Yes 
```

Clean categories:

```python
df["branch"] = df["branch"].str.strip().str.upper()

df["internship"] = df["internship"].str.strip().str.lower()
df["internship"] = df["internship"].replace({
    "yes": "Yes",
    "y": "Yes",
    "no": "No",
    "n": "No"
})
```

---

## Encoding

ML models need numerical inputs, so categorical columns must be encoded.

### Binary Encoding

```python
df["internship_encoded"] = df["internship"].map({
    "No": 0,
    "Yes": 1
})
```

### Ordinal Encoding

```python
df["skill_level_encoded"] = df["skill_level"].map({
    "Beginner": 0,
    "Intermediate": 1,
    "Advanced": 2
})
```

### One-Hot Encoding

```python
df = pd.get_dummies(df, columns=["branch"], dtype=int)
```

Use One-Hot Encoding for nominal categories such as:

- Branch
    
- City
    
- Gender
    
- Department
    
- Payment method
    

---

## Feature Scaling

Feature scaling brings numerical columns to comparable scale.

### Standardization

Mean = 0  
Standard deviation = 1

Tool:

```python
StandardScaler()
```

### Normalization

Usually scales values between 0 and 1.

Tool:

```python
MinMaxScaler()
```

Correct scaling workflow:

```text
Train-test split
        ↓
Fit scaler on X_train
        ↓
Transform X_train
        ↓
Transform X_test using same scaler
```

Never fit scaler on full data before splitting.

---

## Pipeline and ColumnTransformer

Manual preprocessing can become messy and risky.  
Pipeline and ColumnTransformer make preprocessing cleaner, reusable, and leakage-safe.

### Numerical Pipeline

```python
numerical_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
```

### Categorical Pipeline

```python
categorical_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])
```

### ColumnTransformer

```python
preprocessor = ColumnTransformer(transformers=[
    ("num", numerical_pipeline, numerical_features),
    ("cat", categorical_pipeline, categorical_features)
])
```

### Final Model Pipeline

```python
model_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("model", LinearRegression())
])
```

---

## Mini Project

# Student Performance Data Preprocessing Pipeline

## Problem Statement

Prepare messy student performance data for a machine learning model that predicts final marks.

## ML Type

Supervised Learning

## Problem Type

Regression

## Features

- cgpa
    
- attendance
    
- previous_score
    
- branch
    
- internship
    
- study_method
    
- skill_level
    

## Label

- final_marks
    

## Goal

Convert raw messy data into clean, encoded, scaled, model-ready data using Pandas and scikit-learn Pipeline.

---

## Files in This Folder

```text
day-02-data-preprocessing/
│
├── README.md
├── notes.md
├── day2_slot1_missing_duplicates.py
├── day2_slot2_invalid_values.py
├── day2_slot3_encoding.py
├── day2_slot4_scaling.py
├── day2_slot5_pipeline_columntransformer.py
├── day2_preprocessing_mini_project.py
└── debugging_notes.md
```

---

## Debugging Notes

Common errors learned:

- `KeyError` from wrong column names
    
- `NameError` from missing imports
    
- `ValueError` from text in numerical pipeline
    
- `SettingWithCopyWarning`
    
- Unknown category error during encoding
    
- Scaling before train-test split
    
- Fitting scaler separately on test data
    
- Leaving text columns unencoded
    
- Including target column in features
    
- Saving only model without preprocessing
    

---

## Interview Questions Covered

- What is data preprocessing?
    
- Why is preprocessing important?
    
- How do you handle missing values?
    
- Mean vs median imputation?
    
- How do you handle categorical missing values?
    
- What are invalid values?
    
- What is category cleaning?
    
- What is One-Hot Encoding?
    
- What is feature scaling?
    
- What is StandardScaler?
    
- What is MinMaxScaler?
    
- Why should scaling happen after train-test split?
    
- What is Pipeline?
    
- What is ColumnTransformer?
    
- Why should preprocessing be saved with the model?
    

---

## Final Learning Outcome

After completing Day 2, I can take a messy tabular dataset, clean it, handle missing and invalid values, remove duplicates, clean categories, encode categorical variables, scale numerical features, and build a leakage-safe preprocessing pipeline using scikit-learn Pipeline and ColumnTransformer.

---

## Resume Bullet

Built a data preprocessing pipeline for messy student performance data using Pandas and scikit-learn, including missing-value handling, duplicate removal, category cleaning, invalid-value treatment, one-hot encoding, feature scaling, ColumnTransformer, and Pipeline-based leakage-safe model training.