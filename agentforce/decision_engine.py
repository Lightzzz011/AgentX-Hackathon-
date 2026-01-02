from agentforce.classifier import classify_message
from salesforce.actions import create_case


def process_complaint(message: str):
    classification = classify_message(message)

    if classification == "QUESTION":
        return {
            "action": "ANSWERED",
            "reply": "Resolved instantly by AgentForce."
        }

    if classification == "URGENT_ISSUE":
        case = create_case(priority="HIGH", escalate=True)
        return {
            "action": "CASE_CREATED_AND_ESCALATED",
            "reply": "Critical issue detected. Case created and escalated.",
            **case
        }

    case = create_case(priority="MEDIUM", escalate=False)
    return {
        "action": "CASE_CREATED",
        "reply": "Issue logged. Support team will respond shortly.",
        **case
    }
