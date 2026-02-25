# Movie Booking Assistant — Demo

A demo movie booking system for Bangalore cinemas, built to showcase two ways of integrating AI with a Python backend:

1. **Gemini chat** — a terminal chatbot powered by Google Gemini with function calling
2. **MCP server** — exposes the same APIs as tools for MCP-compatible AI clients (e.g. Claude)

---

## Project Structure

```
demo1/
├── api_v1.py       # Movies & Showtimes API
├── api_v2.py       # Bookings API
├── api_v3.py       # Theatres & Seats API
├── chat.py         # Gemini AI terminal chatbot
└── mcp_server.py   # MCP server (for Claude / other MCP clients)
```

### API Files

| File | Responsibility | Key Functions |
|---|---|---|
| `api_v1.py` | Movies & showtimes | `search_movies`, `get_movie_details`, `get_showtimes` |
| `api_v2.py` | Bookings | `book_tickets`, `cancel_booking`, `get_booking_details`, `list_user_bookings` |
| `api_v3.py` | Theatres & seats | `list_theatres`, `get_theatre_details`, `check_seat_availability` |

All data is hardcoded in-memory — no database required.

---

## How It Works

### Gemini Chat (`chat.py`)

```
You type a message
  → Sent to Gemini API
    → Gemini picks a tool to call (based on function docstrings)
      → Your code runs the function locally
        → Result sent back to Gemini
          → Gemini replies in plain English
```

Gemini never runs your code directly. It reads the function name, parameters, and docstring to decide what to call — your code executes it and reports back.

### MCP Server (`mcp_server.py`)

FastMCP automatically converts each FastAPI app into MCP tools, namespaced as `movies_*`, `bookings_*`, and `theatres_*`. An MCP-compatible client (like Claude Code) connects to the server and calls tools the same way Gemini does — but over the MCP protocol instead.

---

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set your Gemini API key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_key_here
```

Get a key at [aistudio.google.com](https://aistudio.google.com).

---

## Usage

### Run the Gemini chatbot

```bash
python chat.py
```

Example interaction:

```
You: What sci-fi movies are showing today?
  [calling tool: search_movies with {'genre': 'Sci-Fi'}]

Gemini: There are two sci-fi movies showing today — Inception and The Matrix...

You: Book 2 tickets for Inception at PVR Orion Mall
  [calling tool: get_showtimes with {'movie_id': 'MOVIE-003'}]
  [calling tool: book_tickets with {'showtime_id': 'SHOW-001', 'seats': 2, 'user_name': 'Joshua'}]

Gemini: Done! I've booked 2 tickets for Inception...
```

Type `quit` or `exit` to stop.

### Run the MCP server

```bash
python mcp_server.py
```

Then connect any MCP-compatible client to it. For Claude Code, add it to your MCP settings pointing to this script.

---

## Data Overview

- **10 movies** — including Inception, The Matrix, Oppenheimer, and more
- **10 theatres** — across Bangalore (PVR, INOX, Cinepolis)
- **15 showtimes** — across 2 days, with 2D and IMAX options
- **3 pre-existing bookings** — for user "Joshua"
