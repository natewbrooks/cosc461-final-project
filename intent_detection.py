from enum import Enum

class TutorMode(str, Enum):
    EXPLAIN = "explain"
    DEBUG = "debug"
    EXERCISE_REQUEST = "exercise_request"
    EXERCISE_ANSWER = "exercise_answer"
    GENERAL = "general"

# Detects the intent of the users input and returns the corresponding TutorMode Enum 
def detect_intent(user_input: str) -> TutorMode:
    text = user_input.lower()
    if "explain" in text or "what is" in text or "how does" in text:
        return TutorMode.EXPLAIN
    if "exercise" in text or "practice" in text or "give me a problem" in text:
        return TutorMode.EXERCISE_REQUEST
    if "def " in text or "for " in text or "while " in text or "traceback" in text:
        if "my answer is" in text or "here is my solution" in text:
            return TutorMode.EXERCISE_ANSWER
        return TutorMode.DEBUG
    return TutorMode.GENERAL
