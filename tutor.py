from llm_client import LLMClient
from intent_detection import detect_intent
from prompt_builder import build_messages

class PythonTutor:
    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        self.client = LLMClient(api_key=api_key, model=model)

    def respond(self, user_input: str) -> str:
        mode = detect_intent(user_input)
        messages = build_messages(mode, user_input)
        response = self.client.chat(messages)
        return response
