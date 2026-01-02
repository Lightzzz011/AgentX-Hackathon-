from fastapi import FastAPI
from models.schemas import ComplaintRequest, AgentResponse
from agentforce.decision_engine import process_complaint

app = FastAPI(title="AgentX – AgentForce Service Automation")


@app.post("/complaint", response_model=AgentResponse)
def handle_complaint(data: ComplaintRequest):
    return process_complaint(data.message)
