from fastapi import FastAPI

app_v3 = FastAPI(title="Movie Booking - Theatres & Seats API")

THEATRES = {
    "THR-001": {"theatre_id": "THR-001", "name": "PVR Orion Mall",                      "area": "Rajajinagar",       "city": "Bangalore", "screens": 8,  "parking": True,  "food_court": True},
    "THR-002": {"theatre_id": "THR-002", "name": "PVR Nexus Mall",                      "area": "Koramangala",       "city": "Bangalore", "screens": 11, "parking": True,  "food_court": True},
    "THR-003": {"theatre_id": "THR-003", "name": "Cinepolis LuLu Global Mall",           "area": "Rajajinagar",       "city": "Bangalore", "screens": 11, "parking": True,  "food_court": True},
    "THR-004": {"theatre_id": "THR-004", "name": "INOX Garuda Mall",                     "area": "Ashok Nagar",       "city": "Bangalore", "screens": 5,  "parking": True,  "food_court": True},
    "THR-005": {"theatre_id": "THR-005", "name": "INOX Mantri Square",                   "area": "Malleswaram",       "city": "Bangalore", "screens": 6,  "parking": True,  "food_court": True},
    "THR-006": {"theatre_id": "THR-006", "name": "Cinepolis Royal Meenakshi Mall",       "area": "Bannerghatta Road", "city": "Bangalore", "screens": 7,  "parking": True,  "food_court": True},
    "THR-007": {"theatre_id": "THR-007", "name": "PVR VR Bengaluru",                     "area": "Whitefield",        "city": "Bangalore", "screens": 9,  "parking": True,  "food_court": True},
    "THR-008": {"theatre_id": "THR-008", "name": "Urvashi Theatre",                      "area": "Lalbagh Road",      "city": "Bangalore", "screens": 1,  "parking": False, "food_court": False},
    "THR-009": {"theatre_id": "THR-009", "name": "PVR Phoenix Marketcity",               "area": "Whitefield",        "city": "Bangalore", "screens": 8,  "parking": True,  "food_court": True},
    "THR-010": {"theatre_id": "THR-010", "name": "INOX RMZ Galleria",                    "area": "Yelahanka",         "city": "Bangalore", "screens": 5,  "parking": True,  "food_court": False},
}

THEATRE_AMENITIES = {
    "THR-001": {"formats": ["2D", "3D", "IMAX"],       "food_options": ["PVR Munchies", "Baskin Robbins"],          "accessibility": True},
    "THR-002": {"formats": ["2D", "3D", "4DX", "IMAX"],"food_options": ["PVR Munchies", "Subway"],                  "accessibility": True},
    "THR-003": {"formats": ["2D", "3D"],               "food_options": ["Cinepolis Gourmet", "KFC"],                 "accessibility": True},
    "THR-004": {"formats": ["2D", "3D", "4DX"],        "food_options": ["INOX Eats", "Cafe Coffee Day"],             "accessibility": True},
    "THR-005": {"formats": ["2D", "3D", "IMAX"],       "food_options": ["INOX Eats", "McDonald's"],                  "accessibility": True},
    "THR-006": {"formats": ["2D", "3D"],               "food_options": ["Cinepolis Gourmet", "Pizza Hut"],           "accessibility": True},
    "THR-007": {"formats": ["2D", "3D", "IMAX"],       "food_options": ["PVR Munchies", "Starbucks"],                "accessibility": True},
    "THR-008": {"formats": ["2D"],                     "food_options": ["Snack counter"],                            "accessibility": False},
    "THR-009": {"formats": ["2D", "3D", "4DX", "IMAX"],"food_options": ["PVR Munchies", "Pizza Hut", "Starbucks"],  "accessibility": True},
    "THR-010": {"formats": ["2D", "3D", "IMAX"],       "food_options": ["INOX Eats", "Juice bar"],                   "accessibility": True},
}

