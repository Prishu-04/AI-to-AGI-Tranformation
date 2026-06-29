# Scikit-learn Pipeline and ColumnTransformer Basics
## 1. Goal
```
1. Why manual preprocessing becomes messy
2. What is a Pipeline?
3. What is ColumnTransformer?
4. Numerical preprocessing pipeline
5. Categorical preprocessing pipeline
6. SimpleImputer
7. StandardScaler
8. OneHotEncoder
9. Leakage-safe preprocessing
10. First production-style ML workflow
```
Main Idea:
```
Raw Dataset
   ↓
ColumnTransformer
   ↓
Numerical Pipeline + Categorical Pipeline
   ↓
Model
   ↓
Prediction
```
---
## 2. Why This Topic matter?
Manual Preprocessing looks easy in small notebooks:
![[Pasted image 20260611121212.png]]
But in real projects, this becomes messy because:
```
Numerical columns need different treatment
Categorical columns need different treatment
Train/test preprocessing must stay consistent
You must avoid data leakage
Production input must follow the same transformations
```
A beginner preprocesses manually.
A strong ML engineer builds a reusable preprocessing pipeline.
Scikit-learn provides a consistent interface for ML workflows, and its tools are designed for predictive data analysis and reusable contexts.

---
## 3. Beginner Explanation
### What is a Pipeline?
A Pipeline is a sequence of steps.
Example:
```
Step 1: Fill missing values
Step 2: Scale numerical values
Step 3: Train model
```
In scikit-learn:
```
Pipeline = multiple preprocessing/model steps connected together
```
Example:
```
SimpleImputer → StandardScaler → Model
```
---
### What is ColumnTransformer?
ColumnTransformer allows different preprocessing for different columns.
Example:
```
Numerical columns:
cgpa, attendance, previous_score        
			  ↓
SimpleImputer + StandardScaler

Categorical columns:branch, internship
	          ↓
SimpleImputer + OneHotEncoder
```
Visual:
```
Dataset
│
├── Numerical Columns
│   └── Imputer → Scaler
│
└── Categorical Columns
    └── Imputer → OneHotEncoder
```
This is much cleaner than manually transforming each column.

---
# 4. Why Pipeline + ColumnTransformer is Industry-Level
Without Pipeline:
```
Preprocessing code scattered everywhereEasy to forget a step
Train/test mismatch risk
Production mismatch risk
Harder to save model
Harder to debug
```
With Pipeline:
```
Preprocessing is organized
Same transformation applies to train/test
Less leakage risk
Easier to deploy
Easier to save full workflow
Cleaner GitHub project
```
Industry mindset:
```
Do not only save the model.
Save preprocessing + model together.
```
---
## 5. Dataset for This Slot
Run this:
![[Pasted image 20260611122342.png]]
Columns:
```
Numerical features:
	cgpa
	attendance
	previous_score
Categorical features:
	branch
	internship

Label:final_marks
```
Problem type:
```
Supervised Learning → Regression
```
---
## 6. Separate X and y
![[Pasted image 20260611122725.png]]

---
## 7. Identify Column Types
```Python
numerical_features = ["cgpa", "attendance", "previous_score"]
categorical_features = ["branch", "internship"]
```
Why separate them?
Because:
```
Numerical features need imputation + scaling
Categorical features need imputation + one-hot encoding
```
---
## 8. Create Numerical Pipeline
![[Pasted image 20260611124306.png]]
Meaning:
```
For numerical columns:
1. Fill missing values using median
2. Standardize values
```
Why median?
```
Median is safer than mean when outliers may exist.
```
---
## 9. Create Categorical Pipeline
![[Pasted image 20260611124452.png]]
Meaning:
```
For categorical columns:
1. Fill missing values using most frequent category
2. One-hot encode categories
```
Why `handle_unknown="ignore"`?
Because production data may contain new categories.
Example:
```
Training branch values:
	CSE,
	ECE,
	ME
Production branch value:
	CIVIL
```
Without handling unknown categories, your model can crash.

---
## 10. Combine Using ColumnTransformer
![[Pasted image 20260611124820.png]]
Meaning:
```
Apply numerical_pipeline to numerical_features
Apply categorical_pipeline to categorical_features
Combine all outputs
```
This is the main power of `ColumnTransformer`.

