import numpy as np

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"

def check_result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"

# main program
students = ["Pratyaksh", "Rahul", "Sneha", "Aman", "Priya"]
marks = np.array([
	[85, 90, 78],
    [70, 88, 92],
    [35, 40, 45],
    [95, 92, 88],
    [60, 75, 80]])
try:
    totals = np.sum(marks, axis=1)
    averages = np.mean(marks, axis=1)

    topper_index = np.argmax(totals)
    topper_name = students[topper_index]
    topper_marks = totals[topper_index]

    print("========== Student Marks Analyzer ==========\n")

    report = "========== Student Marks Analyzer ==========\n\n"

    for i in range(len(students)):
        grade = calculate_grade(averages[i])
        result = check_result(averages[i])

        print("Student Name:", students[i])
        print("Marks:", marks[i])
        print("Total Marks:", totals[i])
        print("Average Marks:", round(averages[i], 2))
        print("Grade:", grade)
        print("Result:", result)
        print("----------------------------------")

        report += "Student Name: " + students[i] + "\n"
        report += "Marks: " + str(marks[i]) + "\n"
        report += "Total Marks: " + str(totals[i]) + "\n"
        report += "Average Marks: " + str(round(averages[i], 2)) + "\n"
        report += "Grade: " + grade + "\n"
        report += "Result: " + result + "\n"
        report += "----------------------------------\n"

    print("\nClass Topper:", topper_name)
    print("Topper Total Marks:", topper_marks)

    report += "\nClass Topper: " + topper_name + "\n"
    report += "Topper Total Marks: " + str(topper_marks) + "\n"

    with open("student_marks_report.txt", "w") as file:
        file.write(report)

    print("\nReport saved successfully as student_marks_report.txt")

except Exception as e:
    print("An error occurred:", e)