SEAT_AVAILABILITY = {
    "SHOW-001": {"total_seats": 120, "available": 45, "categories": {"recliner": {"available": 8,  "price_inr": 450}, "premium": {"available": 20, "price_inr": 320}, "regular": {"available": 17, "price_inr": 280}}},
    "SHOW-002": {"total_seats": 120, "available": 82, "categories": {"recliner": {"available": 12, "price_inr": 450}, "premium": {"available": 35, "price_inr": 320}, "regular": {"available": 35, "price_inr": 280}}},
    "SHOW-003": {"total_seats": 100, "available": 12, "categories": {"recliner": {"available": 0,  "price_inr": 420}, "premium": {"available": 5,  "price_inr": 310}, "regular": {"available": 7,  "price_inr": 300}}},
    "SHOW-004": {"total_seats": 150, "available": 90, "categories": {"recliner": {"available": 15, "price_inr": 400}, "premium": {"available": 40, "price_inr": 280}, "regular": {"available": 35, "price_inr": 250}}},
    "SHOW-005": {"total_seats": 130, "available": 60, "categories": {"premium": {"available": 25,  "price_inr": 290}, "regular": {"available": 35, "price_inr": 260}}},
    "SHOW-006": {"total_seats": 200, "available": 3,  "categories": {"imax":    {"available": 2,  "price_inr": 500}, "premium": {"available": 1,  "price_inr": 380}, "regular": {"available": 0,  "price_inr": 350}}},
    "SHOW-007": {"total_seats": 180, "available": 55, "categories": {"imax":    {"available": 20, "price_inr": 480}, "premium": {"available": 20, "price_inr": 350}, "regular": {"available": 15, "price_inr": 320}}},
    "SHOW-008": {"total_seats": 140, "available": 75, "categories": {"premium": {"available": 30,  "price_inr": 260}, "regular": {"available": 45, "price_inr": 220}}},
    "SHOW-009": {"total_seats": 900, "available": 320,"categories": {"regular": {"available": 320, "price_inr": 180}}},
    "SHOW-010": {"total_seats": 150, "available": 65, "categories": {"recliner": {"available": 10, "price_inr": 420}, "premium": {"available": 28, "price_inr": 300}, "regular": {"available": 27, "price_inr": 250}}},
}


@app_v3.get("/list_theatres")
def list_theatres(area: str = None):
    """List all theatres in and around Bangalore.
    Optionally filter by area or neighbourhood (e.g. 'Whitefield', 'Koramangala', 'Malleswaram').
    Returns theatre IDs, names, areas, number of screens, parking, and food court availability.
    Use this when the user wants to find theatres near a specific location."""
    results = list(THEATRES.values())
    if area:
        results = [t for t in results if area.lower() in t["area"].lower()]
    return {"theatres": results, "total": len(results)}


@app_v3.get("/check_seat_availability")
def check_seat_availability(showtime_id: str):
    """Check seat availability for a specific showtime.
    Returns total seats, available seats, and a breakdown by category (regular, premium, recliner, IMAX) with prices.
    Use this before booking to confirm seats are available and check pricing tiers."""
    availability = SEAT_AVAILABILITY.get(showtime_id, {
        "total_seats": 120,
        "available": 60,
        "categories": {
            "premium": {"available": 25, "price_inr": 300},
            "regular": {"available": 35, "price_inr": 240},
        },
    })
    return {"showtime_id": showtime_id, **availability}


@app_v3.get("/get_theatre_details")
def get_theatre_details(theatre_id: str):
    """Get detailed information about a specific theatre including location, number of screens, formats supported, and amenities.
    Use this when the user wants to know more about a theatre before choosing a showtime."""
    theatre = THEATRES.get(theatre_id, THEATRES["THR-001"])
    amenities = THEATRE_AMENITIES.get(theatre_id, THEATRE_AMENITIES["THR-001"])
    return {**theatre, **amenities}
