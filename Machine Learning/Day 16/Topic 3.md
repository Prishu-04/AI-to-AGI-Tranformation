# Encoding Categorical Variables: Label Encoding and One-Hot Encoding
## 1. Goal
```
1. Why categorical data must be encoded
2. Difference between nominal and ordinal categories
3. Label Encoding
4. One-Hot Encoding
5. pd.get_dummies()
6. sklearn OneHotEncoder
7. When Label Encoding is dangerous
8. Encoding target y vs encoding feature X
9. Common encoding errors
10. Production-safe encoding mindset
```
---
## 2. Why Encoding Mattters
ML models usually work with numbers.
This dataset is not fully model-ready:
```
cgpa = 8.5
branch = CSE
internship = Yes
placed = Yes
```
---
The model undersatnds:
```
8.5
```
But it does not naturally understand:
So we convert categories into numerical form.
Scikit-learn’s `OneHotEncoder` is designed to encode categorical features as a one-hot numeric array, where each category becomes binary columns.

----
## 3. Beginner Explanation
Categorical data means values represent groups or names.
Examples:
```
Branch: CSE, ECE, ME
City: Delhi, Patna, Mumbai
Internship: Yes, No
Grade: Low, Medium, High
T-shirt size: S, M, L, XL
```
Before using ML, these need numerical representation.
There are two important category types:
```
Norinal categories
Ordinal categories
```
---
## 4. Nominal vs Ordinal Categories
### Nominal Categories
Nominal means there is no natural order:
Examples:
```
City: Delhi, Patna, Mumbai
Branch: CSE, ECE, ME
Blood Group: A, B, AB, O
Payment Method: UPI, Cash, Card
```
There is no ranking like:
```
CSE > ECE > ME
```
For nominal categories, use:
```
One-Hot Encoding
```
### Ordinal Categories
Ordinal means there **is a natural order**.
Examples:
```
Low < Medium < High
Beginner < Intermediate < Advanced
Poor < Average < Good < Excellent
S < M < L < XL
```
For ordinal categories, controlled numerical mapping can make sense:
```
Low = 0
Medium = 1
High = 2
```
---
## 5. Label Encoding
Label Encoding means converting categories into integer numbers.
Example:
```
No  → 0
Yes → 1
```
Code:
```Python
df["internship_encoded"] = df["internship"].map({
    "No": 0,
    "Yes": 1
})
```
This works well for binary categories like:
```
Yes/No
True/False
Placed/Not Placed
```
---
## 6. Important Warning About Label Encoding
Scikit-learn’s `LabelEncoder` documentation says it should be used to encode **target values y**, not input features `X`.
Good use:
```Python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y_encoded = le.fit_transform(df["placed"])
```
Output:
```
No  → 0
Yes → 1
```
Be careful using `LabelEncoder` on input features like `branch`, because it may create fake order:
```
CSE = 0
ECE = 1
ME = 2
```
A model may wrongly think:
```
ME > ECE > CSE
```
That order does not actually exist.

---
## 7. One-Hot Encoding
One-Hot Encoding creates separate binary columns for each category.
Example:
Original:

| branch |
| ------ |
| CSE    |
| ECE    |
| ME     |
After one-hot encoding
![[Pasted image 20260611093359.png]]
This avoids fake order:
Pandas `get_dummies()` converts categorical variables into dummy/indicator variables, where each category becomes a 0/1-style column.

---
## 8. Dateset for this Slot.
![[Pasted image 20260611093600.png]]
Columns:
```
cgpa → numerical feature
branch → nominal categorical feature
internship → binary categorical feature
skill_level → ordinal categorical feature
placed → target label
```
---
## 9. Encoding Binary category
For `Internship`:
![[Pasted image 20260611094015.png]]

---
## 10. Encoding Ordinal Category
For `skill_level`, order exists:
```
Beginner < Intermediate < Advanced
```
Use mapping:
![[Pasted image 20260611094849.png]]
This is valid because the order is meaningful.

---
## 11. One-hot Encoding Using Pandas
For `branch`, order does not exist.
![[Pasted image 20260611095052.png]]
Now combine:
![[Pasted image 20260611095252.png]]
Drop orginal text column:
![[Pasted image 20260611095607.png]]

