# Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

The scenario selected for this task is a Student Attendance Checker.

The system contains private attendance information for three students:

- Alice: 85%
- Bob: 72%
- Charlie: 91%

The minimum attendance required for eligibility is 75%.

The same type of attendance-related request is handled using three different approaches: a plain chatbot, a rule-based workflow, and an AI agent.

---

## 2. Plain Chatbot

The plain chatbot uses a Large Language Model to respond to the user's questions. It does not have access to the private attendance database.

For example, when the user asks for Alice's attendance, the chatbot cannot retrieve the actual private value from the attendance data. Instead, it must explain that it does not have access to the private records.

The chatbot does not use any external tools or predefined decision rules. Its main component is the LLM.

The main limitation in this scenario is private-data access. Even though the chatbot can understand the user's question and produce a natural-language response, it cannot reliably retrieve the actual attendance information.

Therefore, a plain chatbot is useful for general questions but is limited when the task requires access to private or structured data.

---

## 3. Rule-Based Workflow

The rule-based workflow stores the attendance data directly in Python.

It uses predefined conditions to process the user's request. For example, the workflow checks whether the student exists in the attendance data, retrieves the attendance percentage, and compares it with the minimum attendance requirement of 75%.

If the attendance is greater than or equal to 75%, the student is considered eligible. Otherwise, the student is considered not eligible.

The workflow does not use an LLM. It follows fixed instructions and conditions.

The main advantage is reliability for the exact cases that have been programmed. The main limitation is flexibility. If the user asks a new type of question that was not included in the predefined rules, the workflow may not be able to handle it.

---

## 4. AI Agent

The AI agent combines an LLM with tools and a loop.

The private attendance data is accessed through Python tools. The agent receives the user's request, determines which tool is required, uses the tool to obtain the private information, and then uses the LLM to provide a natural-language response.

For example, when the user asks whether Bob is eligible, the agent can use the attendance lookup and eligibility tools. The tool retrieves Bob's attendance of 72% and checks it against the 75% minimum requirement.

The agent is more flexible because the LLM can understand natural-language requests while the tools provide access to reliable private data.

The agent still depends on the tools being correctly implemented. If a tool contains incorrect data or logic, the agent's result can also be affected.

---

## 5. Comparison Table

| Basis | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Flexibility | High for natural language but limited by lack of private data | Low because it follows fixed rules | High because the LLM can interpret requests and tools can perform actions |
| Decision-making | LLM generates responses | Predefined conditions | LLM selects appropriate tools and uses their results |
| Tool usage | No tools | No external AI tools | Uses Python tools |
| Private-data access | No | Yes, directly through programmed data | Yes, through tools |
| Multi-step task handling | Limited | Possible only if explicitly programmed | Can combine LLM reasoning and tools |
| Automation | Basic response generation | Strong for fixed tasks | Strong for flexible tasks |
| Reliability | Can be unreliable for private-data questions | Reliable for programmed cases | Reliable when tools and data are correctly implemented |

---

## 6. Suitability Analysis

For this student attendance scenario, the AI agent can handle natural-language questions while also accessing private attendance information through tools.

The plain chatbot is useful when the user only needs general information and private attendance data is not required.

The rule-based workflow is useful when the questions and required actions are predictable. For example, checking whether attendance is above 75% can be handled reliably using predefined conditions.

The AI agent is suitable when users may ask different attendance-related questions in natural language and the system needs access to private attendance information through tools. It combines the language understanding capability of an LLM with the reliability of programmatic tools.

The comparison shows that each approach has different characteristics. The appropriate choice depends on whether the task requires private data, flexible language understanding, fixed rules, or tool-based actions.

---

## 7. Conclusion

A plain chatbot mainly provides responses using an LLM and is appropriate for general conversational tasks where private data or external tools are not required.

A rule-based workflow follows predefined steps and conditions. It is appropriate for predictable tasks where the required logic can be clearly defined in advance.

An AI agent combines an LLM, tools, and a loop. It is appropriate for tasks where the system needs to understand natural-language requests, access information through tools, and perform multiple actions.

Therefore, the three approaches solve different types of problems. The choice depends on the requirements of the particular task, especially the need for flexibility, private-data access, tool usage, automation, and reliability.