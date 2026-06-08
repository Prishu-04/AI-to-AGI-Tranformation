# Types of Machine Learning + Supervised vs Unsupervised Learning
Goal :
```
Supervised Learning
Unsupervised Learning
Classification
Regression
Clustering
Reinforcement Learning overview
```
You should also be able to look at a real world problem and say:
```
This is classification.
This is regression.
This is clustering.
This needs labeled data.
This does not need labeled data.
```
---
## 2. Why This Topic Matters
Before choosing an algorithm, you must identify the **type of ML problem**.
A beginner mistake is directly asking:
```
Which algorithm should I use?
```
A strong ML engineer first take:
```
Do I have labels?
What am I predicting?
Is the output a category or a number?
Am I trying to discover hidden groups?
```
This decision controls everything:
```
Dataset format
Algorithm choice
Evaluation metric
Business use case
Model deployment
Interview explanation
```
---
## 3. Industrial Applications
![[Pasted image 20260608125818.png]]

---
## 4. Beginner Explanation
Machine Learning can be divided like this :
```
Machine Learning
│
├── Supervised Learning
│   ├── Classification
│   └── Regression
│
├── Unsupervised Learning
│   ├── Clustering
│   ├── Dimensionality Reduction
│   └── Anomaly Detection
│
├── Semi-Supervised Learning
│
└── Reinforcement Learning
```
Today we mainly focus on :
```
Supervised Learning
Unsupervised Learning
Classification
Regression
Clustering
```
---
## 5. Supervised learning
Supervised Learning means the model learns from data where the correct answer is already given.
Google explains supervised learning as using **labeled data** to train models that predict outcomes for new, unseen data. The model learns the relationship between **features** and **labels** from examples.
### Structure
```
Features + Label
        ↓
Model learns relationship
        ↓
Prediction on new data
```
Example:
![[Pasted image 20260608142032.png]]
Here:
```
Features = Study Hours, Attendance
Label = Result
```
Because the answer/result is already given, this is supervised learning.

---
## 6. Supervised Learning has Two Types
```
Supervised Learning
│
├── Classification
└── Regression
```
---
## 7. Classification
Classification means predicting a **category/class**.
Output is usually:
```
Yes / No
Spam / Not Spam
Fraud / Not Fraud
Pass / Fail
Disease / No Disease
Placed / Not Placed
```
Scikit-learn describe classification as identifying which category an object belongs to, with examples like spam detection and image recognition.
Examples:
![[Pasted image 20260608142341.png]]
### Mathematical Intuition
A classification model tries to learn a boundary.
Example:
```
Low risk customers      High risk customers

        | Decision Boundary |
```
Visual :
```
Income ↑

Good Customers      |      Risky Customers
                    |
                    |
--------------------|--------------------→ Loan Amount
                    |
```
The model learns a line, curve or region that separates one class into another.

---
## 8. Regression
Regression means predicting a **continuous numerical value**.
output is a number:
```
Price
Marks
Salary
Temperature
Sales
Revenue
Delivery time
```
Scikit-learn describes regression as predicting a continuous-valued attribute, with examples such as drug response and stock prices.
![[Pasted image 20260608142704.png]]
### Mathematical Intuition 
A regression model tries to fit a line or curve.
Example:
```
Marks = weight × Study Hours + bias
```
Visual :
```
Marks ↑
100 |                         *
 90 |                    *
 80 |               *
 70 |          *
 60 |     *
    |____________________________→ Study Hours
```
The model learns the relationship:
```
More study hours usually means higher marks
```
----
## 9. Classification vs Regression
![[Pasted image 20260608142934.png]]
Simple rule:
```
If output is a category → Classification
If output is a number → Regression
```
---
## 10. Unsupervised Learning
Unsupervised Learning means the model learns from data where the correct answer is **not given**.
There is no label.
Only input data exists.
```
Features only
      ↓
Model finds hidden patterns
```
Example:
![[Pasted image 20260608143535.png]]
There is no label like :
```
Premium / Budget / Regular
```
The model tries to discover groups by itself.
Scikit-learn’s unsupervised learning section includes clustering, density estimation, dimensionality reduction, and outlier detection.

---
## 11. Clustering
Clustering means grouping similar data points together.
Scikit-learn states that clustering of unlabeled data can be performed using `sklearn.cluster`, and includes methods such as K-Means, Mean Shift, and Spectral Clustering.
### Example Customer Segmentation
Input:
```
Age
Income
Spending Score
Purchase Frequency
```
Output discovered by model:
```
Cluster 1: Budget Customers
Cluster 2: Premium Customers
Cluster 3: Occasional Customers
```
No one gave these labels before. The model discovered them.
### Visual Intuition
```
Spending ↑

Premium Customers       * * *
                       * * *

Regular Customers   * * *
                   * * *

Budget Customers * * *
                * * *
--------------------------------→ Income
```
The algorithm groups based on similarity.

