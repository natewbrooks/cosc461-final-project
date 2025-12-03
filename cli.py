import os
from dotenv import load_dotenv
from tutor import PythonTutor

# Handles the CLI, continuously prompting the user for input until they quit or exit the program
def main():
    load_dotenv()
    api_key = os.getenv("HF_API_KEY")
    if not api_key:
        raise RuntimeError("HF_API_KEY not set")
    tutor = PythonTutor()

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
