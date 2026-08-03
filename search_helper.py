def search_by_department(students, department):
    result = []

    for student in students:
        if student["department"].lower() == department.lower():
            result.append(student)

    return result