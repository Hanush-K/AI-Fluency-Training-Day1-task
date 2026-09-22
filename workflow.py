attendance = {
    "alice": 85,
    "bob": 72,
    "charlie": 91
}

MINIMUM_ATTENDANCE = 75

print("=== RULE-BASED WORKFLOW ===")
print("Ask about Alice, Bob, or Charlie.")
print("Type 'exit' to stop.")


while True:
    name = input("\nEnter student name: ").lower()

    if name == "exit":
        break

    if name in attendance:
        percentage = attendance[name]

        print(f"Attendance: {percentage}%")

        if percentage >= MINIMUM_ATTENDANCE:
            print("Status: Eligible")
        else:
            print("Status: Not Eligible")

    else:
        print("Student not found.")