---
## 12. Supervised vs Unsupervised
![[Pasted image 20260608144328.png]]
Shortcut:
```
Has label? → Supervised
No label? → Unsupervised
```
---
## 13. Semi - Supervised Learning
Semi-supervised learning is used when:
```
Some data has labels.Most data has no labels.
```
Example:
You have:
```
1,000 labeled medical images
100,000 unlabeled medical images
```
Labeling medical images is expensive, so we use both labeled and unlabeled data.
This is useful in:
```
Healthcare
Image classification
Speech recognition
Document classification
```
For now, just remember:
```
Semi-supervised = small labeled data + large unlabeled data
```
---
## 14. Reinforcement learning
Reinforcement Learning is different.
Here, an agent learns by taking actions and receiving rewards or penalties.
Structure:
```
Agent → Action → Environment → Reward/Penalty → Learn
```
Examples:
```
Game playing
Robotics
Self-driving simulation
Trading strategy research
Resource allocation
```
Simple analogy:
```
A child learns a game by trying moves.Good move → reward.Bad move → penalty.
```
You do not need to master RL now. Just know it is another type of ML.

---
## 15. How to Identify ML Problem Type
Ask these questions:
###
```
Do I have a target/label column?
```
If yes:
```
Supervised Learning
```
If no:
```
Unsupervised Learning
```
### Question 2
```
If supervised, is the output a category or number?
```
Category:
```
Classification
```
Number:
```
Regression
```
### Question 3
```
If unsupervised, am I grouping similar data?
```
Yes:
```
Clustering
```
---
## 16. Real examples
![[Pasted image 20260608144709.png]]

---
## 17. Code Example: Classification vs Regression vs Clustering
### Classification Dataset Example
![[Pasted image 20260608145549.png]]
Output type:
```
placed = yes/no
```
---
### Regression Dataset Example:
![[Pasted image 20260608145705.png]]
Output type:
```
Marks=number
```
----
### Clustering Dataset Example
![[Pasted image 20260608145818.png]]
Notice:
```
No target column
No answer given
```
---
## 18. Mini Coding Task
Write this;
```python
problems = [
    "Predict house price",
    "Predict whether email is spam",
    "Group customers by behavior",
    "Predict student marks",
    "Detect fraud transaction",
    "Segment users for marketing"
]

for problem in problems:
    print(problem)
```
Now:
```
# Predict house price - Regression
# Predict whether email is spam - Classification
# Group customers by behavior - Clustering
# Predict student marks - Regression
# Detect fraud transaction - Classification
# Segment users for marketing - Clustering
```
----
## 19. Debugging Section
### Bug 1: Confusing Classification and Regression
Wrong thinking:
```
House price prediction is classification.
```
Why wrong:
```
House price is a continuous number.
```
Correct:
```
House price prediction is regression.
```
---
### Bug 2: Calling Clustering Supervised Learning
Wrong thinking:
```
Customer segmentation is supervised learning.
```
Why wrong:
```
There is usually no target label.The model discovers groups.
```
Correct:
```
Customer segmentation is usually unsupervised clustering.
```
---
### Bug 3: Python Syntax Error
Broken code:
```
problems = [    "Predict house price",    "Predict spam email",    "Group customers"for problem in problems:    print(problem)
```
Actual error:
```
SyntaxError: '[' was never closed
```
Why it happens:
```
The list is missing closing bracket ]
```
Correct code:
```
problems = [    "Predict house price",    "Predict spam email",    "Group customers"]for problem in problems:    print(problem)
```
---
## 20. Common Beginner Mistakes
```
1. Thinking all prediction problems are classification.
2. Thinking all ML needs labels.
3. Thinking clustering gives real labels automatically.
4. Thinking logistic regression is regression because of its name.
5. Choosing accuracy for regression problems.
6. Choosing MAE/MSE for classification problems.
7. Calling recommendation systems only one type of ML.
8. Forgetting that anomaly detection can be supervised or unsupervised.
9. Thinking unsupervised learning is less useful.
10. Starting algorithm selection before understanding problem type.
```
Important trap:
```
Logistic Regression is used for classification, not regression.
```
---
## 21. Production Thinking
In production, problem type affects system design.
```

```