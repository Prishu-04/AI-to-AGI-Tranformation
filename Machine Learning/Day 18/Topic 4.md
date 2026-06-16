# Decision Tree Classifier + Random Forest Classifier
## 1. Goal
```
1. Explain how a Decision Tree classifies data
2. Identify root, internal and leaf nodes
3. Understand feature splits and thresholds
4. Explain Gini impurity
5. Understand Entropy and Information Gain basics
6. Train DecisionTreeClassifier
7. Control tree overfitting
8. Explain Random Forest intuition
9. Understand bootstrap sampling
10. Understand random feature selection
11. Train RandomForestClassifier
12. Compare Decision Tree and Random Forest
13. Interpret feature importance carefully
14. Debug common tree-model errors
```
---
## 2. Why Tree-Based Models Matter
Tree-based classifiers can learn non-linear decision rules without requiring a linear relationship between the inputs and target.
Examples:
```
Loan approval:
If credit score is high
and existing debt is low
and income is sufficient→ 
ApprovePlacement:If DSA score is high
and projects >= 3
and communication is strong→ Likely placed
```

Decision trees are easy to visualize and explain, but unconstrained trees can become overly complex and overfit. Random forests combine many randomized trees to improve robustness and generalization.

---

# 3. Decision Tree Intuition

A decision tree behaves like a flowchart.

Example:

```
Is petal length <= 2.45?│├── Yes│   └── Predict Setosa│└── No    │    └── Is petal width <= 1.75?        │        ├── Yes        │   └── Predict Versicolor        │        └── No            └── Predict Virginica
```

Each decision divides the data into smaller groups.

The objective is to produce child groups that contain increasingly similar class labels.

---

# 4. Main Parts of a Decision Tree

## Root node

The first decision at the top of the tree.

```
petal length <= 2.45
```

It contains all training samples before the first split.

## Internal node

A decision point inside the tree.

```
petal width <= 1.75
```

## Branch

The outcome of a decision.

```
True branchFalse branch
```

## Leaf node

The final prediction node.

```
Predicted class = Virginica
```

A fitted scikit-learn tree stores this binary structure internally; node `0` is the root, and the estimator exposes details such as node count and maximum depth through `tree_`.

---

# 5. How Does a Tree Choose a Split?

Suppose the current node contains:

```
10 Setosa10 Versicolor10 Virginica
```

The classes are mixed.

The model tests possible questions:

```
petal length <= 2.5?petal width <= 1.4?sepal length <= 5.8?
```

For each candidate split, it asks:

```
How pure are the child nodes after this split?
```

A good split produces child nodes with fewer mixed classes.

DecisionTreeClassifier supports criteria including Gini impurity and entropy-based information gain.

---

# 6. Gini Impurity

Gini impurity measures how mixed the classes are inside a node.

Gini=1−∑k=1Kpk2Gini = 1-\sum_{k=1}^{K}p_k^2Gini=1−∑k=1K​pk2​

Where:

```
K   = number of classespₖ  = proportion of class k in the node
```

## Pure node

Suppose all 10 samples belong to class A:

```
p(A) = 1p(B) = 0
```

Then:

```
Gini = 1 - (1² + 0²)Gini = 0
```

Meaning:

```
Perfectly pure node
```

## Mixed binary node

Suppose:

```
50% class A50% class B
```

Then:

```
Gini = 1 - (0.5² + 0.5²)Gini = 0.5
```

Meaning:

```
Highly mixed binary node
```

Lower Gini generally indicates a purer node.

---

# 7. Entropy

Entropy is another measure of class disorder.

H(S)=−∑k=1Kpklog⁡2(pk)H(S)=-\sum_{k=1}^{K}p_k\log_2(p_k)H(S)=−∑k=1K​pk​log2​(pk​)

Interpretation:

```
Entropy = 0→ Node contains one class onlyHigher Entropy→ Classes are more mixed
```

The tree can choose the split that creates the largest reduction in entropy, known as Information Gain.

```
Information Gain=Parent Entropy− Weighted Child Entropy
```

Scikit-learn supports `"gini"`, `"entropy"` and `"log_loss"` as split criteria for DecisionTreeClassifier.

