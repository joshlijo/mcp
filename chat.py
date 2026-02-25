import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

from api_v1 import search_movies, get_movie_details, get_showtimes
from api_v2 import book_tickets, cancel_booking, get_booking_details, list_user_bookings
from api_v3 import list_theatres, check_seat_availability, get_theatre_details

TOOLS_MAP = {
    "search_movies": search_movies,
    "get_movie_details": get_movie_details,
    "get_showtimes": get_showtimes,
    "book_tickets": book_tickets,
    "cancel_booking": cancel_booking,
    "get_booking_details": get_booking_details,
    "list_user_bookings": list_user_bookings,
    "list_theatres": list_theatres,
    "check_seat_availability": check_seat_availability,
    "get_theatre_details": get_theatre_details,
}


def main():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    model = genai.GenerativeModel(
        model_name="gemini-flash-lite-latest",
        tools=list(TOOLS_MAP.values()),
    )

    chat_session = model.start_chat()

    print("\nMovie Booking Assistant ready. Type your question (or 'quit' to exit).\n")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit"):
            break

        response = chat_session.send_message(user_input)

        while True:
            function_calls = []
            for part in response.parts:
                try:
                    if part.function_call and part.function_call.name:
                        function_calls.append(part.function_call)
                except AttributeError:
                    pass

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

        reply = "".join(part.text for part in response.parts if hasattr(part, "text") and part.text)
        print(f"\nGemini: {reply}\n")


if __name__ == "__main__":
    main()
