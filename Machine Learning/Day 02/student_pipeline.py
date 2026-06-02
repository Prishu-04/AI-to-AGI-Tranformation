import csv
import json
from pathlib import Path


class StudentRecord:
    def __init__(self, name, marks, attendance, study_hours):
        self.name = name
        self.marks = marks
        self.attendance = attendance
        self.study_hours = study_hours

    def is_valid(self):
        if self.marks < 0 or self.marks > 100:
            return False

        if self.attendance < 0 or self.attendance > 100:
            return False

        if self.study_hours < 0:
            return False

        return True

    def predict_performance(self):
        if self.marks >= 80 and self.attendance >= 85 and self.study_hours >= 5:
            return "Excellent"
        elif self.marks >= 50 and self.attendance >= 75:
            return "Good"
        else:
            return "Needs Improvement"

    def to_dictionary(self):
        return {
            "name": self.name,
            "marks": self.marks,
            "attendance": self.attendance,
            "study_hours": self.study_hours,
            "prediction": self.predict_performance()
        }


class StudentPipeline:
    def __init__(self, students):
        self.students = students
        self.clean_students = []
        self.invalid_students = []

    def clean_data(self):
        for student in self.students:
            if student.is_valid():
                self.clean_students.append(student)
            else:
                self.invalid_students.append(student)

    def count_predictions(self):
        counts = {
            "Excellent": 0,
            "Good": 0,
            "Needs Improvement": 0
        }

        for student in self.clean_students:
            prediction = student.predict_performance()
            counts[prediction] += 1

        return counts

    def save_clean_data(self, filename):
        fieldnames = ["name", "marks", "attendance", "study_hours", "prediction"]

        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for student in self.clean_students:
                writer.writerow(student.to_dictionary())

    def save_report(self, filename):
        report = {
            "project_name": "Reusable OOP Student Pipeline",
            "total_students": len(self.students),
            "valid_students": len(self.clean_students),
            "invalid_students": len(self.invalid_students),
            "prediction_counts": self.count_predictions()
        }

        with open(filename, "w") as file:
            json.dump(report, file, indent=4)

    def show_summary(self):
        print("Student Pipeline Summary")
        print(f"Total students: {len(self.students)}")
        print(f"Valid students: {len(self.clean_students)}")
        print(f"Invalid students: {len(self.invalid_students)}")
        print(f"Prediction counts: {self.count_predictions()}")


def main():
    data_folder = Path("data")
    reports_folder = Path("reports")

    data_folder.mkdir(exist_ok=True)
    reports_folder.mkdir(exist_ok=True)

    students = [
        StudentRecord("Rahul", 85, 90, 5.5),
        StudentRecord("Aman", 45, 70, 3),
        StudentRecord("Priya", 72, 80, 4),
        StudentRecord("Sneha", 92, 95, 6),
        StudentRecord("Rohit", 120, 80, 4),
        StudentRecord("Neha", 66, -10, 3.5),
        StudentRecord("Karan", 58, 78, 2.5),
        StudentRecord("Anjali", 91, 89, 5.2)
    ]

    pipeline = StudentPipeline(students)

    pipeline.clean_data()
    pipeline.save_clean_data(data_folder / "clean_students.csv")
    pipeline.save_report(reports_folder / "summary_report.json")
    pipeline.show_summary()


if __name__ == "__main__":
    main()