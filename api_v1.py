from fastapi import FastAPI

app_v1 = FastAPI(title="Movie Booking - Movies & Showtimes API")

MOVIES = {
    "MOVIE-001": {"movie_id": "MOVIE-001", "title": "Jurassic Park", "genre": "Adventure/Sci-Fi", "duration_min": 127, "rating": "U/A", "language": "English", "year": 1993},
    "MOVIE-002": {"movie_id": "MOVIE-002", "title": "Ocean's Eleven", "genre": "Crime/Heist", "duration_min": 116, "rating": "U/A", "language": "English", "year": 2001},
    "MOVIE-003": {"movie_id": "MOVIE-003", "title": "Inception", "genre": "Sci-Fi/Thriller", "duration_min": 148, "rating": "U/A", "language": "English", "year": 2010},
    "MOVIE-004": {"movie_id": "MOVIE-004", "title": "Batman Begins", "genre": "Action/Superhero", "duration_min": 140, "rating": "U/A", "language": "English", "year": 2005},
    "MOVIE-005": {"movie_id": "MOVIE-005", "title": "Oppenheimer", "genre": "Drama/Historical", "duration_min": 180, "rating": "U/A", "language": "English", "year": 2023},
    "MOVIE-006": {"movie_id": "MOVIE-006", "title": "Forrest Gump", "genre": "Drama", "duration_min": 142, "rating": "U/A", "language": "English", "year": 1994},
    "MOVIE-007": {"movie_id": "MOVIE-007", "title": "The Matrix", "genre": "Sci-Fi/Action", "duration_min": 136, "rating": "U/A", "language": "English", "year": 1999},
    "MOVIE-008": {"movie_id": "MOVIE-008", "title": "Magnolia", "genre": "Drama", "duration_min": 188, "rating": "A", "language": "English", "year": 1999},
    "MOVIE-009": {"movie_id": "MOVIE-009", "title": "Scent of a Woman", "genre": "Drama", "duration_min": 157, "rating": "U/A", "language": "English", "year": 1992},
    "MOVIE-010": {"movie_id": "MOVIE-010", "title": "The Grand Budapest Hotel", "genre": "Comedy/Drama", "duration_min": 99, "rating": "U/A", "language": "English", "year": 2014},
}

MOVIE_DETAILS = {
    "MOVIE-001": {"synopsis": "A theme park suffers a major power breakdown that allows its cloned dinosaur exhibits to run amok.", "director": "Steven Spielberg", "cast": ["Sam Neill", "Laura Dern", "Jeff Goldblum"]},
    "MOVIE-002": {"synopsis": "A group of professional thieves plan and execute a heist on three Las Vegas casinos simultaneously.", "director": "Steven Soderbergh", "cast": ["George Clooney", "Brad Pitt", "Matt Damon"]},
    "MOVIE-003": {"synopsis": "A thief who steals corporate secrets through dream-sharing technology is tasked with planting an idea into the mind of a CEO.", "director": "Christopher Nolan", "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"]},
    "MOVIE-004": {"synopsis": "The early years of Bruce Wayne and his training before he becomes Batman.", "director": "Christopher Nolan", "cast": ["Christian Bale", "Michael Caine", "Liam Neeson"]},
    "MOVIE-005": {"synopsis": "The story of J. Robert Oppenheimer and his role in developing the atomic bomb during WWII.", "director": "Christopher Nolan", "cast": ["Cillian Murphy", "Emily Blunt", "Robert Downey Jr."]},
    "MOVIE-006": {"synopsis": "The presidencies of Kennedy through Reagan seen through the eyes of an Alabama man with an unusually low IQ.", "director": "Robert Zemeckis", "cast": ["Tom Hanks", "Robin Wright", "Gary Sinise"]},
    "MOVIE-007": {"synopsis": "A computer hacker learns the true nature of reality and joins a rebellion against its machine controllers.", "director": "The Wachowskis", "cast": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]},
    "MOVIE-008": {"synopsis": "An epic mosaic of interrelated characters searching for love, forgiveness, and meaning in the San Fernando Valley.", "director": "Paul Thomas Anderson", "cast": ["Tom Cruise", "Julianne Moore", "Philip Seymour Hoffman"]},
    "MOVIE-009": {"synopsis": "A prep school student agrees to escort a blind, retired Army officer for a weekend — a trip that changes his life.", "director": "Martin Brest", "cast": ["Al Pacino", "Chris O'Donnell", "James Rebhorn"]},
    "MOVIE-010": {"synopsis": "A writer encounters the owner of an aging high-class hotel between the wars and learns of his fabled past.", "director": "Wes Anderson", "cast": ["Ralph Fiennes", "Tony Revolori", "Saoirse Ronan"]},
}