---

# 8. Gini vs Entropy

|Point|Gini|Entropy|
|---|---|---|
|Purpose|Measures impurity|Measures disorder/information|
|Pure node|0|0|
|Computation|Slightly simpler|Uses logarithm|
|scikit-learn setting|`criterion="gini"`|`criterion="entropy"`|
|Typical result|Often similar|Often similar|

For beginner projects:

```
DecisionTreeClassifier(    criterion="gini")
```

is a reasonable starting point.

Model selection should still depend on validation performance rather than assuming one criterion is universally superior.

---

# 9. Decision Tree Important Parameters

## `max_depth`

Maximum number of levels in the tree.

```
DecisionTreeClassifier(    max_depth=3)
```

Smaller depth:

```
Simpler treeEasier explanationLower overfitting riskPossible underfitting
```

Large or unlimited depth:

```
More detailed rulesLower training errorHigher overfitting risk
```

## `min_samples_split`

Minimum number of samples required to divide an internal node.

```
DecisionTreeClassifier(    min_samples_split=10)
```

Larger value prevents the model from creating splits based on very few samples.

## `min_samples_leaf`

Minimum number of training samples that must remain in a leaf.

```
DecisionTreeClassifier(    min_samples_leaf=5)
```

Larger leaves can produce smoother, more stable rules.

## `ccp_alpha`

Controls cost-complexity post-pruning.

```
DecisionTreeClassifier(    ccp_alpha=0.01)
```

Increasing `ccp_alpha` prunes more nodes. Scikit-learn documents `max_depth`, `min_samples_leaf` and cost-complexity pruning as ways to control tree size and overfitting.

---

# 10. Underfitting and Overfitting in Trees

## Underfitting

```
Tree is too shallowRules are too simpleTraining performance is weakTesting performance is weak
```

Example:

```
DecisionTreeClassifier(    max_depth=1)
```

## Overfitting

```
Tree grows very deepCreates tiny leavesMemorizes training examplesTraining accuracy becomes extremely highTest performance is lower
```

Example:

```
DecisionTreeClassifier(    max_depth=None,    min_samples_leaf=1)
```

## Balanced tree

```
Reasonable depthReasonable leaf sizesSmall train-test performance gapGood validation performance
```

Decision-tree learners can create over-complex trees that fail to generalize, so depth control, minimum sample constraints and pruning should be evaluated using validation or cross-validation.

---

# 11. Dataset for This Slot

We will use the Iris multiclass dataset again so that you can compare KNN with tree-based models.

Features:

```
Sepal lengthSepal widthPetal lengthPetal width
```

Classes:

```
SetosaVersicolorVirginica
```

Create:

```
day4_slot4_tree_random_forest.py
```

---

# 12. Load the Iris Dataset

```
import pandas as pdfrom sklearn.datasets import load_irisiris = load_iris(as_frame=True)X = iris.datay = iris.targetprint("Features:")print(X.head())print("\nClass Names:")print(iris.target_names)print("\nDataset Shape:")print(X.shape)print("\nClass Distribution:")print(y.value_counts().sort_index())
```

---

# 13. Train-Test Split

```
from sklearn.model_selection import train_test_splitX_train, X_test, y_train, y_test = train_test_split(    X,    y,    test_size=0.20,    random_state=42,    stratify=y)print("Training shape:", X_train.shape)print("Testing shape:", X_test.shape)
```

`stratify=y` helps preserve the proportion of all three Iris classes in both subsets.

---

# 14. Train an Unrestricted Decision Tree

First, train a tree without depth restriction:

```
from sklearn.tree import DecisionTreeClassifierfull_tree = DecisionTreeClassifier(    criterion="gini",    random_state=42)full_tree.fit(X_train, y_train)
```

Evaluate training and test performance:

```
from sklearn.metrics import accuracy_scorefull_train_pred = full_tree.predict(X_train)full_test_pred = full_tree.predict(X_test)full_train_accuracy = accuracy_score(    y_train,    full_train_pred)full_test_accuracy = accuracy_score(    y_test,    full_test_pred)print("Full Tree Training Accuracy:",      full_train_accuracy)print("Full Tree Testing Accuracy:",      full_test_accuracy)print("Full Tree Depth:",      full_tree.get_depth())print("Full Tree Leaves:",      full_tree.get_n_leaves())
```

