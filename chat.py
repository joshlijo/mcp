import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

from api_v1 import get_transcript, get_call_metadata, list_recent_calls
from api_v2 import analyze_sentiment, score_call_quality, detect_keywords, summarize_call
from api_v3 import flag_call, detect_speakers, get_compliance_check

TOOLS_MAP = {
    "get_transcript": get_transcript,
    "get_call_metadata": get_call_metadata,
    "list_recent_calls": list_recent_calls,
    "analyze_sentiment": analyze_sentiment,
    "score_call_quality": score_call_quality,
    "detect_keywords": detect_keywords,
    "summarize_call": summarize_call,
    "flag_call": flag_call,
    "detect_speakers": detect_speakers,
    "get_compliance_check": get_compliance_check,
}


def main():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    model = genai.GenerativeModel(
        model_name="gemini-flash-lite-latest",
        tools=list(TOOLS_MAP.values()),
    )

    chat_session = model.start_chat()

    print("\nCQA Assistant ready. Type your question (or 'quit' to exit).\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit"):
            break

        response = chat_session.send_message(user_input)

        while True:
            function_calls = [
                part.function_call
                for part in response.parts
                if part.function_call.name
            ]

            if not function_calls:
                break

            tool_response_parts = []
            for fn in function_calls:
                fn_args = dict(fn.args)
                print(f"  [calling tool: {fn.name} with {fn_args}]")
                result = TOOLS_MAP[fn.name](**fn_args)
                tool_response_parts.append(
                    genai.protos.Part(
                        function_response=genai.protos.FunctionResponse(
                            name=fn.name,
                            response={"result": json.dumps(result)},
                        )
                    )
                )

            response = chat_session.send_message(tool_response_parts)

        print(f"\nGemini: {response.text}\n")


if __name__ == "__main__":
    main()
