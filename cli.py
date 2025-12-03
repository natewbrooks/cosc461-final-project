import os
from tutor import PythonTutor

def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")
    tutor = PythonTutor(api_key=api_key)

    print("Python Tutor. Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in {"quit", "exit"}:
            break
        answer = tutor.respond(user_input)
        print("\nTutor:\n")
        print(answer)
        print("\n" + "-" * 60 + "\n")

if __name__ == "__main__":
    main()
