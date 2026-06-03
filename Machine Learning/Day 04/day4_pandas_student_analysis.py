import pandas as pd


data = {
    "name": ["Rahul", "Aman", "Priya", "Sneha", "Karan", "Anjali", "Rohit"],
    "marks": [85, 72, 45, 91, 60, 88, 35],
    "attendance": [90, 80, 70, 95, 78, 92, 60],
    "study_hours": [5, 4, 3, 6, 2, 5, 1],
    "department": ["AI", "Data", "Web", "AI", "Data", "AI", "Web"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("-" * 40)

print("Dataset Info:")
df.info()

print("-" * 40)

print("Statistics:")
print(df.describe())

print("-" * 40)


def get_result(row):
    if row["marks"] >= 80 and row["attendance"] >= 85 and row["study_hours"] >= 5:
        return "Excellent"
    elif row["marks"] >= 50 and row["attendance"] >= 75:
        return "Good"
    else:
        return "Needs Improvement"


df["result"] = df.apply(get_result, axis=1)

print("DataFrame with Result:")
print(df)

print("-" * 40)

excellent_students = df[df["result"] == "Excellent"]
good_students = df[df["result"] == "Good"]
needs_improvement_students = df[df["result"] == "Needs Improvement"]

print("Excellent Students:")
print(excellent_students)

print("-" * 40)

print("Good Students:")
print(good_students)

print("-" * 40)

print("Needs Improvement Students:")
print(needs_improvement_students)

print("-" * 40)

sorted_by_marks = df.sort_values(by="marks", ascending=False)

print("Students Sorted by Marks:")
print(sorted_by_marks)

print("-" * 40)

print("Analytics Summary")
print("Average marks:", df["marks"].mean())
print("Highest marks:", df["marks"].max())
print("Lowest marks:", df["marks"].min())
print("Average attendance:", df["attendance"].mean())
print("Average study hours:", df["study_hours"].mean())

print("-" * 40)

print("Result Counts:")
print(df["result"].value_counts())

print("-" * 40)

print("Department Counts:")
print(df["department"].value_counts())

df.to_csv("day4_student_analysis_report.csv", index=False)

print("-" * 40)
print("Report saved as day4_student_analysis_report.csv")