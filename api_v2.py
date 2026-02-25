from fastapi import FastAPI

app_v2 = FastAPI(title="Movie Booking - Bookings API")

BOOKINGS = {
    "BKG-1001": {
        "booking_id": "BKG-1001",
        "user_name": "Joshua",
        "showtime_id": "SHOW-006",
        "movie_title": "Oppenheimer",
        "theatre": "PVR Orion Mall, Rajajinagar",
        "date": "2026-02-25",
        "time": "18:00",
        "format": "IMAX",
        "seats": 2,
        "total_amount_inr": 700,
        "status": "confirmed",
        "booked_at": "2026-02-24T10:30:00Z",
    },
    "BKG-1002": {
        "booking_id": "BKG-1002",
        "user_name": "Joshua",
        "showtime_id": "SHOW-010",
        "movie_title": "Ocean's Eleven",
        "theatre": "PVR Nexus Mall, Koramangala",
        "date": "2026-02-25",
        "time": "20:00",
        "format": "2D",
        "seats": 3,
        "total_amount_inr": 840,
        "status": "confirmed",
        "booked_at": "2026-02-24T11:00:00Z",
    },
    "BKG-1003": {
        "booking_id": "BKG-1003",
        "user_name": "Joshua",
        "showtime_id": "SHOW-001",
        "movie_title": "Inception",
        "theatre": "PVR Orion Mall, Rajajinagar",
        "date": "2026-02-25",
        "time": "10:00",
        "format": "2D",
        "seats": 1,
        "total_amount_inr": 280,
        "status": "confirmed",
        "booked_at": "2026-02-24T14:00:00Z",
    },
}


@app_v2.post("/book_tickets")
def book_tickets(showtime_id: str, seats: float, user_name: str):
    seats = int(seats)
    """Book tickets for a specific showtime. Requires the showtime ID, number of seats, and user name.
    Returns a booking confirmation with booking ID, seat numbers, and total amount.
    Use this when the user is ready to confirm and purchase tickets."""
    return {
        "booking_id": "BKG-1004",
        "user_name": user_name,
        "showtime_id": showtime_id,
        "seats_booked": seats,
        "seat_numbers": ["F5", "F6", "F7"][:seats],
        "total_amount_inr": seats * 280,
        "status": "confirmed",
        "booking_confirmed_at": "2026-02-25T13:00:00Z",
        "message": f"Successfully booked {seats} ticket(s). Enjoy the movie!",
    }


@app_v2.post("/cancel_booking")
def cancel_booking(booking_id: str):
    """Cancel an existing booking by its booking ID.
    Returns cancellation status and refund details.
    Use this when the user wants to cancel their ticket booking."""
    booking = BOOKINGS.get(booking_id)
    if not booking:
        return {"success": False, "message": f"Booking {booking_id} not found."}
    return {
        "booking_id": booking_id,
        "status": "cancelled",
        "refund_amount_inr": booking["total_amount_inr"],
        "refund_to": "original payment method",
        "refund_eta": "5-7 business days",
        "message": "Booking successfully cancelled.",
    }


@app_v2.get("/get_booking_details")
def get_booking_details(booking_id: str):
    """Get full details of a specific booking by its booking ID.
    Returns movie, theatre, date, time, seats, amount paid, and booking status.
    Use this when the user wants to check their booking information."""
    return BOOKINGS.get(booking_id, {"error": f"Booking {booking_id} not found."})


@app_v2.get("/list_user_bookings")
def list_user_bookings(user_name: str):
    """List all bookings made by a specific user.
    Returns a summary of all their upcoming and past bookings.
    Use this to show a user their booking history."""
    user_bookings = [b for b in BOOKINGS.values() if b["user_name"].lower() == user_name.lower()]
    return {
        "user_name": user_name,
        "bookings": user_bookings,
        "total": len(user_bookings),
    }