A very high training score does not prove the tree generalizes. Compare it with test or validation performance.

---

# 15. Train a Controlled Decision Tree

```
controlled_tree = DecisionTreeClassifier(    criterion="gini",    max_depth=3,    min_samples_split=4,    min_samples_leaf=2,    random_state=42)controlled_tree.fit(    X_train,    y_train)tree_train_pred = controlled_tree.predict(    X_train)tree_test_pred = controlled_tree.predict(    X_test)tree_train_accuracy = accuracy_score(    y_train,    tree_train_pred)tree_test_accuracy = accuracy_score(    y_test,    tree_test_pred)print("Controlled Tree Training Accuracy:",      tree_train_accuracy)print("Controlled Tree Testing Accuracy:",      tree_test_accuracy)print("Controlled Tree Depth:",      controlled_tree.get_depth())print("Controlled Tree Leaves:",      controlled_tree.get_n_leaves())
```

Compare:

```
Training accuracyTesting accuracyTree depthNumber of leaves
```

A slightly lower training score can be acceptable when test performance becomes more stable.
# 16. Evaluate the Controlled Tree

```
from sklearn.metrics import (    confusion_matrix,    classification_report)print("Confusion Matrix:")print(    confusion_matrix(        y_test,        tree_test_pred    ))print("\nClassification Report:")print(    classification_report(        y_test,        tree_test_pred,        target_names=iris.target_names,        zero_division=0    ))
```

Because Iris is multiclass, inspect:

```
Per-class PrecisionPer-class RecallPer-class F1Macro averageWeighted average
```

---

# 17. Visualize the Decision Tree

```
import matplotlib.pyplot as pltfrom sklearn.tree import plot_treeplt.figure(figsize=(16, 8))plot_tree(    controlled_tree,    feature_names=X.columns,    class_names=iris.target_names,    filled=True,    rounded=True,    fontsize=9)plt.title("Iris Decision Tree")plt.tight_layout()plt.show()
```

Each node displays information such as:

```
Splitting conditionImpurityNumber of samplesClass countsPredicted class
```

---

# 18. How to Read a Tree Node

Example:

```
petal width (cm) <= 0.8gini = 0.667samples = 120value = [40, 40, 40]class = setosa
```

Meaning:

```
Rule:petal width <= 0.8Impurity:Classes are currently mixedSamples:120 training samples reached this nodeValue:40 Setosa40 Versicolor40 VirginicaClass:Current majority prediction
```

The true and false branches continue until a leaf is reached.

---

# 19. Decision Tree Feature Importance

```
tree_importance = pd.DataFrame({    "Feature": X.columns,    "Importance":        controlled_tree.feature_importances_}).sort_values(    "Importance",    ascending=False)print(tree_importance)
```

Impurity-based feature importance measures how much each feature contributed to impurity reduction across the tree.

Important caution:

```
Importance does not prove causation.Correlated features can share or distort importance.High-cardinality features can receive misleading importance.
```

Scikit-learn provides examples comparing forest impurity-based importance with permutation importance because the two can behave differently.

---

# 20. Predict a New Flower

```
new_flower = pd.DataFrame(    [[5.9, 3.0, 5.1, 1.8]],    columns=X.columns)predicted_class = controlled_tree.predict(    new_flower)[0]class_probabilities = (    controlled_tree.predict_proba(        new_flower    )[0])print(    "Predicted Class:",    iris.target_names[predicted_class])for class_name, probability in zip(    iris.target_names,    class_probabilities):    print(        f"{class_name}: {probability:.2%}"    )
```

Tree class probabilities are based on the class distribution in the reached leaf.

---

# 21. What Is an Ensemble?

An ensemble combines multiple models rather than relying on one model.

```
Single model:One opinionEnsemble:Many model opinions combined
```

Potential benefits:

```
Greater stabilityLower varianceImproved generalizationReduced dependence on one training sample
```