---
## 11. Add Model to Final Pipeline
![[Pasted image 20260611124917.png]]
Now the full pipeline is:
```
Raw X 
↓
Preprocessor   
	├── Numerical: impute + scale
			└── Categorical: impute + one-hot encode 
↓
LinearRegression
```
---
## 12. Train-Test Split
![[Pasted image 20260611125424.png]]
Correct workflow:
```
Split first
↓
Fit pipeline on training data
↓
Predict on test data
```
---
## 13. Train Full Pipeline
![[Pasted image 20260611125551.png]]
This one line does many things:
```
Fills missing numerical values
Scales numerical values
Fills missing categorical values
One-hot encodes categorical values
Trains LinearRegression model
```
This is why pipelines are powerful.

---
## 14. Predict and Evaluate
![[Pasted image 20260611125950.png]]
Meaning:
```
The pipeline automatically preprocesses X_test using training-learned transformations,then sends it to the trained model.
```

---
## 15. Complete Code
```Python
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
    "cgpa": [8.5, 6.2, 7.8, np.nan, 9.1, 8.0, 5.8, 7.0],
    "attendance": [85, 45, 78, 55, 95, np.nan, 40, 70],
    "previous_score": [82, 45, 76, 50, 95, 88, np.nan, 65],
    "branch": ["CSE", "ECE", "CSE", "ME", "ECE", "CSE", np.nan, "ME"],
    "internship": ["Yes", "No", "Yes", "No", "Yes", np.nan, "No", "Yes"],
    "final_marks": [85, 48, 78, 52, 96, 88, 45, 68]
}

df = pd.DataFrame(data)

X = df.drop("final_marks", axis=1)
y = df["final_marks"]

numerical_features = ["cgpa", "attendance", "previous_score"]
categorical_features = ["branch", "internship"]

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

print("Actual:", y_test.values)
print("Predicted:", y_pred)
print("MAE:", mae)
```
---
## 16. What Happens Internally?
When you call:
```Python
model_pipeline.fit(X_train, y_train)
```
Internally:
```
Numerical columns:
	median imputer learns median from X_train
	StandardScaler learns mean/std from X_train

Categorical columns:
	imputer learns most frequent category from X_train
	OneHotEncoder learns categories from X_train
	
Model:
	LinearRegression learns relationship from transformed X_train to y_train
```
When you call:
```Python
model_pipeline.predict(X_test)
```
Internally:
```
X_test is transformed using training-learned preprocessing
Model predicts final_marks
```
This avoids many beginner mistakes.

---
## 17. Leakage-Safe Thinking
Bad manual workflow:
```
Fill missing values using full dataset
Scale full dataset
Encode full dataset
Split train/test
Train model
```
Why bad?
```
Preprocessing learned information from test data.
```
Good pipeline workflow:
```
Split train/test
Fit pipeline on training data only
Predict on test data
```
This is the main reason `Pipeline` and `ColumnTransformer` are important.

---
## 18. Debugging Section
### Bug 1: Wrong Column Name
Broken code:
```
numerical_features = ["cgpa", "attendence", "previous_score"]
```
Error:
```
ValueError: A given column is not a column of the dataframe
```
Why:
```
Correct column name is attendance, not attendence.
```
Debug:
```
print(X.columns)
```
Fix:
```
numerical_features = ["cgpa", "attendance", "previous_score"]
```
---
### Bug 2: Forgetting to Import Pipeline
Broken code:
```Python
numerical_pipeline = Pipeline(steps=[    
	("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
```
Error:
```
NameError: name 'Pipeline' is not defined
```
Fix:
```
from sklearn.pipeline import Pipeline
```
---
### Bug 3: Using OneHotEncoder on Numerical Columns
Wrong:
```
categorical_features = ["branch", "internship", "cgpa"]
```
Problem:
```
cgpa is numerical, not categorical.One-hot encoding CGPA creates unnecessary many columns.
```
Fix:
```
numerical_features = ["cgpa", "attendance", "previous_score"]
categorical_features = ["branch", "internship"]
```
---
### Bug 4: Scaling Categorical Text Columns
Wrong:
```
numerical_features = ["cgpa", "attendance", "branch"]
```
Possible error:
```
could not convert string to float: 'CSE'
```
Why:
```
branch is text and should not go into StandardScaler.
```
Fix:
```
categorical_features = ["branch"]
```
---
### Bug 5: Unknown Category Error
Without:
```
OneHotEncoder(handle_unknown="ignore")
```
A new category in test/production can produce an error.
Possible error:
```
Found unknown categories during transform
```
Fix:
```
OneHotEncoder(handle_unknown="ignore")
```
---
## 19. Common Beginner Mistakes
```
1. Manually preprocessing full data before split.
2. Forgetting to separate numerical and categorical columns.
3. Scaling categorical columns.
4. One-hot encoding numerical columns.
5. Forgetting handle_unknown="ignore".
6. Not using same preprocessing for train and test.
7. Saving only the model, not the preprocessing.
8. Forgetting imports.
9. Misspelling column names.
10. Not checking feature columns before training.
```
---
## 20. Production Thinking
In production, your model must receive raw user input like:
```
cgpa = 8.2
attendance = 82
previous_score = 75
branch = CIVIL
internship = Yes
```
Your pipeline should:
```
Fill missing values if needed
Scale numerical values
Encode categorical values
Handle unknown branch safely
Predict final marks
```
A strong production system saves the full pipeline:
```
preprocessing + model
```
not only:
```
model
```
Later you will save it using:
```
import joblibjoblib.dump(model_pipeline, "student_marks_pipeline.pkl")
```

