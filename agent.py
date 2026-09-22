from openai import OpenAI
from config import GROQ_API_KEY, MODEL
from tools import (
    get_attendance,
    check_eligibility,
    calculate_difference
)

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


def run_agent(question):

    question_lower = question.lower()

    # Tool selection
    if "attendance" in question_lower:
        words = question_lower.split()

        for name in ["alice", "bob", "charlie"]:
            if name in words:
                result = get_attendance(name)
                break
        else:
            result = {"error": "Student name not found"}

    elif "eligible" in question_lower:
        words = question_lower.split()

        for name in ["alice", "bob", "charlie"]:
            if name in words:
                result = check_eligibility(name)
                break
        else:
            result = {"error": "Student name not found"}

    elif "difference" in question_lower:
        result = calculate_difference("alice", "bob")

    else:
        result = {
            "message": "I could not determine which attendance tool to use."
        }

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": """
You are a college attendance AI agent.

You have access to private attendance data through tools.
Explain the tool result clearly.
Do not invent attendance values.
"""
            },
            {
                "role": "user",
                "content": question
            },
            {
                "role": "system",
                "content": f"Tool result: {result}"
            }
        ]
    )

    return response.choices[0].message.content


print("=== AI AGENT ===")
print("Ask an attendance question.")
print("Type 'exit' to stop.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    answer = run_agent(question)

    print("\nAgent:", answer)