Scikit-learn describes ensemble methods as combining multiple base estimators to improve robustness or generalizability.

---

# 22. Random Forest Intuition

Random Forest creates many decision trees.

Each tree is intentionally made different through:

```
1. Different bootstrap sample of training rows2. Random subset of features considered at splits
```

The final classifier averages predicted class probabilities across the trees and selects the class with the highest mean probability. This is often simplified as “voting,” but probability averaging is the more precise description of scikit-learn’s implementation.

Example:

```
Tree 1 → Versicolor: 70%Tree 2 → Versicolor: 90%Tree 3 → Virginica: 60%Tree 4 → Versicolor: 80%Average probabilities↓Final class selected
```

---

# 23. Bootstrap Sampling

Bootstrap sampling means drawing training rows:

```
RandomlyWith replacement
```

With replacement means the same row can appear more than once in one tree’s sample, while some rows may not appear at all.

Example original rows:

```
A B C D E
```

One bootstrap sample:

```
A C C E B
```

RandomForestClassifier uses bootstrap sampling by default unless configured otherwise.

---

# 24. Random Feature Selection

At each candidate split, Random Forest considers only a random subset of the available features.

Suppose the dataset has:

```
20 features
```

A tree split may consider only a smaller subset, rather than all 20.

Why?

```
It reduces similarity between trees.Different trees learn different patterns.Averaging diverse trees is more useful than averaging identical trees.
```

The `max_features` parameter controls how many features are considered for each split.

---

# 25. Important Random Forest Parameters

## `n_estimators`

Number of trees.

```
RandomForestClassifier(    n_estimators=200)
```

More trees often make predictions more stable, but increase training time, prediction time and memory use.

## `max_depth`

Maximum depth of each tree.

```
RandomForestClassifier(    max_depth=5)
```

## `max_features`

Features considered at each split.

```
RandomForestClassifier(    max_features="sqrt")
```

## `bootstrap`

Whether rows are sampled with replacement.

```
RandomForestClassifier(    bootstrap=True)
```

## `n_jobs`

Number of CPU jobs.

```
RandomForestClassifier(    n_jobs=-1)
```

`-1` uses all available processors managed by joblib.

## `class_weight`

Can assign greater importance to minority classes.

```
RandomForestClassifier(    class_weight="balanced")
```

Class imbalance will be covered properly in Slot 5.

---

# 26. Train RandomForestClassifier

```
from sklearn.ensemble import RandomForestClassifierforest_model = RandomForestClassifier(    n_estimators=200,    max_depth=5,    min_samples_leaf=2,    max_features="sqrt",    bootstrap=True,    random_state=42,    n_jobs=-1)forest_model.fit(    X_train,    y_train)
```

---

# 27. Evaluate Random Forest

```
forest_train_pred = forest_model.predict(    X_train)forest_test_pred = forest_model.predict(    X_test)forest_train_accuracy = accuracy_score(    y_train,    forest_train_pred)forest_test_accuracy = accuracy_score(    y_test,    forest_test_pred)print("Forest Training Accuracy:",      forest_train_accuracy)print("Forest Testing Accuracy:",      forest_test_accuracy)print("\nForest Confusion Matrix:")print(    confusion_matrix(        y_test,        forest_test_pred    ))print("\nForest Classification Report:")print(    classification_report(        y_test,        forest_test_pred,        target_names=iris.target_names,        zero_division=0    ))
```

---

# 28. Compare Decision Tree and Random Forest

```
from sklearn.metrics import (    precision_score,    recall_score,    f1_score)comparison = pd.DataFrame([    {        "Model": "Decision Tree",        "Train Accuracy":            tree_train_accuracy,        "Test Accuracy":            tree_test_accuracy,        "Macro Precision":            precision_score(                y_test,                tree_test_pred,                average="macro",                zero_division=0            ),        "Macro Recall":            recall_score(                y_test,                tree_test_pred,                average="macro",                zero_division=0            ),        "Macro F1":            f1_score(                y_test,                tree_test_pred,                average="macro",                zero_division=0            )    },    {        "Model": "Random Forest",        "Train Accuracy":            forest_train_accuracy,        "Test Accuracy":            forest_test_accuracy,        "Macro Precision":            precision_score(                y_test,                forest_test_pred,                average="macro",                zero_division=0            ),        "Macro Recall":            recall_score(                y_test,                forest_test_pred,                average="macro",                zero_division=0            ),        "Macro F1":            f1_score(                y_test,                forest_test_pred,                average="macro",                zero_division=0            )    }])comparison["Train-Test Gap"] = (    comparison["Train Accuracy"]    - comparison["Test Accuracy"])print(comparison)
```

