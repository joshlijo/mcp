from fastapi import FastAPI

app_v3 = FastAPI(title="CQA Compliance & Speaker API")


@app_v3.post("/flag_call")
def flag_call(call_id: str, reason: str):
    """Flag a specific sales call for manual review by a QA manager.
    Provide the call ID and a reason (e.g. 'compliance_violation', 'customer_complaint', 'coaching_opportunity').
    Use this when automated analysis detects an issue that needs human attention."""
    return {
        "call_id": call_id,
        "flagged": True,
        "reason": reason,
        "review_queue": "qa_manager",
        "priority": "high" if reason == "compliance_violation" else "medium",
        "estimated_review_time": "2026-02-26T09:00:00Z",
    }


@app_v3.post("/detect_speakers")
def detect_speakers(call_id: str):
    """Identify and label all speakers in a sales call using speaker diarization.
    Returns each speaker's role, talk-time percentage, and number of turns.
    Use this to understand conversation dynamics and agent-to-customer talk ratio."""
    return {
        "call_id": call_id,
        "speakers": [
            {"speaker_id": "SPK-01", "role": "agent", "name": "Sarah Johnson", "talk_time_pct": 42.5, "turns": 14},
            {"speaker_id": "SPK-02", "role": "customer", "name": "John Smith", "talk_time_pct": 51.3, "turns": 16},
            {"speaker_id": "SPK-03", "role": "unknown", "name": None, "talk_time_pct": 6.2, "turns": 2},
        ],
        "dominant_speaker": "customer",
        "talk_ratio_agent_customer": "0.83:1",
    }


@app_v3.get("/get_compliance_check")
def get_compliance_check(call_id: str):
    """Run a compliance check on a sales call to detect potential regulatory or policy violations.
    Checks for required disclosures, prohibited language, consent verification, and DNC list compliance.
    Use this to ensure calls meet legal and company policy requirements."""
    return {
        "call_id": call_id,
        "compliant": False,
        "issues": [
            {"rule": "required_disclosure", "status": "pass", "detail": "Pricing disclosure was provided"},
            {"rule": "recording_consent", "status": "pass", "detail": "Recording consent obtained at 00:02"},
            {"rule": "prohibited_language", "status": "fail", "detail": "Guarantee language detected at 00:45 — 'I guarantee you will see ROI'"},
            {"rule": "dnc_check", "status": "pass", "detail": "Number not on DNC registry"},
        ],
        "risk_level": "medium",
    }