---
## 12. One-Hot Encoding Multiple Columns
![[Pasted image 20260611095743.png]]
This keeps other columns and convert `branch`.
But remember: for ML pipeline, scikit-learn `Òne-HotEncoder` is better because it store category mapping and can handle train/test consisitency better.

---
## 13. Encoding target Label y
For `placed`:
![[Pasted image 20260611100102.png]]
Now :
```
x=features
y=placed_encoded
```
Example:
![[Pasted image 20260611100311.png]]

---
## 15 sklearn OneHotEncoder
For Production of ML, use scikit-learn tranformers.
Example:
![[Pasted image 20260611100734.png]]
Why is this useful:
```
encoder.fit() learns categories from training data
encoder.transform() applies same categories to new data
```
This matters in production

---
## 16. Train/Test Encoding Problem
Bad workflow:
```
Encode full dataset↓Train-test split
```
Risk:
```
Test-set category information may leak into training preprocessing.
```
Better workflow:
```
Train-test split↓Fit encoder on X_train↓Transform X_train↓Transform X_test using same encoder
```
This avoids leakage and keeps train/test transformations consistent.

---
## 17. Unknown Category Problem
Imagine model was trained with:
```
CSE, ECE, ME
```
But in production, user enters:
```
CIVIL
```
Default `OneHotEncoder` may throw an error unless configured.
Use:
```
encoder = OneHotEncoder(    sparse_output=False,    handle_unknown="ignore")
```
This means unknown categories will not crash prediction.
Production mindset:
```
Always expect new categories in real-world data.
```
---
## 18. Debugging Section
### Bug 1: NaN After map()
Broken code:
```
df["internship_encoded"] = df["internship"].map({    "No": 0,    "Yes": 1})
```
But your data has:
```
yes
YESY
No
```
Problem:
```
Unmatched categories become NaN.
```
Debug:
```
print(df["internship"].unique())print(df["internship_encoded"].isnull().sum())
```
Fix:
```
df["internship"] = df["internship"].str.strip().str.lower()df["internship_encoded"] = df["internship"].map({    "no": 0,    "n": 0,    "yes": 1,    "y": 1})
```
---
### Bug 2: Label Encoding Nominal Feature
Bad:
```
df["branch_encoded"] = df["branch"].map({    "CSE": 0,    "ECE": 1,    "ME": 2})
```
Why bad:
```
Branch has no true order.Model may assume ME > ECE > CSE.
```
Correct:
```
df = pd.get_dummies(df, columns=["branch"], dtype=int)
```
---
### Bug 3: Forgetting to Drop Original Text Columns
Broken:
```
X = df.drop("placed_encoded", axis=1)
```
But `X` still contains:
```
branchinternshipskill_levelplaced
```
Possible error:
```
ValueError: could not convert string to float
```
Fix:
```
X = df.drop(    ["placed_encoded", "branch", "internship", "skill_level", "placed"],    axis=1)
```
Or encode/drop all text columns properly.

---
### Bug 4: OneHotEncoder Dense/Sparse Confusion
In newer scikit-learn, use:
```
OneHotEncoder(sparse_output=False)
```
If you use older code:
```
OneHotEncoder(sparse=False)
```
It may fail in newer versions.
Fix:
```
encoder = OneHotEncoder(sparse_output=False)
```
---
## 19. Common Beginner Mistakes
```
1. Using Label Encoding for nominal features.
2. Forgetting to clean categories before encoding.
3. Encoding target and features in the same careless way.
4. Forgetting to drop original text columns.
5. Encoding full dataset before train-test split.
6. Not handling unknown categories in production.
7. Thinking 0/1 always means false/true.
8. Treating ordinal and nominal categories the same.
9. Using LabelEncoder on X features blindly.
10. Not documenting category mappings.
```
---
## 20. Production Thinking
A production encoder must remember:
```
What categories existed during trainingWhat columns were createdHow unknown categories are handledWhat order columns are expected in
```
Example problem:
Training columns:
```
branch_CSE
branch_ECE
branch_ME
```
Production creates:
```
branch_CSE
branch_CIVIL
```
Now model input columns do not match.
Senior solution:
```
Use sklearn OneHotEncoder inside Pipeline/ColumnTransformer.Save the entire preprocessing pipeline with the model.
```
This prevents training-serving mismatch.