Do not automatically choose the model with the highest single test score.

Also examine:

```
Train-test gapCross-validation stabilityPer-class RecallPrediction speedInterpretability requirementsModel sizeBusiness risk
```

---

# 29. Decision Tree vs Random Forest

|Point|Decision Tree|Random Forest|
|---|---|---|
|Number of trees|One|Many|
|Interpretability|High|Lower|
|Visualization|Easy|Difficult for whole forest|
|Overfitting risk|Higher|Usually lower|
|Stability|Sensitive to data changes|More stable|
|Prediction speed|Usually faster|Usually slower|
|Feature scaling|Generally unnecessary|Generally unnecessary|
|Non-linear patterns|Yes|Yes|
|Feature interactions|Yes|Yes|

Tree-based models split using thresholds rather than distance calculations, so standardization usually does not change their split ordering and is generally unnecessary. However, preprocessing may still be required for missing values, text categories and invalid inputs.

---

# 30. Random Forest Feature Importance

```
forest_importance = pd.DataFrame({    "Feature": X.columns,    "Importance":        forest_model.feature_importances_}).sort_values(    "Importance",    ascending=False)print(forest_importance)
```

Visualize it:

```
import matplotlib.pyplot as pltimportance_plot = forest_importance.sort_values(    "Importance")plt.figure(figsize=(8, 5))plt.barh(    importance_plot["Feature"],    importance_plot["Importance"])plt.xlabel("Impurity-Based Importance")plt.ylabel("Feature")plt.title("Random Forest Feature Importance")plt.tight_layout()plt.show()
```

Use feature importance as an investigation tool—not as proof that a feature causes the prediction.

---

# 31. Out-of-Bag Evaluation Awareness

When bootstrap sampling is enabled, some training examples are excluded from a particular tree’s bootstrap sample.

These are called:

```
Out-of-bag samples
```

They can provide an internal performance estimate.

```
oob_forest = RandomForestClassifier(    n_estimators=200,    bootstrap=True,    oob_score=True,    random_state=42,    n_jobs=-1)oob_forest.fit(    X_train,    y_train)print(    "OOB Score:",    oob_forest.oob_score_)
```

Out-of-bag error uses predictions from trees that did not train on a given observation. It is a useful additional estimate, but it does not replace a final untouched test set.

# 32. Complete Working Program

