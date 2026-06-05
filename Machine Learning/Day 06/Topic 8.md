# Debugging Matplotlib and Seaborn Errors
## 1. Most Common Visualization Errors

|Problem|Common reason|
|---|---|
|`ModuleNotFoundError`|Matplotlib or Seaborn is not installed|
|`NameError`|Forgot to import `plt` or `sns`|
|`KeyError`|Wrong Pandas column name|
|`ValueError: Could not interpret value`|Seaborn column does not exist|
|Shape mismatch|x and y contain different numbers of values|
|Heatmap error|Correlation includes non-numeric columns|
|Blank saved image|`savefig()` called after `show()`|
|Plots overlap|Previous figure was not closed|
|Labels are cut off|Layout or figure size is too small|
|Memory warning|Too many figures remain open|

---

# 2. Error 1 — Library Not Installed

## Broken code

```
import seaborn as sns
```

Possible error:

```
ModuleNotFoundError: No module named 'seaborn'
```

## Fix

Run in the terminal:

```
pip install matplotlib seaborn pandas
```

Then verify:

```
import pandas as pdimport matplotlib.pyplot as pltimport seaborn as snsprint("Libraries imported successfully.")
```

---

# 3. Error 2 — `plt` or `sns` Is Not Defined

## Broken code

```
plt.figure(figsize=(8, 5))sns.countplot(data=df, x="department")
```

Possible errors:

```
NameError: name 'plt' is not definedNameError: name 'sns' is not defined
```

## Fix

```
import matplotlib.pyplot as pltimport seaborn as sns
```

---

# 4. Error 3 — Wrong Column Name

## Broken code

```
sns.scatterplot(    data=df,    x="experiences",    y="salary")
```

Your actual column is:

```
experience
```

Possible error:

```
ValueError: Could not interpret value `experiences`
```

## Debug

```
print(df.columns)
```

## Fix

```
sns.scatterplot(    data=df,    x="experience",    y="salary")
```

Seaborn can access variables by their column names when a long-form DataFrame is passed using `data=df`.

---

# 5. Error 4 — x and y Have Different Lengths

## Broken code

```
names = ["Amit", "Riya", "Karan"]salary = [28000, 45000]plt.bar(names, salary)plt.show()
```

Possible error:

```
ValueError: shape mismatch
```

## Fix

```
names = ["Amit", "Riya", "Karan"]salary = [28000, 45000, 80000]plt.bar(names, salary)plt.show()
```

Always verify:

```
print(len(names))print(len(salary))
```

---

# 6. Error 5 — Heatmap Includes Text Columns

## Risky code

```
correlation_matrix = df.corr()
```

The DataFrame contains text columns such as:

```
namedepartmentlevel
```

## Fix

Select numeric columns:

```
numeric_columns = df[    ["salary", "experience", "rating"]]correlation_matrix = numeric_columns.corr()sns.heatmap(    correlation_matrix,    annot=True)plt.show()
```

A Seaborn heatmap expects rectangular data, while a correlation matrix should be created from the numerical features being analyzed.

---

# 7. Error 6 — Blank Saved Image

## Wrong order

```
plt.plot(df["experience"], df["salary"])plt.show()plt.savefig("experience_salary.png")
```

The saved image may be blank because a blocking `show()` closes and unregisters the figure before the later `savefig()` call.

## Correct order

```
plt.plot(df["experience"], df["salary"])plt.savefig("experience_salary.png")plt.show()
```

Better object-oriented version:

```
fig, ax = plt.subplots(figsize=(8, 5))ax.plot(df["experience"], df["salary"])ax.set_title("Experience vs Salary")ax.set_xlabel("Experience")ax.set_ylabel("Salary")fig.savefig("experience_salary.png")plt.show()
```

`plt.subplots()` conveniently creates a figure and its axes together.

---

# 8. Error 7 — Multiple Plots Overlap

## Broken code

```
sns.histplot(data=df, x="salary")sns.boxplot(data=df, x="level", y="salary")plt.show()
```

Both plots may appear on the same active figure.

## Fix

Create and close each figure separately:

```
plt.figure(figsize=(8, 5))sns.histplot(data=df, x="salary")plt.title("Salary Distribution")plt.savefig("salary_distribution.png")plt.close()plt.figure(figsize=(8, 5))sns.boxplot(data=df, x="level", y="salary")plt.title("Salary by Level")plt.savefig("salary_by_level.png")plt.close()
```

Matplotlib keeps references to figures created with `pyplot`; explicitly closing completed figures releases them from `pyplot`.

---

# 9. Error 8 — Labels Are Cut Off or Overlap

## Problem

Long department names, rotated labels, legends, or titles may be cut off.

## Fix

```
plt.figure(figsize=(10, 5))sns.countplot(    data=df,    x="department")plt.xticks(rotation=45)plt.tight_layout()plt.savefig("department_count.png")plt.show()
```

`tight_layout()` adjusts padding between and around plot elements to reduce overlap.

---

# 10. Error 9 — Wrong Plot for the Data

## Wrong choice

```
sns.countplot(    data=df,    x="salary")
```

This creates a separate bar for nearly every salary value.

## Better choice

```
sns.histplot(    data=df,    x="salary",    bins=6)
```

A count plot shows counts across categorical groups, while a histogram shows how numerical observations fall into value ranges or bins.

Use:

|Data question|Suitable plot|
|---|---|
|Count employees by department|`countplot()`|
|Salary distribution|`histplot()`|
|Salary across levels|`boxplot()`|
|Experience vs salary|`scatterplot()`|
|Numeric correlations|`heatmap()`|

---

# 11. Error 10 — Too Much Information in Scatter Plot

## Difficult-to-read plot

```
sns.scatterplot(    data=df,    x="experience",    y="salary",    hue="department",    size="rating",    style="level")
```

Seaborn supports `hue`, `size`, and `style` to represent additional variables, but using too many visual dimensions can make a chart difficult to interpret.

## Simpler version

```
sns.scatterplot(    data=df,    x="experience",    y="salary",    hue="level")
```

Only add extra dimensions when they help answer a specific question.