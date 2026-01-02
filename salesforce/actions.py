import uuid


def create_case(priority="MEDIUM", escalate=False):
    return {
        "case_id": f"SF-CASE-{uuid.uuid4().hex[:6].upper()}",
        "priority": priority,
        "status": "OPEN",
        "escalated": escalate
    }
