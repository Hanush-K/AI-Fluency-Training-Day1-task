from openai import OpenAI
from config import GROQ_API_KEY, MODEL

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

print("=== PLAIN CHATBOT ===")
print("Ask about student attendance.")
print("Type 'exit' to stop.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": """
You are a helpful college assistant.

You do NOT have access to private attendance records.
Do not pretend that you know private student attendance.
If asked about a student's attendance, explain that
you do not have access to the private database.
"""
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    print("\nBot:", response.choices[0].message.content)