---
## 21. Mini Assignment Before Next Slot
Create file:
```
day2_slot5_pipeline_columntransformer.py
```
Complete:
```
Task 1:Create the dataset from this slot.

Task 2:Separate X and y.

Task 3:Create numerical_features and categorical_features.

Task 4:Create numerical_pipeline:
SimpleImputer(strategy="median")
StandardScaler()

Task 5:Create categorical_pipeline:
SimpleImputer(strategy="most_frequent")
OneHotEncoder(handle_unknown="ignore")

Task 6:Create ColumnTransformer.

Task 7:Create final Pipeline with LinearRegression.

Task 8:Train-test split.

Task 9:Fit pipeline on X_train, y_train.

Task 10:Predict on X_test and calculate MAE.

Task 11:Write 5 lines explaining how this prevents leakage.
```
---
## 22. Interview Questions
Prepare answers:
```
1. What is a scikit-learn Pipeline?
2. What is ColumnTransformer?
3. Why do we need different pipelines for numerical and categorical columns?
4. Why use SimpleImputer?
5. Why use StandardScaler?
6. Why use OneHotEncoder?
7. Why should preprocessing be fitted only on training data?
8. What does handle_unknown="ignore" do?
9. Why should we save preprocessing with the model?
10. What is the difference between manual preprocessing and pipeline preprocessing?
```
---
## 23. Interview Trap Questions
### Trap 1
Question:
```
Can I fit scaler and encoder before train-test split?
```
Answer:
```
No. Split first, then fit preprocessing only on training data to reduce leakage risk.
```
### Trap 2
Question:
```
Should I save only model.pkl?
```
Answer:
```
No. Save the full preprocessing + model pipeline so production data receives the same transformations as training data.
```
### Trap 3
Question:
```
Why does ColumnTransformer help with mixed data?
```
Answer:
```
Because numerical and categorical columns need different transformations, and ColumnTransformer applies the correct transformer to each selected column.
```
---
## 24. Cheat Sheet
```
Pipeline:
Chains multiple steps together.

ColumnTransformer:
Applies different transformations to different columns.

SimpleImputer:
Fills missing values.

StandardScaler:
Standardizes numerical features.

OneHotEncoder:
Converts categorical columns to binary columns.

handle_unknown="ignore":
Prevents crash on unseen categories.

fit():
Learns preprocessing parameters/model parameters.

transform():
Applies learned preprocessing.

predict():
Preprocesses input and predicts output.

Best workflow:
Split → fit pipeline on train → predict on test.
```
---
## 25. Mind Map
```
Pipeline + ColumnTransformer
│
├── Input Data
│   ├── Numerical Columns
│   │   ├── SimpleImputer
│   │   └── StandardScaler
│   │
│   └── Categorical Columns
│       ├── SimpleImputer│       
└── OneHotEncoder
│
├── ColumnTransformer
│   └── Combines transformed columns
│
├── Final Pipeline
│   ├── Preprocessor
│   └── Model
│
└── Production Benefit    
	├── Leakage-safe    
	├── Reusable    
	├── Saveable    
	└── Consistent train/test/prediction workflow
```
