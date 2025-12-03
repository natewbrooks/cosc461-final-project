from intent_detection import TutorMode

# The message that tells the AI how to respond and what its core responsbility is
BASE_SYSTEM_PROMPT = """
You are a friendly but rigorous Python tutor for absolute beginners.
You always respond in the following sections, in this exact order:

Concept Explanation:
[plain-language explanation]

Code Example:
[short Python example, or "None"]

Practice Exercise:
[a simple exercise, or "None"]

Feedback:
[feedback on user's code if they provided code; otherwise a short motivational tip]

Constraints:
- Use only Python concepts appropriate for an introductory course.
- Keep examples under 15 lines.
- Use clear variable names.
"""

# Insert additional context for the users request based off the provided tutor mode enum so the AI can give a more informed answer
def build_messages(mode: TutorMode, user_input: str):
    if mode == TutorMode.EXPLAIN:
        user_prompt = f"Explain this Python concept for a beginner and follow the required format strictly:\n\n{user_input}"
    elif mode == TutorMode.DEBUG:
        user_prompt = f"A beginner has written this code and it is not working. Explain the error and how to fix it, then give one small exercise:\n\n{user_input}"
    elif mode == TutorMode.EXERCISE_REQUEST:
        user_prompt = f"Generate one beginner-level exercise for Python, then provide a sample solution only in the Feedback section. Use the requested topic if present:\n\n{user_input}"
    elif mode == TutorMode.EXERCISE_ANSWER:
        user_prompt = f"Evaluate the following solution from a beginner to a Python exercise. Explain what is correct, what is wrong, and how to improve it, using the required format:\n\n{user_input}"
    else:
        user_prompt = f"The user is asking a general Python beginner question. Respond as a tutor using the required format:\n\n{user_input}"

    messages = [
        {"role": "system", "content": BASE_SYSTEM_PROMPT.strip()},
        {"role": "user", "content": user_prompt.strip()},
    ]
    return messages
