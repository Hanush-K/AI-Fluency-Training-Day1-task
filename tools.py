attendance = {
    "alice": 85,
    "bob": 72,
    "charlie": 91
}

MINIMUM_ATTENDANCE = 75


def get_attendance(student_name):
    student_name = student_name.lower()

    if student_name in attendance:
        return {
            "student": student_name,
            "attendance": attendance[student_name]
        }

    return {
        "error": "Student not found"
    }


def check_eligibility(student_name):
    result = get_attendance(student_name)

    if "error" in result:
        return result

    percentage = result["attendance"]

    return {
        "student": student_name,
        "attendance": percentage,
        "eligible": percentage >= MINIMUM_ATTENDANCE
    }


def calculate_difference(student1, student2):
    result1 = get_attendance(student1)
    result2 = get_attendance(student2)

    if "error" in result1:
        return result1

    if "error" in result2:
        return result2

    difference = abs(
        result1["attendance"] - result2["attendance"]
    )

    return {
        "student1": student1,
        "student2": student2,
        "difference": difference
    }