SHOWTIMES = [
    {"showtime_id": "SHOW-001", "movie_id": "MOVIE-003", "theatre_id": "THR-001", "theatre_name": "PVR Orion Mall, Rajajinagar",               "date": "2026-02-25", "time": "10:00", "price_inr": 280, "format": "2D"},
    {"showtime_id": "SHOW-002", "movie_id": "MOVIE-003", "theatre_id": "THR-001", "theatre_name": "PVR Orion Mall, Rajajinagar",               "date": "2026-02-25", "time": "14:00", "price_inr": 280, "format": "2D"},
    {"showtime_id": "SHOW-003", "movie_id": "MOVIE-003", "theatre_id": "THR-004", "theatre_name": "INOX Garuda Mall, Ashok Nagar",              "date": "2026-02-25", "time": "11:30", "price_inr": 300, "format": "2D"},
    {"showtime_id": "SHOW-004", "movie_id": "MOVIE-007", "theatre_id": "THR-002", "theatre_name": "PVR Nexus Mall, Koramangala",                "date": "2026-02-25", "time": "13:00", "price_inr": 250, "format": "2D"},
    {"showtime_id": "SHOW-005", "movie_id": "MOVIE-007", "theatre_id": "THR-006", "theatre_name": "Cinepolis Royal Meenakshi Mall, Bannerghatta Road", "date": "2026-02-25", "time": "15:30", "price_inr": 260, "format": "2D"},
    {"showtime_id": "SHOW-006", "movie_id": "MOVIE-005", "theatre_id": "THR-001", "theatre_name": "PVR Orion Mall, Rajajinagar",               "date": "2026-02-25", "time": "18:00", "price_inr": 350, "format": "IMAX"},
    {"showtime_id": "SHOW-007", "movie_id": "MOVIE-005", "theatre_id": "THR-005", "theatre_name": "INOX Mantri Square, Malleswaram",            "date": "2026-02-25", "time": "17:00", "price_inr": 320, "format": "IMAX"},
    {"showtime_id": "SHOW-008", "movie_id": "MOVIE-004", "theatre_id": "THR-003", "theatre_name": "Cinepolis LuLu Global Mall, Rajajinagar",    "date": "2026-02-25", "time": "12:00", "price_inr": 220, "format": "2D"},
    {"showtime_id": "SHOW-009", "movie_id": "MOVIE-006", "theatre_id": "THR-008", "theatre_name": "Urvashi Theatre, Lalbagh Road",              "date": "2026-02-25", "time": "16:00", "price_inr": 180, "format": "2D"},
    {"showtime_id": "SHOW-010", "movie_id": "MOVIE-002", "theatre_id": "THR-002", "theatre_name": "PVR Nexus Mall, Koramangala",                "date": "2026-02-25", "time": "20:00", "price_inr": 280, "format": "2D"},
    {"showtime_id": "SHOW-011", "movie_id": "MOVIE-001", "theatre_id": "THR-007", "theatre_name": "PVR VR Bengaluru, Whitefield",               "date": "2026-02-25", "time": "11:00", "price_inr": 240, "format": "2D"},
    {"showtime_id": "SHOW-012", "movie_id": "MOVIE-010", "theatre_id": "THR-004", "theatre_name": "INOX Garuda Mall, Ashok Nagar",              "date": "2026-02-25", "time": "19:00", "price_inr": 250, "format": "2D"},
    {"showtime_id": "SHOW-013", "movie_id": "MOVIE-008", "theatre_id": "THR-009", "theatre_name": "PVR Phoenix Marketcity, Whitefield",         "date": "2026-02-25", "time": "14:30", "price_inr": 300, "format": "2D"},
    {"showtime_id": "SHOW-014", "movie_id": "MOVIE-009", "theatre_id": "THR-010", "theatre_name": "INOX RMZ Galleria, Yelahanka",               "date": "2026-02-25", "time": "20:30", "price_inr": 280, "format": "2D"},
    {"showtime_id": "SHOW-015", "movie_id": "MOVIE-003", "theatre_id": "THR-002", "theatre_name": "PVR Nexus Mall, Koramangala",                "date": "2026-02-26", "time": "10:00", "price_inr": 280, "format": "2D"},
]


@app_v1.get("/search_movies")
def search_movies(genre: str = None, title: str = None):
    """Search for movies currently showing. Optionally filter by genre (e.g. 'Drama', 'Sci-Fi') or title keyword.
    Returns a list of movies with their IDs, titles, genres, duration, and ratings.
    Use this when the user wants to find what movies are available."""
    results = list(MOVIES.values())
    if genre:
        results = [m for m in results if genre.lower() in m["genre"].lower()]
    if title:
        results = [m for m in results if title.lower() in m["title"].lower()]
    return {"movies": results, "total": len(results)}


@app_v1.get("/get_movie_details")
def get_movie_details(movie_id: str):
    """Get detailed information about a specific movie including synopsis, cast, and director.
    Use this when the user wants to know more about a particular movie before booking."""
    movie = MOVIES.get(movie_id, MOVIES["MOVIE-001"])
    extra = MOVIE_DETAILS.get(movie_id, MOVIE_DETAILS["MOVIE-001"])
    return {**movie, **extra}


@app_v1.get("/get_showtimes")
def get_showtimes(movie_id: str, theatre_id: str = None, date: str = None):
    """Get available showtimes for a specific movie.
    Optionally filter by theatre ID or date in YYYY-MM-DD format.
    Returns showtime IDs, times, theatre names, ticket prices, and format (2D/IMAX).
    Use this to find when and where a movie is playing."""
    results = [s for s in SHOWTIMES if s["movie_id"] == movie_id]
    if theatre_id:
        results = [s for s in results if s["theatre_id"] == theatre_id]
    if date:
        results = [s for s in results if s["date"] == date]
    return {"movie_id": movie_id, "showtimes": results, "total": len(results)}
