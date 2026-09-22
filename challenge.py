from tools import get_attendance, check_eligibility

print("=== CHALLENGE ===")

students = ["alice", "bob", "charlie"]

for student in students:
    attendance = get_attendance(student)

    print(
        f"{student.title()}: "
        f"{attendance['attendance']}%"
    )

print("\nEligibility:")

for student in students:
    result = check_eligibility(student)

    status = "Eligible" if result["eligible"] else "Not Eligible"

    print(f"{student.title()}: {status}")