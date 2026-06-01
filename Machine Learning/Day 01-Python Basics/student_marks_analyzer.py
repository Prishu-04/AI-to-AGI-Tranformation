# Mini Project Building — Student Marks Analyzer
#importing libraries
import json

# Calculation of Average Marks
def cal_avg(students):
     tot_marks=0
     for stu in students:
          tot_marks+=stu["marks"]
     avg_marks=tot_marks/len(students)
     return avg_marks

# Calculation of Topper
def topper(students):
     top_stu=students[0]
     for stu in students:
          if stu["marks"]>top_stu["marks"]:
               top_stu=stu
     return top_stu

# Calculation of Number of Pass and Fail
def pass_fail(students):
     pass_count=0
     fail_count=0
     for stu in students:
          if(stu['marks']>=40):
               pass_count+=1
          else:
               fail_count+=1
     return pass_count, fail_count

# Assigning grades to students
def assign_grade(students):
     for stu in students:
          stu["grade"]=""
          if stu["marks"]>=90:
               stu["grade"]="O"
          elif stu["marks"]>=80:
               stu["grade"]="E"
          elif stu["marks"]>=70:
               stu["grade"]="A"
          elif stu["marks"]>=60:
               stu["grade"]="B"
          elif stu["marks"]>=50:
               stu["grade"]="C"
          elif stu["marks"]>=40:
               stu["grade"]="D"
          else:
               stu["grade"]="F"
     return students

# main function
students = []
n=int(input("Enter the number of students: "))
for i in range(0,n):
     name=input("Enter the name of student: ")
     subject=input("Enter the subject of student: ")
     marks=int(input("Enter the marks of student: "))
     while marks<0 or marks>100:
          print("Invalid marks! Please enter marks between 0 and 100.")
          marks=int(input("Enter the marks of student: "))
     stu={
          "name": name,
          "subject": subject,
          "marks": marks
     }
     students.append(stu)
print("Student Details:")
print(students)
assign_grade(students)

top_student = topper(students)
pass_count, fail_count = pass_fail(students)
avg_marks = cal_avg(students)

print("Student Report:")
print("Total students: ", len(students))
print("Average marks: ", avg_marks)
print("Topper: ", top_student["name"])
print("Topper Marks: ", top_student["marks"])
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)

print("\n Individual Student Details")

for stu in students:
     print(stu["name"], "-", stu["subject"], "-", stu["marks"], "-", stu["grade"])

report = {
     "students": students,
     "total_students": len(students),
     "average_marks": avg_marks,
     "topper": top_student,
     "pass_count": pass_count,
     "fail_count": fail_count
}

with open("student_report.json", "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4)

print("\nReport saved successfully in student_report.json")