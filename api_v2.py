from fastapi import FastAPI

app_v2 = FastAPI(title="CQA Analysis API")


@app_v2.post("/analyze_sentiment")
def analyze_sentiment(call_id: str):
    """Analyze the overall sentiment of a sales call and break it down by speaker.
    Returns a sentiment label (positive/neutral/negative), a confidence score from 0 to 1,
    and per-speaker sentiment. Use this to gauge how a call went emotionally."""
    return {
        "call_id": call_id,
        "overall_sentiment": "positive",
        "confidence": 0.87,
        "speaker_sentiment": {
            "Agent": {"sentiment": "positive", "confidence": 0.91},
            "Customer": {"sentiment": "positive", "confidence": 0.82},
        },
    }


@app_v2.post("/score_call_quality")
def score_call_quality(call_id: str):
    """Score the overall quality of a sales call on a 0-100 scale across multiple dimensions:
    greeting, discovery, objection handling, closing technique, and professionalism.
    Use this to evaluate agent performance on a specific call."""
    return {
        "call_id": call_id,
        "overall_score": 82,
        "breakdown": {
            "greeting": 90,
            "discovery_questions": 75,
            "objection_handling": 80,
            "closing_technique": 70,
            "professionalism": 95,
        },
        "grade": "B+",
    }


@app_v2.post("/detect_keywords")
def detect_keywords(call_id: str):
    """Detect important keywords and phrases mentioned during a sales call, categorized by type:
    product mentions, competitor mentions, objections, and buying signals.
    Use this to quickly understand the key topics discussed without reading the full transcript."""
    return {
        "call_id": call_id,
        "keywords": {
            "product_mentions": ["enterprise plan", "volume discount", "annual billing"],
            "competitor_mentions": ["Salesforce", "HubSpot"],
            "objections": ["too expensive", "need to check with my team"],
            "buying_signals": ["send me a proposal", "sounds reasonable", "when can we start"],
        },
        "keyword_count": 8,
    }


@app_v2.post("/summarize_call")
def summarize_call(call_id: str):
    """Generate a concise summary of a sales call including the main discussion points,
    customer intent, next steps, and a one-line executive summary.
    Use this when you need a quick overview of what happened on a call."""
    return {
        "call_id": call_id,
        "executive_summary": "Prospect from TechCorp expressed strong interest in enterprise plan; proposal requested.",
        "discussion_points": [
            "Customer inquired about enterprise plan pricing",
            "Agent explained $499/month base with volume discounts",
            "Customer mentioned evaluating competitors (Salesforce, HubSpot)",
            "Customer requested a formal proposal",
        ],
        "customer_intent": "high_purchase_intent",
        "next_steps": ["Send proposal by EOD", "Schedule follow-up call for Friday"],
    }