```
import pandas as pdimport matplotlib.pyplot as pltfrom sklearn.datasets import load_irisfrom sklearn.model_selection import train_test_splitfrom sklearn.tree import (    DecisionTreeClassifier,    plot_tree)from sklearn.ensemble import RandomForestClassifierfrom sklearn.metrics import (    accuracy_score,    precision_score,    recall_score,    f1_score,    confusion_matrix,    classification_report)iris = load_iris(as_frame=True)X = iris.datay = iris.targetX_train, X_test, y_train, y_test = train_test_split(    X,    y,    test_size=0.20,    random_state=42,    stratify=y)tree_model = DecisionTreeClassifier(    criterion="gini",    max_depth=3,    min_samples_split=4,    min_samples_leaf=2,    random_state=42)forest_model = RandomForestClassifier(    n_estimators=200,    max_depth=5,    min_samples_leaf=2,    max_features="sqrt",    bootstrap=True,    random_state=42,    n_jobs=-1)tree_model.fit(X_train, y_train)forest_model.fit(X_train, y_train)tree_train_pred = tree_model.predict(    X_train)tree_test_pred = tree_model.predict(    X_test)forest_train_pred = forest_model.predict(    X_train)forest_test_pred = forest_model.predict(    X_test)tree_train_accuracy = accuracy_score(    y_train,    tree_train_pred)tree_test_accuracy = accuracy_score(    y_test,    tree_test_pred)forest_train_accuracy = accuracy_score(    y_train,    forest_train_pred)forest_test_accuracy = accuracy_score(    y_test,    forest_test_pred)comparison = pd.DataFrame([    {        "Model": "Decision Tree",        "Train Accuracy":            tree_train_accuracy,        "Test Accuracy":            tree_test_accuracy,        "Macro Precision":            precision_score(                y_test,                tree_test_pred,                average="macro",                zero_division=0            ),        "Macro Recall":            recall_score(                y_test,                tree_test_pred,                average="macro",                zero_division=0            ),        "Macro F1":            f1_score(                y_test,                tree_test_pred,                average="macro",                zero_division=0            )    },    {        "Model": "Random Forest",        "Train Accuracy":            forest_train_accuracy,        "Test Accuracy":            forest_test_accuracy,        "Macro Precision":            precision_score(                y_test,                forest_test_pred,                average="macro",                zero_division=0            ),        "Macro Recall":            recall_score(                y_test,                forest_test_pred,                average="macro",                zero_division=0            ),        "Macro F1":            f1_score(                y_test,                forest_test_pred,                average="macro",                zero_division=0            )    }])comparison["Train-Test Gap"] = (    comparison["Train Accuracy"]    - comparison["Test Accuracy"])print("Model Comparison:")print(comparison)print("\nDecision Tree Report:")print(    classification_report(        y_test,        tree_test_pred,        target_names=iris.target_names,        zero_division=0    ))print("\nRandom Forest Report:")print(    classification_report(        y_test,        forest_test_pred,        target_names=iris.target_names,        zero_division=0    ))forest_importance = pd.DataFrame({    "Feature": X.columns,    "Importance":        forest_model.feature_importances_}).sort_values(    "Importance",    ascending=False)print("\nRandom Forest Feature Importance:")print(forest_importance)new_flower = pd.DataFrame(    [[5.9, 3.0, 5.1, 1.8]],    columns=X.columns)tree_prediction = tree_model.predict(    new_flower)[0]forest_prediction = forest_model.predict(    new_flower)[0]print(    "\nTree Prediction:",    iris.target_names[tree_prediction])print(    "Forest Prediction:",    iris.target_names[forest_prediction])plt.figure(figsize=(16, 8))plot_tree(    tree_model,    feature_names=X.columns,    class_names=iris.target_names,    filled=True,    rounded=True,    fontsize=9)plt.title("Controlled Decision Tree")plt.tight_layout()plt.show()
```

---

# 33. Production Thinking

## Decision Tree advantage

A single tree can provide an understandable rule path:

```
petal length > 2.45petal width > 1.75→ Virginica
```

This can help when model decisions require explanation.

## Random Forest advantage

A Random Forest is usually more stable and less sensitive to individual training records.

## Production trade-off

```
Need maximum interpretability→ Small controlled Decision TreeNeed stronger predictive stability→ Random ForestNeed both→ Use Random Forest with explanation tools,plus a simpler benchmark model
```

---

# 34. Production Failure Scenarios

## Scenario 1: Fully grown tree memorizes data

Symptoms:

```
Training Accuracy = 100%Testing Accuracy = 78%Very deep treeMany leaves with one sample
```

Solution:

```
Reduce max_depthIncrease min_samples_leafIncrease min_samples_splitUse pruningUse cross-validationCompare with Random Forest
```

---

## Scenario 2: Forest is too large

Configuration:

```
RandomForestClassifier(    n_estimators=10000)
```

Possible consequences:

```
Long training timeHigher memory useSlower deploymentLarge serialized model
```

Solution:

```
Measure learning curve against number of trees.Choose enough trees for stable performance,not the largest possible number.
```

---

## Scenario 3: Feature importance is misused

Bad conclusion:

```
Feature X has the highest importance,therefore it causes the outcome.
```

Correct conclusion:

```
The forest relied heavily on Feature Xfor impurity-reducing splits in this dataset.
```

Then verify using:

```
Domain knowledgePermutation importanceError analysisStability across foldsFairness review
```