---
## 21. Interview Questions
Prepare answers:
```
1. Why do we encode categorical variables?
2. What is Label Encoding?
3. What is One-Hot Encoding?
4. Difference between nominal and ordinal categories?
5. When is Label Encoding safe?
6. Why is Label Encoding dangerous for city/branch?
7. What does pd.get_dummies() do?
8. What does OneHotEncoder do?
9. Why should we fit encoder only on training data?
10. How do you handle unknown categories in production?
```
---
## 22. Interview Trap Questions
### Trap 1
Question:
```
Can I encode CSE, ECE, ME as 0, 1, 2?
```
Answer:
```
Technically yes, but it is usually wrong because it creates fake order. Use one-hot encoding for nominal categories.
```
### Trap 2
Question:
```
Should LabelEncoder be used for input features X?
```
Answer:
```
In scikit-learn, Label
Encoder is intended for target labels y, not input features X. 
For categorical input features, use OneHotEncoder or OrdinalEncoder depending on category type.
```
### Trap 3
Question:
```
Why can encoding before train-test split be risky?
```
Answer:
```
Because preprocessing may learn category information from the test set. Safer workflow is split first, fit encoder on training data, then transform train and test using the same encoder.
```
---
## 23. Mini Assignment Before Next Slot.
```
Task 1:
Create the dataset from this slot.

Task 2:
Clean all category values using strip/case normalization if needed.

Task 3:
Encode internship as:
No = 0
Yes = 1

Task 4:
Encode skill_level as:
Beginner = 0
Intermediate = 1
Advanced = 2

Task 5:
One-hot encode branch using pd.get_dummies().

Task 6:
Encode placed as:
No = 0
Yes = 1

Task 7:
Drop original text columns.

Task 8:
Print final model-ready DataFrame.

Task 9:
Write which columns used label/binary encoding, ordinal encoding, and one-hot encoding.

Task 10:
Write 3 encoding mistakes you must avoid.
```
---
## 24. Real-World Challenge
You are building:
```
AI Placement Readiness Predictor
```
Your columns:
```
branch: CSE, ECE, ME, CIVIL
internship: Yes, No
skill_level: Beginner, Intermediate, Advanced
city: Delhi, Patna, Bhubaneswar, Kolkata
placed: Yes, No
```
Answer:
```
1. Which columns are nominal?
2. Which columns are ordinal?
3. Which columns are binary?
4. Which columns should use One-Hot Encoding?
5. Which columns can use 0/1 mapping?
6. Which column is target y?
7. How will you handle a new city during prediction?
```
---
## 25. Cheat Sheet
```
Categorical variable:
A column with categories/text labels.

Nominal:
No natural order.
Use one-hot encoding.

Ordinal:
Natural order exists.
Use ordered mapping.

Binary:
Two categories.
Use 0/1 mapping.

Label Encoding:
Converts labels into integers.

One-Hot Encoding:
Creates binary columns for each category.

pd.get_dummies():
Quick Pandas one-hot encoding.

OneHotEncoder:
Scikit-learn encoder for categorical features.

handle_unknown="ignore":
Prevents crash on unseen categories.

Encoding leakage:
When category information from test data influences preprocessing.
```
---
## 26. Mind Map

```
Categorical Encoding
│
├── Category Types
│   ├── Nominal
│   │   └── One-Hot Encoding
│   ├── Ordinal
│   │   └── Ordered Mapping
│   └── Binary
│       └── 0/1 Mapping
│
├── Tools
│   ├── map()
│   ├── replace()
│   ├── pd.get_dummies()
│   └── OneHotEncoder
│
├── Risks
│   ├── Fake order
│   ├── Unknown categories
│   ├── Train-test mismatch
│   └── Text columns left unencoded
│
└── Production Fix
    ├── fit on train only
    ├── transform train/test
    ├── handle_unknown="ignore"
    └── save preprocessing pipeline
```
---
