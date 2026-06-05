# Build Visual EDA Project

## 1. Project Goal

Create:

```
day6_visual_eda_project.py
```

The project will answer:

```
1. How many employees belong to each department?2. Which department has the highest average salary?3. How are employee salaries distributed?4. How does salary differ across employee levels?5. Is salary related to experience?6. Which numeric features have strong correlations?7. Who is the highest-paid employee?
```

---

## 2. Project Structure

Your folder should look like this after running the project:

```
day6_visual_eda_project/│├── day6_visual_eda_project.py│└── outputs/    ├── plots/    │   ├── employee_count_by_department.png    │   ├── average_salary_by_department.png    │   ├── salary_distribution.png    │   ├── salary_by_level_boxplot.png    │   ├── experience_vs_salary.png    │   └── correlation_heatmap.png    │    └── reports/        ├── employee_dataset.csv        ├── department_summary.csv        ├── level_summary.csv        ├── correlation_matrix.csv        └── eda_insights.txt
```

---

# 3. Visual EDA Workflow

Follow this order in every visual-EDA project:

```
Step 1: Load or create datasetStep 2: Inspect rows, columns, data types, and null valuesStep 3: Calculate numerical and categorical summariesStep 4: Analyze category countsStep 5: Analyze numeric distributionsStep 6: Compare categoriesStep 7: Analyze relationships between featuresStep 8: Calculate correlationsStep 9: Write observationsStep 10: Save plots and reports
```

---

# 4. Charts Used in This Project

|Chart|Question answered|
|---|---|
|Count plot|How many employees are in each department?|
|Bar chart|Which department has the highest average salary?|
|Histogram|How are salaries distributed?|
|Box plot|How does salary vary across employee levels?|
|Scatter plot|Is salary related to experience?|
|Heatmap|How strongly are numeric features related?|

A Seaborn count plot displays observation counts across categorical groups. A histogram represents the distribution of numerical data, while a box plot helps compare quantitative distributions across category levels. A heatmap displays rectangular values as a color-encoded matrix.

---

# 5. Complete Visual EDA Project Code

