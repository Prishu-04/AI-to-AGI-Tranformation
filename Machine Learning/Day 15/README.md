# Day 15: Machine Learning Foundations
## Overview

Day 1 focuses on building a strong foundation in Machine Learning.  
The goal of this day is to understand what Machine Learning is, how it differs from Artificial Intelligence and Deep Learning, and how a basic ML workflow works from problem statement to prediction.

This day also introduces the most important beginner concepts such as features, labels, supervised learning, unsupervised learning, train-test split, model training, prediction, evaluation, and debugging.

---

## Topics Covered

- What is Artificial Intelligence?
    
- What is Machine Learning?
    
- What is Deep Learning?
    
- Difference between AI, ML, and DL
    
- Traditional Programming vs Machine Learning
    
- Types of Machine Learning
    
    - Supervised Learning
        
    - Unsupervised Learning
        
    - Semi-Supervised Learning
        
    - Reinforcement Learning
        
- Classification vs Regression
    
- Clustering basics
    
- Features and Labels
    
- Dataset structure
    
- X and y separation
    
- Machine Learning pipeline workflow
    
- Train-test split
    
- First scikit-learn model
    
- Linear Regression basics
    
- MAE evaluation
    
- Beginner debugging
    
- Mini project planning
    

---

## Slot-Wise Learning

|Slot|Topic|
|---|---|
|Slot 1|AI vs ML vs DL + What is Machine Learning|
|Slot 2|Types of Machine Learning|
|Slot 3|Features, Labels, Dataset Structure, X and y|
|Slot 4|Complete Machine Learning Pipeline Workflow|
|Slot 5|Train-Test Split + First scikit-learn Model|
|Slot 6|Revision + Debugging + Interview + Mini Project Planning|

---

## Tools Used

- Python
    
- Pandas
    
- scikit-learn
    
- VS Code / Google Colab / Jupyter Notebook
    

---

## Key Concepts

### Machine Learning

Machine Learning is a subset of Artificial Intelligence where models learn patterns from data and use those patterns to make predictions or decisions on unseen data.

### Supervised Learning

Supervised Learning is used when the dataset has input features and a known target label.

Examples:

- Student marks prediction
    
- House price prediction
    
- Spam email detection
    
- Loan approval prediction
    

### Unsupervised Learning

Unsupervised Learning is used when the dataset does not have a target label.  
The model tries to find hidden patterns or groups in data.

Examples:

- Customer segmentation
    
- Student grouping
    
- Market basket analysis
    

### Features and Labels

Features are input columns used by the model.

Example:

- study_hours
    
- attendance
    
- previous_score
    

Label is the output column the model predicts.

Example:

- final_marks
    
- placed
    
- pass_fail
    

### Train-Test Split

Train-test split separates data into two parts:

- Training data: used to train the model
    
- Testing data: used to evaluate the model on unseen data
    

---

## ML Pipeline Learned

```text
Problem Statement
        ↓
Data Collection
        ↓
Data Understanding
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Encoding
        ↓
Scaling
        ↓
Train-Test Split
        ↓
Model Selection
        ↓
Model Training
        ↓
Prediction
        ↓
Evaluation
        ↓
Error Analysis
        ↓
Improvement
        ↓
Deployment
        ↓
Monitoring
```

---

## Mini Project Planned

# Student Marks Prediction System

## Problem Statement

Predict a student's final marks using study hours, attendance, and previous score.

## ML Type

Supervised Learning

## Problem Type

Regression

## Features

- study_hours
    
- attendance
    
- previous_score
    

## Label

- final_marks
    

## Model

- LinearRegression
    

## Metric

- Mean Absolute Error
    

## Product Idea

The user enters study hours, attendance, and previous score.  
The model predicts expected final marks.

Better product output:

```text
Expected marks range: 75–82
```

Instead of:

```text
Your marks will be exactly 78.342
```

---

## Files in This Folder

```text
day-01-ml-foundations/
│
├── README.md
├── notes.md
├── day1_slot1_ai_ml_dl.py
├── day1_slot2_types_of_ml.py
├── day1_slot3_features_labels.py
├── day1_slot4_ml_pipeline.py
├── day1_slot5_first_ml_model.py
├── day1_final_assessment.py
└── debugging_notes.md
```

---

## Important Code Concepts

### X and y Separation

```python
X = df[["study_hours", "attendance", "previous_score"]]
y = df["final_marks"]
```

### Train-Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

### Model Training

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

### Prediction

```python
y_pred = model.predict(X_test)
```

### Evaluation

```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)
print("MAE:", mae)
```

---

## Debugging Notes

Common errors learned:

- `KeyError` from wrong column names
    
- `NameError` from missing imports
    
- `ValueError` from wrong input shape
    
- `NotFittedError` from calling `predict()` before `fit()`
    
- Using classification metrics for regression
    
- Including target column inside features
    
- Data leakage from wrong feature selection
    

---

## Interview Questions Covered

- What is Machine Learning?
    
- Difference between AI, ML, and DL?
    
- What is Supervised Learning?
    
- What is Unsupervised Learning?
    
- Difference between Classification and Regression?
    
- What are features and labels?
    
- What is train-test split?
    
- What is data leakage?
    
- What does `fit()` do?
    
- What does `predict()` do?
    
- What is MAE?
    

---

## Final Learning Outcome

After completing Day 1, I can explain the basic Machine Learning workflow, identify features and labels, separate X and y, split data into training and testing sets, train my first scikit-learn model, make predictions, evaluate using MAE, and debug beginner ML errors.

---

## Resume Bullet

Built a foundational supervised ML workflow using Python, Pandas, and scikit-learn, including feature-target separation, train-test split, Linear Regression training, prediction, MAE evaluation, and beginner-level debugging.