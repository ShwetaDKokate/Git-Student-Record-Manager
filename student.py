import json
import os

FILE = "data/students.json"

class StudentManager:

    def __init__(self):
        if not os.path.exists(FILE):
            with open(FILE, "w") as f:
                json.dump([], f)

    def load(self):
        with open(FILE, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(FILE, "w") as f:
            json.dump(data, f, indent=4)

    def add_student(self):
        students = self.load()

        roll = input("Roll No: ")
        name = input("Name: ")
        dept = input("Department: ")

        students.append({
            "roll": roll,
            "name": name,
            "department": dept
        })

        self.save(students)
        print("Student Added Successfully.")

    def view_students():
        students = StudentManager().load()

        if not students:
            print("No Records Found")
            return

        for s in students:
            print(s["roll"], s["name"], s["department"])

    def search_student(self):
        roll = input("Enter Roll No: ")

        for s in self.load():
            if s["roll"] == roll:
                print(s)
                return

        print("Student Not Found")

    def delete_student(self):
        roll = input("Enter Roll No: ")

        students = self.load()

        updated = [s for s in students if s["roll"] != roll]

        self.save(updated)

        print("Student Deleted")