```
from pathlib import Pathimport pandas as pdimport matplotlib.pyplot as pltimport seaborn as sns# --------------------------------------------------# 1. Create Output Folders# --------------------------------------------------OUTPUT_DIR = Path("outputs")PLOTS_DIR = OUTPUT_DIR / "plots"REPORTS_DIR = OUTPUT_DIR / "reports"PLOTS_DIR.mkdir(parents=True, exist_ok=True)REPORTS_DIR.mkdir(parents=True, exist_ok=True)# --------------------------------------------------# 2. Create Employee Dataset# --------------------------------------------------data = {    "employee_id": [        101, 102, 103, 104, 105,        106, 107, 108, 109, 110,        111, 112, 113, 114, 115    ],    "name": [        "Amit", "Riya", "Karan", "Neha", "Vikas",        "Anjali", "Rohit", "Priya", "Rahul", "Sneha",        "Arjun", "Meera", "Dev", "Pooja", "Varun"    ],    "salary": [        28000, 45000, 80000, 120000, 36000,        70000, 30000, 95000, 55000, 42000,        65000, 105000, 50000, 75000, 33000    ],    "experience": [        1, 3, 6, 9, 2,        5, 1, 7, 4, 2,        5, 8, 3, 6, 2    ],    "rating": [        3, 4, 5, 5, 2,        4, 3, 5, 4, 3,        4, 5, 4, 4, 3    ],    "department": [        "HR", "IT", "AI", "AI", "SALES",        "DATA", "IT", "DATA", "WEB", "HR",        "WEB", "AI", "DATA", "IT", "SALES"    ],    "level": [        "Junior", "Mid-Level", "Senior", "Senior", "Junior",        "Senior", "Junior", "Senior", "Mid-Level", "Mid-Level",        "Mid-Level", "Senior", "Mid-Level", "Senior", "Junior"    ]}df = pd.DataFrame(data)# --------------------------------------------------# 3. Inspect Dataset# --------------------------------------------------print("Employee Dataset:")print(df)print("-" * 50)print("First 5 Rows:")print(df.head())print("-" * 50)print("Dataset Shape:")print(df.shape)print("-" * 50)print("Columns:")print(df.columns)print("-" * 50)print("Data Types:")print(df.dtypes)print("-" * 50)print("Missing Values:")print(df.isnull().sum())print("-" * 50)print("Statistical Summary:")print(df.describe())# --------------------------------------------------# 4. Create Summary Tables# --------------------------------------------------department_summary = (    df.groupby("department")    .agg(        employee_count=("employee_id", "count"),        average_salary=("salary", "mean"),        highest_salary=("salary", "max"),        lowest_salary=("salary", "min"),        average_experience=("experience", "mean"),        average_rating=("rating", "mean")    )    .reset_index()    .sort_values(by="average_salary", ascending=False))level_summary = (    df.groupby("level")    .agg(        employee_count=("employee_id", "count"),        average_salary=("salary", "mean"),        highest_salary=("salary", "max"),        average_experience=("experience", "mean"),        average_rating=("rating", "mean")    )    .reset_index()    .sort_values(by="average_salary", ascending=False))numeric_columns = df[["salary", "experience", "rating"]]correlation_matrix = numeric_columns.corr()print("-" * 50)print("Department Summary:")print(department_summary)print("-" * 50)print("Level Summary:")print(level_summary)print("-" * 50)print("Correlation Matrix:")print(correlation_matrix)# --------------------------------------------------# 5. Save Reports# --------------------------------------------------df.to_csv(    REPORTS_DIR / "employee_dataset.csv",    index=False)department_summary.to_csv(    REPORTS_DIR / "department_summary.csv",    index=False)level_summary.to_csv(    REPORTS_DIR / "level_summary.csv",    index=False)correlation_matrix.to_csv(    REPORTS_DIR / "correlation_matrix.csv")# --------------------------------------------------# 6. Employee Count by Department# --------------------------------------------------plt.figure(figsize=(9, 5))sns.countplot(    data=df,    x="department",    order=df["department"].value_counts().index)plt.title("Employee Count by Department")plt.xlabel("Department")plt.ylabel("Employee Count")plt.tight_layout()plt.savefig(    PLOTS_DIR / "employee_count_by_department.png",    dpi=300)plt.close()# --------------------------------------------------# 7. Average Salary by Department# --------------------------------------------------plt.figure(figsize=(9, 5))plt.bar(    department_summary["department"],    department_summary["average_salary"])plt.title("Average Salary by Department")plt.xlabel("Department")plt.ylabel("Average Salary")plt.xticks(rotation=45)plt.tight_layout()plt.savefig(    PLOTS_DIR / "average_salary_by_department.png",    dpi=300)plt.close()# --------------------------------------------------# 8. Salary Distribution# --------------------------------------------------plt.figure(figsize=(9, 5))sns.histplot(    data=df,    x="salary",    bins=6,    kde=True)plt.title("Employee Salary Distribution")plt.xlabel("Salary")plt.ylabel("Employee Count")plt.tight_layout()plt.savefig(    PLOTS_DIR / "salary_distribution.png",    dpi=300)plt.close()# --------------------------------------------------# 9. Salary Distribution by Employee Level# --------------------------------------------------plt.figure(figsize=(9, 5))sns.boxplot(    data=df,    x="level",    y="salary")plt.title("Salary Distribution by Employee Level")plt.xlabel("Employee Level")plt.ylabel("Salary")plt.tight_layout()plt.savefig(    PLOTS_DIR / "salary_by_level_boxplot.png",    dpi=300)plt.close()# --------------------------------------------------# 10. Experience vs Salary Scatter Plot# --------------------------------------------------plt.figure(figsize=(9, 5))sns.scatterplot(    data=df,    x="experience",    y="salary",    hue="level",    size="rating")plt.title("Experience vs Salary by Level and Rating")plt.xlabel("Years of Experience")plt.ylabel("Salary")plt.tight_layout()plt.savefig(    PLOTS_DIR / "experience_vs_salary.png",    dpi=300)plt.close()# --------------------------------------------------# 11. Correlation Heatmap# --------------------------------------------------plt.figure(figsize=(7, 5))sns.heatmap(    correlation_matrix,    annot=True)plt.title("Employee Feature Correlation Heatmap")plt.tight_layout()plt.savefig(    PLOTS_DIR / "correlation_heatmap.png",    dpi=300)plt.close()# --------------------------------------------------# 12. Generate EDA Insights# --------------------------------------------------highest_paid_employee = df.loc[df["salary"].idxmax()]highest_average_salary_department = department_summary.iloc[0]salary_experience_correlation = correlation_matrix.loc[    "salary",    "experience"]insights = f"""EMPLOYEE VISUAL EDA INSIGHTS========================================Total Employees:{len(df)}Highest-Paid Employee:Name: {highest_paid_employee["name"]}Salary: {highest_paid_employee["salary"]}Department: {highest_paid_employee["department"]}Level: {highest_paid_employee["level"]}Department with Highest Average Salary:Department: {highest_average_salary_department["department"]}Average Salary: {highest_average_salary_department["average_salary"]:.2f}Salary and Experience Correlation:{salary_experience_correlation:.3f}General Observations:- Senior employees generally have higher salaries.- Salary generally increases with experience.- AI has the highest average salary in this dataset.- Salary and experience have a strong positive relationship."""with open(    REPORTS_DIR / "eda_insights.txt",    "w",    encoding="utf-8") as file:    file.write(insights)print("-" * 50)print(insights)print("Visual EDA project completed successfully.")print(f"Plots saved inside: {PLOTS_DIR}")print(f"Reports saved inside: {REPORTS_DIR}")
```