---

## Scenario 4: Category codes create fake ordering

Suppose:

```
City:Delhi = 0Mumbai = 1Kolkata = 2
```

A tree can split:

```
City <= 0.5
```

This treats arbitrary codes as ordered.

Better:

```
Use OneHotEncoder for nominal categories,or use an appropriate categorical-data method.
```

---

# 35. Debugging Section

## Error 1: Missing imports

Broken:

```
model = RandomForestClassifier()
```

Error:

```
NameError:name 'RandomForestClassifier' is not defined
```

Fix:

```
from sklearn.ensemble import (    RandomForestClassifier)
```

---

## Error 2: Continuous target

Broken:

```
y = df["final_marks"]tree_model.fit(    X_train,    y_train)
```

Possible error:

```
ValueError:Unknown label type: continuous
```

Reason:

```
DecisionTreeClassifier expects class labels.
```

Fix:

```
y = df["placed"]
```

For continuous targets, use:

```
DecisionTreeRegressorRandomForestRegressor
```

---

## Error 3: Wrong `max_depth` type

Broken:

```
DecisionTreeClassifier(    max_depth="3")
```

Possible error:

```
InvalidParameterError
```

Fix:

```
DecisionTreeClassifier(    max_depth=3)
```

---

## Error 4: Text features

Broken:

```
branch = CSE / ECE / ME
```

Possible error:

```
ValueError:could not convert string to float
```

Fix:

```
Clean categoriesOne-hot encode nominal columnsTrain the tree on transformed numerical data
```

---

## Error 5: Assuming scaling is required

Unnecessary workflow:

```
StandardScaler()DecisionTreeClassifier()
```

This is not normally harmful, but it usually adds no benefit to threshold-based trees.

Senior habit:

```
Do not add preprocessing without a reason.
```

Scaling may still be needed when the same pipeline compares trees with KNN, SVM or Logistic Regression.

---

## Error 6: `feature_importances_` before fitting

Broken:

```
forest_model = RandomForestClassifier()print(    forest_model.feature_importances_)
```

Possible error:

```
AttributeError
```

Fix:

```
forest_model.fit(    X_train,    y_train)print(    forest_model.feature_importances_)
```

---

## Error 7: Wrong classification averaging

Broken multiclass code:

```
f1_score(    y_test,    y_pred)
```

Possible error:

```
ValueError:Target is multiclass but average='binary'
```

Fix:

```
f1_score(    y_test,    y_pred,    average="macro")
```

---

# 36. Common Beginner Mistakes

```
1. Allowing a tree to grow without constraints2. Choosing the model using training accuracy3. Assuming 100% training accuracy is ideal4. Scaling tree features unnecessarily5. Treating arbitrary category codes as ordered6. Reading feature importance as causation7. Ignoring per-class metrics8. Using one train-test split as final proof9. Assuming Random Forest can never overfit10. Using too many trees without measuring cost11. Forgetting random_state12. Including target inside X13. Ignoring class imbalance14. Using classifier models for continuous targets15. Selecting hyperparameters on the test set
```

---

# 37. Interview Questions

Prepare answers for:

```
1. What is a Decision Tree?2. What are root, internal and leaf nodes?3. How does a tree select a split?4. What is Gini impurity?5. What is Entropy?6. What is Information Gain?7. How can a Decision Tree overfit?8. What does max_depth control?9. What does min_samples_leaf control?10. What is pruning?11. What is Random Forest?12. What is bootstrap sampling?13. Why does Random Forest use random features?14. How does Random Forest make classification predictions?15. Why is Random Forest more stable than one tree?16. Do trees require feature scaling?17. What is feature importance?18. What is an out-of-bag score?19. Decision Tree vs Random Forest?20. When would you choose a single tree?
```

---

# 38. Interview Trap Questions

## Trap 1

**Does Random Forest always use majority voting?**

Strong answer:

```
It is commonly explained as voting, but scikit-learn's RandomForestClassifier predicts by averaging class probabilities across trees and selecting the class with the highest mean probability.
```

## Trap 2

**Does Random Forest completely eliminate overfitting?**

Strong answer:

```
No. It usually reduces variance compared with one tree, but it can still overfit because of noisy data, leakage, unsuitable hyperparameters or insufficient validation.
```

## Trap 3

**Should a Decision Tree always be fully grown?**

Strong answer:

```
No. Fully grown trees often overfit. Complexity should be controlled using parameters such as max_depth, min_samples_leaf, min_samples_split or pruning.
```

## Trap 4

**Are tree feature importances causal?**

Strong answer:

```
No. They reflect how the fitted model used features for splitting, not whether those features caused the target outcome.
```

## Trap 5

**Why do trees usually not need scaling?**

Strong answer:

```
Trees compare feature values with thresholds. Positive rescaling generally preserves their ordering, unlike distance-based models whose calculations depend directly on scale.
```

---

# 39. MCQs

### Q1. A leaf node contains:

A. Only raw data  
B. The final decision or prediction  
C. A scaler  
D. The train-test split

**Answer: B**

### Q2. Gini impurity is lowest when:

A. Classes are equally mixed  
B. The node contains one class  
C. The tree is deepest  
D. Features are scaled

**Answer: B**

### Q3. A very deep Decision Tree commonly risks:

A. Underfitting only  
B. Overfitting  
C. Missing all columns  
D. Becoming linear

**Answer: B**

### Q4. Random Forest builds:

A. One Logistic Regression model  
B. Multiple randomized trees  
C. One nearest-neighbor model  
D. One polynomial equation

**Answer: B**

### Q5. Which parameter controls the number of trees?

A. `max_depth`  
B. `n_estimators`  
C. `min_samples_leaf`  
D. `criterion`

**Answer: B**

---

# 40. Coding Assignment

Complete before moving to Slot 5:

```
Task 1:Load Iris.Task 2:Use stratified train-test split.Task 3:Train an unrestricted Decision Tree.Task 4:Print:Train AccuracyTest AccuracyDepthNumber of leavesTask 5:Train a controlled tree with:max_depth=3min_samples_split=4min_samples_leaf=2Task 6:Compare unrestricted and controlled trees.Task 7:Visualize the controlled tree.Task 8:Print the classification report.Task 9:Train RandomForestClassifier with 200 trees.Task 10:Compare tree and forest using:Train AccuracyTest AccuracyMacro PrecisionMacro RecallMacro F1Train-Test GapTask 11:Print feature importances.Task 12:Predict one new flower.Task 13:Try:max_depth = 1, 2, 3, 5, NoneTask 14:Explain which depths underfit or overfit.Task 15:Train a forest with oob_score=True.
```

---

# 41. Real-World Challenge

A loan-risk classifier gives:

|Model|Train Accuracy|Test Accuracy|Recall for Default|
|---|---|---|---|
|Tree depth=None|100%|76%|61%|
|Tree depth=4|88%|84%|78%|
|Random Forest|95%|89%|85%|

Answer:

```
1. Which model is most likely overfitting?2. Which tree appears better balanced?3. Which model gives the strongest test result?4. Why might Recall for Default matter?5. Should Random Forest automatically be deployed?6. What further checks are required?
```

Expected reasoning:

```
The unrestricted tree is overfitting.The depth-4 tree is better balanced.Random Forest has the strongest test performanceand highest default Recall.Before deployment, check:cross-validationclass imbalancethreshold selectionfairnessprobability calibrationdata leakagelatencymonitoring
```

---

# 42. Quick Revision Sheet

```
Decision Tree:Rule-based classifier using feature thresholds.Root:First node.Internal node:Intermediate decision.Leaf:Final prediction.Gini:Measures class impurity.Entropy:Measures class disorder.max_depth:Limits tree depth.min_samples_split:Minimum samples needed to split.min_samples_leaf:Minimum samples required in each leaf.Random Forest:Ensemble of randomized decision trees.Bootstrap:Sampling rows with replacement.Random feature selection:Different feature subsets considered at splits.Forest prediction:Average class probabilities across trees.Feature importance:Model-based contribution to impurity reduction.Scaling:Generally unnecessary for tree models.Main tree risk:Overfitting.Main forest benefit:Greater stability and lower variance.
```