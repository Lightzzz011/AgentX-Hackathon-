URGENT_KEYWORDS = [
    "urgent", "immediately", "down", "not working",
    "losing money", "critical", "emergency"
]

QUESTION_KEYWORDS = [
    "how", "what", "when", "where", "can i", "do i"
]


def classify_message(message: str):
    text = message.lower()

    if any(word in text for word in URGENT_KEYWORDS):
        return "URGENT_ISSUE"

    if any(word in text for word in QUESTION_KEYWORDS):
        return "QUESTION"

    return "NORMAL_ISSUE"