---

# 6. What the Project Creates

## Plot Files

```
employee_count_by_department.pngaverage_salary_by_department.pngsalary_distribution.pngsalary_by_level_boxplot.pngexperience_vs_salary.pngcorrelation_heatmap.png
```

## Report Files

```
employee_dataset.csvdepartment_summary.csvlevel_summary.csvcorrelation_matrix.csveda_insights.txt
```

`savefig()` saves the current Matplotlib figure as an image or vector graphic. Closing each completed figure is useful when generating several plots because Matplotlib otherwise keeps references to figures created through `pyplot`.# 8. Important Project Concepts

## `Path.mkdir()`

```
PLOTS_DIR.mkdir(parents=True, exist_ok=True)
```

Creates the output folders automatically.

```
parents=TrueCreates missing parent folders.exist_ok=TrueDoes not raise an error if the folder already exists.
```

---

## `groupby()` and `agg()`

```
df.groupby("department").agg(...)
```

Groups employees by department and calculates multiple summary values. Pandas describes groupby operations as splitting data into groups, applying functions, and combining the results.

---

## `idxmax()`

```
df["salary"].idxmax()
```

Returns the index position containing the highest salary.

Then:

```
df.loc[df["salary"].idxmax()]
```

Returns the complete row of the highest-paid employee.

---

## Correlation

```
df[["salary", "experience", "rating"]].corr()
```

Calculates pairwise correlations between the selected numeric columns while excluding missing values.

# 10. Interview Questions

1. What is visual EDA?
2. What steps are followed in a visual-EDA workflow?
3. Why do we create summary tables before plots?
4. Why do we create separate output folders?
5. What does `Path.mkdir()` do?
6. Why do we use `plt.figure()` for every plot?
7. Why do we use `plt.close()` after saving?
8. What does a count plot show?
9. What does a histogram show?
10. What information does a box plot provide?
11. What does a scatter plot show?
12. What does a correlation heatmap show?
13. Why should only numeric columns be used for correlation?
14. What does `idxmax()` return?
15. Why should an EDA project include written observations?
16. What is the difference between correlation and causation?
17. How can this project help before ML model training?