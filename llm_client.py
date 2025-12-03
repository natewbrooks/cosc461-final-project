from huggingface_hub import InferenceClient

# Handles the connection to the HF LLM
# Sends and recieves messages from it
class LLMClient:
    def __init__(self, api_key: str, model: str = "deepseek-ai/DeepSeek-V3.2"):
        self.model = f"{model}:novita" if model == "deepseek-ai/DeepSeek-V3.2" else model
        self.client = InferenceClient(
            api_key=api_key, 
        )

    def chat(self, messages, max_tokens: int = 512) -> str:
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=max_tokens,
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Error communicating with LLM: {e}"