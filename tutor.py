import os
from dotenv import load_dotenv
from llm_client import LLMClient
from intent_detection import detect_intent
from prompt_builder import build_messages

# Acts as the wrapper/main interface for the different functionality that is created in other files 
class PythonTutor:
    def __init__(self, model: str = "deepseek-ai/DeepSeek-V3.2"):
        load_dotenv()
        api_key = os.getenv("HF_API_KEY")
        if not api_key:
            raise RuntimeError("HF_API_KEY not set")
        self.client = LLMClient(api_key=api_key, model=model)

    # Takes in the user input and returns the AI response
    def respond(self, user_input: str) -> str:
        mode = detect_intent(user_input)
        messages = build_messages(mode, user_input)
        response = self.client.chat(messages)
        return response
