from fastapi import FastAPI

app_v1 = FastAPI(title="CQA Call Data API")


@app_v1.get("/get_transcript")
def get_transcript(call_id: str):
    """Retrieve the full transcript of a sales call by its unique call ID.
    Returns the transcript as a list of timestamped speaker turns.
    Use this when you need to read or analyze what was said during a specific call."""
    return {
        "call_id": call_id,
        "transcript": [
            {"timestamp": "00:00", "speaker": "Agent", "text": "Hi, thanks for calling Acme Sales. How can I help you today?"},
            {"timestamp": "00:05", "speaker": "Customer", "text": "I'm interested in your enterprise plan pricing."},
            {"timestamp": "00:12", "speaker": "Agent", "text": "Sure! Our enterprise plan starts at $499/month with volume discounts."},
            {"timestamp": "00:30", "speaker": "Customer", "text": "That sounds reasonable. Can you send me a proposal?"},
        ],
        "duration_seconds": 247,
    }


@app_v1.get("/get_call_metadata")
def get_call_metadata(call_id: str):
    """Retrieve metadata for a specific sales call including agent info, duration, timestamps, and outcome.
    Use this to get context about a call before analyzing its content."""
    return {
        "call_id": call_id,
        "agent_name": "Sarah Johnson",
        "agent_id": "AGT-4021",
        "customer_name": "John Smith",
        "customer_company": "TechCorp Inc.",
        "call_date": "2026-02-20T14:30:00Z",
        "duration_seconds": 247,
        "outcome": "proposal_sent",
        "disposition": "qualified_lead",
    }


@app_v1.get("/list_recent_calls")
def list_recent_calls(agent_id: str, limit: int = 5):
    """List the most recent sales calls for a given agent, ordered by date descending.
    Use this to see an agent's recent call activity or find specific calls to analyze."""
    return {
        "agent_id": agent_id,
        "calls": [
            {"call_id": "CALL-1001", "date": "2026-02-20T14:30:00Z", "duration_seconds": 247, "outcome": "proposal_sent"},
            {"call_id": "CALL-1002", "date": "2026-02-19T10:15:00Z", "duration_seconds": 183, "outcome": "follow_up_scheduled"},
            {"call_id": "CALL-1003", "date": "2026-02-18T16:45:00Z", "duration_seconds": 421, "outcome": "closed_won"},
            {"call_id": "CALL-1004", "date": "2026-02-17T09:00:00Z", "duration_seconds": 95, "outcome": "no_answer"},
            {"call_id": "CALL-1005", "date": "2026-02-16T11:30:00Z", "duration_seconds": 312, "outcome": "objection_handled"},
        ][:limit],
    }
